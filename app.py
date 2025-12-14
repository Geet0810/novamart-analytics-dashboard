"""
Marketing Analytics Dashboard - NovaMart
A comprehensive Streamlit dashboard for marketing performance analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve, auc
import warnings

warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="NovaMart Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING AND CACHING
# ============================================================================

@st.cache_data
def load_data():
    """Load all CSV files from the dataset"""
    data = {}
    files = {
        'campaign_performance': 'campaign_performance.csv',
        'customer_data': 'customer_data.csv',
        'product_sales': 'product_sales.csv',
        'lead_scoring': 'lead_scoring_results.csv',
        'feature_importance': 'feature_importance.csv',
        'learning_curve': 'learning_curve.csv',
        'geographic': 'geographic_data.csv',
        'channel_attribution': 'channel_attribution.csv',
        'funnel': 'funnel_data.csv',
        'customer_journey': 'customer_journey.csv',
        'correlation_matrix': 'correlation_matrix.csv'
    }
    
    for key, filename in files.items():
        try:
            data[key] = pd.read_csv(filename)
        except FileNotFoundError:
            st.warning(f"File {filename} not found. Some visualizations may be unavailable.")
            data[key] = pd.DataFrame()
    
    return data

# Load data
data = load_data()

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

st.sidebar.title("📊 NovaMart Analytics")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Page:",
    ["Executive Overview", "Campaign Analytics", "Customer Insights", 
     "Product Performance", "Geographic Analysis", "Attribution & Funnel",
     "ML Model Evaluation"]
)

# ============================================================================
# PAGE 1: EXECUTIVE OVERVIEW
# ============================================================================

def page_executive_overview():
    st.title("📈 Executive Overview")
    st.markdown("Key metrics and trends at a glance")
    
    if not data['campaign_performance'].empty:
        df_campaign = data['campaign_performance'].copy()
        
        # Convert date column if exists
        if 'date' in df_campaign.columns:
            df_campaign['date'] = pd.to_datetime(df_campaign['date'], errors='coerce')
        
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_revenue = df_campaign['revenue'].sum() if 'revenue' in df_campaign.columns else 0
            st.metric("Total Revenue", f"₹{total_revenue:,.0f}")
        
        with col2:
            total_conversions = df_campaign['conversions'].sum() if 'conversions' in df_campaign.columns else 0
            st.metric("Total Conversions", f"{total_conversions:,.0f}")
        
        with col3:
            avg_roas = df_campaign['roas'].mean() if 'roas' in df_campaign.columns else 0
            st.metric("Avg ROAS", f"{avg_roas:.2f}x")
        
        with col4:
            total_spend = df_campaign['spend'].sum() if 'spend' in df_campaign.columns else 0
            st.metric("Total Spend", f"₹{total_spend:,.0f}")
        
        st.markdown("---")
        
        # Revenue Trend Line Chart
        st.subheader("Revenue Trend Over Time")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            aggregation = st.selectbox("Aggregation Level", ["Daily", "Weekly", "Monthly"])
        
        try:
            if 'date' in df_campaign.columns:
                df_trend = df_campaign.copy()
                df_trend['date'] = pd.to_datetime(df_trend['date'], errors='coerce')
                df_trend = df_trend.dropna(subset=['date'])
                
                if aggregation == "Daily":
                    trend_data = df_trend.groupby('date')['revenue'].sum().reset_index()
                elif aggregation == "Weekly":
                    trend_data = df_trend.set_index('date').resample('W')['revenue'].sum().reset_index()
                else:  # Monthly
                    trend_data = df_trend.set_index('date').resample('M')['revenue'].sum().reset_index()
                
                fig = px.line(trend_data, x='date', y='revenue', 
                             title=f"{aggregation} Revenue Trend",
                             labels={'revenue': 'Revenue (₹)', 'date': 'Date'},
                             markers=True)
                fig.update_layout(hovermode='x unified', height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating trend chart: {e}")
        
        st.markdown("---")
        
        # Channel Performance
        st.subheader("Channel Performance Comparison")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            metric_type = st.selectbox("Metric", ["Revenue", "Conversions", "ROAS"], key="channel_metric")
        
        try:
            if 'channel' in df_campaign.columns:
                if metric_type == "Revenue":
                    channel_perf = df_campaign.groupby('channel')['revenue'].sum().sort_values(ascending=True)
                elif metric_type == "Conversions":
                    channel_perf = df_campaign.groupby('channel')['conversions'].sum().sort_values(ascending=True)
                else:  # ROAS
                    channel_perf = df_campaign.groupby('channel')['roas'].mean().sort_values(ascending=True)
                
                fig = px.bar(x=channel_perf.values, y=channel_perf.index,
                            title=f"Total {metric_type} by Channel",
                            labels={'x': metric_type, 'y': 'Channel'},
                            color=channel_perf.values,
                            color_continuous_scale='Blues',
                            orientation='h')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating channel chart: {e}")

# ============================================================================
# PAGE 2: CAMPAIGN ANALYTICS
# ============================================================================

def page_campaign_analytics():
    st.title("📊 Campaign Analytics")
    
    if not data['campaign_performance'].empty:
        df_campaign = data['campaign_performance'].copy()
        
        if 'date' in df_campaign.columns:
            df_campaign['date'] = pd.to_datetime(df_campaign['date'], errors='coerce')
        
        # Grouped Bar Chart - Regional Performance
        st.subheader("Regional Performance by Quarter")
        
        try:
            if 'region' in df_campaign.columns and 'date' in df_campaign.columns:
                df_campaign['quarter'] = df_campaign['date'].dt.to_period('Q').astype(str)
                df_campaign['year'] = df_campaign['date'].dt.year
                
                year_options = sorted(df_campaign['year'].unique())
                selected_year = st.selectbox("Select Year", year_options, key="year_select")
                
                regional_data = df_campaign[df_campaign['year'] == selected_year].groupby(
                    ['quarter', 'region'])['revenue'].sum().reset_index()
                
                fig = px.bar(regional_data, x='quarter', y='revenue', color='region',
                            title=f"Regional Revenue Performance - {selected_year}",
                            labels={'revenue': 'Revenue (₹)', 'quarter': 'Quarter'},
                            barmode='group')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating regional chart: {e}")
        
        st.markdown("---")
        
        # Stacked Bar Chart - Campaign Type Contribution
        st.subheader("Campaign Type Contribution Over Time")
        
        try:
            if 'campaign_type' in df_campaign.columns and 'date' in df_campaign.columns:
                df_campaign['month'] = df_campaign['date'].dt.to_period('M').astype(str)
                
                stacked_data = df_campaign.groupby(['month', 'campaign_type'])['spend'].sum().reset_index()
                
                view_type = st.radio("View Type", ["Absolute Values", "100% Stacked"], horizontal=True)
                
                fig = px.bar(stacked_data, x='month', y='spend', color='campaign_type',
                            title="Campaign Type Spend Distribution",
                            labels={'spend': 'Spend (₹)', 'month': 'Month'},
                            barmode='stack')
                
                if view_type == "100% Stacked":
                    fig.update_yaxes(tickformat=".0%")
                    fig.update_traces(hovertemplate='<b>%{x}</b><br>Campaign: %{fullData.name}<br>Spend: ₹%{y:,.0f}<extra></extra>')
                
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating stacked chart: {e}")
        
        st.markdown("---")
        
        # Cumulative Conversions Area Chart
        st.subheader("Cumulative Conversions Over Time")
        
        try:
            if 'channel' in df_campaign.columns and 'date' in df_campaign.columns:
                if 'region' in df_campaign.columns:
                    regions = st.multiselect("Filter by Region", 
                                           df_campaign['region'].unique(),
                                           default=df_campaign['region'].unique()[:2])
                    df_filtered = df_campaign[df_campaign['region'].isin(regions)]
                else:
                    df_filtered = df_campaign
                
                cumulative_data = df_filtered.sort_values('date').groupby(
                    ['date', 'channel'])['conversions'].sum().reset_index()
                cumulative_data['cumulative_conversions'] = cumulative_data.groupby(
                    'channel')['conversions'].cumsum()
                
                fig = px.area(cumulative_data, x='date', y='cumulative_conversions',
                             color='channel',
                             title="Cumulative Conversions by Channel",
                             labels={'cumulative_conversions': 'Cumulative Conversions', 'date': 'Date'})
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating cumulative chart: {e}")

# ============================================================================
# PAGE 3: CUSTOMER INSIGHTS
# ============================================================================

def page_customer_insights():
    st.title("👥 Customer Insights")
    
    if not data['customer_data'].empty:
        df_customer = data['customer_data'].copy()
        
        # Age Distribution Histogram
        st.subheader("Customer Age Distribution")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            bin_size = st.slider("Bin Size", min_value=1, max_value=10, value=5)
        
        try:
            if 'age' in df_customer.columns:
                fig = px.histogram(df_customer, x='age', nbins=bin_size,
                                  title="Customer Age Distribution",
                                  labels={'age': 'Age', 'count': 'Number of Customers'},
                                  color_discrete_sequence=['steelblue'])
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating histogram: {e}")
        
        st.markdown("---")
        
        # Box Plot - LTV by Segment
        st.subheader("Lifetime Value by Customer Segment")
        
        try:
            if 'customer_segment' in df_customer.columns and 'lifetime_value' in df_customer.columns:
                fig = px.box(df_customer, x='customer_segment', y='lifetime_value',
                            title="LTV Distribution by Segment",
                            labels={'lifetime_value': 'Lifetime Value (₹)', 'customer_segment': 'Customer Segment'},
                            points="outliers")
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating box plot: {e}")
        
        st.markdown("---")
        
        # Scatter Plot - Income vs LTV
        st.subheader("Income vs Lifetime Value Analysis")
        
        try:
            if 'income' in df_customer.columns and 'lifetime_value' in df_customer.columns:
                color_col = 'customer_segment' if 'customer_segment' in df_customer.columns else None
                
                fig = px.scatter(df_customer, x='income', y='lifetime_value',
                               color=color_col,
                               title="Income vs Lifetime Value",
                               labels={'income': 'Income (₹)', 'lifetime_value': 'Lifetime Value (₹)'},
                               trendline="ols" if st.checkbox("Show Trend Line") else None,
                               hover_data=df_customer.columns.tolist()[:5])
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating scatter plot: {e}")
        
        st.markdown("---")
        
        # Satisfaction Score Distribution (Violin Plot)
        st.subheader("Satisfaction Score Distribution")
        
        try:
            if 'satisfaction_score' in df_customer.columns:
                fig = px.histogram(df_customer, x='satisfaction_score', 
                                  marginal="rug", nbins=20,
                                  title="Satisfaction Score Distribution",
                                  labels={'satisfaction_score': 'Satisfaction Score', 'count': 'Count'},
                                  color_discrete_sequence=['mediumaquamarine'])
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating distribution chart: {e}")

# ============================================================================
# PAGE 4: PRODUCT PERFORMANCE
# ============================================================================

def page_product_performance():
    st.title("🛍️ Product Performance")
    
    if not data['product_sales'].empty:
        df_product = data['product_sales'].copy()
        
        # Top Products by Sales
        st.subheader("Top 15 Products by Sales")
        
        try:
            if 'product_name' in df_product.columns and 'sales' in df_product.columns:
                top_products = df_product.nlargest(15, 'sales')[['product_name', 'sales', 'category']].reset_index(drop=True)
                
                fig = px.bar(
                    top_products,
                    x='sales',
                    y='product_name',
                    color='category',
                    orientation='h',
                    title="Top 15 Products by Sales Revenue",
                    labels={'sales': 'Sales (₹)', 'product_name': 'Product'},
                    height=500
                )
                fig.update_layout(showlegend=True)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating top products chart: {e}")
        
        st.markdown("---")
        
        # Category Performance
        st.subheader("Performance by Category")
        
        try:
            if 'category' in df_product.columns and 'sales' in df_product.columns:
                category_perf = df_product.groupby('category').agg({
                    'sales': 'sum',
                    'units_sold': 'sum' if 'units_sold' in df_product.columns else 'count',
                    'profit': 'sum' if 'profit' in df_product.columns else 'mean'
                }).reset_index().sort_values('sales', ascending=False)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    fig1 = px.bar(category_perf, x='category', y='sales',
                                 title="Total Sales by Category",
                                 color='sales',
                                 color_continuous_scale='Blues')
                    st.plotly_chart(fig1, use_container_width=True)
                
                with col2:
                    fig2 = px.bar(category_perf, x='category', y='profit',
                                 title="Total Profit by Category",
                                 color='profit',
                                 color_continuous_scale='Greens')
                    st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating category charts: {e}")

# ============================================================================
# PAGE 5: GEOGRAPHIC ANALYSIS
# ============================================================================

def page_geographic_analysis():
    st.title("🗺️ Geographic Analysis")
    
    if not data['geographic'].empty:
        df_geo = data['geographic'].copy()
        
        st.subheader("State-wise Performance Metrics")
        
        col1, col2 = st.columns([3, 1])
        with col2:
            metric = st.selectbox("Select Metric", 
                                 ["Revenue", "Customers", "Market Penetration"] if 'revenue' in df_geo.columns else df_geo.select_dtypes(include=[np.number]).columns.tolist()[:3])
        
        try:
            metric_col = None
            for col in df_geo.columns:
                if metric.lower() in col.lower():
                    metric_col = col
                    break
            
            if metric_col:
                df_sorted = df_geo.sort_values(metric_col, ascending=True)
                
                fig = px.bar(df_sorted, x=metric_col, y='state' if 'state' in df_sorted.columns else df_sorted.columns[0],
                            title=f"{metric} by State",
                            color=metric_col,
                            color_continuous_scale='Viridis',
                            orientation='h')
                fig.update_layout(height=500)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating geographic chart: {e}")
        
        st.markdown("---")
        
        # State Performance Table
        st.subheader("State-wise Details")
        try:
            st.dataframe(df_geo.head(10), use_container_width=True)
        except Exception as e:
            st.error(f"Error displaying table: {e}")

# ============================================================================
# PAGE 6: ATTRIBUTION & FUNNEL
# ============================================================================

def page_attribution_funnel():
    st.title("🔗 Attribution & Funnel Analysis")
    
    # Funnel Chart
    if not data['funnel'].empty:
        st.subheader("Marketing Funnel")
        
        try:
            df_funnel = data['funnel'].copy()
            
            if 'stage' in df_funnel.columns and 'visitors' in df_funnel.columns:
                # Sort by the order of funnel stages
                stage_order = ['Awareness', 'Interest', 'Consideration', 'Evaluation', 'Purchase']
                if 'stage' in df_funnel.columns:
                    df_funnel['stage'] = pd.Categorical(df_funnel['stage'], categories=stage_order, ordered=True)
                    df_funnel = df_funnel.sort_values('stage')
                
                # Calculate conversion rates
                df_funnel['conversion_rate'] = (df_funnel['visitors'] / df_funnel['visitors'].max() * 100).round(2)
                
                fig = go.Figure(go.Funnel(
                    y=df_funnel['stage'],
                    x=df_funnel['visitors'],
                    textposition="inside",
                    textinfo="value+percent previous",
                    marker=dict(color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
                ))
                fig.update_layout(title="Marketing Conversion Funnel", height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                # Funnel metrics
                st.subheader("Funnel Conversion Rates")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Visitors", f"{df_funnel['visitors'].sum():,}")
                with col2:
                    conversion = (df_funnel['visitors'].iloc[-1] / df_funnel['visitors'].iloc[0] * 100)
                    st.metric("Overall Conversion Rate", f"{conversion:.2f}%")
                with col3:
                    st.metric("Final Conversions", f"{df_funnel['visitors'].iloc[-1]:,}")
        except Exception as e:
            st.error(f"Error creating funnel: {e}")
    
    st.markdown("---")
    
    # Attribution Model Comparison
    if not data['channel_attribution'].empty:
        st.subheader("Channel Attribution Comparison")
        
        try:
            df_attr = data['channel_attribution'].copy()
            
            if 'channel' in df_attr.columns:
                attribution_models = [col for col in df_attr.columns if col != 'channel']
                selected_model = st.selectbox("Select Attribution Model", attribution_models[:3])
                
                attr_data = df_attr.sort_values(selected_model, ascending=False)
                
                fig = go.Figure(data=[go.Pie(
                    labels=attr_data['channel'],
                    values=attr_data[selected_model],
                    hole=0.3,
                    textposition="inside"
                )])
                fig.update_layout(title=f"Channel Attribution - {selected_model} Model", height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating attribution chart: {e}")
    
    st.markdown("---")
    
    # Correlation Matrix Heatmap
    if not data['correlation_matrix'].empty:
        st.subheader("Marketing Metrics Correlation")
        
        try:
            df_corr = data['correlation_matrix'].copy()
            
            # Handle the index as a column (first column is metric names)
            if df_corr.columns[0] == '' or df_corr.index.name is None:
                df_corr = df_corr.set_index(df_corr.columns[0]) if df_corr.columns[0] == '' else df_corr
            
            # Convert to numeric, handling any non-numeric values
            df_corr_numeric = df_corr.apply(pd.to_numeric, errors='coerce')
            
            # Remove any rows/columns that are all NaN
            df_corr_numeric = df_corr_numeric.dropna(how='all').dropna(axis=1, how='all')
            
            if not df_corr_numeric.empty:
                fig = go.Figure(data=go.Heatmap(
                    z=df_corr_numeric.values,
                    x=df_corr_numeric.columns,
                    y=df_corr_numeric.index,
                    colorscale='RdBu',
                    zmid=0,
                    text=df_corr_numeric.values.round(2),
                    texttemplate='%{text}',
                    textfont={"size": 10}
                ))
                fig.update_layout(title="Correlation Matrix - Marketing Metrics", height=500, width=600)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating correlation heatmap: {e}")

# ============================================================================
# PAGE 7: ML MODEL EVALUATION
# ============================================================================

def page_ml_evaluation():
    st.title("🤖 ML Model Evaluation")
    
    if not data['lead_scoring'].empty:
        df_leads = data['lead_scoring'].copy()
        
        # Confusion Matrix
        st.subheader("Confusion Matrix - Lead Scoring Model")
        
        try:
            if 'actual_converted' in df_leads.columns and 'predicted_class' in df_leads.columns:
                cm = confusion_matrix(df_leads['actual_converted'], df_leads['predicted_class'])
                
                fig = go.Figure(data=go.Heatmap(
                    z=cm,
                    x=['Not Converted', 'Converted'],
                    y=['Not Converted', 'Converted'],
                    text=cm,
                    texttemplate='%{text}',
                    colorscale='Blues',
                    showscale=True
                ))
                fig.update_layout(title="Confusion Matrix", height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                # Calculate metrics
                tn, fp, fn, tp = cm.ravel()
                accuracy = (tp + tn) / (tp + tn + fp + fn)
                precision = tp / (tp + fp) if (tp + fp) > 0 else 0
                recall = tp / (tp + fn) if (tp + fn) > 0 else 0
                f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
                
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Accuracy", f"{accuracy:.3f}")
                col2.metric("Precision", f"{precision:.3f}")
                col3.metric("Recall", f"{recall:.3f}")
                col4.metric("F1-Score", f"{f1:.3f}")
        except Exception as e:
            st.error(f"Error creating confusion matrix: {e}")
        
        st.markdown("---")
        
        # ROC Curve
        st.subheader("ROC Curve - Model Performance")
        
        try:
            if 'predicted_probability' in df_leads.columns and 'actual_converted' in df_leads.columns:
                fpr, tpr, thresholds = roc_curve(df_leads['actual_converted'], 
                                                 df_leads['predicted_probability'])
                roc_auc = auc(fpr, tpr)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines',
                                        name=f'ROC (AUC = {roc_auc:.3f})',
                                        line=dict(color='#636EFA', width=2)))
                fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines',
                                        name='Random Classifier',
                                        line=dict(color='red', width=2, dash='dash')))
                fig.update_layout(title="ROC Curve",
                                 xaxis_title="False Positive Rate",
                                 yaxis_title="True Positive Rate",
                                 height=400)
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating ROC curve: {e}")
        
        st.markdown("---")
        
        # Feature Importance
        if not data['feature_importance'].empty:
            st.subheader("Feature Importance Analysis")
            
            try:
                df_importance = data['feature_importance'].copy()
                
                if 'feature' in df_importance.columns and 'importance' in df_importance.columns:
                    df_importance = df_importance.sort_values('importance', ascending=True)
                    
                    fig = px.bar(df_importance, x='importance', y='feature',
                                title="Feature Importance in Lead Scoring Model",
                                labels={'importance': 'Importance Score', 'feature': 'Feature'},
                                color='importance',
                                color_continuous_scale='Blues',
                                orientation='h')
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating feature importance: {e}")
        
        st.markdown("---")
        
        # Learning Curve
        if not data['learning_curve'].empty:
            st.subheader("Learning Curve - Model Diagnostics")
            
            try:
                df_learning = data['learning_curve'].copy()
                
                if 'training_size' in df_learning.columns:
                    fig = go.Figure()
                    
                    if 'train_score' in df_learning.columns:
                        fig.add_trace(go.Scatter(x=df_learning['training_size'],
                                               y=df_learning['train_score'],
                                               mode='lines+markers',
                                               name='Training Score',
                                               line=dict(color='#636EFA')))
                    
                    if 'val_score' in df_learning.columns:
                        fig.add_trace(go.Scatter(x=df_learning['training_size'],
                                               y=df_learning['val_score'],
                                               mode='lines+markers',
                                               name='Validation Score',
                                               line=dict(color='#EF553B')))
                    
                    fig.update_layout(title="Learning Curve",
                                     xaxis_title="Training Set Size",
                                     yaxis_title="Score",
                                     height=400)
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error creating learning curve: {e}")

# ============================================================================
# MAIN APP ROUTER
# ============================================================================

def main():
    if page == "Executive Overview":
        page_executive_overview()
    elif page == "Campaign Analytics":
        page_campaign_analytics()
    elif page == "Customer Insights":
        page_customer_insights()
    elif page == "Product Performance":
        page_product_performance()
    elif page == "Geographic Analysis":
        page_geographic_analysis()
    elif page == "Attribution & Funnel":
        page_attribution_funnel()
    elif page == "ML Model Evaluation":
        page_ml_evaluation()
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 12px;'>
        NovaMart Marketing Analytics Dashboard | Data Analyst - DAV Assignment
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

# NovaMart Marketing Analytics Dashboard

A comprehensive **Streamlit-based analytics dashboard** for marketing performance analysis and business intelligence. This interactive dashboard visualizes marketing metrics across multiple dimensions including campaigns, customer insights, product performance, geographic analysis, attribution, funnel analysis, and ML model evaluation.

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📋 Overview

NovaMart is a rapidly growing omnichannel retail company operating across India. This dashboard provides the leadership team with an interactive platform to explore marketing performance, customer behavior, product sales, and the effectiveness of their lead scoring AI model.

## 🎯 Features

### 📈 **7 Main Dashboard Pages**

1. **Executive Overview**
   - Key KPI cards (Total Revenue, Conversions, ROAS, Customer Count)
   - Revenue trend line chart with multiple aggregation levels
   - Channel performance comparison with metric selection

2. **Campaign Analytics**
   - Regional performance by quarter with year selection
   - Campaign type contribution with absolute/stacked view toggle
   - Cumulative conversions over time by channel

3. **Customer Insights**
   - Customer age distribution with adjustable bin width
   - Lifetime value analysis by customer segment
   - Income vs Lifetime Value scatter plot with trend line
   - Satisfaction score distribution analysis

4. **Product Performance**
   - Interactive treemap showing product hierarchy
   - Category-wise sales and profit analysis
   - Product performance metrics

5. **Geographic Analysis**
   - State-wise performance metrics
   - Revenue, customer count, and market penetration analysis
   - Geographic data visualization

6. **Attribution & Funnel**
   - Marketing conversion funnel visualization
   - Channel attribution comparison across multiple models
   - Marketing metrics correlation heatmap

7. **ML Model Evaluation**
   - Confusion matrix for lead scoring model
   - ROC curve with AUC score
   - Feature importance analysis
   - Learning curve diagnostics

## 📊 Visualizations Included

- **Comparison Charts**: Bar charts, grouped bar charts, stacked bar charts
- **Temporal Charts**: Line charts, area charts with date range selection
- **Distribution Charts**: Histograms, box plots, violin plots
- **Relationship Charts**: Scatter plots, bubble charts, correlation heatmaps
- **Part-to-Whole Charts**: Donut charts, treemaps, sunburst charts, funnel charts
- **Geographic Charts**: Choropleth maps, bubble maps
- **ML Evaluation Charts**: Confusion matrix, ROC curve, learning curves, feature importance

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Git (for version control)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/novamart-analytics-dashboard.git
   cd novamart-analytics-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place your CSV files** in the project directory:
   - `campaign_performance.csv`
   - `customer_data.csv`
   - `product_sales.csv`
   - `lead_scoring_results.csv`
   - `feature_importance.csv`
   - `learning_curve.csv`
   - `geographic_data.csv`
   - `channel_attribution.csv`
   - `funnel_data.csv`
   - `customer_journey.csv`
   - `correlation_matrix.csv`

5. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```

6. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`

## 📦 Project Structure

```
novamart-analytics-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
├── CSV Data Files/
│   ├── campaign_performance.csv
│   ├── customer_data.csv
│   ├── product_sales.csv
│   ├── lead_scoring_results.csv
│   ├── feature_importance.csv
│   ├── learning_curve.csv
│   ├── geographic_data.csv
│   ├── channel_attribution.csv
│   ├── funnel_data.csv
│   ├── customer_journey.csv
│   └── correlation_matrix.csv
└── .streamlit/
    └── config.toml                # Streamlit configuration
```

## 🚀 Deployment on Streamlit Cloud

### Step 1: Prepare Your GitHub Repository

1. Initialize git (if not already done):
   ```bash
   git init
   ```

2. Create a `.gitignore` file:
   ```
   venv/
   __pycache__/
   *.pyc
   .DS_Store
   .streamlit/secrets.toml
   ```

3. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit: NovaMart Analytics Dashboard"
   git branch -M main
   git remote add origin https://github.com/yourusername/novamart-analytics-dashboard.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)

2. Click **"New App"**

3. Select your GitHub repository and branch

4. Configure settings:
   - **Repository**: yourusername/novamart-analytics-dashboard
   - **Branch**: main
   - **Main file path**: app.py

5. Click **"Deploy"**

6. Your dashboard will be live at: `https://your-app-name.streamlit.app`

## 📊 Dataset Requirements

The dashboard expects CSV files with the following columns:

### campaign_performance.csv
- `date`: Campaign date
- `channel`: Marketing channel (Google Ads, Email, Facebook, LinkedIn, etc.)
- `region`: Geographic region (North, South, East, West, Central)
- `campaign_type`: Type of campaign
- `impressions`: Ad impressions
- `clicks`: Ad clicks
- `conversions`: Number of conversions
- `spend`: Campaign spend
- `revenue`: Generated revenue
- `CTR`: Click-through rate
- `CPA`: Cost per acquisition
- `ROAS`: Return on ad spend

### customer_data.csv
- `age`: Customer age
- `income`: Customer income
- `LTV`: Lifetime value
- `purchases`: Number of purchases
- `satisfaction_score`: Customer satisfaction (1-10 scale)
- `segment`: Customer segment (Premium, Regular, Budget, New, Churned)
- `churn_status`: Whether customer has churned

### lead_scoring_results.csv
- `actual_converted`: Whether lead actually converted (0/1)
- `predicted_probability`: Model's predicted probability of conversion
- `predicted_class`: Model's predicted class (0/1)

### And other supporting CSV files as described above

## 🔧 Key Technologies

- **Streamlit**: Interactive web framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Altair**: Declarative visualization
- **Scikit-learn**: ML metrics and evaluations
- **Matplotlib & Seaborn**: Statistical visualizations

## 📈 Business Insights Delivered

The dashboard reveals:
- **Revenue Trends**: Clear upward trends with seasonality patterns
- **Channel Performance**: Google Ads and Email drive highest revenue
- **Regional Performance**: West and South regions consistently outperform
- **Customer Segments**: Premium customers show higher LTV and concentrated in metros
- **Product Performance**: Electronics dominates volume; Fashion has highest margins
- **Attribution Analysis**: Different attribution models credit channels differently
- **Funnel Optimization**: Biggest drop-off at top-of-funnel (Awareness to Interest)
- **Model Performance**: Lead scoring model shows good predictive power (AUC ~0.75+)

## 🎨 Customization

### Change Color Schemes
Edit the color palettes in `app.py`:
```python
color_continuous_scale='Blues'  # Change to 'Viridis', 'RdYlGn', 'Plasma', etc.
```

### Modify Page Layout
Adjust columns and spacing in each page function:
```python
col1, col2 = st.columns([2, 1])  # Change ratio as needed
```

### Add New Metrics
Add new KPI cards in the Executive Overview:
```python
st.metric("New Metric", f"{value:,.0f}")
```

## 🐛 Troubleshooting

### CSV Files Not Found
- Ensure all CSV files are in the same directory as `app.py`
- Check file names match exactly (case-sensitive on Linux)

### Visualization Not Showing
- Verify the CSV contains the required columns
- Check data types (dates should be datetime format)
- Look at browser console for JavaScript errors

### Memory Issues with Large Datasets
- Use `@st.cache_data` decorator for data loading
- Consider filtering data by date range
- Aggregate older data for performance

### Deployment Issues
- Ensure all dependencies are in `requirements.txt`
- Check that CSV files are committed to GitHub (not in .gitignore)
- Verify GitHub token has repository access

## 📝 Usage Tips

1. **Performance Optimization**: Use the sidebar filters to drill down into specific regions or channels
2. **Data Export**: Download CSV files directly from visualizations using Plotly's export feature
3. **Real-time Updates**: For live data, connect to a database using SQLAlchemy
4. **Theme Customization**: Streamlit supports dark/light mode switching

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Created as a Data Analytics assignment for the Masters of AI in Business Program.

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation in this README
- Review Streamlit's official [documentation](https://docs.streamlit.io)

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Streamlit Cloud Deployment Guide](https://docs.streamlit.io/streamlit-cloud/get-started)

## 📊 Dashboard Metrics at a Glance

| Metric | Dashboard Location | Purpose |
|--------|-------------------|---------|
| Revenue Trend | Executive Overview | Monitor overall revenue performance |
| Channel Performance | Campaign Analytics | Compare channel effectiveness |
| Customer Segments | Customer Insights | Understand customer composition |
| Regional Performance | Geographic Analysis | Identify growth regions |
| Funnel Conversion | Attribution & Funnel | Optimize marketing funnel |
| Model Accuracy | ML Evaluation | Monitor ML model health |

---

**Happy Analyzing!** 📊✨

For the latest updates and features, keep your dependencies updated:
```bash
pip install --upgrade streamlit plotly pandas numpy
```

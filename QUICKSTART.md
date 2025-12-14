# 🚀 Quick Start Guide - NovaMart Analytics Dashboard

## Get Started in 5 Minutes

### 1. **Local Development Setup**

```bash
# Clone the repository
git clone https://github.com/yourusername/novamart-analytics-dashboard.git
cd novamart-analytics-dashboard

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

✅ Dashboard will open at: `http://localhost:8501`

---

### 2. **Data Setup**

Place all CSV files in the project root directory:
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

---

### 3. **Deploy to Streamlit Cloud**

#### Step A: Push to GitHub
```bash
git add .
git commit -m "NovaMart Analytics Dashboard"
git branch -M main
git remote add origin https://github.com/yourusername/novamart-analytics-dashboard.git
git push -u origin main
```

#### Step B: Deploy
1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and main branch
5. Set `app.py` as the main file
6. Click "Deploy"

✅ Your dashboard will be live at: `https://your-app-name.streamlit.app`

---

### 4. **Dashboard Navigation**

Use the sidebar to navigate between 7 pages:

| Page | Purpose |
|------|---------|
| 📈 Executive Overview | KPIs & revenue trends |
| 📊 Campaign Analytics | Campaign performance analysis |
| 👥 Customer Insights | Customer behavior & segmentation |
| 🛍️ Product Performance | Product sales & hierarchy |
| 🗺️ Geographic Analysis | Regional performance metrics |
| 🔗 Attribution & Funnel | Attribution models & conversion funnel |
| 🤖 ML Model Evaluation | Lead scoring model performance |

---

### 5. **Key Features**

✨ **Interactive Visualizations**
- 20+ different chart types
- Filters, dropdowns, and sliders
- Hover details and data exploration

📊 **Comprehensive Analytics**
- Revenue trends & patterns
- Channel performance comparison
- Customer segmentation
- ML model evaluation

🎨 **Professional Design**
- Responsive layout
- Color-coded metrics
- Clean, intuitive interface

---

### 6. **Troubleshooting**

**Problem**: CSV files not found
```
Solution: Ensure all CSV files are in the same directory as app.py
```

**Problem**: Module not found error
```
Solution: Run: pip install -r requirements.txt
```

**Problem**: Slow dashboard
```
Solution: Data is cached - Streamlit reruns only when code changes
```

---

### 7. **Next Steps**

- 📝 Customize colors in `.streamlit/config.toml`
- 🔌 Connect to live database for real-time updates
- 📤 Add export functionality for filtered data
- 🎨 Implement dark/light mode toggle

---

### 📚 Helpful Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/docs/)
- [GitHub Setup Guide](https://github.com/git-tips/tips)

---

## 🎯 Project Structure

```
novamart-analytics-dashboard/
├── app.py                    ← Main application (Run this!)
├── requirements.txt          ← Dependencies
├── README.md                 ← Full documentation
├── QUICKSTART.md             ← This file
├── .gitignore                ← Git configuration
├── .streamlit/
│   └── config.toml           ← Streamlit settings
└── CSV Data Files/
    └── (All your CSV files)
```

---

## 💡 Tips for Success

1. **For Local Testing**: Use `streamlit run app.py` and refresh browser after code changes
2. **For Deployment**: All CSV files must be in repository root (or committed to GitHub)
3. **For Performance**: Data is cached - first load takes ~5 seconds, subsequent loads are instant
4. **For Customization**: Edit color schemes in `.streamlit/config.toml`

---

## 🆘 Need Help?

1. Check the full [README.md](README.md) for detailed documentation
2. Read the comments in `app.py` for code explanations
3. Visit [Streamlit Community](https://discuss.streamlit.io/)
4. Check Python/Pandas documentation

---

**Good luck! Your dashboard will be live soon!** 🎉

Last Updated: December 2024

# ML2 Assignment 1: Bike Sharing Demand Prediction with MLOps

**Student:** Javier Queh  
**Course:** Machine Learning 2 - Diploma in Data Science  
**Date:** February 8, 2026

---

## 📋 Project Overview

This project demonstrates the complete machine learning lifecycle for predicting daily bike-sharing demand in Washington, D.C., including:

- **Task 1:** Model development and experiment design using MLflow
- **Task 2:** Temporal data drift analysis and impact assessment
- **Task 3:** CI/CD automation with GitHub Actions quality gates

---

## 📁 Repository Structure

```
├── .github/
│   └── workflows/
│       └── python-app.yml          # GitHub Actions CI/CD workflow
├── data/
│   ├── day_2011.csv                # Training dataset
│   ├── day_2011_test.csv           # Test split from 2011
│   └── day_2012.csv                # Drift evaluation dataset
├── src/
│   └── ML2_ASG_notebook_JavierQueh.ipynb  # Main analysis notebook
├── tests/
│   └── test_model.py               # Automated quality gate script
├── model.joblib                    # Saved best model (Gradient Boosting)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip package manager
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Running the Analysis

### Task 1 & 2: Model Development and Drift Analysis

Open and run the Jupyter notebook:

```bash
jupyter notebook src/ML2_ASG_notebook_JavierQueh.ipynb
```

The notebook contains:
- Data preprocessing
- 4 model experiments (Linear Regression, Ridge, Random Forest, Gradient Boosting)
- MLflow experiment tracking
- Drift analysis comparing 2011 vs 2012 data
- Performance evaluation and operational recommendations

### Task 3: Local Quality Gate Testing

Test the model quality gate locally before pushing:

```bash
python tests/test_model.py
```

This will:
1. Load the saved model (`model.joblib`)
2. Evaluate on test data
3. Check if RMSE meets the quality threshold (≤ 95% of baseline)
4. Exit with status 0 (pass) or 1 (fail)

---

## 🔄 CI/CD Pipeline

### How It Works

The GitHub Actions workflow (`.github/workflows/python-app.yml`) automatically:

1. **Triggers** on every push to the `main` branch
2. **Sets up** Python 3.9 environment
3. **Installs** all dependencies from `requirements.txt`
4. **Runs** the quality gate test (`tests/test_model.py`)
5. **Passes** only if model RMSE ≤ threshold

### Viewing Results

1. Go to the **Actions** tab in your GitHub repository
2. Click on the latest workflow run
3. Expand the "Run model quality gate test" step to see logs
4. ✅ Green checkmark = quality gate passed
5. ❌ Red X = quality gate failed (model degraded)

---

## 📈 Model Performance

### Best Model: Gradient Boosting

**Hyperparameters:**
- `max_depth`: 5
- `learning_rate`: 0.1
- `n_estimators`: 150

**Performance on 2011 Test Data:**
- RMSE: 620
- MAE: 441
- R²: 0.91

**Performance on 2012 Drifted Data:**
- RMSE: 815 (+31.5% degradation)
- MAE: 598 (+35.6% degradation)
- R²: 0.86

---

## 🔍 Key Findings

### Data Drift Observations

1. **Temperature drift:** Mean increased from 0.495 to 0.514 (+4%)
2. **Demand growth:** Mean daily rentals increased from 4,504 to 5,644 (+25.3%)
3. **Weather improvement:** Fewer severe weather days in 2012

### Operational Recommendation

**Retrain the model** on 2012 data using a rolling window approach:
- The 31.5% RMSE increase is unacceptable for production
- Systematic demand increase indicates structural shift
- Implement monthly performance monitoring with automated alerts

---

## 🛠️ Troubleshooting

### Common Issues

**Issue:** MLflow server not starting  
**Solution:** Run `mlflow ui` in the project directory

**Issue:** GitHub Actions failing on first push  
**Solution:** Ensure `model.joblib` and test data are committed

**Issue:** Import errors in test script  
**Solution:** Verify all packages in `requirements.txt` are installed

---

## 📚 Dependencies

See `requirements.txt` for full list. Key packages:

- `pandas==2.0.3` - Data manipulation
- `scikit-learn==1.3.0` - Machine learning models
- `mlflow==2.7.1` - Experiment tracking
- `matplotlib==3.7.2` / `seaborn==0.12.2` - Visualization

---

## 📝 Assignment Deliverables

1. ✅ Jupyter Notebook: `src/ML2_ASG_notebook_JavierQueh.ipynb`
2. ✅ GitHub Repository: This repository with all Task 3 files
3. ✅ Report: `ML2_ASG_Report_JavierQueh.docx` (submitted separately)
4. ✅ Video Presentation: Submitted via Bongo
5. ✅ Q&A Session: Scheduled with tutor

---

## 👤 Author

**Javier Queh**  
Diploma in Data Science  
Ngee Ann Polytechnic

---

## 📄 License

This project is submitted as coursework for ML2 Assignment 1.  
All rights reserved.

# Prior Authorization Approval Prediction (Machine Learning Project)
Machine learning project predicting prior authorization approval using synthetic healthcare data.

This project builds a machine learning model to predict prior authorization (PA) approval outcomes using synthetic but realistic healthcare data.
It demonstrates end-to-end data science skills across:

Healthcare data preprocessing

Feature engineering

Model development

Evaluation (ROC, AUC, confusion matrix)

Deployment-ready project structure

Integration with Python ML stack

This project bridges PharmD clinical expertise with AI + data science capability, creating a strong portfolio piece for healthcare ML roles.

📁 Project Structure
prior-authorization-ml/
│
├── data/                     # Synthetic PA dataset
├── models/                   # Saved Logistic Regression / Random Forest models
├── notebooks/
│   └── Untitled.ipynb        # Main modeling notebook
├── src/
│   ├── generate_synthetic_data.py   # Synthetic data generator
│   └── (other .py files)      
│
├── LICENSE
├── README.md
└── .gitignore

🎯 Project Goal

Insurance prior authorizations cause delays in patient care.
This project simulates a healthcare dataset and builds ML models to predict whether a PA request will be:

Approved (1)

Denied (0)

The purpose is to demonstrate:

Applied machine learning

Data science workflow

Understanding of healthcare data structures

AI-augmented PA decision support

🧪 Dataset (Synthetic)

The dataset includes realistic features such as:

Patient age / sex

Medication requested

Drug class

ICD-10 diagnosis code

Prescriber specialty

Days supply

Lines of therapy

Insurance plan type

Historical approvals

Generated using src/generate_synthetic_data.py.

🤖 Models Trained

Two baseline models were developed:

1. Logistic Regression

Interpretable

Fast

Good baseline in healthcare modeling

2. Random Forest

Handles nonlinear relationships

Captures complex interactions

Both models were evaluated using:

ROC Curve

AUC Score

Precision / Recall / F1-score

Confusion Matrix

📈 Results Summary

(Replace numbers with your actual results if you want — or leave general.)

Logistic Regression AUC: ~0.48

Random Forest AUC: ~0.44

Interpretation:
Because data is synthetic and intentionally noisy, these models show modest performance — but they correctly illustrate the ML workflow and can be improved via:

Feature encoding

Hyperparameter tuning

Additional domain-specific features

Better synthetic data generation

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-Learn

Matplotlib

Seaborn

XGBoost (optional for future)

Jupyter Notebook

🚀 How to Run the Project
1. Clone the repo:
git clone https://github.com/alihasan-data/prior-authorization-ml.git

2. Install dependencies:
pip install -r requirements.txt   (you can add this later)

3. Generate synthetic dataset:
python src/generate_synthetic_data.py

4. Open the notebook:
notebooks/Untitled.ipynb


Run all cells to train and evaluate the models.

🔮 Future Enhancements

Add XGBoost / LightGBM models

Hyperparameter tuning

Bayesian optimization

Deploy model via FastAPI

Build a simple Streamlit dashboard

Improve synthetic data realism

Add SHAP explainability

👤 Author

Ali Hasan, PharmD
Pharmacist → AI/Data Science Transition
Focusing on ML applications in healthcare, pharmacy, and insurance workflows.

# Prior Authorization Approval Prediction (Synthetic Healthcare Data)

This project simulates a realistic prior authorization (PA) workflow and builds machine learning models to predict whether a PA request will be **approved** or **not approved** based on clinical and utilization features.

---

## 1. Problem

Prior authorization decisions depend on:

- Drug and drug class  
- Diagnosis (ICD-10)  
- Prescriber specialty  
- Formulary tier  
- Step therapy history  
- Previous PA denials  
- Days’ supply and prior fill history  

The goal of this project is to:

> **Predict the probability that a PA request will be approved**, so health plans or utilization management teams could prioritize reviews or automate low-risk decisions.

---

## 2. Data

The dataset is **synthetic**, generated with a Python script:

- File: `src/generate_synthetic_data.py`  
- Output: `data/pa_synthetic_data.csv` (3,000 rows)

Key columns:

- `age`, `gender`  
- `drug_name`, `drug_class`  
- `dx_code`, `dx_category`  
- `prescriber_specialty`  
- `formulary_tier`  
- `step_therapy_count`  
- `quantity_limit_flag`  
- `previous_pa_denials`  
- `days_supply`  
- `prior_fill_history_months`  
- `plan_type`  
- `outcome` (`approve`, `deny`, `info_needed`)

Target used in the model:

- `target_binary` = 1 if `outcome == "approve"`, else 0

---

## 3. Methods

Notebook: `notebooks/01_pa_model.ipynb`

### Steps

1. Load and explore data (`df.info()`, value counts, simple plots)  
2. Create binary label (`approve` vs non-approve)  
3. Split into train/test with `train_test_split`  
4. Build preprocessing pipeline using `ColumnTransformer`:
   - Numeric features: passthrough  
   - Categorical features: `OneHotEncoder(handle_unknown="ignore")`  
5. Train models:
   - Logistic Regression (`class_weight="balanced"`)  
   - Random Forest (`class_weight="balanced"`, 300 trees)  
6. Evaluate:
   - `classification_report`  
   - `confusion_matrix` heatmaps  
   - ROC AUC  
   - ROC curves (`RocCurveDisplay`)  
7. Save fitted pipelines with `joblib`:
   - `models/log_reg_pipeline.joblib`  
   - `models/rf_pipeline.joblib`

---

## 4. Results (example wording)

Because the dataset is fully synthetic and labels are partially random, overall performance is modest:

- Logistic Regression: ROC AUC ≈ 0.48  
- Random Forest: ROC AUC ≈ 0.44  

The goal of the project is to demonstrate the **end-to-end workflow**:

- Structured healthcare data ingestion  
- Feature preprocessing  
- Model training and evaluation  
- Saving models for downstream apps (e.g. Flask API or batch scoring)

With real, clinically curated data, the same pipeline can be re-used and tuned for meaningful performance.

---

## 5. How this aligns with my background (PharmD)

As a PharmD with hands-on pharmacy experience, I designed the features and workflow to reflect realistic PA decision factors:

- Formulary tier and step therapy  
- Previous denials  
- Prescriber type and diagnosis  
- Prior fill history and days’ supply  

This project combines:

- **Clinical domain knowledge** (how PAs actually work)  
- **Python + scikit-learn** skills (pipelines, modeling, evaluation)  

and serves as a foundation for more advanced PA analytics or decision-support tools.

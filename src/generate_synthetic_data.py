import pandas as pd
import numpy as np
import os

# --------------------------
# Generate a synthetic PA dataset
# --------------------------

num_rows = 3000
np.random.seed(42)

ages = np.random.randint(21, 90, size=num_rows)
genders = np.random.choice(["M", "F"], size=num_rows)

drug_names = ["Lantus", "Ozempic", "Eliquis", "Humira", "Enbrel", "Trulicity", "Xarelto", "Stelara", "Farxiga", "Repatha"]
drug_classes = ["Insulin", "GLP-1", "DOAC", "Anti-TNF", "Anti-TNF", "GLP-1", "DOAC", "Biologic", "SGLT2", "PCSK9"]

dx_codes = ["E11.9", "E11.65", "I48.0", "K50.90", "L40.0", "I63.9", "K51.90", "E11.22", "E78.5"]
dx_categories = ["Type 2 Diabetes", "Type 2 Diabetes", "Atrial Fibrillation", "Crohns Disease", "Psoriasis",
                 "Stroke", "Ulcerative Colitis", "Diabetes CKD", "Hyperlipidemia"]

specialties = ["Endocrinology", "Internal Medicine", "Cardiology", "Gastroenterology",
               "Dermatology", "Family Medicine", "Neurology", "Nephrology"]

plan_types = ["Commercial", "Medicare", "Exchange"]

outcomes = ["approve", "deny", "info_needed"]

df = pd.DataFrame({
    "request_id": np.arange(1, num_rows + 1),
    "patient_id": np.random.randint(1000, 9999, size=num_rows),
    "age": ages,
    "gender": genders,
    "drug_name": np.random.choice(drug_names, size=num_rows),
    "drug_class": np.random.choice(drug_classes, size=num_rows),
    "dx_code": np.random.choice(dx_codes, size=num_rows),
    "dx_category": np.random.choice(dx_categories, size=num_rows),
    "prescriber_specialty": np.random.choice(specialties, size=num_rows),
    "formulary_tier": np.random.randint(1, 5, size=num_rows),
    "step_therapy_count": np.random.randint(0, 3, size=num_rows),
    "quantity_limit_flag": np.random.randint(0, 2, size=num_rows),
    "previous_pa_denials": np.random.randint(0, 4, size=num_rows),
    "days_supply": np.random.choice([28, 30, 56, 90], size=num_rows),
    "prior_fill_history_months": np.random.randint(0, 24, size=num_rows),
    "plan_type": np.random.choice(plan_types, size=num_rows),
    "outcome": np.random.choice(outcomes, size=num_rows)
})

# Save file
output_path = os.path.join("..", "data", "pa_synthetic_data.csv")
df.to_csv(output_path, index=False)

print(f"Saved {output_path} with {len(df)} rows")

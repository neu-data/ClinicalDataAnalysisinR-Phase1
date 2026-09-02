# -*- coding: utf-8 -*-
"""
Generate the synthetic clinical dataset for the Clinical Data Analysis in R
pre-course preparation package.

Outputs (written next to this script, in Course_Preparation/Data/):
  clinical_data_raw.csv     - messy version WITH deliberate data-quality problems
  clinical_data_raw.xlsx    - same, as Excel (for read_excel practice)
  clinical_data_clean.csv   - tidy, analysis-ready version

The dataset is fully synthetic. No real patient data is used.
A fixed random seed makes it reproducible.

Design goals (so the teaching models are interpretable, not random noise):
  * hypertension probability increases with age and BMI (and diabetes)
  * diabetes relates to glucose
  * treatment (antihypertensive therapy) is more common in older / hypertensive
  * the follow-up event (cardiovascular event or death) risk rises with
    age and comorbidity, and treatment lowers it
The clean file is exactly the result of the cleaning steps taught in
04_Data_Management, so participants can reproduce it themselves.
"""

import numpy as np
import pandas as pd

SEED = 20260907          # course start week - reproducible
rng = np.random.default_rng(SEED)

N = 430                  # clean patients target (before we add duplicates)

# ----------------------------------------------------------------------------
# 1. Demographics
# ----------------------------------------------------------------------------
age = np.clip(rng.normal(55, 13, N), 30, 88).round().astype(int)
sex = rng.choice(["Female", "Male"], size=N, p=[0.54, 0.46])

# Height depends on sex; weight is drawn from a target BMI so BMI is consistent
height_cm = np.where(sex == "Male",
                     rng.normal(170, 7, N),
                     rng.normal(158, 6.5, N)).round(0)

bmi_target = np.clip(rng.normal(26.5, 4.6, N), 16, 44)
weight_kg = (bmi_target * (height_cm / 100) ** 2).round(1)
# recompute BMI from the recorded weight/height so it is internally consistent
bmi = (weight_kg / (height_cm / 100) ** 2).round(1)

# ----------------------------------------------------------------------------
# 2. Behavioural
# ----------------------------------------------------------------------------
smoking = rng.choice(["Never", "Former", "Current"], size=N, p=[0.55, 0.27, 0.18])
alcohol_use = rng.choice(["None", "Moderate", "Heavy"], size=N, p=[0.5, 0.38, 0.12])

# ----------------------------------------------------------------------------
# 3. Diabetes  (depends on age and BMI)  ->  drives glucose
# ----------------------------------------------------------------------------
z_age = (age - 55) / 10.0
z_bmi = (bmi - 26.5) / 5.0

lin_dm = -1.9 + 0.55 * z_age + 0.75 * z_bmi
p_dm = 1 / (1 + np.exp(-lin_dm))
diabetes = rng.binomial(1, p_dm)

# fasting glucose (mmol/L): higher when diabetic
glucose = np.where(diabetes == 1,
                   rng.normal(8.8, 1.8, N),
                   rng.normal(5.3, 0.6, N))
glucose = np.clip(glucose, 3.5, 20).round(1)

# total cholesterol (mmol/L): rises gently with age and BMI
cholesterol = np.clip(4.6 + 0.35 * z_age + 0.30 * z_bmi + rng.normal(0, 0.8, N),
                      2.5, 9.5).round(1)

# ----------------------------------------------------------------------------
# 4. Hypertension  (depends on age, BMI, diabetes)  ->  drives blood pressure
# ----------------------------------------------------------------------------
lin_htn = -0.7 + 0.7 * z_age + 0.6 * z_bmi + 0.7 * diabetes + 0.25 * (smoking == "Current")
p_htn = 1 / (1 + np.exp(-lin_htn))
hypertension = rng.binomial(1, p_htn)

systolic_bp = np.clip(118 + 16 * hypertension + 4 * z_age + 3 * z_bmi + rng.normal(0, 8, N),
                      90, 210).round().astype(int)
diastolic_bp = np.clip(74 + 9 * hypertension + 1.5 * z_age + 2 * z_bmi + rng.normal(0, 6, N),
                       55, 130).round().astype(int)

# ----------------------------------------------------------------------------
# 5. Treatment  (antihypertensive therapy: more likely if hypertensive/older)
# ----------------------------------------------------------------------------
lin_tx = -0.4 + 1.8 * hypertension + 0.4 * z_age - 0.2 * (alcohol_use == "Heavy")
p_tx = 1 / (1 + np.exp(-lin_tx))
treatment = np.where(rng.binomial(1, p_tx) == 1, "Treated", "Untreated")

# ----------------------------------------------------------------------------
# 6. Hospital site
# ----------------------------------------------------------------------------
hospital = rng.choice(
    ["Central Hospital", "Northern District", "Riverside Clinic",
     "Eastgate Medical", "Lakeside Health"],
    size=N, p=[0.28, 0.22, 0.2, 0.16, 0.14])

# ----------------------------------------------------------------------------
# 7. Follow-up outcome (survival): event = CV event or death within follow-up
#    Hazard rises with age, diabetes, hypertension, BMI; treatment lowers it.
# ----------------------------------------------------------------------------
lin_surv = (-0.4 + 0.55 * z_age + 0.55 * diabetes + 0.45 * hypertension
            + 0.25 * z_bmi - 0.6 * (treatment == "Treated"))
rate = 0.020 * np.exp(lin_surv)                 # monthly hazard (exponential)
event_time = rng.exponential(1 / rate)          # months until event
admin_censor = 24.0                             # study follow-up window (months)
outcome = (event_time <= admin_censor).astype(int)
time_to_event = np.minimum(event_time, admin_censor).round(1)

# admission and follow-up dates
start_pool = pd.to_datetime("2023-01-01")
admit_offset = rng.integers(0, 540, N)          # spread over ~18 months
admission_date = start_pool + pd.to_timedelta(admit_offset, unit="D")
followup_date = admission_date + pd.to_timedelta((time_to_event * 30.44).round(), unit="D")

patient_id = np.array([f"P{1000 + i}" for i in range(N)])

# ----------------------------------------------------------------------------
# Assemble the CLEAN dataframe
# ----------------------------------------------------------------------------
clean = pd.DataFrame({
    "patient_id": patient_id,
    "age": age,
    "sex": sex,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "BMI": bmi,
    "smoking": smoking,
    "alcohol_use": alcohol_use,
    "systolic_bp": systolic_bp,
    "diastolic_bp": diastolic_bp,
    "hypertension": np.where(hypertension == 1, "Yes", "No"),
    "diabetes": np.where(diabetes == 1, "Yes", "No"),
    "glucose": glucose,
    "cholesterol": cholesterol,
    "treatment": treatment,
    "hospital": hospital,
    "admission_date": admission_date.strftime("%Y-%m-%d"),
    "followup_date": followup_date.strftime("%Y-%m-%d"),
    "outcome": outcome,                          # 1 = event, 0 = censored
    "time_to_event": time_to_event,              # months
})

# ----------------------------------------------------------------------------
# Build the RAW (messy) dataframe: start from clean, then inject problems.
# Everything injected here is documented in Data_Quality_Problems.md and fixed
# by the cleaning taught in 04_Data_Management.
# ----------------------------------------------------------------------------
raw = clean.copy().astype(object)


def idx(seed_positions):
    return list(seed_positions)


# (a) Inconsistent categorical coding -------------------------------------
# sex: mix of codings
sex_map_choices = {"Female": ["Female", "female", "F", "f"],
                   "Male": ["Male", "male", "M", "m"]}
raw["sex"] = [rng.choice(sex_map_choices[s]) for s in clean["sex"]]
# hypertension / diabetes: mix Yes/No with 1/0 and yes/no
for col in ["hypertension", "diabetes"]:
    newvals = []
    for v in clean[col]:
        r = rng.random()
        if r < 0.6:
            newvals.append(v)                    # "Yes"/"No"
        elif r < 0.8:
            newvals.append("1" if v == "Yes" else "0")
        else:
            newvals.append(v.lower())            # "yes"/"no"
    raw[col] = newvals
# smoking: introduce a stray coding
raw.loc[raw.sample(6, random_state=1).index, "smoking"] = "current"

# (b) Missing values -------------------------------------------------------
for col, k in [("glucose", 22), ("cholesterol", 18), ("alcohol_use", 12),
               ("BMI", 9), ("followup_date", 7), ("diastolic_bp", 5)]:
    miss_idx = rng.choice(N, size=k, replace=False)
    raw.loc[miss_idx, col] = np.nan

# (c) Impossible / extreme values (teaching outliers) ----------------------
raw.loc[3, "age"] = 219                           # impossible age
raw.loc[47, "age"] = 2                            # implausible adult age
raw.loc[88, "height_cm"] = 17                     # impossible height -> crazy BMI
raw.loc[88, "BMI"] = round(float(raw.loc[88, "weight_kg"]) / (17/100)**2, 1)
raw.loc[120, "BMI"] = 4.2                         # impossible BMI
raw.loc[201, "weight_kg"] = 400                   # impossible weight
raw.loc[15, "glucose"] = 41.0                     # extreme lab value
raw.loc[260, "cholesterol"] = -3.0                # impossible negative lab
raw.loc[305, "systolic_bp"] = 350                 # impossible BP

# (d) Date inconsistency: follow-up before admission -----------------------
for i in [9, 133]:
    raw.loc[i, "followup_date"] = (
        pd.to_datetime(clean.loc[i, "admission_date"]) - pd.to_timedelta(40, "D")
    ).strftime("%Y-%m-%d")

# (e) Duplicate records ----------------------------------------------------
dups = raw.loc[[10, 25, 77]].copy()               # 3 exact duplicate rows
raw = pd.concat([raw, dups], ignore_index=True)
# shuffle raw row order so duplicates are not obviously adjacent
raw = raw.sample(frac=1, random_state=7).reset_index(drop=True)

# ----------------------------------------------------------------------------
# Write files
# ----------------------------------------------------------------------------
import os
HERE = os.path.dirname(os.path.abspath(__file__))
raw.to_csv(os.path.join(HERE, "clinical_data_raw.csv"), index=False, na_rep="NA")
raw.to_excel(os.path.join(HERE, "clinical_data_raw.xlsx"), index=False)
clean.to_csv(os.path.join(HERE, "clinical_data_clean.csv"), index=False, na_rep="NA")

print("Wrote clinical_data_raw.csv   rows =", len(raw))
print("Wrote clinical_data_raw.xlsx")
print("Wrote clinical_data_clean.csv rows =", len(clean))
print("\n--- quick signal check (clean) ---")
print("hypertension prevalence:", round((clean.hypertension == 'Yes').mean(), 3))
print("diabetes prevalence:    ", round((clean.diabetes == 'Yes').mean(), 3))
print("treated proportion:     ", round((clean.treatment == 'Treated').mean(), 3))
print("event rate:             ", round(clean.outcome.mean(), 3))
print("mean glucose DM vs no:  ",
      round(clean.loc[clean.diabetes == 'Yes', 'glucose'].mean(), 2), "vs",
      round(clean.loc[clean.diabetes == 'No', 'glucose'].mean(), 2))

"""
Generate the simulated clinical dataset for the course:
"Determinants of Hypertension Treatment Uptake among Adults attending
 Primary Healthcare Facilities" - a multicentre cross-sectional study.

Produces:
  hypertension_phc_raw.csv   - the "raw" messy dataset used in Days 1-2 (import/clean)
  hypertension_phc_raw.xlsx  - same, Excel version (Day 1 imports both)
  hypertension_phc_clean.csv - a tidy reference version (for instructor/solutions)

The raw file deliberately contains realistic data-quality problems so the
Day 2 cleaning exercise is meaningful: mixed category spellings, several
Yes/No codings, missing-value sentinels (blank, "NA", 999, -99),
implausible values, trailing spaces, a couple of duplicate IDs, and
mixed date formats.

A real signal is embedded so that logistic regression on Days 4-5 recovers
sensible determinants of treatment uptake (age, diabetes, family history,
knowledge, insurance, education, residence).

Run:  python generate_dataset.py
Seed is fixed for full reproducibility.
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(20260628)
N = 1500

# ----------------------------------------------------------------------
# 1. Facilities (6 primary healthcare facilities, multicentre)
# ----------------------------------------------------------------------
facilities = [
    "Bugando PHC", "Kisesa HC", "Nyamagana PHC",
    "Ilemela HC", "Buzuruga PHC", "Igoma HC",
]
facility_p = [0.22, 0.15, 0.20, 0.18, 0.13, 0.12]
facility = RNG.choice(facilities, size=N, p=facility_p)

# ----------------------------------------------------------------------
# 2. Demographics
# ----------------------------------------------------------------------
age = np.clip(RNG.normal(52, 14, N), 18, 95).round().astype(int)
sex = RNG.choice(["Female", "Male"], size=N, p=[0.58, 0.42])
residence = RNG.choice(["Urban", "Rural"], size=N, p=[0.55, 0.45])
education = RNG.choice(
    ["None", "Primary", "Secondary", "Tertiary"], size=N, p=[0.18, 0.40, 0.30, 0.12]
)
occupation = RNG.choice(
    ["Unemployed", "Farmer", "Trader", "Professional", "Other"],
    size=N, p=[0.18, 0.30, 0.27, 0.13, 0.12],
)
marital = RNG.choice(
    ["Single", "Married", "Divorced", "Widowed"], size=N, p=[0.16, 0.62, 0.10, 0.12]
)
insurance = RNG.choice(["Yes", "No"], size=N, p=[0.34, 0.66])

# ----------------------------------------------------------------------
# 3. Anthropometry
# ----------------------------------------------------------------------
height_cm = np.where(
    sex == "Male", RNG.normal(170, 7, N), RNG.normal(160, 6, N)
).round(1)
bmi_true = np.clip(RNG.normal(26.5, 4.8, N), 15, 48)
weight_kg = (bmi_true * (height_cm / 100) ** 2).round(1)

# ----------------------------------------------------------------------
# 4. Behavioural / clinical risk factors
# ----------------------------------------------------------------------
smoking = RNG.choice(["Never", "Former", "Current"], size=N, p=[0.62, 0.20, 0.18])
alcohol = RNG.choice(["None", "Moderate", "Heavy"], size=N, p=[0.55, 0.33, 0.12])
phys_act = RNG.choice(["Low", "Moderate", "High"], size=N, p=[0.45, 0.40, 0.15])
family_hx = RNG.choice(["Yes", "No"], size=N, p=[0.38, 0.62])

# diabetes more likely with higher BMI and age
diab_lin = -4.0 + 0.04 * (age - 50) + 0.10 * (bmi_true - 26)
diabetes = (RNG.random(N) < 1 / (1 + np.exp(-diab_lin))).astype(int)

# ----------------------------------------------------------------------
# 5. Blood pressure (all attendees screened; many hypertensive)
# ----------------------------------------------------------------------
sbp = (RNG.normal(138, 18, N) + 0.25 * (age - 50) + 2.5 * diabetes
       + 1.5 * (bmi_true - 26)).round().astype(int)
dbp = (RNG.normal(86, 11, N) + 0.10 * (age - 50) + 1.2 * diabetes).round().astype(int)
sbp = np.clip(sbp, 90, 220)
dbp = np.clip(dbp, 55, 130)

# Hypertension diagnosed if BP elevated OR already on record
htn_diagnosed = ((sbp >= 140) | (dbp >= 90) | (RNG.random(N) < 0.15)).astype(int)

# ----------------------------------------------------------------------
# 6. Laboratory biomarkers (mmol/L unless noted)
# ----------------------------------------------------------------------
tot_chol = np.clip(RNG.normal(5.1, 1.0, N) + 0.02 * (bmi_true - 26), 2.8, 9.5).round(1)
hdl = np.clip(RNG.normal(1.3, 0.35, N), 0.5, 3.0).round(2)
ldl = np.clip(tot_chol - hdl - RNG.normal(1.1, 0.3, N), 1.0, 7.0).round(1)
trig = np.clip(RNG.normal(1.7, 0.7, N) + 0.05 * (bmi_true - 26), 0.4, 8.0).round(1)
fasting_glucose = np.clip(
    RNG.normal(5.4, 0.9, N) + 2.6 * diabetes, 3.0, 22.0
).round(1)
creatinine = np.clip(RNG.normal(82, 18, N) + 0.3 * (age - 50), 40, 220).round().astype(int)  # umol/L
sodium = np.clip(RNG.normal(139, 3, N), 125, 150).round().astype(int)
potassium = np.clip(RNG.normal(4.2, 0.45, N), 2.8, 6.2).round(1)

# ----------------------------------------------------------------------
# 7. Knowledge, access, comorbidity
# ----------------------------------------------------------------------
knowledge = np.clip(
    RNG.normal(10, 3.5, N) + 1.5 * (education == "Tertiary")
    + 0.8 * (education == "Secondary"), 0, 20
).round().astype(int)
distance_km = np.clip(RNG.exponential(6, N) + (residence == "Rural") * 4, 0.2, 60).round(1)
comorbidity = (diabetes
               + (tot_chol > 6.2).astype(int)
               + (bmi_true >= 30).astype(int)
               + RNG.binomial(1, 0.15, N)).astype(int)

# ----------------------------------------------------------------------
# 8. PRIMARY OUTCOME: treatment uptake (on antihypertensive therapy)
#    Only meaningful for those diagnosed hypertensive; embed real signal.
# ----------------------------------------------------------------------
edu_rank = pd.Series(education).map(
    {"None": 0, "Primary": 1, "Secondary": 2, "Tertiary": 3}
).to_numpy()

uptake_lin = (
    -1.30
    + 0.030 * (age - 50)                       # older -> more uptake
    + 0.85 * diabetes                          # diabetes -> more uptake
    + 0.55 * (family_hx == "Yes")              # family history -> more uptake
    + 0.70 * (insurance == "Yes")              # insurance -> more uptake
    + 0.30 * edu_rank                          # education gradient
    + 0.45 * (residence == "Urban")            # urban -> more uptake
    + 0.075 * (knowledge - 10)                 # knowledge -> more uptake
    - 0.020 * distance_km                      # distance -> less uptake
    + 0.010 * (sbp - 140)                      # higher BP -> more uptake
)
uptake_p = 1 / (1 + np.exp(-uptake_lin))
treatment_uptake = np.where(
    htn_diagnosed == 1,
    (RNG.random(N) < uptake_p).astype(int),
    0,
)

# Adherence: only defined among those on treatment
adher_lin = -0.2 + 0.06 * (knowledge - 10) + 0.5 * (insurance == "Yes") - 0.03 * distance_km
adherence = np.where(
    treatment_uptake == 1,
    np.where(RNG.random(N) < 1 / (1 + np.exp(-adher_lin)), "Good", "Poor"),
    "",  # not applicable -> blank in raw
)

# BP controlled: among treated, some achieve control
bp_controlled = np.where(
    treatment_uptake == 1,
    np.where((sbp < 140) & (dbp < 90), "Yes", "No"),
    "",
)

months_since_dx = np.where(
    htn_diagnosed == 1, RNG.integers(1, 120, N), 0
)

# ----------------------------------------------------------------------
# 9. Dates (enrolment) - mixed formats for cleaning practice
# ----------------------------------------------------------------------
start = np.datetime64("2024-01-08")
offsets = RNG.integers(0, 330, N)
dates = start + offsets.astype("timedelta64[D]")
# Most ISO, a chunk dd/mm/yyyy, a few with month names
date_strings = []
for i, d in enumerate(dates):
    ts = pd.Timestamp(d)
    r = RNG.random()
    if r < 0.70:
        date_strings.append(ts.strftime("%Y-%m-%d"))
    elif r < 0.92:
        date_strings.append(ts.strftime("%d/%m/%Y"))
    else:
        date_strings.append(ts.strftime("%d-%b-%Y"))

# ----------------------------------------------------------------------
# 10. Assemble tidy frame first
# ----------------------------------------------------------------------
pid = [f"PHC-{i:04d}" for i in range(1, N + 1)]
df = pd.DataFrame({
    "patient_id": pid,
    "facility": facility,
    "enroll_date": date_strings,
    "age": age,
    "sex": sex,
    "residence": residence,
    "education": education,
    "occupation": occupation,
    "marital_status": marital,
    "health_insurance": insurance,
    "height_cm": height_cm,
    "weight_kg": weight_kg,
    "bmi": (weight_kg / (height_cm / 100) ** 2).round(1),
    "smoking": smoking,
    "alcohol": alcohol,
    "physical_activity": phys_act,
    "family_history_htn": family_hx,
    "diabetes": diabetes,
    "sbp_mmhg": sbp,
    "dbp_mmhg": dbp,
    "total_chol_mmol_l": tot_chol,
    "hdl_mmol_l": hdl,
    "ldl_mmol_l": ldl,
    "triglycerides_mmol_l": trig,
    "fasting_glucose_mmol_l": fasting_glucose,
    "creatinine_umol_l": creatinine,
    "sodium_mmol_l": sodium,
    "potassium_mmol_l": potassium,
    "knowledge_score": knowledge,
    "distance_to_facility_km": distance_km,
    "comorbidity_count": comorbidity,
    "htn_diagnosed": htn_diagnosed,
    "months_since_diagnosis": months_since_dx,
    "treatment_uptake": treatment_uptake,
    "adherence": adherence,
    "bp_controlled": bp_controlled,
})

# Save the tidy reference (clean) version with Yes/No for binaries
clean = df.copy()
clean["diabetes"] = np.where(clean["diabetes"] == 1, "Yes", "No")
clean["htn_diagnosed"] = np.where(clean["htn_diagnosed"] == 1, "Yes", "No")
clean["treatment_uptake"] = np.where(clean["treatment_uptake"] == 1, "Yes", "No")
clean.to_csv("hypertension_phc_clean.csv", index=False)

# ----------------------------------------------------------------------
# 11. Introduce realistic messiness into the RAW version
# ----------------------------------------------------------------------
raw = df.copy().astype(object)  # object dtype so string sentinels can be injected

# 11a. Mixed sex codings
def mess_sex(v, i):
    pool = {"Female": ["Female", "F", "female", "f"], "Male": ["Male", "M", "male", "m"]}
    return RNG.choice(pool[v]) if RNG.random() < 0.30 else v
raw["sex"] = [mess_sex(v, i) for i, v in enumerate(raw["sex"])]

# 11b. Binary vars to mixed Yes/No/1/0/Y/N
def mess_yn(series_vals):
    out = []
    for v in series_vals:
        base = "Yes" if v in (1, "Yes") else "No"
        r = RNG.random()
        if r < 0.15:
            out.append("1" if base == "Yes" else "0")
        elif r < 0.25:
            out.append("Y" if base == "Yes" else "N")
        else:
            out.append(base)
    return out
raw["diabetes"] = mess_yn(df["diabetes"].tolist())
raw["family_history_htn"] = mess_yn(df["family_history_htn"].tolist())
raw["health_insurance"] = mess_yn(df["health_insurance"].tolist())
raw["htn_diagnosed"] = mess_yn(df["htn_diagnosed"].tolist())
raw["treatment_uptake"] = mess_yn(df["treatment_uptake"].tolist())

# 11c. Trailing/leading spaces in some categorical text
for col in ["facility", "residence", "education", "occupation"]:
    mask = RNG.random(N) < 0.08
    raw.loc[mask, col] = " " + raw.loc[mask, col].astype(str) + " "

# 11d. Missing-value sentinels scattered across selected columns
def inject_missing(col, frac, sentinels):
    idx = RNG.choice(N, size=int(frac * N), replace=False)
    raw.loc[idx, col] = [RNG.choice(sentinels) for _ in idx]

inject_missing("bmi", 0.04, ["", "NA", "999"])
inject_missing("weight_kg", 0.03, ["", "NA"])
inject_missing("total_chol_mmol_l", 0.06, ["", "NA", "-99"])
inject_missing("ldl_mmol_l", 0.07, ["", "NA"])
inject_missing("fasting_glucose_mmol_l", 0.05, ["", "999"])
inject_missing("knowledge_score", 0.03, ["", "NA"])
inject_missing("education", 0.02, [""])
inject_missing("smoking", 0.03, ["", "NA"])
inject_missing("distance_to_facility_km", 0.04, ["", "NA"])

# 11e. Implausible values (data-entry errors) to be caught in validation
err_idx = RNG.choice(N, size=8, replace=False)
raw.loc[err_idx[0], "age"] = 200
raw.loc[err_idx[1], "age"] = 0
raw.loc[err_idx[2], "sbp_mmhg"] = 0
raw.loc[err_idx[3], "sbp_mmhg"] = 700
raw.loc[err_idx[4], "weight_kg"] = 7        # impossible adult weight
raw.loc[err_idx[5], "height_cm"] = 17       # decimal-point error (1.7m -> 17)
raw.loc[err_idx[6], "dbp_mmhg"] = 5
raw.loc[err_idx[7], "bmi"] = 120

# 11f. A few duplicate records (same patient entered twice)
dups = raw.iloc[[10, 250, 880]].copy()
raw = pd.concat([raw, dups], ignore_index=True)
# shuffle so duplicates aren't adjacent
raw = raw.sample(frac=1, random_state=7).reset_index(drop=True)

# ----------------------------------------------------------------------
# 12. Write raw outputs
# ----------------------------------------------------------------------
raw.to_csv("hypertension_phc_raw.csv", index=False)
with pd.ExcelWriter("hypertension_phc_raw.xlsx", engine="openpyxl") as xl:
    raw.to_excel(xl, index=False, sheet_name="data")

print(f"Rows written (raw): {len(raw)}  (includes 3 duplicate records)")
print(f"Rows written (clean reference): {len(clean)}")
print("Treatment uptake (clean, diagnosed only):")
diag = clean[clean['htn_diagnosed'] == 'Yes']
print(diag['treatment_uptake'].value_counts())
print("Overall HTN diagnosed:", (clean['htn_diagnosed'] == 'Yes').sum())
print("Files: hypertension_phc_raw.csv / .xlsx, hypertension_phc_clean.csv")

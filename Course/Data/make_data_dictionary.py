"""Generate the data dictionary (CSV + Markdown) for the hypertension PHC dataset."""
import pandas as pd

# variable, label, type, units/coding, role, notes (incl. raw-file quirks)
rows = [
("patient_id","Patient identifier","Character","PHC-0001 ... PHC-1500","ID","Unique per patient. Raw file contains 3 duplicate records to be removed."),
("facility","Healthcare facility","Categorical","6 PHC facilities","Cluster/covariate","Multicentre design. Some values have leading/trailing spaces in raw file."),
("enroll_date","Date of enrolment","Date","Mixed: YYYY-MM-DD, DD/MM/YYYY, DD-Mon-YYYY","Metadata","Mixed formats in raw file; parse on Day 2."),
("age","Age","Numeric","Years","Predictor","Implausible values (0, 200) present in raw file."),
("sex","Sex","Categorical","Female / Male","Predictor","Raw file mixes F/f/female and M/m/male spellings."),
("residence","Place of residence","Categorical","Urban / Rural","Predictor","Determinant of uptake."),
("education","Highest education","Ordinal","None < Primary < Secondary < Tertiary","Predictor","Set as ordered factor. Some blanks in raw file."),
("occupation","Occupation","Categorical","Unemployed/Farmer/Trader/Professional/Other","Predictor",""),
("marital_status","Marital status","Categorical","Single/Married/Divorced/Widowed","Predictor",""),
("health_insurance","Has health insurance","Binary","Yes / No","Predictor","Raw file mixes Yes/No/Y/N/1/0. Determinant of uptake."),
("height_cm","Height","Numeric","centimetres","Derived input","Used to compute BMI. One decimal-point error (17)."),
("weight_kg","Weight","Numeric","kilograms","Derived input","Missing sentinels (NA, blank). One impossible value (7)."),
("bmi","Body mass index","Numeric","kg/m^2","Predictor","Provided but contains errors/missing; recompute from height & weight."),
("smoking","Smoking status","Categorical","Never / Former / Current","Predictor","Some missing in raw file."),
("alcohol","Alcohol intake","Categorical","None / Moderate / Heavy","Predictor",""),
("physical_activity","Physical activity level","Ordinal","Low / Moderate / High","Predictor",""),
("family_history_htn","Family history of hypertension","Binary","Yes / No","Predictor","Mixed coding in raw file. Determinant of uptake."),
("diabetes","Diabetes mellitus","Binary","Yes / No","Predictor","Mixed coding in raw file. Strong determinant of uptake."),
("sbp_mmhg","Systolic blood pressure","Numeric","mmHg","Clinical","Implausible values (0, 700) present in raw file."),
("dbp_mmhg","Diastolic blood pressure","Numeric","mmHg","Clinical","Implausible value (5) present in raw file."),
("total_chol_mmol_l","Total cholesterol","Numeric","mmol/L","Lab biomarker","Missing sentinels: NA, blank, -99."),
("hdl_mmol_l","HDL cholesterol","Numeric","mmol/L","Lab biomarker",""),
("ldl_mmol_l","LDL cholesterol","Numeric","mmol/L","Lab biomarker","Missing sentinels present."),
("triglycerides_mmol_l","Triglycerides","Numeric","mmol/L","Lab biomarker",""),
("fasting_glucose_mmol_l","Fasting glucose","Numeric","mmol/L","Lab biomarker","Missing sentinel 999 present."),
("creatinine_umol_l","Serum creatinine","Numeric","umol/L","Lab biomarker",""),
("sodium_mmol_l","Serum sodium","Numeric","mmol/L","Lab biomarker",""),
("potassium_mmol_l","Serum potassium","Numeric","mmol/L","Lab biomarker",""),
("knowledge_score","Hypertension knowledge score","Numeric","0-20","Predictor","Higher = better knowledge. Determinant of uptake."),
("distance_to_facility_km","Distance to facility","Numeric","kilometres","Predictor","Access barrier. Some missing."),
("comorbidity_count","Number of comorbidities","Count","0+","Predictor",""),
("htn_diagnosed","Diagnosed hypertensive","Binary","Yes / No","Filter","Defines analysis population for uptake (Days 4-5)."),
("months_since_diagnosis","Months since HTN diagnosis","Numeric","Months","Predictor","0 if not diagnosed."),
("treatment_uptake","On antihypertensive treatment","Binary","Yes / No","PRIMARY OUTCOME","Mixed coding in raw file. Analysed among diagnosed patients."),
("adherence","Treatment adherence","Categorical","Good / Poor (blank if untreated)","Secondary outcome","Only defined where treatment_uptake = Yes."),
("bp_controlled","Blood pressure controlled","Binary","Yes / No (blank if untreated)","Secondary outcome","SBP<140 and DBP<90 among treated."),
]

dd = pd.DataFrame(rows, columns=["variable","label","type","units_coding","role","notes"])
dd.to_csv("data_dictionary.csv", index=False)

# Markdown version
with open("data_dictionary.md","w",encoding="utf-8") as f:
    f.write("# Data Dictionary\n\n")
    f.write("**Study:** Determinants of Hypertension Treatment Uptake among Adults "
            "attending Primary Healthcare Facilities\n\n")
    f.write("**Design:** Multicentre cross-sectional study, 6 primary healthcare "
            "facilities, 1,500 adult attendees.\n\n")
    f.write("**Files:** `hypertension_phc_raw.csv` / `.xlsx` (used Days 1-2), "
            "`hypertension_phc_clean.csv` (tidy reference).\n\n")
    f.write("**Primary outcome:** `treatment_uptake` (currently on antihypertensive "
            "therapy), analysed among patients with `htn_diagnosed = Yes`.\n\n")
    f.write("| # | Variable | Label | Type | Units / Coding | Role | Notes |\n")
    f.write("|---|----------|-------|------|----------------|------|-------|\n")
    for i,r in enumerate(rows,1):
        f.write("| "+str(i)+" | `"+r[0]+"` | "+r[1]+" | "+r[2]+" | "+r[3]+" | "+r[4]+" | "+r[5]+" |\n")
    f.write("\n## Known data-quality issues in the raw file (for the Day 2 cleaning exercise)\n\n")
    f.write("- **Inconsistent category spellings:** `sex` coded as Female/F/female/f and Male/M/male/m.\n")
    f.write("- **Mixed binary codings:** `diabetes`, `family_history_htn`, `health_insurance`, "
            "`htn_diagnosed`, `treatment_uptake` mix Yes/No, Y/N and 1/0.\n")
    f.write("- **Missing-value sentinels:** blank, `NA`, `999`, `-99` in several numeric columns.\n")
    f.write("- **Implausible values:** `age` 0 and 200; `sbp_mmhg` 0 and 700; `weight_kg` 7; "
            "`height_cm` 17; `dbp_mmhg` 5.\n")
    f.write("- **Whitespace:** leading/trailing spaces in some `facility`, `residence`, "
            "`education`, `occupation` values.\n")
    f.write("- **Duplicates:** 3 duplicate patient records (1,503 rows, 1,500 unique IDs).\n")
    f.write("- **Mixed date formats** in `enroll_date`.\n")

print("Wrote data_dictionary.csv and data_dictionary.md (", len(rows), "variables )")

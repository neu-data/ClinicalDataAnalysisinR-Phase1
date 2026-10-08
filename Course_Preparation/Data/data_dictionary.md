# Data Dictionary: Pre-course Clinical Dataset

**Files:** `clinical_data_raw.csv` (messy), `clinical_data_clean.csv` (analysis-ready), `clinical_data_raw.xlsx` (Excel copy of the raw file)

This is a **fully synthetic** dataset created for teaching. It contains **no real patient data**. It describes 430 adult patients recruited at five primary-care / hospital facilities, each followed for up to 24 months for a cardiovascular event or death.

> **Units note:** `glucose` and `cholesterol` are in **mmol/L** (the units used in most of the world). Fasting glucose ≥ 7.0 mmol/L and total cholesterol ≥ 5.0 mmol/L are common clinical reference points.

| # | Variable | Label | Type | Units / values | Description |
|---|----------|-------|------|----------------|-------------|
| 1 | `patient_id` | Patient identifier | text | P1000–P1429 | Unique anonymous ID |
| 2 | `age` | Age | integer | years (30–88) | Age at admission |
| 3 | `sex` | Sex | categorical | Female / Male | Biological sex |
| 4 | `weight_kg` | Weight | numeric | kilograms | Measured body weight |
| 5 | `height_cm` | Height | numeric | centimetres | Measured height |
| 6 | `BMI` | Body Mass Index | numeric | kg/m² | `weight_kg / (height_cm/100)^2` |
| 7 | `smoking` | Smoking status | categorical | Never / Former / Current | Self-reported |
| 8 | `alcohol_use` | Alcohol use | categorical | None / Moderate / Heavy | Self-reported |
| 9 | `systolic_bp` | Systolic BP | integer | mmHg | Systolic blood pressure |
| 10 | `diastolic_bp` | Diastolic BP | integer | mmHg | Diastolic blood pressure |
| 11 | `hypertension` | Hypertension | categorical | Yes / No | Diagnosed hypertension |
| 12 | `diabetes` | Diabetes | categorical | Yes / No | Diagnosed diabetes |
| 13 | `glucose` | Fasting glucose | numeric | mmol/L | Fasting plasma glucose |
| 14 | `cholesterol` | Total cholesterol | numeric | mmol/L | Total serum cholesterol |
| 15 | `treatment` | Treatment group | categorical | Treated / Untreated | Received antihypertensive treatment |
| 16 | `hospital` | Recruiting hospital | categorical | 5 facilities | Recruitment site |
| 17 | `admission_date` | Admission date | date | YYYY-MM-DD | Enrolment / admission date |
| 18 | `followup_date` | Follow-up date | date | YYYY-MM-DD | Last follow-up or event date |
| 19 | `outcome` | Follow-up event | integer | 0 / 1 | 1 = cardiovascular event or death; 0 = event-free (censored) |
| 20 | `time_to_event` | Time to event | numeric | months (0–24) | Months from admission to event or censoring |

## How the variables relate (the built-in "truth")

The data were simulated so the statistical models produce **realistic, interpretable** results rather than noise:

- **Hypertension** becomes more likely with higher **age** and **BMI**, and in patients with **diabetes**.
- **Diabetes** is strongly reflected in **fasting glucose** (diabetic patients have much higher glucose).
- **Blood pressure** rises with age, BMI and hypertension.
- **Treatment** is given mostly to hypertensive and older patients.
- The **follow-up event** (`outcome` / `time_to_event`) becomes more likely with older age, diabetes and hypertension, and **treatment lowers the risk**.

These relationships are what your analyses during the course will *rediscover* from the data.

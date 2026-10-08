# Expected Results: Reference Answers (Instructor / Self-check)

All numbers below come from running the supplied code on `clinical_data_clean.csv`
(and `clinical_data_raw.csv` for the raw checks). They are reproducible from the
fixed random seed in `Data/generate_precourse_data.py`. Use them to check that a
participant's installation and code are producing the right answers.

## Raw file (`clinical_data_raw.csv`)
- Rows: **433**; unique patients: **430**; exact duplicate rows: **3**
- Missing values per column: `BMI` 9, `alcohol_use` 12, `diastolic_bp` 5, `glucose` 22, `cholesterol` 18, `followup_date` 7
- `sex` codings present: `f, F, female, Female, m, M, male, Male`

## Clean file (`clinical_data_clean.csv`)
- Rows: **430**; variables: **20**
- Mean age: **54.2** years (SD 12.5)
- Median BMI: **26.6** kg/m² (IQR 23.4–29.6)
- Proportion female: **54.7 %**
- Hypertension prevalence: **36.0 %**
- Diabetes prevalence: **16.0 %**
- Treated proportion: **51.2 %**
- Follow-up event rate: **28.4 %**
- Mean systolic BP: Female **124.3**, Male **124.5** mmHg

## Statistical tests
| Test | Result |
|------|--------|
| t-test, `systolic_bp` by `sex` | t = −0.19, df = 422.6, **p = 0.85** (not significant) |
| Chi-square, `hypertension` × `diabetes` | χ² = 25.98, df = 1, **p < 0.001** (significant) |
| Correlation, `age` vs `systolic_bp` | r = **0.55**, p < 0.001 |

## Logistic regression: `hypertension ~ age + sex + BMI` (Part K example)
| Term | OR | 95% CI | p |
|------|----|--------|---|
| age | 1.09 | 1.07–1.12 | < 0.001 |
| sex (Male) | 1.20 | 0.76–1.90 | 0.43 |
| BMI | 1.16 | 1.10–1.22 | < 0.001 |

## Logistic regression: `hypertension ~ age + sex + BMI + diabetes`
| Term | OR | 95% CI | p |
|------|----|--------|---|
| age | 1.09 | 1.07–1.11 | < 0.001 |
| sex (Male) | 1.17 | 0.74–1.86 | 0.49 |
| BMI | 1.15 | 1.09–1.21 | < 0.001 |
| diabetes (Yes) | 1.96 | 1.06–3.65 | 0.03 |

## Cox model: `Surv(time_to_event, outcome) ~ age + diabetes + hypertension + treatment`
(reference level for treatment = Untreated)
| Term | HR | 95% CI | p |
|------|----|--------|---|
| age | 1.05 | 1.03–1.07 | < 0.001 |
| diabetes (Yes) | 2.21 | 1.46–3.33 | < 0.001 |
| hypertension (Yes) | 1.65 | 1.07–2.56 | 0.03 |
| treatment (Treated) | 0.55 | 0.36–0.85 | 0.007 |

**Interpretation headline:** older age, diabetes and hypertension increase the risk
of the follow-up event; being **treated roughly halves** the hazard (HR 0.55).

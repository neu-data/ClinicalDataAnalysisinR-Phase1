# Key Findings (Instructor Reference)
### Canonical results from the simulated dataset — for marking & teaching

These are the actual numbers produced by the final multivariable logistic
regression model in `Scripts/day5_demo.R` / `Solutions/day5_solution.R`,
run on `analysis_data.rds` restricted to diagnosed hypertensives
(`htn_diagnosed == "Yes"`). Use them to check participants' work.

**Analytic sample:** 1,089 diagnosed hypertensives; **992 complete cases** in the
adjusted model. Overall treatment uptake among diagnosed ≈ **47%**.

## Adjusted odds ratios (final model)
| Predictor | aOR | 95% CI | p | Direction |
|-----------|-----|--------|---|-----------|
| Age (per year) | 1.03 | 1.02–1.04 | <0.001 | ↑ uptake |
| Sex: Male (vs Female) | 0.74 | 0.56–0.97 | 0.031 | ↓ uptake |
| Education (linear trend) | 1.96 | 1.39–2.77 | <0.001 | ↑ with higher education |
| Residence: Urban (vs Rural) | 1.87 | 1.41–2.49 | <0.001 | ↑ uptake |
| Diabetes: Yes | 3.56 | 1.46–9.61 | 0.007 | ↑ uptake |
| Family history of HTN: Yes | 1.91 | 1.44–2.54 | <0.001 | ↑ uptake |
| Health insurance: Yes | 2.05 | 1.54–2.74 | <0.001 | ↑ uptake |
| Knowledge score (per point) | 1.10 | 1.06–1.14 | <0.001 | ↑ uptake |
| Distance to facility (per km) | 0.98 | 0.96–1.01 | 0.128 | NS (trend ↓) |

**Model discrimination:** AUC ≈ **0.71** (acceptable).

## What a correct interpretation should say
- **Significant independent determinants** of treatment uptake: older age, female
  sex, higher education, urban residence, diabetes, family history, health
  insurance, and greater hypertension knowledge.
- **Diabetes** shows the largest effect (over 3× the odds) but the widest CI
  (smaller subgroup) — a good teaching point on precision.
- **Distance to facility** is in the expected (protective-against-uptake)
  direction but not statistically significant after adjustment.
- Crude vs adjusted comparison for **residence** demonstrates mild confounding.

*(Exact decimals can shift trivially with R/package versions; CIs and directions
are stable. Mark on correct method and interpretation, not 2nd-decimal matches.)*

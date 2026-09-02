# R Cheat Sheet — Phân tích Dữ liệu Lâm sàng trong R (Phase I)

Một tài liệu tham khảo ngắn gọn, riêng cho khóa học. Mọi lệnh đều sử dụng các biến của **chúng ta**
(`clinical_data` với `age`, `sex`, `BMI`, `systolic_bp`, `hypertension`, …).
Hãy giữ tài liệu này mở trong khi bạn làm việc.

> Nạp các công cụ một lần cho mỗi phiên làm việc: `library(tidyverse)` (dữ liệu + biểu đồ),
> cùng với `library(gtsummary)`, `library(broom)`, `library(survival)` khi cần.

---

## 1. Nhập dữ liệu

```r
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")  # read a CSV file
library(readxl)
raw <- read_excel("Data/clinical_data_raw.xlsx")           # read an Excel file
```
`read_csv()` đọc tệp phân tách bằng dấu phẩy; `read_excel()` đọc tệp `.xlsx`.

## 2. Khảo sát một bộ dữ liệu

```r
dim(clinical_data)      # number of rows (patients) and columns (variables)
names(clinical_data)    # the variable names
head(clinical_data)     # first 6 rows
str(clinical_data)      # each variable and its type
summary(clinical_data)  # quick summary of every variable
View(clinical_data)     # open a spreadsheet-style viewer (RStudio)
table(clinical_data$sex)# count a categorical variable
```

## 3. Quản lý dữ liệu (dplyr)

```r
# filter(): keep rows meeting a condition
filter(clinical_data, age >= 60)

# select(): keep only some columns
select(clinical_data, patient_id, age, BMI)

# mutate(): create or change a column
mutate(clinical_data, pulse_pressure = systolic_bp - diastolic_bp)

# case_when(): create groups from rules
mutate(clinical_data, bmi_group = case_when(
  BMI < 18.5 ~ "Underweight",
  BMI < 25   ~ "Normal",
  BMI < 30   ~ "Overweight",
  BMI >= 30  ~ "Obese"))

# group_by() + summarise(): statistics by group
clinical_data %>%
  group_by(sex) %>%
  summarise(mean_bmi = mean(BMI, na.rm = TRUE))

# distinct(): remove duplicate rows
distinct(clinical_data)
```
Toán tử pipe `%>%` chuyển kết quả ở bên trái vào hàm ở bên phải
("và sau đó …").

## 4. Dữ liệu khuyết

```r
is.na(clinical_data$glucose)          # TRUE where a value is missing
sum(is.na(clinical_data$glucose))     # how many are missing
colSums(is.na(clinical_data))         # missing count for every column
mean(clinical_data$glucose, na.rm = TRUE)  # ignore missing when calculating
```

## 5. Thống kê mô tả

```r
mean(clinical_data$age)               # average
median(clinical_data$BMI)             # middle value
sd(clinical_data$age)                 # standard deviation (spread)
IQR(clinical_data$BMI)                # interquartile range
range(clinical_data$systolic_bp)      # minimum and maximum
table(clinical_data$smoking)          # counts per category
prop.table(table(clinical_data$smoking)) * 100   # percentages
```

## 6. Biểu đồ (mẫu ggplot2)

Mọi ggplot đều bắt đầu theo cùng một cách: `ggplot(data, aes(...)) + a geom_ + labs()`.

```r
# Histogram - one continuous variable
ggplot(clinical_data, aes(x = age)) +
  geom_histogram(binwidth = 5) +
  labs(x = "Age", y = "Count")

# Boxplot - continuous by group
ggplot(clinical_data, aes(x = sex, y = systolic_bp)) +
  geom_boxplot()

# Bar plot - counts of a category
ggplot(clinical_data, aes(x = smoking)) +
  geom_bar()

# Scatterplot - two continuous variables (with trend line)
ggplot(clinical_data, aes(x = BMI, y = systolic_bp)) +
  geom_point() +
  geom_smooth(method = "lm")
```

## 7. Kiểm định thống kê

```r
# t-test: continuous outcome, two groups
t.test(systolic_bp ~ sex, data = clinical_data)

# Wilcoxon: non-parametric alternative to the t-test
wilcox.test(glucose ~ diabetes, data = clinical_data)

# Chi-square: two categorical variables
chisq.test(table(clinical_data$hypertension, clinical_data$diabetes))

# Fisher's exact: two categorical variables, small counts
fisher.test(table(clinical_data$sex, clinical_data$treatment))

# Correlation: two continuous variables
cor.test(clinical_data$age, clinical_data$systolic_bp)
```

## 8. Mô hình

```r
library(broom)

# Linear regression: continuous outcome
lm(systolic_bp ~ age + BMI, data = clinical_data)

# Logistic regression: binary outcome -> odds ratios
# Make the Yes/No outcome a factor first (glm needs 0/1 or a factor; No = reference)
clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
model <- glm(hypertension ~ age + sex + BMI,
             data = clinical_data, family = binomial)
tidy(model, exponentiate = TRUE, conf.int = TRUE)   # tidy OR + 95% CI

# Survival: time-to-event outcome
library(survival)
survfit(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)  # Kaplan-Meier
coxph(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)     # hazard ratio
```

---

### Những tiện ích hữu ích

```r
?mean                 # open the help page for any function
install.packages("x") # install a package ONCE
library(x)            # load a package EVERY session
c(1, 2, 3)            # build a vector
x <- 5                # store a value (Alt+- types the arrow)
# a comment - R ignores everything after the #
```

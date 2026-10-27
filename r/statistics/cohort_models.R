library(ggplot2)

setwd("C:/Users/17975/OneDrive/Desktop/Interview_Project")

# 1. read cleaned cohort
df <- read.delim("data/processed/cohort_clean.tsv")

# 2. ancestry summary
summary(df)

df |>
  group_by(ancestry) |>
  summarise(
    n = n(),
    mean_age = mean(age, na.rm = TRUE),
    mean_mtdna = mean(mtDNA_CN, na.rm = TRUE),
    sd_mtdna = sd(mtDNA_CN, na.rm = TRUE),
    mean_het = mean(heteroplasmy_count, na.rm = TRUE),
    .groups = "drop"
  )

# 3. mtDNA_CN distribution

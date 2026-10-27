# cohort_models_optimized.R

library(tidyverse)
library(here)

# Read cleaned cohort
df <- readr::read_tsv(here::here("data/processed/cohort_clean.tsv"))

# Summarise by ancestry
summary_by_ancestry <- df %>%
  group_by(ancestry) %>%
  summarise(
    n = n(),
    mean_age = mean(age, na.rm = TRUE),
    mean_mtdna = mean(mtDNA_CN, na.rm = TRUE),
    sd_mtdna = sd(mtDNA_CN, na.rm = TRUE),
    mean_het = mean(heteroplasmy_count, na.rm = TRUE),
    .groups = "drop"
  )

# mtDNA_CN distribution plot
ggplot(df, aes(x = mtDNA_CN)) +
  geom_histogram(binwidth = 1, fill = "steelblue", color = "white") +
  labs(
    title = "mtDNA Copy Number Distribution",
    x = "mtDNA CN",
    y = "Count"
  ) +
  theme_minimal()

ggsave(here::here("mtDNA_CN_distribution.png"))

# Reproducibility
writeLines(capture.output(sessionInfo()), here::here("session_info.txt"))

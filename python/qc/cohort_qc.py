import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
REPORT_DIR = BASE_DIR / "reports"
FIG_DIR = REPORT_DIR / "figures"
TAB_DIR = REPORT_DIR / "tables"

pheno = pd.read_csv(RAW_DIR / "phenotype.tsv", sep="\t")
mtdna = pd.read_csv(RAW_DIR / "mtdna.tsv", sep="\t")

print(pheno.shape)
print(mtdna.shape)

print(pheno.dtypes)
print(mtdna.dtypes)

print(pheno["sample_id"].duplicated().sum())
print(mtdna["sample_id"].duplicated().sum())

pheno_duplicates = pheno[
    pheno["sample_id"].duplicated(keep=False)
].copy()

mtdna_duplicates = mtdna[
    mtdna["sample_id"].duplicated(keep=False)
].copy()

n_pheno_duplicates = pheno["sample_id"].duplicated().sum()
n_mtdna_duplicates = mtdna["sample_id"].duplicated().sum()

n_missing_age = pheno['age'].isna().sum()
print(f"The NA number of age is {n_missing_age}")

MAX_AGE = 100
MIN_AGE = 0

n_invalid_age = pheno[(pheno["age"] < MIN_AGE) | (pheno["age"] > MAX_AGE)].shape[0]
print(f"The number of invalid age is {n_invalid_age}")

pheno_clean = pheno[
    (pheno["age"] >= MIN_AGE) & (pheno["age"] <= MAX_AGE)
].copy()
pheno_clean = pheno_clean.drop_duplicates(subset="sample_id",
                                          keep="first")
print(pheno_clean.shape)

pheno_clean_set = set(pheno_clean["sample_id"])
mtdna_set = set(mtdna["sample_id"])

n_pheno_only = len(pheno_clean_set - mtdna_set)
print(f"Phenotype only : {n_pheno_only}")
n_mtdna_only = len(mtdna_set - pheno_clean_set)
print(f"mtDNA only : {n_mtdna_only}")

merged = pd.merge(pheno_clean, mtdna, how="inner", on="sample_id", validate="one_to_one")
print(merged.shape)
print(merged.head())

q1 = merged["mtDNA_CN"].quantile(0.25)
q3 = merged["mtDNA_CN"].quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = merged[(merged["mtDNA_CN"] < lower_bound) | (merged["mtDNA_CN"] > upper_bound)]
print(f"The outliers are \n{outliers}")

merged_clean = merged[(merged["mtDNA_CN"] >= lower_bound) & (merged["mtDNA_CN"] <= upper_bound)].copy()
print(merged_clean.shape)

merged_clean.to_csv(DATA_DIR / "processed" / "cohort_clean.tsv", sep="\t", index=False)


summary = (merged_clean
           .groupby("ancestry")
           .agg(
    n=("ancestry", "size"),
    mean_age=("age", "mean"),
    n_male=("sex", lambda x: (x == "M").sum()),
    n_female=("sex", lambda x: (x == "F").sum()),
    apoe4_rate=("APOE4", "mean"),
    status_rate=("status", "mean"),
    median_mtdna=("mtDNA_CN", "median"),
    mean_het=("heteroplasmy_count", "mean")
)
.reset_index())
print(summary)

with open(REPORT_DIR / "qc_report.txt", "w") as f:

    f.write("QC REPORT\n")
    f.write("=========\n\n")

    f.write("[Input]\n")
    f.write(f"Phenotype rows: {len(pheno)}\n")
    f.write(f"mtDNA rows: {len(mtdna)}\n\n")

    f.write("[Duplicate QC]\n")
    f.write(f"Phenotype duplicate IDs: {n_pheno_duplicates}\n")
    f.write(f"mtDNA duplicate IDs: {n_mtdna_duplicates}\n\n")

    f.write("[Age QC]\n")
    f.write(f"Missing ages: {n_missing_age}\n")
    f.write(f"Invalid ages: {n_invalid_age}\n")
    f.write(f"Phenotype rows after age and duplicate QC: {len(pheno_clean)}\n\n")

    f.write("[Merge QC]\n")
    f.write(f"Phenotype-only samples: {n_pheno_only}\n")
    f.write(f"mtDNA-only samples: {n_mtdna_only}\n")
    f.write(f"Samples after inner merge: {len(merged)}\n\n")

    f.write("[mtDNA_CN Outlier QC]\n")
    f.write(f"Q1: {q1:.2f}\n")
    f.write(f"Q3: {q3:.2f}\n")
    f.write(f"IQR: {iqr:.2f}\n")
    f.write(f"Lower bound: {lower_bound:.2f}\n")
    f.write(f"Upper bound: {upper_bound:.2f}\n")
    f.write(f"Number of outliers: {len(outliers)}\n")
    f.write(f"Final sample count: {len(merged_clean)}\n")

plt.figure()
plt.hist(
    merged["mtDNA_CN"],
    bins=50,
)
plt.xlabel("MT-DNA Copy Number")
plt.ylabel("Count")
plt.title("Distribution of MT-DNA Copy Number")
plt.show()
plt.tight_layout()

plt.savefig(FIG_DIR / "mtdna_cn_histogram.png",
            dpi=300)
plt.close()
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
TABLES_DIR = BASE_DIR / "reports" / "tables"

pheno = pd.read_csv(RAW_DIR / "phenotype_test.tsv", sep="\t")
mtdna = pd.read_csv(RAW_DIR / "mtdna_test.tsv", sep="\t")

print(pheno.shape)
print(pheno.dtypes)
print(pheno.isna().sum())
print(pheno["sample_id"].duplicated().sum())

merged = pd.merge(pheno, mtdna, on="sample_id", how="inner", validate="one_to_one")
summary = (
    merged
    .groupby("ancestry", observed=True)
    .agg(
        n=("sample_id", "size"),
        mean_age=("age", "mean"),
        mean_mtdna=("mtDNA_CN", "mean"),
        median_het=("heteroplasmy_count", "median")
    )
    .reset_index()
)

summary.to_csv(TABLES_DIR / "cohort_summary.tsv", sep="\t", index=False)
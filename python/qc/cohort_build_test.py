from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

rng = np.random.default_rng(42)
n = int(input("Enter the number of samples: "))

pheno = pd.DataFrame({
    "sample_id" : [f"S{i:03d}" for i in range(1,n+1)],
    "ancestry" : rng.choice(["EUR","AFR","EAS","HIS"], size=n),
    "age" : rng.integers(65,81,size=n),
    "sex" : rng.choice(["M","F"],size=n),
    "APOE4" : rng.integers(0,2,size=n),
    "status" : rng.integers(0,2,size=n)
})

mtdna = pd.DataFrame({
    "sample_id" : [f"S{i:03d}" for i in range(1,n+1)],
    "mtDNA_CN" : rng.uniform(250,351,size=n).round(1),
    "heteroplasmy_count" : rng.integers(0,8,size=n),
})

pheno.to_csv(RAW_DIR / "phenotype_test.tsv", sep="\t" , index=False)
mtdna.to_csv(RAW_DIR / "mtdna_test.tsv", sep="\t" , index=False)
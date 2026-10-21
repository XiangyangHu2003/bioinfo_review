import numpy as np
import pandas as pd
from pandas.tseries.frequencies import key

s = pd.Series([1,2,3,4,5,np.nan])
print(s)

t = pd.DataFrame([1,2,3,4,5,np.nan])
print(t)

dates = pd.date_range(start="2026-09-28", periods=8)
print(dates)

df = pd.DataFrame(
    np.random.randn(8,4),
    index=dates,
    columns=list('ABCD')
)

print(df)

from collections import Counter
from pathlib import Path

p = "data/toy.fasta"

def read_fasta(path: str) -> dict[str, str]:
    record : dict[str, list[str]] = {}
    current_id : str | None = None

    with Path(p).open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == ">":
                current_id = line[1:].split()[0]
                record[current_id] = []
            else:
                if current_id is None:
                    raise ValueError("Sequence is ahead of Header")
                record[current_id].append(line.upper())

    return {key: "".join(value) for key, value in record.items()}

def GC_count(seq: str) -> float:
    if seq is None:
        return "nan"
    counts = Counter(seq)
    return (counts["G"] + counts["C"]) / len(seq)

x = read_fasta(p)

s = {}
for k, v in x.items():
    s[k] = GC_count(v)*100

print(s)

df2 = pd.DataFrame(
    list(s.values()),
    index=list(s.keys()),
    columns=["GC_count"]
)
print(df2)

df3 = pd.DataFrame(
    data={
        "GC_count" : list(s.values())
    },
    index=list(s.keys())
)
print(df3)

def read_fasta_to_df(path: str):
    current_id = None
    seqid = []
    species = []
    record = {}

    with Path(p).open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == ">":
                current_id = line[1:].split()[0]
                seqid.append(current_id)
                species.append(line[1:].split()[1])
                record[current_id] = []
            else:
                if current_id is None:
                    raise ValueError("Sequence is ahead of Header")
                record[current_id].append(line.upper())
    seq = {key: "".join(value) for key, value in record.items()}

    return seq, seqid, species

seq, seqid, species = read_fasta_to_df(p)

df4 = pd.DataFrame({
    "GC_count" : s,
    "species" : species
},
    index=list(seq.keys())
)
print(df4)
df4.head()
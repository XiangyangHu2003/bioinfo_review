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
from collections import Counter
from io import StringIO

data = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

def parse_fasta(data):
    record = {}
    header = []
    sample_id = None

    with StringIO(data) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == ">":
                sample_id = line[1:].split()[0]
                header.append(sample_id)
                record[sample_id] = []
            else:
                if sample_id is None:
                    raise ValueError("Sequence found before FASTA header")
                record[sample_id].append(line.upper())

    record = {x: "".join(y) for x, y in record.items()}
    return header, record

x, y = parse_fasta(data)

def count(record):
    gc_content = {}
    for sample_id in record:
        c = Counter(record[sample_id])
        gc_count = (c["C"] + c["G"]) / len(record[sample_id])
        gc_content[sample_id] = gc_count
    return gc_content

gc_content = count(y)
max_id = max(gc_content, key=gc_content.get)

print(max_id)
print(f"{gc_content[max_id]*100:.6f}")

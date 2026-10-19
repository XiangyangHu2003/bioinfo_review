from collections import Counter

seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def rosalindDna(seq: str):
    counter = Counter(seq.upper())
    return (
        f"A: {counter['A']}\n"
        f"T: {counter['T']}\n"
        f"G: {counter['G']}\n"
        f"C: {counter['C']}"
    )

print(rosalindDna(seq))
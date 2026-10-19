x = "AAAACCCGGT"

def rosalindrevd(seq: str):
    revseq = reversed(seq)
    revc = []
    for x in revseq:
        if x == "A":
            revc.append("T")
        if x == "T":
            revc.append("A")
        if x == "G":
            revc.append("C")
        if x == "C":
            revc.append("G")

    return "".join(revc)

print(rosalindrevd(x))
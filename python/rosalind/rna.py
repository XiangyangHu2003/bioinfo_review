seq = "GATGGAACTTGACTACGTAAATT"

def rosalindrna(seq: str):
    rseq = []

    for x in seq:
        if x == "T":
            rseq.append("U")
        else:
            rseq.append(x)

    return "".join(rseq)

print(rosalindrna(seq))
stringa = """
GAGCCTACTAACGGGAT
""".strip()
stringb = """
CATCGTAATGACGGCCT
""".strip()

def hamm(a,b):
    n = len(a)
    x = 0
    for i in range(n):
        if a[i] != b[i]:
            x = x + 1
    return x

print(hamm(stringa,stringb))

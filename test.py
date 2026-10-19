from Bio import SeqIO

x = "data/toy.fasta"

seqs = SeqIO.parse(x, "fasta")
for record in seqs:
    print(record.id)
    print(record.seq)

species = set()

for record in SeqIO.parse(x, "fasta"):
    parts = record.description.split()
    id = parts[0]
    species.add(parts[1])

print(species)
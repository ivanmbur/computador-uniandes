notas = open("01_notas.tsv", "r").read().split("\t")
count = 0
for l in notas:
	if (l == "MATEMA"):
		count += 1
print count

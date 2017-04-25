infile = open("contacto_de_JaimeForero.txt", "r")

text = infile.readlines()

print text

text1 = []

for i in text:
	text1.append(i.rstrip("\n"))

print text1

print text[2].split(",")

print text[1].split()

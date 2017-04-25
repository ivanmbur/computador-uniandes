import sys
import numpy as np

n = int(sys.argv[1])
sucesion = [n]

while sucesion[len(sucesion)-1] != 1:
	s = sucesion[len(sucesion)-1]
	if s % 2 == 0:
		sucesion.append(s/2)
	else:
		sucesion.append(s*3 + 1)

print "La sucesion dada por %d tuvo longitud %d" %(n, len(sucesion)), "y fue", sucesion
		

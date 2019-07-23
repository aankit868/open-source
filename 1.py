def read(*argv):
	for i in argv:
		i=input()

def write(*argv):
	print(" ".join(map(str,argv)))

a,b,c=0
read(a,b,c)
write(a,b,c)


def read(*argv):
  for i in argv:
    i[0]=input()
	
def write(*argv):
  for i in argv:
    print(i[0])  

a=[0]
b=[0]
c=[0]
read(a,b,c)
write(a,b,c)

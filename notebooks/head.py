import sys
print(sys.argv)
filename=sys.argv[1]
h=open(sys.argv[1]).readlines()
for line in h:
    print (line,end="")
    

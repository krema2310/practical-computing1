import sys
print(sys.argv)
filename=sys.argv[1]
lines=open(sys.argv[1]).readlines()
for line in lines:
     print(line.upper(),end="")

import sys


# x = int((sys.argv[1]))
# y = int((sys.argv[2]))
# z = int((sys.argv[3]))

x = 10
y = 20
z = 30



if (x < y+z) and (y < x+z) and (z < x+y):
    print("triangle")
else:
    print("not triangle")
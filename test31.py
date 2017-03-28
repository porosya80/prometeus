import sys

x = int((sys.argv[1]))


x +=1
b = 0
a = 1

for i in range(x):
    tmp = b
    b = a + b
    a = tmp
print (a)
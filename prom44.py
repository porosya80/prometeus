import sys

x = int((sys.argv[1]))
y = int((sys.argv[2]))

counter = 0

for i in range(x,y+1):
    the_summ1 = 0
    the_summ2 = 0
    cyfer = str(i)
    cyfer = "0"*(6-len(cyfer))+cyfer
    second = cyfer[3:]
    first = cyfer[:3]
    for j in first:the_summ1 += int(j)
    for k in second:the_summ2 += int(k)
    if the_summ1 == the_summ2:
             counter += 1


print(counter)

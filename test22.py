import sys


x = int((sys.argv[1]))
y = int((sys.argv[2]))
z = int((sys.argv[3]))

str_i = "la"
result = "la"
for i in range(x-1):
    result += ("-" + str_i)
result = " " + result
result *= y
print("Everybody sing a song:{}{}".format(result, "." if z == 0 else "!"))



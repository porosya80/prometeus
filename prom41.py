import sys

x = str((sys.argv[1]))

x = ''.join(x.lower().split())
rx = ''.join(reversed(x))
if x == rx:
    print("YES")
else:
    print("NO")
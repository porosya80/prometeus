import sys

pars_string = str((sys.argv[1]))



count = 0
for sym in pars_string:
        if sym == '(':
            count += 1
        elif sym == ')':
            count -= 1
            if count < 0:
                break

print ("YES" if count ==0 else "NO")
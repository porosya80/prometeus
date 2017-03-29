import sys

pars_string = sys.argv

del pars_string[0]

print(" ".join(reversed(pars_string) ))


import sys
import math


# x = float(sys.argv[1])
# y = float(sys.argv[2])
# z = float(sys.argv[3])

x = float(1)
y = float(1.1)
z = float(0.1)



print (1/(z*math.sqrt(2*math.pi))*math.exp(-math.pow(x-y,2)/(2*(math.pow(z,2)))))

print(1/(z * math.sqrt(2 * math.pi)) * math.exp(-1*(((x - y)**2)/(2*z**2))))
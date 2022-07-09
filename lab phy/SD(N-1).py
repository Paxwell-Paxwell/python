labNumber = [8.78,8.80,8.80,8.79,8.81,8.80]
sumLabNumber = sum(labNumber)
print(sumLabNumber)
import math
Xbar = sumLabNumber/len(labNumber)
a = 0
N = len(labNumber)
for i in labNumber:
 a = (math.fabs(Xbar-i))**2+a
# SD_N is sd: /N
SD_N = math.sqrt(a/N)
#SD_N1 is sd: /N-1
SD_N1 = math.sqrt(a/(N-1))
print(f'len : {len(labNumber)}')
print(f'Xbar : {Xbar}')
print(f'SD_N1 = {SD_N1},SD_N = {SD_N}')




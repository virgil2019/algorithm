import sys
import math

a = int(sys.argv[1])
# q = int(math.sqrt(a))
q = a
rg = range(2, q + 1)
r = []
print(rg)
for i in rg:
    k = 0
    while True:
        if q % i == 0:
            k += 1
            q = q / i
        else:
            break

    if k > 0:
        r.append([i, k])

print(r)
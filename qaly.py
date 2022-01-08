import sys
import math
periods = int(next(sys.stdin))

total = 0
for line in sys.stdin:
    values = line.split()
    q = float(values[0])
    y = float(values[1])
    total += q * y
print(total)
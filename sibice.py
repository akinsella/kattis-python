import sys
import math

values = next(sys.stdin).split()
n = int(values[0])
w = int(values[1])
h = int(values[2])

max_size = math.sqrt(w ** 2 + h ** 2)

for line in sys.stdin:
    size = int(line)
    print("DA" if size <= max_size else "NE")
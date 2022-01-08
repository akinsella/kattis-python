import sys

for i in sys.stdin:
    inputs = i.split()
    R1 = int(inputs[0])
    S = int(inputs[1])

R2 = 2 * S - R1

print(R2)
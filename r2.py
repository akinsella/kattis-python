import sys

for i in sys.stdin:
    ab = i.split()
    R1 = int(ab[0])
    S = int(ab[1])

R2 = 2 * S - R1

print(R2)
import sys

count = int(next(sys.stdin))

total = 0
for line in sys.stdin:
    line = line.rstrip()
    value = int(line[:-1])
    pow = int(line[-1])
    total += value ** pow
print(total)
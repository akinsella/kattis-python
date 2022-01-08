import sys

n = 0
for line in sys.stdin:
    if n % 2 == 1:
        v = line.split()[0]
        print(v) 
    n += 1

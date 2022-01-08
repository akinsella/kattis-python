import sys

for line in sys.stdin:
    tokens = line.split()
    a = int(tokens[0])
    b = int(tokens[1])
result = a + b

print(result)
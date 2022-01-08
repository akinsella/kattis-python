import sys

line = next(sys.stdin).split()
a = int(line[0])
b = int(line[1])

print (f"{a} {b}") if a < b else print(f"{b} {a}")
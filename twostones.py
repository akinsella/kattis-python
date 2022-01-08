import sys

count = int(next(sys.stdin))
print("Alice") if count % 2 == 1 else print("Bob")
import sys

count = int(next(sys.stdin))

items = list()
for line in sys.stdin:
    items.append(int(line))

for item in reversed(items):
    print(item)
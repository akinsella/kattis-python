import sys

count = int(next(sys.stdin))

if count % 2 == 1:
    print("still running")
else:
    total = 0
    for i in range(count // 2):
        start = int(next(sys.stdin))
        stop = int(next(sys.stdin))
        total += stop - start
    print(total)

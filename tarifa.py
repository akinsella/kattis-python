import sys

x = int(next(sys.stdin))
#print(f"{x=}")
r = int(next(sys.stdin))
#print(f"{r=}")

total = 0
for idx in range(r):
    #print(f"{idx=}")
    total += x

    consumed = int(next(sys.stdin))
    #print(f"{consumed=}")

    total -= consumed
    #print(f"{total=}")
total += x

print(total)

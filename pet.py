import sys


winner = (0, 0)
for idx, line in enumerate(sys.stdin):
    values = line.split()
    points = 0
    for value in values:
        points += int(value)
    if points > winner[1]:
        winner = (idx + 1, points)
print(f"{winner[0]} {winner[1]}")
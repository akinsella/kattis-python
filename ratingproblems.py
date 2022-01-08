import sys

line = next(sys.stdin).split()
n = int(line[0])
k = int(line[1])

total = 0
for line in sys.stdin:
    total += int(line)

remaining_voters = n - k
min_avg_note = (total + (remaining_voters * -3)) / n
max_avg_note = (total + (remaining_voters * 3)) / n

print(f"{min_avg_note} {max_avg_note}")
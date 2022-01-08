import sys

for line in sys.stdin:
    result = set()
    for i in line.split(';'):
        if '-' in i:
            (start, end) = i.split('-')
            elts = set(range(int(start), int(end) + 1))
        else:
            elts = set([int(i)])
        # print(f"{elts=}", file=sys.stderr)
        result = set.union(result, elts)
    count = len(result)
    print(count)
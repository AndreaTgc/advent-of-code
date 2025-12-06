import sys
from functools import reduce
import operator

with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f if l.strip()]
    rows = lines[:-1]
    ops = lines[-1].split()
    ncols = len(rows[0].split())
    problems = [[] for _ in range(ncols)]
    sum1 = 0

    for line in rows:
        nums = line.split()
        for i in range(ncols):
            problems[i].append(int(nums[i]))

    for i, op in enumerate(ops):
        sum1 += sum(problems[i]) if op == "+" else reduce(operator.mul, problems[i], 1)

print(f"part1 = {sum1}\npart2 = 0")


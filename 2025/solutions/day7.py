import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    lines = [list(l.strip()) for l in file.readlines()]

width = len(lines[0])
start = lines[0].index("S")
beams = {start}
counts = defaultdict(int)
counts[start] = 1
sum1 = 0

for row in lines[1:]:
    splitters = {i for i, c in enumerate(row) if c == "^"}
    new_counts = defaultdict(int)
    for pos in set(beams) | set(counts):
        hit = pos in splitters
        if pos in beams:
            c = counts[pos]
            if hit:
                sum1 += 1
                beams.remove(pos)
                if pos - 1 >= 0:
                    beams.add(pos - 1)
                    new_counts[pos - 1] += c
                if pos + 1 < width:
                    beams.add(pos + 1)
                    new_counts[pos + 1] += c
            else:
                new_counts[pos] += c
    counts = new_counts

sum2 = sum(counts.values())
print(f"part1 = {sum1}\npart2 = {sum2}")


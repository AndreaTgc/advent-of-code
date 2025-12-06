import sys
import bisect

with open(sys.argv[1]) as file:
    lines = [l.strip() for l in file.readlines()]

ranges = []
i = 0
sum1 = 0
sum2 = 0

while lines[i] != "":
    a, b = map(int, lines[i].split("-"))
    ranges.append((a, b))
    i += 1
    
i += 1 
ranges.sort()
merged = []
start, end = ranges[0]

for a, b in ranges[1:]:
    if a <= end + 1:
        end = max(end, b)
    else:
        merged.append((start, end))
        start, end = a, b

merged.append((start, end))
starts = [r[0] for r in merged]

while i < len(lines):
    k = int(lines[i])
    i += 1
    idx = bisect.bisect_right(starts, k) - 1
    if idx >= 0:
        lo, hi = merged[idx]
        sum1 += lo <= k <= hi

for c in merged:
    sum2 += c[1] - c[0] + 1

print(f"part1 = {sum1}\npart2 = {sum2}")


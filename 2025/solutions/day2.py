import sys

with open(sys.argv[1]) as file:
    ranges = [r.split("-") for r in file.read().strip().split(",")] 

sum1 = 0
sum2 = 0
for r in ranges:
    for c in range(int(r[0]), int(r[1])):
        s = str(c)
        l = len(s)
        if l % 2 == 0 and s[:l//2] == s[l//2:]:
            sum1 += c
        # Naive loop version
        # TODO: Find the optimized solution
        for k in range(l // 2, 0, -1):
            if l % k == 0:
                if s == s[:k] * (l // k):
                    sum2 += c
                    break

print(f"part1 = {sum1}\npart2 = {sum2}")

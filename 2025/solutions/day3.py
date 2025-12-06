import sys
# Note part 1 and part 2 are split for readability

with open(sys.argv[1]) as file:
    lines = [l.strip() for l in file.readlines()]

sum1 = 0
sum2 = 0
# part 1
for l in lines:
    numeric = [int(c) for c in list(l)]
    first = numeric[:len(numeric) - 1]
    i1 = first.index(max(first))
    x = first[i1]
    rem = numeric[i1 + 1:]
    i2 = rem.index(max(rem))
    y = rem[i2]
    sum1 += x * 10 + y
# part 2
for l in lines:
    numeric = [int(c) for c in l]
    for i in range(12, 0, -1): 
        search_space = numeric[:len(numeric) - (i - 1)]
        j = search_space.index(max(search_space))
        x = search_space[j]
        sum2 += x * (10 ** (i - 1))  
        numeric = numeric[j+1:]
        
print(f"part1 = {sum1}\npart2 = {sum2}")


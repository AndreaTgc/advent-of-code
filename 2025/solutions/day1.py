import sys

with open(sys.argv[1]) as f:
    pos = 50
    count1 = count2 = 0
    for line in f:
        line = line.strip()
        n = int(line[1:])
        delta = -n if line[0] == 'L' else n
        old = pos
        pos += delta
        if pos > 99:
            count2 += pos // 100
        elif pos < 1:
            count2 += ((old - 1) // 100) - ((pos - 1) // 100)

        pos %= 100
        count1 += (pos == 0)

    print(f"Part 1: {count1}")
    print(f"Part 2: {count2}")


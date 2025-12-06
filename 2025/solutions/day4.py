import sys

with open(sys.argv[1]) as file:
    matrix = [l.strip() for l in file.readlines()]    
    rows = len(matrix)
    cols = len(matrix[0])
    sum1 = 0
    sum2 = 0
    def get_adjacent(x, y):
        count = 0
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                count += matrix[nx][ny] == "@"
        return count                    

    for i in range(rows):
        for j in range(cols):
            sum1 += get_adjacent(i, j) < 4 and matrix[i][j] == "@"

    while True:
        changes = 0
        for i in range(rows):
            for j in range(cols):
                if get_adjacent(i, j) < 4 and matrix[i][j] == "@":
                    changes += 1
                    matrix[i] = matrix[i][:j] + '.' + matrix[i][j+1:]

        if changes > 0:
            sum2 += changes
        else:
            break

    print(f"part1 = {sum1}\npart2 = {sum2}")

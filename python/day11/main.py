f = open("test.txt")
lines = f.readlines()

y_indices = [0]
x_indices = [0]

for y, line in enumerate(lines):
    if all([x == '.' for x in line[:-1]]):
        y_indices[y] += 99

    y_indices.append(y_indices[-1] + 1)

y_indices = y_indices[:-1]

for x in range(len(lines[0]) - 1):
    empty = True
    for line in lines:
        if line[x] != ".":
            empty = False
    
    if empty:
        x_indices[x] += 99

    x_indices.append(x_indices[-1] + 1)

x_indices = x_indices[:-1]

# print(x_indices, y_indices)

# Gather positions of galaxies
stars = []
for y, line in enumerate(lines):
    for x, c in enumerate(line[:-1]):
        if c == "#":
            stars.append((x_indices[x], y_indices[y]))

# print(stars)

result = 0
for i, (x1, y1) in enumerate(stars):
    for (x2, y2) in stars[i + 1:]:
        result += abs(x1 - x2) + abs(y1 - y2)

print(result)
f = open("input.txt")
lines = f.readlines()

# X1Y1 is the previous position in the pipe
# X2Y2 is the current position
# I need the previous position to know which side of the pipe is a new part
def get_next_pipe(x1, x2, y1, y2) -> (int, int):
    # print(x1, x2, y1, y2)
    match lines[y2][x2]:
        case "|":
            if y1 == y2 + 1:
                return (x2, y2 - 1)
            else:
                return (x2, y2 + 1)
        case "-":
            if x1 == x2 + 1:
                return (x2 - 1, y2)
            else:
                return (x2 + 1, y2)
        case "F":
            if y1 == y2:
                return (x2, y2 + 1)
            else:
                return (x2 + 1, y2)
        case "J":
            if y1 == y2:
                return (x2, y2 - 1)
            else:
                return (x2 - 1, y2)
        case "L":
            if y1 == y2:
                return (x2, y2 - 1)
            else:
                return (x2 + 1, y2)
        case "7":
            if y1 == y2:
                return (x2, y2 + 1)
            else:
                return (x2 - 1, y2)
            
def find_next_pipe(x1, x2, y1, y2) -> (int, int):
    # only at starting point, find a valid neighbouring pipe segment.
    if x1 == -1 or y1 == -1:
        if lines[y2 + 1][x2] in ["|", "J", "L"]:
            return (x2, y2 + 1)
        if lines[y2 - 1][x2] in ["|", "F", "7"]:
            return (x2, y2 - 1)
        if lines[y2][x2 + 1] in ["-", "J", "7"]:
            return (x2 + 1, y2)
        if lines[y2][x2 - 1] in ["-", "L", "F"]:
            return (x2 - 1, y2)
        
    # Otherwise, use the current pipe to find the next pipe
    return get_next_pipe(x1, x2, y1, y2)
        

# Find position of "S" first.
xs, ys = 0, 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            xs = x
            ys = y
            break
    
    # Found 'S'
    if xs != 0:
        break

# Build loop
x, y = find_next_pipe(-1, xs, -1, ys)
loop: list((int, int)) = [(xs, ys), (x, y)]

while lines[y][x] != "S":
    (prev_x, prev_y) = loop[-2]
    (x, y) = find_next_pipe(prev_x, x, prev_y, y)
    loop.append((x, y))

mid = len(loop) / 2
print("Steps: ", int(mid))

# Plot loop in new map
loop_map = [[0 for _ in range(len(lines[0]) - 1)] for _ in range(len(lines))]
for (x, y) in loop:
    loop_map[y][x] = 1

# Use loop_map as a mask for the real map
real_map = []
for y, line in enumerate(lines):
    real_map.append([])
    for x, c in enumerate(line[:-1]):
        if loop_map[y][x] == 0:
            real_map[y].append(".")
        else:
            real_map[y].append(lines[y][x])
    real_map[y].append("\n")

# Replace "S" with a correct pipe
if real_map[ys][xs + 1] in ["-", "J", "7"] and real_map[ys][xs - 1] in ["-", "L", "F"]:
    real_map[ys][xs] = "-"
if real_map[ys][xs + 1] in ["-", "J", "7"] and real_map[ys - 1][xs] in ["|", "7", "F"]:
    real_map[ys][xs] = "L"
if real_map[ys][xs + 1] in ["-", "J", "7"] and real_map[ys + 1][xs] in ["|", "L", "J"]:
    real_map[ys][xs] = "F"
if real_map[ys][xs - 1] in ["-", "F", "L"] and real_map[ys - 1][xs] in ["|", "F", "7"]:
    real_map[ys][xs] = "J"
if real_map[ys][xs - 1] in ["-", "L", "F"] and real_map[ys + 1][xs] in ["|", "L", "J"]:
    real_map[ys][xs] = "7"
if real_map[ys - 1][xs] in ["|", "F", "7"] and real_map[ys + 1][xs] in ["|", "J", "L"]:
    real_map[ys][xs] = "|"

# Find positions inside the pipe
result = 0
for y, line in enumerate(real_map):
    inside_score: int = 0
    vertical_dir = 0
    for x, c in enumerate(line[:-1]):
        if c == ".":
            if inside_score == 1:
                if y == 9:
                    print(y, x)
                loop_map[y][x] = 2
                result += 1
        if c == "|":
            inside_score = (inside_score + 1) % 2
        if c == "F" or c == "7":
            # --F
            if vertical_dir == 0:
                vertical_dir = -1
                # inside_score = max(0, (inside_score - 0.5)) % 2
            # F--7
            elif vertical_dir == -1:
                vertical_dir = 0
                # inside_score = max(0, (inside_score + 1)) % 2
            # L--7
            else:
                vertical_dir = 0
                inside_score = max(0, (inside_score + 1)) % 2
        if c == "L" or c == "J":
            # --L
            if vertical_dir == 0:
                vertical_dir = 1
                # inside_score = max(0, (inside_score - 0.5)) % 2
            # L--J
            elif vertical_dir == 1:
                vertical_dir = 0
                # inside_score = max(0, (inside_score + 1)) % 2
            else:
                vertical_dir = 0
                inside_score = max(0, (inside_score + 1)) % 2

# Write map to file
out = open("out.txt", "w")
for l in loop_map:
    out.write(''.join([str(c) for c in l]) + "\n")

# Write map to file
out = open("real.txt", "w")
for l in real_map:
    out.write(''.join([str(c) for c in l]))

number_of_twos = 0
for line in loop_map:
    for c in line:
        if c == 2:
            number_of_twos += 1

print("Number of twos: ", number_of_twos)
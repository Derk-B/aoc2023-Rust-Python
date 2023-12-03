import time

start_time = time.time()

f = open("input.txt")
lines = f.readlines()

def isSymbolAtLocation(x: int, y: int) -> bool:
    # If outside of input then return False
    if x < 0 or y < 0:
        return False
    if y >= len(lines):
        return False
    if x >= len(lines[0]) - 1:
        return False
    
    # Check if the char at this position is a symbol.
    # It is a symbol when it is not a number and when it is not a '.'
    return not lines[y][x].isnumeric() and not lines[y][x] == '.'

def getSymbolsForNumber(number_str: [str, (int, int), int]) -> bool:
    [_, (x, y), l] = number_str
    symbols_for_part: [str, (int, int)] = []

    # Check all positions above the number
    # . x x x .
    # . 1 2 3 .
    for dx in range(l):
        lx, ly = x + dx, y - 1
        if isSymbolAtLocation(lx, ly):
            symbols_for_part.append((lines[ly][lx], (lx, ly)))
    # Check positions at left and right
    # x . . . x
    # x 1 2 3 x
    # x . . . x
    for dy in range(3):
        # Left
        lx, ly = x - 1, y - 1 + dy
        if isSymbolAtLocation(x - 1, y - 1 + dy): 
            symbols_for_part.append((lines[ly][lx], (lx, ly)))
        # Right
        lx, ly = x + l, y - 1 + dy
        if isSymbolAtLocation(x + l, y - 1 + dy):
            symbols_for_part.append((lines[ly][lx], (lx, ly)))
    # Check all positions below the number
    # . 1 2 3 .
    # . x x x .
    for dx in range(l):
        lx, ly = x + dx, y + 1
        if isSymbolAtLocation(x + dx, y + 1):
            symbols_for_part.append((lines[ly][lx], (lx, ly)))
    
    return symbols_for_part

numbers_with_len: [[str, (int, int), int]] = []

for y_index, line in enumerate(lines):
    number_str = ""
    number_pos = None
    number_len = 0
    for x_index, c in enumerate(line):
        if c.isnumeric():
            number_str += c
            if number_pos == None: 
                number_pos = (x_index, y_index)
            number_len += 1
        else:
            if number_str != "":
                numbers_with_len.append([number_str, number_pos, number_len])
            number_str = ""
            number_pos = None
            number_len = 0

# For every number, check if it is a part
result1: int = 0
result2: int = 0
gear_location_map = {}
for n in numbers_with_len:
    symbols = getSymbolsForNumber(n)

    # Part 1
    if len(symbols) > 0:
        # Count number to result
        result1 += int(n[0])

    # Part 2
    for s in symbols:
        if s[0] == "*":
            if s[1] in gear_location_map:
                gear_location_map[s[1]].append(n)
            else:
                gear_location_map[s[1]] = [n]
    
for gear_loc in gear_location_map:
    gear_numbers = gear_location_map[gear_loc]
    if len(gear_numbers) == 2:
        result2 += int(gear_numbers[0][0]) * int(gear_numbers[1][0])


print(result1)
print(result2)

end_time = time.time()
print((end_time - start_time) * 1000)
import re
import time

start_time = time.time()

f = open("input.txt")
lines = f.readlines()

# Part 1
def checkSetPossibility(actions: str) -> bool:
    return all(checkActionPossibility(a) for a in actions.split(", "))

def checkActionPossibility(a: str) -> bool:
    [count, color] = a.split(' ')
    match color:
        case "green":
            return int(count) <= 13
        case "red":
            return int(count) <= 12
        case "blue":
            return int(count) <= 14

result = 0
for index, line in enumerate(lines):
    sets: [str] = line[:-1].split(": ")[1].split("; ")
    if all(checkSetPossibility(s) for s in sets):
        result += index + 1

print("Part 1: " + str(result))

# Part 2
def getFactorInGame(s: str) -> [int]:
    maxGreen, maxRed, maxBlue = 0, 0, 0
    actions: [str] = re.split('; |, ', s)
    
    for a in actions:
        [count, color] = a.split(" ")
        match color:
            case "green":
                maxGreen = max(maxGreen, int(count))
            case "red":
                maxRed = max(maxRed, int(count))
            case "blue":
                maxBlue = max(maxBlue, int(count))

    return maxGreen * maxRed * maxBlue

result = 0
for index, line in enumerate(lines):
    game: str = line[:-1].split(": ")[1]
    result += getFactorInGame(game)

print("Part 2: " + str(result))

end_time = time.time()
time_diff = end_time - start_time
print(f'Time: {time_diff * 1000}ms')
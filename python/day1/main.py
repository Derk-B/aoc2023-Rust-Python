f = open("input.txt")
lines = f.readlines()

# Part 1
def findFirstDigit(line: str) -> int:
    for c in line:
        if c.isnumeric():
            return int(c)

def findLastDigit(line: str) -> int:
    for c in reversed(line):
        if c.isnumeric():
            return int(c)

calibration_sum = 0

for line in lines:
    first = findFirstDigit(line)
    last = findLastDigit(line)
    calibration_sum += 10 * first + last

print(" sum = " + str(calibration_sum))


# Part 2
str_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def findRealFirstDigit(line: str) -> int:
    first_occurence = len(line)
    found_str_digit = None
    for i, digit in enumerate(str_digits):
        index = line.find(digit)

        if index > -1 and first_occurence > index:
            first_occurence = index
            found_str_digit = i + 1

    for i, c in enumerate(line):
        if c.isnumeric():
            if first_occurence < i:
                return found_str_digit
            else:
                return int(c)

def findRealLastDigit(line: str) -> int:
    first_occurence = 0
    found_str_digit = None

    for i, digit in enumerate(str_digits):
        try:
            index = line.rindex(digit) + 1
            if first_occurence < index:
                first_occurence = index
                found_str_digit = i + 1
        except:
            continue

    for i, c in enumerate(reversed(line)):
        if c.isnumeric():
            if first_occurence > len(line) - i:
                return found_str_digit
            else:
                return int(c)

calibration_sum = 0
for i, line in enumerate(lines):
    first = findRealFirstDigit(line)
    last = findRealLastDigit(line)
    calibration_sum += 10 * first + last

print(calibration_sum)


        

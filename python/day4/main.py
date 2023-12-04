import time
start_time = time.time()

f = open("input.txt")
lines: list[str] = f.readlines()

result: int = 0
win_numbers: list[bool] = [False for _ in range(100)]
card_count: list[int] = [1 for _ in lines]
for lIndex, line in enumerate(lines):
    # Remove "Card x:"
    line_data: str = line.split(": ")[1]
    # Split remaining line into winning numbers and our own numbers
    [line_win, line_nums] = line_data.split(" | ")
    win_nums: list[int] = [int(n) for n in list(filter(None, line_win.split(" ")))]
    our_nums: list[int] = [int(n) for n in list(filter(None, line_nums.split(" ")))]
    
    # Set the winning_numbers as true in the array
    for n in win_nums:
        win_numbers[n] = True
    
    # Check for every number that we have if it is a winning number
    match_count: int = 0
    for n in our_nums:
        if win_numbers[n]:
            match_count += 1
    
    # Part 1
    # Only if we have matches
    # Add our score to the result
    if match_count > 0:
        result += 2**(match_count-1)

    # Reset winning numbers
    win_numbers = [False for _ in range(100)]

    # Part 2
    # Update the card count
    for i in range(match_count):
        card_count[lIndex + i + 1] += card_count[lIndex]

# Part 1 result
print(result)

# Part 2 result
result = 0
for card in card_count:
    result += card

print(result)

end_time = time.time()

print(f"{(end_time - start_time) * 1000}ms")
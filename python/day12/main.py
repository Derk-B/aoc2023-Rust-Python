def generate(spring_array, record_lengths, count_list, max_len):
    # print("Input array and records:", spring_array, record_lengths)
    if len(record_lengths) == 0:
        # print("Records empty", len(record_lengths))
        return [spring_array]
    if len(spring_array) >= max_len:
        # print("Max len reached!", len(spring_array))
        return [spring_array]

    (sign, remaining_length) = record_lengths[0]
    current_count = count_list[0]

    if sign == ".":
        new_array = spring_array.copy()
        new_array.extend([0 for _ in range(remaining_length)])
        # print(".", new_array, record_lengths[1:])
        return generate(new_array, record_lengths[1:], count_list, max_len)
    elif sign == "?":
        new_arrays = []
        new_records = record_lengths.copy()
        new_record = record_lengths[0]
        # Update record (in case adding a number to the array did not fill the segment)
        # ("?", 3) -> ("?", 2)
        if record_lengths[0][1] > 0:
            new_record = (new_record[0], new_record[1] - 1)
            new_records[0] = new_record
        else:
            new_records = record_lengths[1:]

        # Add 0
        new_array = spring_array.copy()
        new_array.append(0)
        new_arrays.append(new_array)
        if len(count_list) > 0 and len(new_array) + count_list[0] <= max_len:
            new_arrays.extend(generate(new_array, new_records, count_list, max_len))
        # else:
        #     print("Too long afer 0", new_array, count_list, max_len, len(new_array))

        # Add 1
        new_array = spring_array.copy()
        # [0, 1, 0] -> [0, 1, 0, 1, 1, 1, 0] (added 3x 1 and 1x 0)
        new_array.extend([1 for _ in range(current_count)])
        #if current_count > remaining_length:
        new_array.append(0)
        # print(current_count, remaining_length)
        new_record = (new_record[0], new_record[1] - 1)
        new_records[0] = new_record

        new_arrays.append(new_array)

        # If there are still springs to add to the array
        if len(count_list) > 1 and len(new_array) + count_list[1] <= max_len:
            new_arrays.extend(generate(new_array, new_records, count_list[1:], max_len))
        # else:
            # print("Too long afer 1", new_array, count_list[1:], max_len, len(new_array))

        return new_arrays

record = ".??..??...?##."
result = generate([], [('.', 1), ('?', 2), ('.', 2), ('?', 2), ('.', 3), ('?', 3), ('.', 1)], [1, 1, 3], 14)
for r in result:
    correct = True

    if len(r) != 14:
        correct = False
        continue

    if len([i for i in r if i == 1]) != 5:
        correct = False

    for i, c in enumerate(r):
        if record[i] == "#" and c != 1:
            correct = False
        if record[i] == "." and c == 1:
            correct = False
    
    if correct:
        print("CORRECT:", r)
#print(result)

f = open("test.txt")
lines = f.readlines()
final_result = 0

for line in lines:
    record, count_list = line.split(" ")
    count_list = [int(x) for x in count_list.split(",")]

    record_lengths = []

    # Gather record data
    for c in record:
        if c == "#":
            if record_lengths == []:
                record_lengths.append(("#", 1))
            # (#, a) -> (#, a + 1)
            elif record_lengths[-1][0] == "#":
                record_lengths[-1] = (record_lengths[-1][0], record_lengths[-1][1] + 1)
            else:
                record_lengths.append(("#", 1))
        elif c == "?":
            if record_lengths == []:
                record_lengths.append(("?", 1))
            # (?, a) -> (?, a + 1)
            elif record_lengths[-1][0] == "?":
                record_lengths[-1] = (record_lengths[-1][0], record_lengths[-1][1] + 1)
            else:
                record_lengths.append(("?", 1))
        elif c == ".":
            if record_lengths == []:
                record_lengths.append((".", 1))
            # (?, a) -> (?, a + 1)
            elif record_lengths[-1][0] == ".":
                record_lengths[-1] = (record_lengths[-1][0], record_lengths[-1][1] + 1)
            else:
                record_lengths.append((".", 1))

    record_lengths = []
    line_length = len(record)

    # Gather record data
    for c in record:
        if c == "#" or c == "?":
            if record_lengths == []:
                record_lengths.append(("?", 1))
            # (#, a) -> (#, a + 1)
            elif record_lengths[-1][0] == "?":
                record_lengths[-1] = (record_lengths[-1][0], record_lengths[-1][1] + 1)
            else:
                record_lengths.append(("?", 1))
        elif c == ".":
            if record_lengths == []:
                record_lengths.append((".", 1))
            # (?, a) -> (?, a + 1)
            elif record_lengths[-1][0] == ".":
                record_lengths[-1] = (record_lengths[-1][0], record_lengths[-1][1] + 1)
            else:
                record_lengths.append((".", 1))

    max_len = len(record)
    sum_springs = sum(count_list)
    print("Per line: ", record_lengths, count_list, max_len)

    result = generate([], record_lengths, count_list, max_len)
    result = [(r + max_len * [0])[:max_len] for r in result]
    partial_result = 0
    for r in result:
        correct = True

        if len(r) != max_len:
            correct = False

        if len([i for i in r if i == 1]) != sum_springs:
            correct = False

        for i, c in enumerate(r):
            if record[i] == "#" and c != 1:
                correct = False
            if record[i] == "." and c == 1:
                correct = False
        
        if correct:
            print(r)
            final_result += 1
            partial_result +=1

    print("Partial", partial_result)
print(final_result)
    



# Get all segments seperated by "." (so "#" and "?" together)
# Find all possible places for the segments
# Filter possibilities where positions with "#" also contain records

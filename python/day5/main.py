from seed_map import SeedMap

def merge_ranges(ranges: list[(int, int)]) -> list[(int, int)]:
    print(ranges)
    new_ranges: list[(int, int)] = []
    for (rs, rl) in ranges:
        for i, (nrs, nrl) in enumerate(new_ranges):
            if nrs <= rs <= nrs + nrl:
                new_len = max(rs + rl, nrs + nrl) - nrs
                new_ranges[i] = (nrs, new_len)
            elif nrs <= (rs + rl) <= nrs + nrl:
                new_start = min(nrs, rs)
                new_len = max(rs + rl, nrs + nrl) - new_start
                new_ranges[i] = (new_start, new_len)
    else:
        new_ranges.append((rs, rl))

    return new_ranges

f = open("input.txt")
lines = f.readlines()

seeds: list[int] = [int(s) for s in lines[0][7:].split(" ")]
print(seeds)

seed_map = SeedMap()

# Split remainig input on empty lines.
# Also remove the first line for each part, since that is just the map label.
input_per_map: list[list[str]] = [[]]
map_index: int = 0
for l in lines[2:]:
    if l == "\n":
        map_index += 1
        input_per_map.append([])
        continue
    if l[0].isnumeric():
        input_per_map[map_index].append(l)

# Create the map for the given input
seed_map.build(input_per_map)

# Part 1
result = min([seed_map.find_location_for_seed(s) for s in seeds])
print(result)

# Part 2
seed_ranges: list[(int, int)] = []
locations: list[int] = []
i = 0
while i < len(seeds):
    seed_ranges.append((seeds[i], seeds[i+1]))
    i += 2
    
new_ranges: list[(int, int)] = merge_ranges(seed_ranges)
print(new_ranges)
for (s, l) in new_ranges:
    for loc in range(l):
        locations.append(seed_map.find_location_for_seed(s + loc))

result = min(locations)
print(result)



from seed_map import SeedMap


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

for (s, l) in seed_ranges:
    for loc in range(l):
        locations.append(seed_map.find_location_for_seed(s + loc))

result = min(locations)
print(result)



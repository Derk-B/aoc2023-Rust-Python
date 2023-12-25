def fillList(arr, line):
    nums: (int, int, int) = [int(x) for x in line[:].split(" ")]
    arr.append(nums)

def mapList(current_arr: list((int, int)), loc_map: list((int, int, int))) -> list((int, int)):
    next_arr: list((int, int)) = []
    # Get unmappable ranges
    for (first, last) in current_arr:
        if all([last < source or first >= source + l for (_, source, l) in loc_map]):
            next_arr.append((first, last))

    for (first, last) in current_arr:
        # print("Looking at: ", first, last, loc_map)
        for (dest, source, l) in loc_map:
            delta: int = dest - source
            # If whole range between the list item
            # Then easy solution: map whole range to new destination
            if first >= source and last < source + l:
                # print("Full map: ", (first + delta, last + delta))
                next_arr.append((first + delta, last + delta))
            # If first inside range but last outside range
            if first >= source and first < source + l and last >= source + l:
                next_arr.append((first + delta, dest + l - 1))
                current_arr.append((source + l, last))
            # If first outside range but last inside range
            if first < source and last >= source and last < source + l:
                # print(first, last)
                next_arr.append((dest, last + delta))
                # print(next_arr)
                current_arr.append((first, source - 1))
                # print(current_arr)
            # If first before range and last after range
            if first < source and last >= source + l:
                # split in 3 parts
                current_arr.append((first, source - 1))
                current_arr.append((source + l, last))
                next_arr.append((dest, dest + l - 1))
    
    return next_arr

# Part 2
f = open("input.txt")
lines = f.readlines()

seeds: list[int] = [int(s) for s in lines[0][7:].split(" ")]

seed_ranges: list[(int, int)] = []
i: int = 0

# Read seed ranges from input
while i < len(seeds):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    i += 2

# initialise maps
seed_to_soil: list((int, int, int)) = []
soil_to_fert: list((int, int, int)) = []
fert_to_water: list((int, int, int)) = []
water_to_light: list((int, int, int)) = []
light_to_temp: list((int, int, int)) = []
temp_to_humid: list((int, int, int)) = []
humid_to_loc: list((int, int, int)) = []
maps_list: list(list((int, int, int))) = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc]

next_line = ""
line_index = 0
list_index = 0
map_lines = lines[3:]
while True:
    next_line = map_lines[line_index]
    if next_line == "\n":
        line_index += 2
        list_index += 1
        print(line_index)
        next_line = map_lines[line_index]

    print(next_line, list_index)
    fillList(maps_list[list_index], next_line)

    line_index += 1

    if line_index >= len(map_lines):
        break

print("Seed ranges:", seed_ranges)
print(maps_list)

# Calculate soil positions for each range
soil: list((int, int)) = mapList(seed_ranges, seed_to_soil)
print("Soil: ", soil)
fert: list((int, int)) = mapList(soil, soil_to_fert)
print("Fert: ", fert)
water: list((int, int)) = mapList(fert, fert_to_water)
print("Water: ", water)
light: list((int, int)) = mapList(water, water_to_light)
print("Light: ", light)
temp: list((int, int)) = mapList(light, light_to_temp)
print("Temps: ", temp)
humid: list((int, int)) = mapList(temp, temp_to_humid)
print("Humid: ", humid)
loc: list((int, int)) = mapList(humid, humid_to_loc)
print("loc: ", loc)

minimum: int = loc[0][0]
for (loc, _) in loc:
    if loc < minimum:
        minimum = loc

print("Minimum: ", minimum)

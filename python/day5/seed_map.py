class SeedMap:
    def __init__(self):
        self.maps: list[dict()] = [dict(), dict(), dict(), dict(), dict(), dict(), dict()]

    def _find_in_map(self, seed_map: dict, loc: int) -> int:
        for (source, (target, length)) in seed_map.items():
            diff_from_source = loc - source
            if diff_from_source >= 0 and diff_from_source < length:
                return target + diff_from_source
            
        return loc


    def seed_to_soil(self, loc: int) -> int:
        return self._find_in_map(self.maps[0], loc)

    def soil_to_fertilizer(self, loc: int) -> int:
        return self._find_in_map(self.maps[1], loc)
    
    def fertilizer_to_water(self, loc: int) -> int:
        return self._find_in_map(self.maps[2], loc)
    
    def water_to_light(self, loc: int) -> int:
        return self._find_in_map(self.maps[3], loc)

    def light_to_temperature(self, loc: int) -> int:
        return self._find_in_map(self.maps[4], loc)

    def temperature_to_humidity(self, loc: int) -> int:
        return self._find_in_map(self.maps[5], loc)

    def humidity_to_location(self, loc: int) -> int:
        return self._find_in_map(self.maps[6], loc)
    
    def build(self, maps: list[list[str]]) -> None:
        for mi, m in enumerate(maps):
            for line in m:
                line_parts = [int(n) for n in line.split(" ")]
                source = line_parts[1]
                target = line_parts[0]
                length = line_parts[2]
                
                self.maps[mi][source] = (target, length)

    def find_location_for_seed(self, seed_loc: int) -> int:
        soil_loc = self.seed_to_soil(seed_loc)
        fert_loc = self.soil_to_fertilizer(soil_loc)
        water_loc = self.fertilizer_to_water(fert_loc)
        light_loc = self.water_to_light(water_loc)
        temp_loc = self.light_to_temperature(light_loc)
        humid_loc = self.temperature_to_humidity(temp_loc)
        return self.humidity_to_location(humid_loc)


# [
#     (start1, len1), for i in [ 79 , 80, ... , 79 + 14 ] | min([[1], 2, 3, 4, 5, 6 ])

#     (start2, len2),
#     (start3, len3),
#     (start4, len4),
# ]


# # Single mapping scenario:
# input = [[1], 2, 3, 4, 5, 6 ] # seed range
# mapping = "5 1 6"
# input_mapped = [5, 6, 7, 8, 9, 10]
# input_smart = (5, 6)

# # Seedrenge
# (1, 6) = [1, 2, 3, 4, 5, 6]
# map: 5 1 6
# (5, 6) = [5, 6, 7, 8, 9, 10]
# map: 18 5 6
# (18, 6) = [18, 19, 20, 21, 22, 23]


# # Difficult scenario
# (1, 6) = [1, 2, 3, 4, 5, 6]
# 0 <= 1 <= 10
# 1 + 6 <= 0 + 10
# map: 5 0 10
# (5 + 1 = 6, 6) = [6, 7, 8, 9, 10, 11]

# # Split scenario
# (1, 6) = [1, 2, 3, 4, 5, 6]
# map: 5 0 3 # [0, 1, 2] -> [5, 6, 7]

# (s, l) = [6, 7] [3, 4, 5, 6]
# (6, 2) and (3, 4)

# # next mapping step:
# for r in [(6, 2), (3, 4)]:


# # location ranges
# [(6, 2), (3, 2), (18, 6), (1, 2)] = 1
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

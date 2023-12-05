def give(num, mp: dict):
    for (k, v) in mp.items():
        source = k
        dest = v[0]
        delta = v[1]
        if num >= source and num <= source + delta - 1:
            return dest + (num - source)
    return num


def part1(input_file: str):
    stage = 0
    seeds = []
    seed_to_soil_map = {}
    soil_to_fertilizer_map = {}
    fertilizer_to_water_map = {}
    water_to_light_map = {}
    light_to_temp_map = {}
    temp_to_humidity_map = {}
    humidity_to_loc_map = {}

    with open(input_file) as f:
        for line in f:
            if line == "\n":
                continue
            if stage == 0 and "seeds" in line:
                seeds = [int(i) for i in line.split(":")[1].strip().split(" ")]
            elif "map" in line:
                stage += 1
                continue
            elif stage == 1:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                seed_to_soil_map[source] = (dest, delta)
            elif stage == 2:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                soil_to_fertilizer_map[source] = (dest, delta)
            elif stage == 3:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                fertilizer_to_water_map[source] = (dest, delta)
            elif stage == 4:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                water_to_light_map[source] = (dest, delta)
            elif stage == 5:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                light_to_temp_map[source] = (dest, delta)
            elif stage == 6:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                temp_to_humidity_map[source] = (dest, delta)
            elif stage == 7:
                nums = [int(i) for i in line.strip().split(" ")]
                dest = nums[0]
                source = nums[1]
                delta = nums[2]
                humidity_to_loc_map[source] = (dest, delta)

        locs = []
        for seed in seeds:
            soil = give(seed, seed_to_soil_map)
            fert = give(soil, soil_to_fertilizer_map)
            water = give(fert, fertilizer_to_water_map)
            light = give(water, water_to_light_map)
            temp = give(light, light_to_temp_map)
            hum = give(temp, temp_to_humidity_map)
            loc = give(hum, humidity_to_loc_map)
            locs.append(loc)
        return min(locs)


if __name__ == '__main__':
    print(part1("input.txt"))

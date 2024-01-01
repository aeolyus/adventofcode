seeds = []
seed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temp_map = {}
temp_to_humidity_map = {}
humidity_to_loc_map = {}


def calculate(i):
    hum = give_reverse(humidity_to_loc_map, i)
    temp = give_reverse(temp_to_humidity_map, hum)
    light = give_reverse(light_to_temp_map, temp)
    water = give_reverse(water_to_light_map, light)
    fert = give_reverse(fertilizer_to_water_map, water)
    soil = give_reverse(soil_to_fertilizer_map, fert)
    seed = give_reverse(seed_to_soil_map, soil)
    return seed


def valid_seed(s, seeds_lst):
    for seeds in seeds_lst:
        start, delta = seeds
        if start <= s < start + delta:
            return True
    return False


def give_reverse(mp, num):
    for (k, v) in mp.items():
        source = k
        dest = v[0]
        delta = v[1]
        if dest <= num < dest + delta:
            return source + (num - dest)
    return num


def give(num, mp: dict):
    for (k, v) in mp.items():
        source = k
        dest = v[0]
        delta = v[1]
        if num >= source and num <= source + delta - 1:
            return dest + (num - source)
    return num


# TODO: optimize with range slices
def part2(input_file: str):
    stage = 0
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

        seeds_lst = list(zip(seeds[::2], seeds[1::2]))
        for i in range(0, 100000000):
            seed = calculate(i)
            if valid_seed(seed, seeds_lst):
                return i

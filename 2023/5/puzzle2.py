import multiprocessing


def parse_mapping_section(section):
    mappings = []
    lines = section.strip().split('\n')
    for line in lines[1:]:
        dest_start, source_start, length = map(int, line.split())
        mappings.append((source_start, dest_start, length))
    return mappings


def apply_mapping(number, mappings):
    for src_start, dest_start, length in mappings:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number


def process_seed_range(seed_range, mappings):
    lowest_location = float('inf')
    start, length = seed_range
    for seed in range(start, start + length):
        soil = apply_mapping(seed, mappings[0])
        fertilizer = apply_mapping(soil, mappings[1])
        water = apply_mapping(fertilizer, mappings[2])
        light = apply_mapping(water, mappings[3])
        temperature = apply_mapping(light, mappings[4])
        humidity = apply_mapping(temperature, mappings[5])
        location = apply_mapping(humidity, mappings[6])

        if location < lowest_location:
            lowest_location = location

    return lowest_location


def process_almanac(data):
    sections = data.split('\n\n')
    seed_ranges_line = sections[0].split(': ')[1]
    seed_ranges = [tuple(map(int, seed_ranges_line.split()[i:i + 2]))
                   for i in range(0, len(seed_ranges_line.split()), 2)]

    mappings = [parse_mapping_section(section) for section in sections[1:8]]

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    results = [pool.apply_async(process_seed_range, args=(
        seed_range, mappings)) for seed_range in seed_ranges]
    pool.close()
    pool.join()

    return min(result.get() for result in results)


if __name__ == "__main__":
    almanac_data = None
    with open("2023/5/data.txt", 'r') as file:
        almanac_data = file.read()

    print(f"The lowest location number is: {process_almanac(almanac_data)}")

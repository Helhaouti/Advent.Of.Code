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

def process_almanac(data):
    sections = data.split('\n\n')
    
    seeds = list(map(int, sections[0].split(': ')[1].split()))

    seed_to_soil = parse_mapping_section(sections[1])
    soil_to_fertilizer = parse_mapping_section(sections[2])
    fertilizer_to_water = parse_mapping_section(sections[3])
    water_to_light = parse_mapping_section(sections[4])
    light_to_temperature = parse_mapping_section(sections[5])
    temperature_to_humidity = parse_mapping_section(sections[6])
    humidity_to_location = parse_mapping_section(sections[7])

    locations = []
    for seed in seeds:
        soil = apply_mapping(seed, seed_to_soil)
        fertilizer = apply_mapping(soil, soil_to_fertilizer)
        water = apply_mapping(fertilizer, fertilizer_to_water)
        light = apply_mapping(water, water_to_light)
        temperature = apply_mapping(light, light_to_temperature)
        humidity = apply_mapping(temperature, temperature_to_humidity)
        location = apply_mapping(humidity, humidity_to_location)
        locations.append(location)

    return min(locations)

almanac_data = None
with open("data.txt", 'r') as file:
    almanac_data = file.read()

print(f"The lowest location number is: {process_almanac(almanac_data)}")
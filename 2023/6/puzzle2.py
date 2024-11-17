from re import sub


def determine_options_to_beat_distance(time, distance):
    options = []

    for t in range(1, time):
        distance_at_t_speed = (time - t) * t
        if distance < distance_at_t_speed:
            options.append(distance_at_t_speed)

    return len(options)


def process_data(data):
    time = int(sub(r"\s+", '', ''.join(data[0].split(': ')[1])))
    distance = int(sub(r"\s+", '', ''.join(data[1].split(': ')[1])))

    return determine_options_to_beat_distance(time, distance)


data = None
with open("data.txt", 'r') as file:
    data = file.readlines()

print(f"The number of ways you can beat the record is: {process_data(data)}")

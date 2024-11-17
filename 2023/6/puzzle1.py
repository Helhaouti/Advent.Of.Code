from functools import reduce


def determine_options_to_beat_distance(time, distance):
    options = []

    for t in range(1, time):
        distance_at_t_speed = (time - t) * t
        if distance < distance_at_t_speed:
            options.append(distance_at_t_speed)

    return len(options)


def process_data(data):
    times = list(map(int, data[0].split(': ')[1].split()))
    distances = list(map(int, data[1].split(': ')[1].split()))

    options_per_game = [determine_options_to_beat_distance(times[game_i], distances[game_i])
                        for game_i in range(len(times))]

    return reduce(lambda x, y: x*y, options_per_game)


data = None
with open("data.txt", 'r') as file:
    data = file.readlines()

print(f"The number of ways you can beat the record is: {process_data(data)}")

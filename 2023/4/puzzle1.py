from re import findall, split


def clean_card_data(data: str) -> (int, [], []):
    data_split = data.split(":")

    card_number = int("".join(findall(r"\d", data_split[0])))

    numbers = data_split[1].split("|")

    winning_numbers = [int(number) for number in split(r"\s+", numbers[0].strip())]
    owned_numbers = [int(number) for number in split(r"\s+", numbers[1].strip())]

    return (card_number, winning_numbers, owned_numbers)


def determine_game_score(data: (int, [], [])) -> (int, int):
    id, l1, l2 = data[0], data[1], data[2]
    score = 0

    for l2_item in l2:
        if l2_item in l1:
            if score == 0:
                score = 1
                continue

            score *= 2

    return (id, score)


game_data = None
with open("data.txt", "r") as file:
    game_data = file.readlines()

game_data = list(map(clean_card_data, game_data))
game_data = list(map(determine_game_score, game_data))

total_points = sum([score[1] for score in game_data])
print(f"The total amount of points are: {total_points}")

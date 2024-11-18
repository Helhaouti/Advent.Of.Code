from re import findall, split


def clean_card_data(data: str) -> (int, list, list):
    data_split = data.split(":")

    card_number = int("".join(findall(r"\d", data_split[0])))

    numbers = data_split[1].split("|")

    winning_numbers = [int(number) for number in split(r"\s+", numbers[0].strip())]
    owned_numbers = [int(number) for number in split(r"\s+", numbers[1].strip())]

    return (card_number, winning_numbers, owned_numbers)


def determine_game_score(data: (int, list, list)) -> (int, int):
    card_number, winning_numbers, owned_numbers = data
    matches = len(set(winning_numbers) & set(owned_numbers))
    additional_cards = 0

    for i in range(1, matches + 1):
        additional_card = card_number + i
        if additional_card <= len(game_data):
            additional_cards += 1

    return (card_number, additional_cards)


game_data = None
with open("data.txt", "r") as file:
    game_data = file.readlines()

game_data = list(map(clean_card_data, game_data))
game_data = list(map(determine_game_score, game_data))

card_counts = {card[0]: 1 for card in game_data}
for card_number, additional_cards in game_data:
    for i in range(1, additional_cards + 1):
        next_card_number = card_number + i
        if next_card_number <= len(game_data):
            card_counts[next_card_number] = (
                card_counts.get(next_card_number, 0) + card_counts[card_number]
            )

total_scratchcards = sum(card_counts.values())
print(f"The total number of scratchcards is: {total_scratchcards}")

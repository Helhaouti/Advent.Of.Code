from itertools import groupby
from re import findall

MAX_CUBES_PER_COLOR = {"red": 12, "green": 13, "blue": 14}

content = None
with open("data.txt", "r") as file:
    content = file.read().split("\n")


def clean_item(s: str) -> dict:
    def determine_cubes_per_set(cube_sets_s: str) -> {}:
        return list(
            map(
                lambda x: (
                    int("".join(findall(r"\d", x))),
                    "".join(findall(r"[a-z]", x)),
                ),
                cube_sets_s.split(","),
            )
        )

    return {
        "id": int("".join(findall(r"\d", s.split(":")[0]))),
        "results": list(map(determine_cubes_per_set, s.split(":")[1].split(";"))),
    }


def determine_game_validity(data: dict[int, str]) -> bool:
    results, valid = data["results"], True

    for i in results:
        for color, value in i:
            if value > MAX_CUBES_PER_COLOR[color]:
                valid = False

    return valid


def determine_the_power(data: dict[int, str]) -> int:
    flattened_data = [item for sublist in data["results"] for item in sublist]
    power = 1

    grouped_data = {}
    for item, category in flattened_data:
        grouped_data.setdefault(category, []).append(item)

    for _, values in grouped_data.items():
        largest_value = max(values)
        power *= largest_value

    return power


content = list(map(clean_item, content))
content = list(map(determine_the_power, content))

print(sum(content))

# content = list(filter(determine_game_validity, content))
# sum_of_ids = sum(map(lambda x: x["id"], content))

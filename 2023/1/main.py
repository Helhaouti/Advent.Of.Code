from re import sub, match

DECIMAL_TO_WORD_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

items: str = None
with open("data.txt", "r") as file: items = file.read().split("\n")


def convert_to_numbers(s: str) -> str:
    helper_string = ""

    for i in range(len(s)):
        if match(r"[1-9]", s[i]):
            helper_string += (s[i])
            continue

        for length in [3, 4, 5]:
            if i + length <= len(s):
                substr = s[i:i + length].lower()
                if substr in DECIMAL_TO_WORD_MAP:
                    helper_string += DECIMAL_TO_WORD_MAP[substr] 
                    break

    return helper_string


items_numbered = list(map(convert_to_numbers, items))

items_dropped_non_decimals = list(map(
    lambda s: sub(r"[^1-9]", "", s),
    items_numbered
))

numbered_list = list(map(
    lambda s: list(s),
    items_dropped_non_decimals
))

items_contatenated_firstlast_pair = list(map(
    lambda l: int(str(l[0]) + str(l[-1])),
    numbered_list
))

print(f"sum: {sum(items_contatenated_firstlast_pair)}")
from functools import reduce

matrix = None
with open("data.txt", 'r') as file:
    matrix = file.readlines()


def is_symbol(char):
    """Check if the character is a symbol (not a digit or period)."""
    return not char.isdigit() and char not in ['.', '\n']


def calculate_total_gear_ratio(matrix):
    """Find and sum all part numbers in the schematic."""
    n_rows = len(matrix)
    gear_ratio = 0

    def get_r_size(r: int) -> int: return len(matrix[r])

    # Function to extract a number starting at a specific position
    def extract_number(r, c):
        coordinates = (r, c)
        num = ''

        if c < get_r_size(r):
            while c >= 0 and matrix[r][c].isdigit():
                coordinates = (r, c)
                c -= 1

            for char_i in range(coordinates[1], get_r_size(r)):
                char = matrix[r][char_i]

                if char.isdigit():
                    num += char
                else:
                    break

        return coordinates, int(num) if num.isdigit() else None

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(n_rows):
        for c in range(get_r_size(r)):
            if is_symbol(matrix[r][c]):
                neighbouring_noumbers = {}

                for dv, dh in directions:
                    iv, ih = r + dv, c + dh
                    if 0 <= iv < n_rows and 0 <= ih < get_r_size(r):
                        coör, num = extract_number(iv, ih)

                        if num is not None:
                            neighbouring_noumbers \
                                .setdefault(coör, set()) \
                                .add(num)

                if len(neighbouring_noumbers.items()) > 1:
                    numbers = [
                        item
                        for sublist in neighbouring_noumbers.values()
                        for item in sublist
                    ]
                    gear_ratio += int(reduce(lambda x, y: x*y, numbers))

    return gear_ratio


print(f"The total gear ratio of all is: {calculate_total_gear_ratio(matrix)}")

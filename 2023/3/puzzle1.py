matrix = None
with open("data.txt", "r") as file:
    matrix = file.readlines()


def is_symbol(char):
    """Check if the character is a symbol (not a digit or period)."""
    return not char.isdigit() and char not in [".", "\n"]


def find_part_numbers(matrix):
    """Find and sum all part numbers in the schematic."""
    n_rows = len(matrix)
    part_numbers = {}

    def get_r_size(r: int) -> int:
        return len(matrix[r])

    # Function to extract a number starting at a specific position
    def extract_number(r, c):
        coordinates = (r, c)
        num = ""

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

        return (coordinates, int(num) if num.isdigit() else None)

    # Check all 8 directions around a symbol
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(n_rows):
        for c in range(get_r_size(r)):
            if is_symbol(matrix[r][c]):
                for dv, dh in directions:
                    iv, ih = r + dv, c + dh
                    if 0 <= iv < n_rows and 0 <= ih < get_r_size(r):
                        coordinates, number = extract_number(iv, ih)

                        if number is not None:
                            part_numbers.setdefault(coordinates, set()).add(number)

    return sum([item for sublist in part_numbers.values() for item in sublist])


print(f"The sum of all part numbers is: {find_part_numbers(matrix)}")

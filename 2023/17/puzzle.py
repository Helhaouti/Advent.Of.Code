import heapq

DIRECTIONS = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def find_minimal_heat(end, min_distance, max_distance, heat_map):
    queue = [(0, 0, 0, 0, 0)]
    seen = set()

    while queue:
        heat, x, y, px, py = heapq.heappop(queue)

        if (x, y) == end:
            return heat
        if (x, y, px, py) in seen:
            continue

        seen.add((x, y, px, py))

        for dx, dy in DIRECTIONS - {(px, py), (-px, -py)}:
            new_x, new_y, current_heat = x, y, heat

            for i in range(1, max_distance + 1):
                new_x += dx
                new_y += dy
                if (new_x, new_y) in heat_map:
                    current_heat += heat_map[new_x, new_y]
                    if i >= min_distance:
                        heapq.heappush(queue, (current_heat, new_x, new_y, dx, dy))


def read_grid():
    with open("2023/17/data.txt", "r") as file:
        return {
            (i, j): int(c)
            for i, line in enumerate(file)
            for j, c in enumerate(line.strip())
        }


if __name__ == "__main__":
    board = read_grid()
    end_point = max(board)
    print(
        f"Part 1. The least heat loss it can incur: {find_minimal_heat(end_point, 1, 3, board)}"
    )
    print(
        f"Part 2. The least heat loss it can incur: {find_minimal_heat(end_point, 4, 10, board)}"
    )

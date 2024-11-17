def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value = (current_value + ascii_code) * 17 % 256
    return current_value


def parse_operation(operation):
    if '=' in operation:
        label, focal_length = operation.split('=')
        return (label, '=', int(focal_length))
    else:
        label = operation.rstrip('-')
        return (label, '-', None)


with open("data.txt", 'r') as file:
    boxes = {i: [] for i in range(256)}

    for operation in file.read().split(','):
        label, op, focal_length = parse_operation(operation)

        box_number = hash_algorithm(label)

        if op == "=":
            lens_in_box = next(
                (lens for lens in boxes[box_number] if lens[0] == label), None)
            if lens_in_box:
                boxes[box_number] = [(l, f) if l != label else (
                    label, focal_length) for l, f in boxes[box_number]]
            else:
                boxes[box_number].append((label, focal_length))

        elif op == "-":
            boxes[box_number] = [
                lens for lens in boxes[box_number] if lens[0] != label]

    total_focusing_power = sum(
        (box_number + 1) * (slot_number + 1) * focal_length
        for box_number, lenses in boxes.items()
        for slot_number, (_, focal_length) in enumerate(lenses)
    )

    print(f"The total the focusing power is: {total_focusing_power}")

def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value = (current_value + ascii_code) * 17 % 256
    return current_value

def process_data(data):
    steps = data.split(',')
    hash_results = [hash_algorithm(step) for step in steps]

    return sum(hash_results)


with open("data.txt", 'r') as file:
    data = process_data(file.read())
    print(f"The sum of the results is: {data}")

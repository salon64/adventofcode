with open('2025/day3/day_3_input.txt', 'r') as file:
    data = file.read().strip()

def update_rest_to_zero(arr, start_index):
    for k in range(start_index, len(arr)):
        arr[k] = 0

lines = [list(map(int, line)) for line in data.split('\n')]
sum = 0
for line in lines:
    # print(line)
    batteries = []
    remaining_batteries = 12
    start = -1

    while remaining_batteries > 0:
        available_digits = line[start+1 : len(line) - remaining_batteries + 1]
        i, largest_digit = max(enumerate(available_digits), key=lambda x: x[1])
        # print(f"available_digits: {available_digits}, largest_digit: {largest_digit}, index: {i}")
        batteries.append(largest_digit)
        start = i + start + 1
        remaining_batteries -= 1

    # print("".join(str(battery) for battery in batteries))
    sum += int("".join(str(battery) for battery in batteries))

print(sum)
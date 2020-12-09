
# fname, window_size = 'inputs/day09.test.txt', 5
fname, window_size = 'inputs/day09.txt', 25

with open(fname, 'r') as f:
    numbers = [int(l.strip()) for l in f.readlines()]


for i in range(window_size, len(numbers)):
    number_window = numbers[(i - window_size):i]
    valid_numbers = [x + y for x in number_window for y in number_window if x != y]
    if numbers[i] not in valid_numbers:
        print(numbers[i])
        break

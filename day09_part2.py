
# fname, window_size = 'inputs/day09.test.txt', 5
fname, window_size = 'inputs/day09.txt', 25

with open(fname, 'r') as f:
    numbers = [int(l.strip()) for l in f.readlines()]


for i in range(window_size, len(numbers)):
    number_window = numbers[(i - window_size):i]
    valid_numbers = [x + y for x in number_window for y in number_window if x != y]
    if numbers[i] not in valid_numbers:
        invalid_number = numbers[i]
        break


for i in range(len(numbers)):
    for j in range(i+1, len(numbers)-1):
        number_window = numbers[i:j+1]
        cumsum = sum(number_window)
        if cumsum == invalid_number:
            print(min(number_window) + max(number_window))
            raise Exception()
        elif cumsum > invalid_number:
            break

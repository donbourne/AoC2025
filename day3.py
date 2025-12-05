day=3
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def get_joltage(digits, num_digits):
    selected_digits = [0 for x in range(num_digits)]

    last_index = -1
    for i in range(num_digits):
        a = last_index + 1
        b = -num_digits+1+i
        available_digits = digits[a:b] if b < 0 else digits[a:]
        selected_digits[i] = max(available_digits)
        index = digits.index(selected_digits[i], last_index+1)
        last_index = index

    joltage = int(''.join(map(str, selected_digits)))
    return joltage


total_joltage_1 = 0
total_joltage_2 = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line_len = len(line)
        digits = [int(x) for x in line]
        total_joltage_1 += get_joltage(digits, 2)
        total_joltage_2 += get_joltage(digits, 12) 
 
print(f'part 1: {total_joltage_1}')
print(f'part 2: {total_joltage_2}')

        

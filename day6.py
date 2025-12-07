day=6
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def multiply(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def process_groups(operators, groups):
    results = []
    for op, group in zip(operators, groups):
        match op:
            case '+':
                results.append(sum(group))
            case '*':
                results.append(multiply(group))
    return results

with open(filename, 'rt') as f:
    lines = f.readlines()

# part 1
str_lines = [line.split() for line in lines]

# convert to ints
int_lines = []
for line in str_lines[:-1]:
    int_line = [int(i) for i in line]
    int_lines.append(int_line)

# build groups
num_groups = len(int_lines[0])
groups = [[] for _ in range(num_groups)]
for group in range(num_groups):
    for row in range(len(int_lines)):
        groups[group].append(int_lines[row][group])

# get operators
operators = str_lines[-1]

print(f'part 1: {sum(process_groups(operators, groups))}')

# part 2
chars = [list(line.replace('\n','')) for line in lines]
chars = chars[:-1]

# build groups
groups = []
group = []
for digits in zip(*chars):
    content = ''.join(digits).strip()
    if content != '':
        digits = int(content)
        group.append(digits)
    else:
        groups.append(group)
        group = []
groups.append(group)

print(f'part 2: {sum(process_groups(operators, groups))}')
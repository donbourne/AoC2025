day=2
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def check_repeats(s, num_repeats):
    if len(s) // num_repeats * num_repeats == len(s):
        # split the string into num_repeats parts
        part_len = len(s) // num_repeats
        parts = [s[i:i+part_len] for i in range(0, len(s), part_len)]
        for p in parts:
            if p != parts[0]:
                return False
        return True
    return False

# read the input file
pairs = []
with open(filename, 'rt') as f:
    data = f.readline()
    data = data.strip()
    data = data.split(',')
    for d in data:
        a,b = d.split('-')
        a = int(a)
        b = int(b)
        pairs.append((a,b))

# part 1
invalid_ids = []
for a,b in pairs:
    print(f'{a} - {b} ({b - a + 1})')
    for i in range(a,b+1):
        s = f'{i}'
        if check_repeats(s, 2):
            invalid_ids.append(i)

print(f'************** part 1: {sum(invalid_ids)}')

# part 2
invalid_ids = []
for a,b in pairs:
    print(f'{a} - {b} ({b - a + 1})')
    for i in range(a,b+1):
        s = f'{i}'
        for num_repeats in range(2, len(s)+1):
            if check_repeats(s, num_repeats):
                invalid_ids.append(i)
                break

print(f'************** part 2: {sum(invalid_ids)}')

day=5
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def within(x, a, b):
    return a <= x <= b

def overlap(a1, b1, a2, b2):
    if within(a1, a2, b2) or within(b1, a2, b2) or within(a2, a1, b1) or within(b2, a1, b1):
        return True

# merge 2 ranges that overlap - return merged range
def merge(a1, b1, a2, b2):
    return (min(a1, a2), max(b1, b2))

with open(filename, 'rt') as f:
    lines = f.readlines()

fresh_ranges = [(int(line.split('-')[0]), int(line.split('-')[1])) for line in lines if '-' in line] 
available = [int(line) for line in lines if '-' not in line and line.strip() != '']

count = 0
for x in available:
    for fresh_range in fresh_ranges:
        if within(x, fresh_range[0], fresh_range[1]):
            count += 1
            break
print(f"part 1: {count}")

added_ranges = []
for fresh_range in fresh_ranges:
    ranges_to_remove = []
    for added_range in added_ranges:
        if overlap(fresh_range[0], fresh_range[1], added_range[0], added_range[1]):
            fresh_range = merge(fresh_range[0], fresh_range[1], added_range[0], added_range[1])
            ranges_to_remove.append(added_range)
    for range_to_remove in ranges_to_remove:
        if range_to_remove not in added_ranges:
            print(f'ERROR: {range_to_remove} is not in {added_ranges}')
        added_ranges.remove(range_to_remove)
    added_ranges.append(fresh_range)

fresh_count = 0

# check if any of the ranges overlap
for added_range in added_ranges:
    for other_range in added_ranges:
        if added_range != other_range and overlap(added_range[0], added_range[1], other_range[0], other_range[1]):
            print(f'ERROR: {added_range} overlaps {other_range}')

for added_range in added_ranges:
    fresh_count += added_range[1] - added_range[0] + 1
print(f"part 2: {fresh_count}")

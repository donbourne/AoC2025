day=4
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def is_set(grid, row, col, row_max, col_max):
    if row < 0 or col < 0:
        return False 
    if row >= row_max or col >= col_max:
        return False
    return grid[row][col] == "@"

def count_adjacents(grid, row, col, row_max, col_max):
    count = 0
    count += is_set(grid, row - 1, col - 1, row_max, col_max)
    count += is_set(grid, row - 1, col, row_max, col_max)
    count += is_set(grid, row - 1, col + 1, row_max, col_max)
    count += is_set(grid, row, col - 1, row_max, col_max)
    count += is_set(grid, row, col + 1, row_max, col_max)
    count += is_set(grid, row + 1, col - 1, row_max, col_max)
    count += is_set(grid, row + 1, col, row_max, col_max)
    count += is_set(grid, row + 1, col + 1, row_max, col_max)
    return count

def is_available(grid, row, col, row_max, col_max):
    return is_set(grid, row, col, row_max, col_max) and count_adjacents(grid, row, col, row_max, col_max) < 4

def find_available_cells(grid, row_max, col_max):
    available_cells = []
    for row in range(row_max):
        for col in range(col_max):
            if is_available(grid, row, col, row_max, col_max):
                available_cells.append((row, col))
    return available_cells


# read the file into a list of lists
grid = []
with open(filename, 'rt') as f:
    grid = f.readlines()

for i, grid_row in enumerate(grid):
    grid[i] = list(grid_row.strip())

row_max = len(grid)
col_max = len(grid[0])

total_1 = 0
available_cells = find_available_cells(grid, row_max, col_max)
num_available_cells = len(available_cells)
print(f"part 1: {num_available_cells}")

total_2 = num_available_cells
while num_available_cells > 0:
    for row, col in available_cells:
        grid[row][col] = '.'
    available_cells = find_available_cells(grid, row_max, col_max)
    num_available_cells = len(available_cells)
    total_2 += num_available_cells

print(f"part 2: {total_2}")

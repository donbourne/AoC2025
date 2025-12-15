
# REMAINING STEPS...
# create a list of all the rectangles, with red at 2 opposite corners, that only contain red or green tiles
# create the corresponding list of rectangles using the original coordinates
# compute the area of each rectangle
# find the area of the largest rectangle

import time
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)

day=9
mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def print_array(arr):
    for i in range(arr.shape[0]):
        print(''.join(arr[i,:]))


def compute_area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

# returns True if point is inside the perimeter (including points on the perimeter), False otherwise
# ray cast a line to the right from the given point
# odd number of perimeter crossings means point is inside the perimeter
# only count perimeter crossings where with a vertical span of perimeter (approximated by cell above or below or both being a perimeter cell)
def is_in_polygon(x, y, grid):
    if grid[y][x] != '.':
        return True

    count = 0
    prev_is_edge = False 
    for i in range(x, grid.shape[1]):
        # print(y, i, ":", grid[y][i])
        curr_is_edge = grid[y][i] != '.'
        if curr_is_edge and not prev_is_edge:
            above = (y - 1 >= 0) and grid[y - 1][i] != '.'
            below = (y + 1 < grid.shape[0]) and grid[y + 1][i] != '.'
            if above or below:
                count += 1

        prev_is_edge = curr_is_edge

    return count % 2 == 1

def point_is_in_grid(x, y, grid):
    return grid.shape[1] > x >= 0 and grid.shape[1] > y >= 0    

def fill_polygon(x, y, grid, fill_char):
    stack = [(x,y)]
    while stack:
        cx, cy = stack.pop()
        if cx < 0 or cx >= grid.shape[1]:
            continue
        if cy < 0 or cy >= grid.shape[0]:
            continue
        # if not is_in_polygon(cx, cy, grid):
        #     continue
        if grid[cy,cx] != '.':
            continue
        grid[cy,cx] = fill_char
        if grid[cy, cx-1] == '.':
            stack.append((cx-1, cy))
        if grid[cy, cx+1] == '.':
            stack.append((cx+1, cy))
        if grid[cy-1, cx] == '.':
            stack.append((cx, cy-1))
        if grid[cy+1, cx] == '.':
            stack.append((cx, cy+1))
        # print_array(grid)
        # time.sleep(.1)



with open(filename, "rt") as f:
    lines = f.readlines()
    lines2 = [line.strip().split(',') for line in lines]
    points = [(int(x),int(y)) for x,y in lines2]

max_area = 0
for point in points:
    for other_point in points:
        if point == other_point:
            continue
        x1, y1 = point
        x2, y2 = other_point
        area = compute_area(x1, y1, x2, y2)
        if area > max_area:
            max_area = area
print(f'Part 1: {max_area}')

# miniaturize by enumerating the unique x/y values (keep a map from remaining points to original values)
x_points = set()
y_points = set()
for point in points:
    x,y = point
    x_points.add(x)
    y_points.add(y)
x_points = list(x_points)
y_points = list(y_points)
x_points.sort()
y_points.sort()

print(f'x points: {x_points}')
print(f'y points: {y_points}')
x_indexes = {}
x_rev_map = {}
y_indexes = {}
y_rev_map = {}
for i, point in enumerate(x_points):
    x_indexes.update({i:point})
    x_rev_map.update({point:i})
    
for i, point in enumerate(y_points):
    y_indexes.update({i:point})
    y_rev_map.update({point:i})

# create a grid
grid = np.zeros((len(y_points), len(x_points)), dtype=str)
grid.fill('.')

# create a list of points using the new point coordinates
mapped_points = []
for x,y in points:
    x_index = x_rev_map[x]
    y_index = y_rev_map[y]
    mapped_points.append((x_index, y_index))

# print(mapped_points)

for point in mapped_points:
    grid[point[1]][point[0]] = '#'

# print_array(grid)

# connect the points
for i in range(len(mapped_points)):
    mapped_point_a = mapped_points[i]
    mapped_point_b = mapped_points[(i+1)%len(mapped_points)]
    if mapped_point_a[0] == mapped_point_b[0]:
        for y in range(min(mapped_point_a[1], mapped_point_b[1])+1, max(mapped_point_a[1], mapped_point_b[1])):
            grid[y][mapped_point_a[0]] = 'X'
    elif mapped_point_a[1] == mapped_point_b[1]:
        for x in range(min(mapped_point_a[0], mapped_point_b[0])+1, max(mapped_point_a[0], mapped_point_b[0])):
            grid[mapped_point_a[1]][x] = 'X'
print_array(grid)

# find a point that is inside the polygon but not on the edge, then fill the polygon from that point
edge = grid != '.'
for px, py in [(mapped_points[0][0]-1, mapped_points[0][1]-1), (mapped_points[0][0]-1, mapped_points[0][1]+1), (mapped_points[0][0]+1, mapped_points[0][1]-1), (mapped_points[0][0]+1, mapped_points[0][1]+1)]:
    if not edge[py, px] and is_in_polygon(px, py, grid):
        fill_polygon(px, py, grid, 'X')

print_array(grid)


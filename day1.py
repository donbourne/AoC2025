
day=1
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

dial_start = 50

# returns the new dial position and the number of zero clicks
def move(current_dial_position, direction, distance):
    full_spins = int(distance / 100)
    zero_clicks = full_spins
    distance = distance - 100 * full_spins

    dial_position = current_dial_position

    if direction == 'R':
        new_dial_position = (dial_position + distance) % 100
        if new_dial_position < dial_position:
            zero_clicks += 1
        dial_position = new_dial_position
    elif direction == 'L':
        new_dial_position = (dial_position - distance) % 100
        if dial_position > 0 and (new_dial_position > dial_position or new_dial_position == 0):
            zero_clicks += 1
        dial_position = new_dial_position
    else:
        raise ValueError(f'Invalid direction: {direction}')
    return dial_position, zero_clicks


with (open(filename, 'rt') as f):
    data = f.readlines()
    data = [x.strip() for x in data]
    data = [(x[0], int(x[1:])) for x in data]
    
    dial_position = dial_start
    zero_stops = 0
    total_zero_clicks = 0
    for direction, distance in data:
        dial_position, zero_clicks = move(dial_position, direction, distance)
        if dial_position == 0:
            zero_stops += 1
        total_zero_clicks += zero_clicks
        print(f'{direction} {distance} zero stops: {zero_stops}, zero clicks: {total_zero_clicks}, new position: {dial_position}')

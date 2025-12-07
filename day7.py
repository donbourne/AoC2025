day=7
# mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'

def get_positions(c, lines):
    positions = []
    for line in lines:
        p = [i for i, x in enumerate(line) if x == c]
        positions.append(p)
    return positions

with open(filename) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

start_position = get_positions('S', lines)[0][0]
splitter_positions = get_positions('^', lines)

# first beam is on line 1, below the start position
beam_positions = [[] for _ in lines]
beam_position_counts = [{} for _ in lines]
beam_positions[1].append(start_position)
beam_position_counts[1]={start_position:1}
print(beam_positions)

split_count = 0
for line_number in range(2,len(lines)):
    bps = []
    bpcs = {}
    print("beam line     ", line_number-1, " - ", beam_positions[line_number-1])
    print("splitter line ", line_number, " - ", splitter_positions[line_number])

    for i, beam_position in enumerate(beam_positions[line_number-1]):
        beam_position_count = beam_position_counts[line_number-1].get(beam_position)
        if beam_position in splitter_positions[line_number]:
            split_count += 1
            bps.append(beam_position-1)
            bps.append(beam_position+1)
            bpcs.update({beam_position-1:beam_position_count+bpcs.get(beam_position-1,0)})
            bpcs.update({beam_position+1:beam_position_count+bpcs.get(beam_position+1,0)})
        else:
            bps.append(beam_position)
            bpcs.update({beam_position:beam_position_count+bpcs.get(beam_position,0)})
            
    bps = list(set(bps))
    bps.sort()
    beam_positions[line_number] = bps
    beam_position_counts[line_number] = bpcs
    
    print("new beam line ", line_number, " - ", beam_positions[line_number])
    print("counts        ", line_number, " - ", beam_position_counts[line_number])
    print()

print(f"part1: {split_count}")
print(f"part2: {sum(beam_position_counts[-1].values())}")
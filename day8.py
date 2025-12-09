from math import dist, sqrt

day=8
mode='test'
mode='real'
filename=f'input/day{day}-{mode}.txt'
part = 1

max_connections = 10 if mode == 'test' else 1000

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = Circuit(self)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    @staticmethod
    def distance_between(p1, p2):
        return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

    def __eq__(self, other):
        x = True
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __gt__(self, other):
        x = 0
        if self.x < other.x:
            pass
        elif self.x > other.x:
            x = 1
        elif self.y < other.y:
            pass
        elif self.y > other.y:
            x = 1
        elif self.z < other.z:
            pass
        elif self.z > other.z:
            x = 1
        return x

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'

class Connection:
    def __init__(self, junction_box_1, junction_box_2):
        # always put the smaller one first (in case it matters)
        if junction_box_1 > junction_box_2:
            self.junction_box_1 = junction_box_2
            self.junction_box_2 = junction_box_1
        else:
            self.junction_box_1 = junction_box_1
            self.junction_box_2 = junction_box_2

class Circuit:
    all_circuits = set()

    def __init__(self, junction_box) -> None:
        self.connections = list()
        self.junction_boxes = set()
        self.junction_boxes.add(junction_box)
        junction_box.circuit = self
        Circuit.all_circuits.add(self)

    def merge(self, new_junction_box, new_connection):
        self.connections.append(new_connection)
        circuit_to_remove = new_junction_box.circuit
        self.connections.extend(circuit_to_remove.connections)
        self.junction_boxes.update(circuit_to_remove.junction_boxes)
        for junction_box in circuit_to_remove.junction_boxes:
            junction_box.circuit = self
        Circuit.all_circuits.remove(circuit_to_remove)

    @staticmethod
    def print_all_circuits():
        for circuit in Circuit.all_circuits:
            circuit.count = len(circuit.junction_boxes)

        circuit_count_list = [circuit.count for circuit in Circuit.all_circuits]
        circuit_count_list.sort(reverse=True)
        if part == 1:
            print(f'{circuit_count_list} - top 3: {circuit_count_list[0]*circuit_count_list[1]*circuit_count_list[2]}')


def compute_distances(junction_boxes):
    distances = []
    for point in junction_boxes:
        for other_point in junction_boxes:
            if point is not other_point:
                if point > other_point:
                    pass
                else:
                    distances.append((point, other_point, JunctionBox.distance_between(point, other_point)))
    return distances

with open(filename, "rt") as f:
    junction_boxes = [JunctionBox(*map(int, line.strip().split(','))) for line in f.readlines()]

distances = compute_distances(junction_boxes)
distances.sort(key=lambda x: x[2])

num_connections = 0
for i, (jb_0, jb_1, distance) in enumerate(distances):
    Circuit.print_all_circuits()

    if part == 1 and num_connections == max_connections:
        break
    if part == 2 and len(Circuit.all_circuits) == 1:
        break

    connection = Connection(jb_0,jb_1)
    print(f"Connecting {jb_0} and {jb_1} - {jb_0.x * jb_1.x}")
    for circuit in Circuit.all_circuits:
        if jb_0 in circuit.junction_boxes:
            if jb_1 in circuit.junction_boxes:
                num_connections += 1
                
                break
            else:
                circuit.merge(jb_1, connection)
                num_connections += 1
                break
        elif jb_1 in circuit.junction_boxes:
            circuit.merge(jb_0, connection)
            num_connections += 1
            break

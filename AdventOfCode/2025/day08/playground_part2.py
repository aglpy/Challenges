""" Advent Of Code 2025: Day 07 Part 1 """
import sys
import time
from typing import List, Optional
from juction_box import Circuit, JunctionBox, SingleWire

def calculate_possible_wires(junction_boxes: list[JunctionBox]) -> List[SingleWire]:
    """ Calculate possible wires """
    possible_wires = []
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            possible_wires.append(SingleWire(junction_boxes[i], junction_boxes[j]))
    return sorted(possible_wires)

def circuit_junction_boxes(junction_boxes: list[JunctionBox]) -> int:
    """ Circuit junction boxes """
    possible_wires = calculate_possible_wires(junction_boxes)
    circuits: List[Circuit] = []
    for candidate_wire in possible_wires:
        circuit_box_a: Optional[Circuit] = None
        circuit_box_b: Optional[Circuit] = None
        for circuit in circuits:
            if candidate_wire.a in circuit:
                circuit_box_a = circuit
            if candidate_wire.b in circuit:
                circuit_box_b = circuit
            if circuit_box_a and circuit_box_b:
                break
        if circuit_box_a and circuit_box_b:
            if circuit_box_a is circuit_box_b:
                continue
            new_circuit = circuit_box_a + circuit_box_b
            circuits.remove(circuit_box_a)
            circuits.remove(circuit_box_b)
            circuits.append(new_circuit)
        elif circuit_box_a:
            circuit_box_a.connect(candidate_wire.b)
        elif circuit_box_b:
            circuit_box_b.connect(candidate_wire.a)
        else:
            circuits.append(Circuit([candidate_wire.a, candidate_wire.b]))
        candidate_wire.a.connections += 1
        candidate_wire.b.connections += 1
        if len(circuits) == 1 and len(junction_boxes) == circuits[0].length:
            break
    return candidate_wire.a.x * candidate_wire.b.x

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()
    
    junction_boxes = [JunctionBox.from_string(line) for line in data.splitlines()]

    start = time.time()
    result = circuit_junction_boxes(junction_boxes)
    print(f'Joined junction boxes: {result}')

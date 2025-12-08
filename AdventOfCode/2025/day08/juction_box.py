""" Junction box related objects """

class JunctionBox:
    """ Junction Box object """

    def __init__(self, x: int, y: int, z: int):
       self.x, self.y, self.z = x, y, z
       self.connections = 0

    @classmethod
    def from_string(cls, string: str):
        """ Create a JunctionBox object from a string """
        x, y, z = string.split(',')
        return cls(int(x), int(y), int(z))

    def __lt__(self, other: 'JunctionBox') -> bool:
        return self.connections < other.connections

    def __repr__(self) -> str:
        return f'JunctionBox({self.x},{self.y},{self.z})-{self.connections}'

class SingleWire:
    """ Single wire joining 2 Junction Boxes """

    def __init__(self, a: JunctionBox, b: JunctionBox):
        self.a = a
        self.b = b
        self.square_distance = (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

    def __lt__(self, other: 'SingleWire') -> bool:
        return self.square_distance < other.square_distance
    
    def __repr__(self) -> str:
        return (f'{self.a.x},{self.a.y},{self.a.z}'
                f' <--{self.square_distance}--> '
                f'{self.b.x},{self.b.y},{self.b.z}')

class Circuit:
    """ Circuit of junction boxes or a reduced List class called Circuit """

    def __init__(self, junction_boxes: list[JunctionBox]):
        self.junction_boxes = junction_boxes

    def connect(self, junction_box: JunctionBox):
        """ Append a junction box to the circuit """
        self.junction_boxes.append(junction_box)

    @property
    def length(self) -> int:
        """ Return the length of the circuit """
        return len(self.junction_boxes)

    def __lt__(self, other: 'Circuit') -> bool:
        return self.length < other.length
    
    def __contains__(self, junction_box: JunctionBox) -> bool:
        return junction_box in self.junction_boxes

    def __add__(self, other: 'Circuit') -> 'Circuit':
        return Circuit(self.junction_boxes + other.junction_boxes)

    def __repr__(self) -> str:
        return f"Circuit({'\n\t'.join(str(junction_box) for junction_box in self.junction_boxes)})"
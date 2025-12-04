""" Sub Interval class """

class SubInterval:
    """ Object representing an interval of same digits with a sub division """

    def __init__(self, start: int, end: int, subdivisions: int):
        self.start = start
        self.end = end
        self.digits = len(str(start))
        self.subdivisions = subdivisions
        self.subdivisions_length = self.digits // subdivisions
    
    @property
    def invalid_ids(self) -> list[int]:
        """ Get the invalid IDs of the interval """
        start_divisions = []
        str_start = str(self.start)
        for i in range(0, len(str_start), self.subdivisions_length):
            start_divisions.append(int(str_start[i:i+self.subdivisions_length]))
        for i in range(len(start_divisions)-1, 0, -1):
            if start_divisions[i] > start_divisions[i-1]:
                start_divisions[i-1] += 1
        end_divisions = []
        str_end = str(self.end)
        for i in range(0, len(str_end), self.subdivisions_length):
            end_divisions.append(int(str_end[i:i+self.subdivisions_length]))
        for i in range(len(end_divisions)-1, 0, -1):
            if end_divisions[i] < end_divisions[i-1]:
                end_divisions[i-1] -= 1

        invalid_division_range = range(start_divisions[0], end_divisions[0] + 1)
        return [
            int(str(invalid_division)*self.subdivisions)
            for invalid_division in invalid_division_range
        ]

    def __repr__(self):
        return f"DigitInterval({self.start}, {self.end}, {self.subdivisions})"
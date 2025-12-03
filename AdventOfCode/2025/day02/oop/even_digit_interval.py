""" Event digit interval class """

class EvenDigitInterval:
    """ Object representing an interval of even number of digits """

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.digits = len(str(start))
    
    @property
    def invalid_ids(self) -> list[int]:
        """ Get the invalid IDs of the interval """
        first_half_start = int(str(self.start)[:self.digits // 2])
        last_half_start = int(str(self.start)[self.digits // 2:])
        if first_half_start < last_half_start:
            invalid_half_start = first_half_start + 1
        else:
            invalid_half_start = first_half_start

        first_half_end = int(str(self.end)[:self.digits // 2])
        last_half_end = int(str(self.end)[self.digits // 2:])
        if first_half_end > last_half_end:
            invalid_half_end = first_half_end - 1
        else:
            invalid_half_end = first_half_end

        invalid_half_range = range(invalid_half_start, invalid_half_end + 1)
        return [int(str(invalid_half)*2) for invalid_half in invalid_half_range]
        
    def __repr__(self):
        return f"EvenDigitInterval({self.start}, {self.end})"
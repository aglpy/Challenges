""" Interval class """
from even_digit_interval import EvenDigitInterval
from sub_interval import SubInterval

class Interval:
    """ Object representing a whole interval """

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.even_digit_intervals = self._get_even_digit_intervals()
        self.sub_intervals = self._get_sub_intervals()

    def _get_even_digit_intervals(self) -> list[EvenDigitInterval]:
        """ Get the even digit intervals of the interval """
        start_digits = len(str(self.start))
        end_digits = len(str(self.end))
        even_digit_intervals = []
        for i in range(start_digits, end_digits + 1):
            if i % 2 == 0:
                start = max(self.start, 10 ** (i - 1))
                end = min(self.end, 10 ** i - 1)
                even_digit_intervals.append(EvenDigitInterval(start, end))
        return even_digit_intervals

    def _get_equal_digit_intervals(self) -> list[tuple[int, int]]:
        """ Get the equal digit intervals of the interval """
        start_digits = len(str(self.start))
        end_digits = len(str(self.end))
        equal_digit_intervals = []
        for i in range(start_digits, end_digits + 1):
            start = max(self.start, 10 ** (i - 1))
            end = min(self.end, 10 ** i - 1)
            equal_digit_intervals.append((start, end))
        return equal_digit_intervals

    def _get_sub_intervals(self) -> list[SubInterval]:
        """ Get the sub intervals of the interval """
        equal_digit_intervals = self._get_equal_digit_intervals()
        sub_intervals = []
        for start, end in equal_digit_intervals:
            for i in range(1, (len(str(start)) // 2) + 1):
                if len(str(start)) % i == 0:
                    sub_intervals.append(SubInterval(start, end, len(str(start)) // i))
        return sub_intervals
    
    @classmethod
    def from_string(cls, string: str):
        """ Create an interval from a string """
        start, end = string.split("-")
        return cls(int(start), int(end))

    @property
    def invalid_ids(self) -> list[int]:
        """ Get the invalid IDs of the interval """
        return [
            invalid_id
            for interval in self.even_digit_intervals for invalid_id in interval.invalid_ids
        ]

    @property
    def invalid_ids_any_length(self) -> list[int]:
        """ Get the invalid IDs of the interval """
        return list({
            invalid_id
            for interval in self.sub_intervals for invalid_id in interval.invalid_ids
        })

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"
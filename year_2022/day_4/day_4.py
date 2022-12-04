import timeit
from typing import Union

######################################
# https://adventofcode.com/2022/day/4
######################################

with open("input_data.txt") as file:
    data = file.read()


class SectionAssignmentRange:
    def __init__(self, start: Union[str, int], end: Union[str, int]):
        self.start = int(start)
        self.end = int(end)

    def __contains__(self, item: Union[str, int, "SectionAssignmentRange"]) -> bool:
        if isinstance(item, SectionAssignmentRange):
            return self.start <= item.start <= item.end <= self.end
        elif isinstance(item, str):
            return self.start <= int(item) <= self.end
        else:
            raise TypeError(f"Unsupported type {type(item)}")

    def has_intersection(self, other: "SectionAssignmentRange") -> bool:
        """
        Check if two ranges have an intersection
        """
        return (
            self.start <= other.start <= self.end
            or other.start <= self.start <= other.end
        )


def convert_input_data_line_to_tuple_of_ranges(line: str) -> tuple:
    assignment_1, assignment_2 = line.split(",")
    range_1 = SectionAssignmentRange(*assignment_1.split("-"))
    range_2 = SectionAssignmentRange(*assignment_2.split("-"))
    return range_1, range_2


def solution_part_1():
    subset_assignments = 0
    for line in data.splitlines():
        range_1, range_2 = convert_input_data_line_to_tuple_of_ranges(line)
        if range_2 in range_1:
            subset_assignments += 1
        elif range_1 in range_2:
            subset_assignments += 1

    return subset_assignments


def solution_part_2():
    overlapping_assignments = 0
    for line in data.splitlines():
        range_1, range_2 = convert_input_data_line_to_tuple_of_ranges(line)
        if range_1.has_intersection(range_2):
            overlapping_assignments += 1

    return overlapping_assignments


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10 *1000}ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10 * 1000}ms'
    )

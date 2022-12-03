import string
import timeit
from string import ascii_letters

######################################
# https://adventofcode.com/2022/day/3
######################################

with open("input_data.txt") as file:
    data = file.read()

priority = {char: value + 1 for value, char in enumerate(ascii_letters)}


def solution_part_1():
    sum_of_priorities = 0
    for line in data.splitlines():
        line_middle = len(line) // 2
        first_compartment_items, second_compartment_items = (
            line[:line_middle],
            line[line_middle:],
        )
        common_letter = (
            set(first_compartment_items) & set(second_compartment_items)
        ).pop()

        sum_of_priorities += priority[common_letter]

    return sum_of_priorities


def solution_part_2():
    sum_of_priorities = 0
    lines = data.splitlines()
    groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    for group in groups:
        common_letter_in_group = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        sum_of_priorities += priority[common_letter_in_group]

    return sum_of_priorities


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000 * 1000}ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000 * 1000}ms'
    )

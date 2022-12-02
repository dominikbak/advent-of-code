import timeit

######################################
# https://adventofcode.com/2022/day/{DAY}
######################################

with open("input_data.txt") as file:
    data = file.read()


def solution_part_1():
    pass


def solution_part_2():
    pass


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )

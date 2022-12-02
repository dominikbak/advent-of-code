import timeit

######################################
# https://adventofcode.com/2022/day/1
######################################

with open("input_data.txt") as file:
    data = file.read()


def solution_part_1():
    return max(
        [sum([int(x) for x in elf.split("\n")]) for elf in data.strip().split("\n\n")]
    )


def solution_part_2():
    return sum(
        sorted(
            [
                sum([int(x) for x in elf.split("\n")])
                for elf in data.strip().split("\n\n")
            ],
            reverse=True,
        )[:3]
    )


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )

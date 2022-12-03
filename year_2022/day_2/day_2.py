import timeit
from enum import IntEnum
from typing import Optional

######################################
# https://adventofcode.com/2022/day/2
######################################

with open("input_data.txt") as file:
    data = file.read()


class GameOutcome(IntEnum):
    """
    int values are the scores for the outcome
    """

    LOSE = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def get_by_actions(
        cls,
        player_action: "Action",
        opponent_action: "Action",
    ) -> "GameOutcome":
        """
        Determine the outcome of a round of rock paper scissors for the player
        """
        if player_action == opponent_action:
            return cls.DRAW
        elif player_action.get_stronger_action() == opponent_action:
            return cls.LOSE
        elif player_action.get_weaker_action() == opponent_action:
            return cls.WIN

    @classmethod
    def get_by_letter(cls, letter):
        if letter == "X":
            return cls.LOSE
        elif letter == "Y":
            return cls.DRAW
        elif letter == "Z":
            return cls.WIN
        else:
            raise ValueError(f"Invalid letter {letter}")


class Action(IntEnum):
    """
    The players get different scores for using different actions.
    Int values are the scores of the actions
    """

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def get_by_letter(cls, letter: str) -> Optional["Action"]:
        if letter in ["A", "X"]:
            return cls.ROCK
        elif letter in ["B", "Y"]:
            return cls.PAPER
        elif letter in ["C", "Z"]:
            return cls.SCISSORS
        else:
            ValueError(f"Invalid letter {letter}")

    @classmethod
    def get_by_opponent_action(
        cls, opponent_action: "Action", expected_outcome: GameOutcome
    ) -> "Action":
        """

        :param opponent_action:
        :param expected_outcome:
        :return: action that should be played in order to achieve expected outcome
        """
        if expected_outcome == GameOutcome.DRAW:
            return opponent_action
        elif expected_outcome == GameOutcome.LOSE:
            return opponent_action.get_weaker_action()
        elif expected_outcome == GameOutcome.WIN:
            return opponent_action.get_stronger_action()

    def get_stronger_action(self):
        """
        :return: action that will win with self
        """
        if self == Action.PAPER:
            return Action.SCISSORS
        if self == Action.SCISSORS:
            return Action.ROCK
        if self == Action.ROCK:
            return Action.PAPER

    def get_weaker_action(self):
        """
        :return: action that will lose with self
        """
        if self == Action.PAPER:
            return Action.ROCK
        if self == Action.ROCK:
            return Action.SCISSORS
        if self == Action.SCISSORS:
            return Action.PAPER


def solution_part_1():
    games = data.strip().split("\n")
    player_score = 0

    for game in games:
        opponent_action, player_action = list(
            map(Action.get_by_letter, game.split(" "))
        )
        player_score += GameOutcome.get_by_actions(player_action, opponent_action).value
        player_score += player_action.value

    return player_score


def solution_part_2():
    games = data.strip().split("\n")
    player_score = 0

    for game in games:
        opponent_action_str, expected_outcome_str = game.split(" ")
        opponent_action = Action.get_by_letter(opponent_action_str)
        expected_outcome = GameOutcome.get_by_letter(expected_outcome_str)

        player_score += Action.get_by_opponent_action(
            opponent_action, expected_outcome
        ).value
        player_score += expected_outcome.value

    return player_score


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )

from typing import List, Dict
from constants import directions


def avoid_walls(my_head: Dict[str, int], board_width: int, board_height: int, possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
          e.g. {"x": 0, "y": 0}
    board_width: Width of the board (x-axis)
    board_height: Height of the board (y-axis)
    possible_moves: List of strings. Moves to pick from.
          e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    if my_head["x"] == 0:
        possible_moves.remove("left")
    elif my_head["x"] == board_width - 1:
        possible_moves.remove("right")

    if my_head["y"] == 0:
        possible_moves.remove("down")
    elif my_head["y"] == board_height - 1:
        possible_moves.remove("up")

    return possible_moves


def avoid_body(my_head: Dict[str, int], body: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """

    def not_in_body(move: str):
        new_position = {"x": my_head["x"] + directions[move]["x"], "y": my_head["y"] + directions[move]["y"]}
        return new_position not in body

    return list(filter(not_in_body, possible_moves))


def avoid_other_snakes(my_head: Dict[str, int], snakes: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    snakes: List of dictionaries containing information about enemy Battlesnakes.
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    for snake in snakes:
        possible_moves = avoid_body(my_head, snake["body"], possible_moves)

    return possible_moves
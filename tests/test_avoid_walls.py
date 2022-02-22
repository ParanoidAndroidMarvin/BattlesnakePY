import server_logic
import pytest


@pytest.mark.parametrize("my_head, board_width, board_height, expected_result", [
    ({"x": 5, "y": 5}, 11, 11, ["up", "down", "left", "right"]),
    ({"x": 5, "y": 0}, 11, 11, ["up", "left", "right"]),
    ({"x": 5, "y": 10}, 11, 11, ["down", "left", "right"]),
    ({"x": 0, "y": 5}, 11, 11, ["up", "down", "right"]),
    ({"x": 10, "y": 5}, 11, 11, ["up", "down", "left"]),
])
def test_avoid_walls(my_head, board_width, board_height, expected_result):
    possible_moves = ["up", "down", "left", "right"]
    server_logic.avoid_walls(my_head, board_width, board_height, possible_moves)
    assert possible_moves == expected_result

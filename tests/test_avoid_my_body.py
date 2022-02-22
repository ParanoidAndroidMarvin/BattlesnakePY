import pytest
from server_logic import avoid_my_body


@pytest.mark.parametrize("my_body, expected_result", [
    ([{"x": 5, "y": 5}, {"x": 5, "y": 5}], ["up", "down", "left", "right"]),  # Starting position
    ([{"x": 4, "y": 5}, {"x": 3, "y": 5}], ["up", "down", "right"]),
    ([{"x": 6, "y": 5}, {"x": 7, "y": 5}], ["up", "down", "left"]),
    ([{"x": 5, "y": 4}, {"x": 5, "y": 3}], ["up", "left", "right"]),
    ([{"x": 5, "y": 6}, {"x": 5, "y": 7}], ["down", "left", "right"]),
    ([{"x": 5, "y": 6}, {"x": 6, "y": 6}, {"x": 6, "y": 5}], ["down", "left"]),
    ([{"x": 4, "y": 5}, {"x": 4, "y": 4}, {"x": 5, "y": 4}], ["up", "right"]),
    ([{"x": 4, "y": 5}, {"x": 4, "y": 4}, {"x": 5, "y": 4}, {"x": 6, "y": 4}, {"x": 6, "y": 5}], ["up"]),
])
def test_avoid_walls(my_body, expected_result):
    possible_moves = ["up", "down", "left", "right"]
    my_head = {"x": 5, "y": 5}

    possible_moves = avoid_my_body(my_head, my_body, possible_moves)

    assert possible_moves == expected_result

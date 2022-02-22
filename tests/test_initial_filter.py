import pytest
from initial_filter import avoid_walls, avoid_body, avoid_other_snakes

dummy_snake_1 = {"body": [{"x": 4, "y": 5}, {"x": 3, "y": 5}, {"x": 3, "y": 6}]}
dummy_snake_2 = {"body": [{"x": 5, "y": 4}, {"x": 5, "y": 3}, {"x": 5, "y": 1}]}
dummy_snake_3 = {"body": [{"x": 5, "y": 6}, {"x": 6, "y": 6}, {"x": 6, "y": 5}]}


@pytest.mark.parametrize("my_head, board_width, board_height, expected_result", [
    ({"x": 5, "y": 5}, 11, 11, ["up", "down", "left", "right"]),
    ({"x": 5, "y": 0}, 11, 11, ["up", "left", "right"]),
    ({"x": 5, "y": 10}, 11, 11, ["down", "left", "right"]),
    ({"x": 0, "y": 5}, 11, 11, ["up", "down", "right"]),
    ({"x": 10, "y": 5}, 11, 11, ["up", "down", "left"]),
])
def test_avoid_walls(my_head, board_width, board_height, expected_result):
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = avoid_walls(my_head, board_width, board_height, possible_moves)
    assert possible_moves == expected_result


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
def test_avoid_body(my_body, expected_result):
    possible_moves = ["up", "down", "left", "right"]
    my_head = {"x": 5, "y": 5}

    possible_moves = avoid_body(my_head, my_body, possible_moves)

    assert possible_moves == expected_result


@pytest.mark.parametrize("snakes, expected_result", [
    ([], ["up", "down", "left", "right"]),
    ([dummy_snake_1], ["up", "down", "right"]),
    ([dummy_snake_2], ["up", "left", "right"]),
    ([dummy_snake_1, dummy_snake_2], ["up", "right"]),
    ([dummy_snake_1, dummy_snake_3], ["down"]),
    ([dummy_snake_1, dummy_snake_2, dummy_snake_3], []),
])
def test_avoid_other_snakes(snakes, expected_result):
    possible_moves = ["up", "down", "left", "right"]
    my_head = {"x": 5, "y": 5}

    possible_moves = avoid_other_snakes(my_head, snakes, possible_moves)

    assert possible_moves == expected_result

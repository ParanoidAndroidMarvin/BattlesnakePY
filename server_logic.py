import random
from initial_filter import avoid_walls, avoid_body, avoid_other_snakes


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """

    # ---------------------------------------------------------
    # VARIABLES
    # ---------------------------------------------------------
    my_head = data["you"]["head"]
    my_body = data["you"][
        "body"]

    board_width = data["board"]["width"]
    board_height = data["board"]["height"]

    snakes = data["board"]["snakes"]

    possible_moves = ["up", "down", "left", "right"]

    # ---------------------------------------------------------
    # STEP 1: FILTER POSSIBLE MOVES
    # ---------------------------------------------------------

    # Don't allow the Battlesnake to move out of the board
    possible_moves = avoid_walls(my_head, board_width, board_height, possible_moves)
    # Don't allow the Battlesnake to collide with own body
    possible_moves = avoid_body(my_head, my_body, possible_moves)
    # Don't allow the Battlesnake to collide with enemy snakes
    possible_moves = avoid_other_snakes(my_head, snakes, possible_moves)

    # ---------------------------------------------------------
    # STEP 2: SELECT BEST POSSIBLE MOVE
    # ---------------------------------------------------------

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

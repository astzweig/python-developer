from math import ceil

def get_tenis_points_of_all_players(points_of_player_one: list[int]) -> (int, int):
    points_of_player_one = points_of_player_one.copy()
    points_of_player_two = calculate_opposite_points(points_of_player_one)

    add_bonus_points(points_of_player_one)
    add_bonus_points(points_of_player_two)

    return sum(points_of_player_one), sum(points_of_player_two)

def calculate_opposite_points(points: list[int]) -> list[int]:
    opposite_points = []
    for point in points:
        opposite_points.append(3 - point)
    return opposite_points

def add_bonus_points(points: list[int]):
    reference_points = points.copy()
    multiplier = 1.5
    offset = 1
    indexes_to_modify = []
    for idx, point in enumerate(reference_points):
        offset_index = idx + offset
        offset_index_exists = len(points) > offset_index
        if point == 2 and offset_index_exists:
            indexes_to_modify.append(offset_index)

    for idx in indexes_to_modify:
        points[idx] = ceil(points[idx] * multiplier)

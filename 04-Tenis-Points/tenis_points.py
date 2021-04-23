from math import ceil, prod

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
    multiplier_lists = get_multiplier_lists(points)
    apply_multiplier_lists(points, multiplier_lists)

def apply_multiplier_lists(points: list[int], multiplier_lists: list[int]):
    for idx, point in enumerate(points):
        multiplier = prod(multiplier_lists[idx])
        points[idx] = ceil(point * multiplier)

def get_multiplier_lists(points: list[int]) -> list[list[float]]:
    multiplier_lists = [[] for point in points]
    for idx, point in enumerate(points):
        multiplier = get_multiplier(point)
        offset = get_index_to_modify_or_return_negative(point, idx, len(points))
        if offset > -1:
            multiplier_lists[offset].append(multiplier)
    return multiplier_lists

def get_index_to_modify_or_return_negative(point: int, at_index: int, amount_of_points: int) -> int:
    offset = get_index_offset(point)
    offset_index = at_index + offset
    if 0 <= offset_index < amount_of_points:
        return offset_index
    return -1

def get_multiplier(point: int) -> float:
    if (point == 3): return 2.0
    if (point == 2): return 1.5
    return 1.0

def get_index_offset(point: int) -> int:
    if (point == 3): return 2
    if (point == 2): return 1
    return 0

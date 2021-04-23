def get_tenis_points_of_all_players(points_of_player_one: list[int]) -> (int, int):
    points_of_player_two = calculate_opposite_points(points_of_player_one)
    return sum(points_of_player_one), sum(points_of_player_two)

def calculate_opposite_points(points: list[int]) -> list[int]:
    opposite_points = []
    for point in points:
        opposite_points.append(3 - point)
    return opposite_points

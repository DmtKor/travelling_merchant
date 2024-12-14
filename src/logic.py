from itertools import permutations
from .gui import algorithm_gui_update

class Points:
    def __init__(self, P):
        self.P = P
    def metric(p1, p2):
        return(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5)
    
def brute_force(points, speed = 0, font = 0, screen = 0, cli = False):
    # Logic
    roads = permutations(points.P[1:])
    min_len = float("inf")
    optimal_road = []
    N = len(points.P)
    for r in roads:
        r = list(r)
        r.insert(0, points.P[0])
        r.append(points.P[0])
        l = 0
        for i in range(N):
            l = l + Points.metric(r[i], r[i + 1])
        if l < min_len:
            min_len = l
            optimal_road = r

        # for GUI
        if not cli: 
            speed = algorithm_gui_update(screen, r, points, f"Searching... Current length: {round(l, 1)}. [RIGHT]/[LEFT] to change speed", font, speed)

    return optimal_road, min_len

def neighbours(points, speed = 0, font = 0, screen = 0, cli = False):
    # Logic
    road = [points.P[0]]
    last_point = False 
    while 1:
        last_point = True
        min_len = float("inf")
        p_next = road[-1]
        for p in points.P:
            if not p in road:
                l = Points.metric(road[-1], p)
                if l < min_len:
                    p_next = p
                    min_len = l
                last_point = False
        if last_point:
            break
        road.append(p_next)

        # for GUI
        if not cli:
            speed = algorithm_gui_update(screen, road, points, "Searching route. [RIGHT]/[LEFT] to change speed", font, speed)

    # Logic
    road.append(points.P[0])

    l = sum(list(Points.metric(road[i], road[i + 1]) for i in range(len(road) - 1)))

    return road, l
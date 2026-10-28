from searching_framework import Problem, astar_search


class Robot(Problem):
    def __init__(self, initial, goal, walls, stations, B):
        super().__init__(initial, goal)
        self.walls = set(walls)
        self.stations = set(stations)
        self.B = B
        self.n = 10

    def valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and (x, y) not in self.walls

    def successor(self, state):
        x, y, battery = state
        successors = {}

        moves = {
            "Up": (0, 1),
            "Down": (0, -1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }

        if battery == 0:
            return successors

        for action, (dx, dy) in moves.items():
            nx, ny = x + dx, y + dy

            if self.valid(nx, ny):
                new_battery = battery - 1

                if (nx, ny) in self.stations:
                    new_battery = self.B

                successors[action] = (nx, ny, new_battery)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        x, y, _ = state
        return (x, y) == self.goal

    def h(self, node):
        x, y, _ = node.state
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)


if __name__ == '__main__':
    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5),
             (1, 6), (1, 7), (0, 6), (0, 8), (0, 9),
             (1, 9), (2, 9), (3, 9)]

    start = tuple(map(int, input().split(",")))
    goal = tuple(map(int, input().split(",")))
    B = int(input())
    n = int(input())

    stations = []
    for _ in range(n):
        stations.append(tuple(map(int, input().split(","))))

    initial_state = (start[0], start[1], B)

    problem = Robot(initial_state, goal, walls, stations, B)
    result = astar_search(problem)

    if result is None:
        print("No Solution!")
    else:
        print(result.solution())
        
        
#here:
# from searching_framework import Problem, astar_search


# class Robot(Problem):
#     def __init__(self, initial, goal, walls, stations, zones, B):
#         super().__init__(initial, goal)
#         self.walls = set(walls)
#         self.stations = set(stations)
#         self.zones = zones
#         self.B = B
#         self.n = 10

#     def in_bounds(self, x, y):
#         return 0 <= x < self.n and 0 <= y < self.n

#     def is_wall(self, x, y, used_zone):
#         if (x, y) in self.walls:
#             return True
#         if used_zone:
#             for r, x1, x2 in self.zones:
#                 if y == r and x1 <= x <= x2:
#                     return True
#         return False

#     def in_zone(self, x, y):
#         for r, x1, x2 in self.zones:
#             if y == r and x1 <= x <= x2:
#                 return (r, x1, x2)
#         return None

#     def slide_zone(self, x, y, zone):
#         r, x1, x2 = zone
#         nx = x2 + 1
#         ny = r
#         return nx, ny

#     def successor(self, state):
#         x, y, battery, used_zone = state
#         succ = {}

#         if battery == 0:
#             return succ

#         moves = {
#             "Up": (0, 1),
#             "Down": (0, -1),
#             "Left": (-1, 0),
#             "Right": (1, 0)
#         }

#         for action, (dx, dy) in moves.items():
#             nx, ny = x + dx, y + dy

#             if not self.in_bounds(nx, ny):
#                 continue

#             if self.is_wall(nx, ny, used_zone):
#                 continue

#             zone = self.in_zone(nx, ny)

#             new_battery = battery - 1
#             new_used = used_zone

#             if zone:
#                 fx, fy = self.slide_zone(nx, ny, zone)

#                 if not self.in_bounds(fx, fy):
#                     continue

#                 if self.is_wall(fx, fy, True):
#                     continue

#                 nx, ny = fx, fy
#                 new_used = True

#             if (nx, ny) in self.stations:
#                 new_battery = self.B

#             succ[action] = (nx, ny, new_battery, new_used)

#         if x == self.n - 1:
#             nx, ny = 0, y
#             if not self.is_wall(nx, ny, used_zone):
#                 new_battery = battery - 1
#                 if new_battery >= 0:
#                     if (nx, ny) in self.stations:
#                         new_battery = self.B
#                     succ["Teleportiraj"] = (nx, ny, new_battery, used_zone)

#         return succ

#     def actions(self, state):
#         return self.successor(state).keys()

#     def result(self, state, action):
#         return self.successor(state)[action]

#     def goal_test(self, state):
#         x, y, _, _ = state
#         return (x, y) == self.goal

#     def h(self, node):
#         x, y, _, _ = node.state
#         gx, gy = self.goal
#         return abs(x - gx) + abs(y - gy)


# if __name__ == '__main__':
#     walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5),
#              (1, 6), (1, 7), (0, 6), (0, 8), (0, 9),
#              (1, 9), (2, 9), (3, 9)]

#     start = tuple(map(int, input().split(",")))
#     goal = tuple(map(int, input().split(",")))
#     B = int(input())
#     n = int(input())

#     stations = []
#     for _ in range(n):
#         stations.append(tuple(map(int, input().split(","))))

#     d = int(input())
#     zones = []
#     for _ in range(d):
#         r, x1, x2 = map(int, input().split(","))
#         zones.append((r, x1, x2))

#     initial = (start[0], start[1], B, False)

#     problem = Robot(initial, goal, walls, stations, zones, B)
#     result = astar_search(problem)

#     if result is None:
#         print("No Solution!")
#     else:
#         print(result.solution())
        
        
        
        
        
        

from searching_framework import Problem, breadth_first_graph_search

goal_positions = {(7, 2), (7, 3)}

opponents = [(3, 3), (5, 4)]


def is_valid_ball(bx, by):
    if not (0 <= bx <= 7 and 0 <= by <= 5):
        return False
    if (bx, by) in opponents:
        return False
    for ox, oy in opponents:
        if abs(bx - ox) <= 1 and abs(by - oy) <= 1:
            return False
    return True


def is_valid_man(mx, my, bx, by):
    if not (0 <= mx <= 7 and 0 <= my <= 5):
        return False
    if (mx, my) == (bx, by):
        return False
    if (mx, my) in opponents:
        return False
    return True


class Football(Problem):
    def __init__(self, initial):
        super().__init__(initial)

    def successor(self, state):
        mx, my, bx, by = state
        dirs = {
            'up': (0, 1),
            'down': (0, -1),
            'right': (1, 0),
            'up-right': (1, 1),
            'down-right': (1, -1)
        }

        succ = {}

        for name, (dx, dy) in dirs.items():
            nmx, nmy = mx + dx, my + dy

            if (nmx, nmy) == (bx, by):
                nbx, nby = bx + dx, by + dy
                if is_valid_ball(nbx, nby) and is_valid_man(nmx, nmy, nbx, nby):
                    succ[f"Push ball {name}"] = (nmx, nmy, nbx, nby)
            else:
                if is_valid_man(nmx, nmy, bx, by):
                    succ[f"Move man {name}"] = (nmx, nmy, bx, by)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return (state[2], state[3]) in goal_positions


if __name__ == '__main__':
    man = tuple(map(int, input().split(',')))
    ball = tuple(map(int, input().split(',')))

    problem = Football((man[0], man[1], ball[0], ball[1]))

    result = breadth_first_graph_search(problem)

    if result is None:
        print("No Solution!")
    else:
        print(result.solution())

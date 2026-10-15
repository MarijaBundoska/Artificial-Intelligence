from constraint import Problem, BacktrackingSolver


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}

    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}

    return families, rooms


if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()
    room_ids = list(rooms.keys())

    for fam in families:
        problem.addVariable(fam, room_ids + [None])

    def different_rooms(*args):
        used = [r for r in args if r is not None]
        return len(used) == len(set(used))

    problem.addConstraint(different_rooms, list(families.keys()))

    def valid_assignment(fam, room):
        if room is None:
            return True
        if families[fam]['size'] > rooms[room]['capacity']:
            return False
        for req in families[fam]['requirements']:
            if req not in rooms[room]['amenities']:
                return False
        return True

    for fam in families:
        problem.addConstraint(lambda room, f=fam: valid_assignment(f, room), (fam,))

    def no_unfair_rejection(*args):
        assigned_rooms = set([r for r in args if r is not None])

        for i, fam in enumerate(families):
            if args[i] is None:
                for r in rooms:
                    if r not in assigned_rooms:
                        if (families[fam]['size'] <= rooms[r]['capacity'] and
                            all(req in rooms[r]['amenities'] for req in families[fam]['requirements'])):
                            return False
        return True

    problem.addConstraint(no_unfair_rejection, list(families.keys()))

    solutions = problem.getSolutions()

    best_solution = None
    best_sum = -1

    for sol in solutions:
        total = 0
        for fam, room in sol.items():
            if room is not None:
                total += families[fam]['size']
        if total > best_sum:
            best_sum = total
            best_solution = sol

    print("Best assignment:")

    if best_solution is not None:
        for fam, room in best_solution.items():
            if room is not None:
                print(f"{fam}->{room}")

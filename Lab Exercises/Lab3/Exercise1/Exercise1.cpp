from constraint import Problem, BacktrackingSolver, MaxSumConstraint, ExactSumConstraint

def not_both_one(a, b):
    return not (a == 1 and b == 1)

if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))

    problem = Problem(solver=BacktrackingSolver())

    variables = []
    for i in range(K):
        for j in range(K):
            problem.addVariable((i, j), [0, 1])
            variables.append((i, j))

    problem.addConstraint(ExactSumConstraint(N), variables)

    regions = {}
    for i in range(K):
        for j in range(K):
            r = grid[i][j]
            if r not in regions:
                regions[r] = []
            regions[r].append((i, j))

    for r in regions:
        problem.addConstraint(MaxSumConstraint(2), regions[r])

    for i in range(K):
        for j1 in range(K):
            for j2 in range(j1 + 1, K):
                if grid[i][j1] != grid[i][j2]:
                    problem.addConstraint(not_both_one, [(i, j1), (i, j2)])

    for j in range(K):
        for i1 in range(K):
            for i2 in range(i1 + 1, K):
                if grid[i1][j] != grid[i2][j]:
                    problem.addConstraint(not_both_one, [(i1, j), (i2, j)])

    for i in range(K):
        for j in range(K):
            if i + 1 < K and grid[i][j] == grid[i + 1][j]:
                problem.addConstraint(not_both_one, [(i, j), (i + 1, j)])
            if j + 1 < K and grid[i][j] == grid[i][j + 1]:
                problem.addConstraint(not_both_one, [(i, j), (i, j + 1)])

    result = problem.getSolution()

    if result is None:
        print("No Solution!")
    else:
        for i in range(K):
            row = []
            for j in range(K):
                if result[(i, j)] == 1:
                    row.append('*')
                else:
                    row.append(str(grid[i][j]))
            print(' '.join(row))

if __name__ == "__main__":
    # Your code here.
    pass
def mines(field):
    n = len(field)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            if field[i][j] == '#':
                row.append('#')
            else:
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < n and y >= 0 and y < n:
                            if field[x][y] == '#':
                                count += 1
                row.append(str(count))
        result.append(row)

    return result


n = int(input())
field = []

for _ in range(n):
    row = input().split()
    field.append(row)

res = mines(field)

for r in res:
    print("   ".join(r))

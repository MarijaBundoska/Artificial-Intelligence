data = {}

while True:
    line = input()
    if line == "end":
        break

    city, temp, rain = line.split()
    temp = float(temp)

    if city not in data:
        data[city] = [0, 0, 0]

    data[city][0] += temp
    data[city][1] += 1

    if rain == "yes":
        data[city][2] += 1

res = []

for city in data:
    s = data[city][0]
    c = data[city][1]
    r = data[city][2]
    avg = s / c
    res.append((city, avg, r))

res.sort(key=lambda x: (-x[2], x[0]))

for city, avg, r in res:
    avg = f"{avg:.2f}"
    if avg[-1] == "0":
        avg = avg[:-1]
    print(city, avg, r)

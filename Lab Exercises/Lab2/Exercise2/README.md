
# Exercise 2 - Robot Navigation with Battery and Charging Stations

## Problem Description

A **10×10 grid** contains a robot, a goal cell, and several charging stations. Some cells are blocked (marked in gray), and the robot cannot move onto those cells.

The objective is to find the shortest sequence of actions that allows the robot to reach the goal cell.

Charging stations are marked in green, while the goal cell is marked in red.

## Movement Rules

The robot can move in four directions: **Up, Down, Left, and Right**.

Each movement action moves the robot one cell in the specified direction, provided that the destination cell is within the grid boundaries and is not blocked.

The movement directions are defined by the following dictionary:

```python
dir = {
    "Up": (0, +1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (+1, 0)
}
```

## Battery Mechanism

The robot has a battery with a maximum capacity of `B`.

- Each movement action consumes **1 unit of battery**.
- A state in which the battery level is `0` is not allowed.
- When the robot enters a charging station, the battery is automatically recharged to its maximum capacity `B`.

## Search Algorithm

The task requires the use of an **informed search algorithm** to find the shortest path from the initial position to the goal cell while respecting the battery constraints and avoiding blocked cells.

## Input Format

The grid dimensions and the positions of blocked cells are fixed for all test cases.

The input consists of the following values, in order:

1. Initial position of the robot: `x,y`
2. Goal position: `g_x,g_y`
3. Battery capacity: `B`
4. Number of charging stations: `n`
5. Coordinates of each charging station: `x_i,y_i`, one per line

### Input Structure

```text
x,y
g_x,g_y
B
n
x1,y1
x2,y2
...
xn,yn
```

<img width="449" height="410" alt="image" src="https://github.com/user-attachments/assets/91a7f88c-4f19-4b26-b4d6-f9f822673893" />


# Задача 2 - Робот со батерија и станици за полнење

## Опис на проблемот

Дадена е **мрежа со димензии 10×10** во која се наоѓаат робот, целна ќелија и неколку станици за полнење. Некои ќелии се блокирани (означени со сива боја), па роботот не смее да влегува во нив.

Целта е да се пронајде најкратката низа од акции со која роботот ќе стигне до целната ќелија.

Станиците за полнење се означени со зелена боја, додека целната ќелија е означена со црвена боја.

## Правила за движење

Роботот може да се движи во четири насоки: **Горе, Долу, Лево и Десно**.

Секоја акција го поместува роботот за една ќелија во соодветната насока, доколку целната ќелија се наоѓа во границите на мрежата и не е блокирана.

Насоките на движење се дефинирани со следниот речник:

```python
dir = {
    "Up": (0, +1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (+1, 0)
}
```

## Механизам на батеријата

Роботот има батерија со максимален капацитет `B`.

- Секоја акција за движење троши **1 единица батерија**.
- Не е дозволена состојба во која нивото на батеријата е `0`.
- Кога роботот ќе влезе во станица за полнење, батеријата автоматски се полни до максималниот капацитет `B`.

## Алгоритам за пребарување

Потребно е да се примени **алгоритам за информирано пребарување** за да се пронајде најкраткиот пат од почетната позиција до целната ќелија, притоа почитувајќи ги ограничувањата на батеријата и избегнувајќи ги блокираните ќелии.

## Формат на влезот

Димензиите на мрежата и позициите на блокираните ќелии се исти за сите тест-примери.

Влезот ги содржи следните вредности, по наведениот редослед:

1. Почетна позиција на роботот: `x,y`
2. Позиција на целта: `g_x,g_y`
3. Капацитет на батеријата: `B`
4. Број на станици за полнење: `n`
5. Координати на секоја станица за полнење: `x_i,y_i`, секоја во посебен ред

### Структура на влезот

```text
x,y
g_x,g_y
B
n
x1,y1
x2,y2
...
xn,yn
```

<img width="449" height="410" alt="image" src="https://github.com/user-attachments/assets/17ddbb6d-d2b4-40f1-a468-516c5313163c" />





## Test Cases


### Test Case 1

**Test:**
```text
ts1
```

**Input:**
```text
	
0,0
6,0
3
1
3,0
```
**Expected output:**

```text
No Solution!
```






### Test Case 2


**Test:**
```text
ts2
```

**Input:**
```text
2,1
8,2
7
2
4,2
6,2
```
**Expected output:**

```text
['Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Right']
```






### Test Case 3

**Test:**
```text
ts3
```

**Input:**
```text
6,6
9,9
5
1
8,8
```
**Expected output:**

```text
['Up', 'Up', 'Right', 'Right', 'Up', 'Right']
```





**Test:**
```text
ts4
```

**Input:**
```text
0,1
9,9
3
2
2,2
5,5
```
**Expected output:**

```text
 Solution!
```






### Test Case 

**Test:**
```text
ts5
```

**Input:**
```text
3,0
9,0
6
2
6,0
8,1
```
**Expected output:**

```text
['Up', 'Right', 'Right', 'Right', 'Down', 'Right', 'Right', 'Right']
```

**Test:**
```text
2,3
7,8
8
2
4,4
6,6
```






### Test Case 

**Test:**
```tex
```

**Input:**
```text
2,3
7,8
8
2
4,4
6,6
```
**Expected output:**

['Up', 'Right', 'Right', 'Up', 'Up', 'Up', 'Up', 'Right', 'Right', 'Right']
```text
```

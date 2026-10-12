
## Exercise 3 – Robot Cleaning Simulation

### Problem Statement

In this problem, you will simulate two robots that clean tiles in a grid.

Create a class `Robot` that stores the current position of the robot, as well as the direction in which the robot is moving. The allowed directions are `up`, `right`, `down`, and `left`.

The class `Robot` should have the following methods:

- `move(grid)` – Moves the robot in its current direction. The robot continues to move in the same direction until it encounters a wall or leaves the boundaries of the grid. Therefore, a single move may traverse multiple tiles. During the movement, the robot cleans all tiles through which it moves. The robots do not collide with each other.

- `turn()` – Changes the direction of movement by 90 degrees clockwise. The directions change in the following order: `up → right → down → left → up`. This function should be called after each move the robot makes. First, the robot moves, and when it stops moving, it rotates.

Then, create a class `Game` that stores the grid (matrix) and two `Robot` objects.

The grid is predefined in the program and looks as follows:

```text
#..#..
.#....
#.....
.#....
...#..
```

In the grid, `.` represents a dirty tile, while `#` represents a wall.

The starting positions and directions of the two robots are read from standard input. The starting positions of the robots are always clean.

In the `Game` class, simulate 15 movements. During each movement, both robots execute the `move()` method.

After the simulation finishes, print the total number of cleaned tiles in the grid.

## Задача 3 – Симулaција на чистење со роботи

### Опис на задачата

Во оваа задача ќе симулирате два роботи кои чистат плочки во мрежа (grid).

Креирајте класа `Robot` која ја чува тековната позиција на роботот, како и насоката во која се движи. Дозволени насоки се `up`, `right`, `down` и `left` (горе, десно, долу и лево).

Класата `Robot` треба да ги има следните методи:

- `move(grid)` – Го движи роботот во моменталната насока. Роботот продолжува да се движи во истата насока сè додека не наиде на ѕид или не излезе од границите на мрежата. Тоа значи дека во еден потег може да помине низ повеќе плочки. При движењето, роботот ги чисти сите плочки низ кои се движи. Роботите не се судираат меѓу себе.

- `turn()` – Ја менува насоката на движење за 90 степени во насока на стрелките на часовникот. Насоките се менуваат по следниот редослед: `up → right → down → left → up`. Овој метод треба да се повика по секој потег на роботот. Роботот прво се движи, а кога ќе заврши со движењето, ја менува насоката.

Потоа, креирајте класа `Game` која ја чува мрежата (матрицата) и два објекти од класата `Robot`.

Мрежата е однапред дефинирана во програмата и изгледа вака:

```text
#..#..
.#....
#.....
.#....
...#..
````


## Test Cases


### Test Case 1

**Input:**
```text
0 1 right
2 3 up
```
**Expected output:**

```text
21
```




### Test Case 2

**Input:**
```text
1 0 down
3 0 down
```
**Expected output:**

```text
3
```





### Test Case 3

**Input:**
```text
2 1 left
2 2 right
```
**Expected output:**

```text
13
```





### Test Case 4

**Input:**
```text
1 3 left
1 2 down
```
**Expected output:**

```text
9
```


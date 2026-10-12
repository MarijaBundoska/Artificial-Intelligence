## Exercise 1 – Robot Repairing Machines

### Problem Statement

A 10×10 grid is given. On the grid, there is a robot, two machines `М1` and `М2`, and parts needed to repair each of the machines.

The robot must collect the parts required to repair each machine and then repair both machines. Some tiles on the grid are blocked by walls (gray-colored tiles), and the robot cannot step onto those tiles.

The goal is reached when both machines have been repaired. An example of the initial state is shown in the image below.

### Robot Actions and Rules

The robot can perform one of the following actions:

- `Up` – Move up.
- `Down` – Move down.
- `Left` – Move left.
- `Right` – Move right.
- `Repair` – Repair a machine.

Machine `М1` must be repaired first, followed by machine `М2`. The robot is not allowed to collect parts for `М2` before `М1` has been repaired.

The robot may stand on the same tile as a machine even if it has not collected all the required parts. However, it cannot repair the machine until all its required parts have been collected.

The robot is also allowed to step onto a tile containing a part for `М2` before `М1` has been repaired, but the part will not be collected in that case.

### Machine Repair Rules

Repairing a machine requires a specific number of consecutive steps.

- Machine `М1` requires `s1` consecutive `Repair` actions.
- Machine `М2` requires `s2` consecutive `Repair` actions.

The robot must first move to the machine's tile and then begin repairing it in the following step.

If the robot starts repairing a machine by performing the `Repair` action but moves to another tile before completing the repair, the repair process must be started over.

### Movement Directions

The movement directions can be defined using the following dictionary:

```python
dir = {
    "Up": (0, +1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (+1, 0)
}

```
### Input Format

For all test cases, the grid dimensions and wall positions are the same.

The input contains the robot's starting position `(x, y)`, followed by the position of machine **M1** `(m1_x, m1_y)` and the number of steps `s1` required to repair **M1**.

The next lines contain the same information for machine **M2**: its position `(m2_x, m2_y)` and the number of steps `s2` required to repair it.

Then, the number of parts for **M1** is given, followed by their positions. Finally, the number of parts for **M2** is given, followed by their positions.

Reading and initializing all input parameters, including wall positions, is handled by the starter code.

The input format is as follows:

```text
x,y m1_x,m1_y
s1
m2_x,m2_y
s2
m1
x11,y11
x12,y12
...
x_m1,y_m1
m2
x21,y21
x22,y22
...
x_m2,y_m2
```


## Задача 1 – Робот за поправање машини

### Опис на задачата

Дадена е табла со димензии 10×10. На таблата има робот, две машини `М1` и `М2`, како и делови потребни за поправање на секоја од машините.

Роботот треба да ги собере потребните делови за секоја машина, а потоа да ги поправи двете машини. Дел од полињата на таблата се блокирани со ѕидови (полиња означени со сива боја), на кои роботот не може да стапне.

Целта е постигната кога двете машини ќе бидат поправени. На сликата подолу е прикажан пример за почетна состојба.

### Дозволени акции и правила за движење

Роботот може да изврши една од следните акции:

- `Up` – Движење нагоре.
- `Down` – Движење надолу.
- `Left` – Движење налево.
- `Right` – Движење надесно.
- `Repair` – Поправање машина.

Машината `М1` мора да биде поправена прва, а потоа машината `М2`. Не е дозволено да се собираат делови за машината `М2` пред да биде поправена машината `М1`.

Дозволено е роботот да се наоѓа на истото поле со некоја од машините дури и ако сè уште ги нема собрано сите потребни делови. Сепак, не може да започне со поправка на машината пред да ги собере сите делови потребни за нејзино поправање.

Исто така, роботот може да стапне на поле на кое се наоѓа дел за машината `М2` пред да биде поправена машината `М1`, но во тој случај делот нема да биде собран.

### Правила за поправање на машините

За поправање на секоја машина е потребен одреден број последователни чекори.

- За поправање на машината `М1` потребни се `s1` последователни акции `Repair`.
- За поправање на машината `М2` потребни се `s2` последователни акции `Repair`.

Роботот мора прво да стигне до полето на кое се наоѓа машината, а потоа, во следниот чекор, да започне со поправката.

Ако роботот започне со поправка со извршување на акцијата `Repair`, но потоа се премести на друго поле пред да ја заврши поправката, процесот на поправање мора да започне од почеток.

### Насоки за движење

Насоките на движење може да се дефинираат со следниот речник во Python:

```python
dir = {
    "Up": (0, +1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (+1, 0)
}
```


За сите тест примери, големината на таблата и позицијата на ѕидовите е иста. На влез се дадени почетната позиција на робот x,y, па потоа позицијата на машината М1 со m1_x,m1_y, па бројот на чекори потребен да се поправи М1 со s1. Потоа се дадени истите информации за М2: позиција со m2_x,m2_y и број на чекори s2 потребен за да се поправи М2. Потоа е даден бројот на делови за М1 и нивните позиции, па бројот на делови за М2 и нивните позиции.

Вчитувањето на сите влезни параметри, како и позициите на ѕидовите се дадени во рамки на почетниот код.

Форматот на влезот е следниот:

```text
x,y
m1_x,m1_y
s1
m2_x,m2_y
s2
m1
x11,y11
x12,y12
...
x_m1,y_m1 
m2
x21,y21
x22,y22
...
x_m2,y_m2 
```



## Test Cases


### Test Case 1

**Test:**
```text
example
```
**Input:**
```text
0,0
3,7
2
8,3
3
2
3,5
7,7
2
5,2
6,2
```
**Expected output:**
```text
['Right', 'Right', 'Right', 'Up', 'Up', 'Up', 'Up', 'Up', 'Right', 'Right', 'Right', 'Up', 'Right', 'Up', 'Left', 'Left', 'Left', 'Left', 'Repair', 'Repair', 'Down', 'Down', 'Down', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Repair', 'Repair', 'Repair']
```


### Test Case 2

**Test:**
```text
no solution
```
**Input:**
```text
1,4
0,3
5
9,9
2
2
0,7
1,8
1
0,0
```
**Expected output:**
```text
No Solution!
```

## Task 4 – Robot Repairing Machines

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

```text
The input format is as follows:

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



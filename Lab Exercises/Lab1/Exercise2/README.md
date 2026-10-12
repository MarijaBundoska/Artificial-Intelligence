## Exercise 2 – Pushing a Ball to the Goal

### Problem Statement

An **8×6 board** is given, on which a man and a ball are placed. The man needs to push the ball to the goal marked in gray. There are also opponents on the board, marked in blue. The opponents are static and do not move.

The man can move one position in five directions:

- `Up`
- `Down`
- `Right`
- `Up-Right`
- `Down-Right`

When moving, if the ball is directly in front of the man, he can push the ball in the direction in which he is moving.

The man cannot occupy the same field as the ball or any of the opponents. The ball cannot occupy a field that is adjacent to any opponent (horizontally, vertically, or diagonally), nor can it occupy the same field as an opponent.

### Input and Board Configuration

For all test cases, the board dimensions remain the same. The positions of the man and the ball change and are read from standard input.

The positions of the opponents and the goal remain the same for all test cases.

### Task Requirements

Your task is to implement the movement of the man, and consequently the pushing of the ball, in the successor function.

The actions should be named as follows:

- `Move man up`
- `Move man down`
- `Move man right`
- `Move man up-right`
- `Move man down-right`
- `Push ball up`
- `Push ball down`
- `Push ball right`
- `Push ball up-right`
- `Push ball down-right`

If the man moves without pushing the ball, the action should be named `Move man [direction]`. If the man pushes the ball while moving, the action should be named `Push ball [direction]`.

Additionally, you need to implement the following functions:

- `goal_test()` – Checks whether the ball has reached the goal.
- `check_valid()` – Checks whether a given state is valid according to the movement rules and restrictions.

Use **uninformed search** to find a solution with the fewest possible steps. 


## Задача 2 – Туркање топка до голот

### Опис на задачата

Дадена е **табла со димензии 8×6**, на која се поставени човече и топка. Потребно е човечето, со туркање на топката, да ја доведе до голот, кој е обележан со сива боја.

На таблата дополнително има **противници**, обележани со сина боја. Противниците се статични и не се движат.

Човечето може да се движи за една позиција во пет насоки:

- `up` – нагоре
- `down` – надолу
- `right` – надесно
- `up-right` – дијагонално нагоре-надесно
- `down-right` – дијагонално надолу-надесно

При движењето, доколку топката се наоѓа непосредно пред човечето, човечето може да ја турне топката во насоката во која се движи.

Човечето не може да се наоѓа на истото поле со топката или со некој од противниците.

Топката не може да се наоѓа на поле кое е соседно со некој од противниците (хоризонтално, вертикално или дијагонално), ниту на истото поле со некој од противниците.

На слика 1 е прикажана една можна почетна состојба на таблата.

### Влезни податоци и поставеност на таблата

За сите тест-примери, големината на таблата е иста, додека позициите на човечето и топката се менуваат и се читаат од стандарден влез.

Позициите на противниците и голот се исти за сите тест-примери.

### Барања на задачата

Ваша задача е да го имплементирате поместувањето на човечето, а со тоа и туркањето на топката, во функцијата `successor`.

Акциите се именуваат на следниот начин:

- `Move man up`
- `Move man down`
- `Move man right`
- `Move man up-right`
- `Move man down-right`

Овие акции се користат кога се поместува само човечето, без да ја турне топката.

Доколку при поместувањето на човечето се турка и топката, акциите се именуваат на следниот начин:

- `Push ball up`
- `Push ball down`
- `Push ball right`
- `Push ball up-right`
- `Push ball down-right`

Дополнително, потребно е да ги имплементирате следните функции:

- `goal_test()` – Проверува дали топката стигнала до голот, односно дали е постигната целта.
- `check_valid()` – Проверува дали дадената состојба е валидна според правилата и ограничувањата на задачата.

Треба да примените **неинформирано пребарување (uninformed search)** за да пронајдете решение со најмал можен број чекори.


## Test Cases


### Test Case 1

**Test:**
```text
TC1
```
**Input:**
```text
0,1
1,2
```
**Expected output:**

```text
Testing methods. Good!
```



### Test Case 2

**Test:**
```text
example
```
**Input:**
```text
0,1
1,2
```
**Expected output:**

```text
['Move man up', 'Move man up', 'Push ball down-right', 'Move man down', 'Push ball right', 'Push ball right', 'Push ball right', 'Move man down', 'Push ball up-right', 'Push ball up-right']
```




### Test Case 3

**Test:**
```text
one step
```
**Input:**
```text
5,1
6,2
```
**Expected output:**

```text
['Push ball up-right']
```




### Test Case 4

**Test:**
```text
goal
```
**Input:**
```text
0,0
7,2
```
**Expected output:**

```text
[]
```





### Test Case 5

**Test:**
```text
test case 5
```
**Input:**
```text
0,5
7,1
```
**Expected output:**

```text
['Move man right', 'Move man right', 'Move man down-right', 'Move man down-right', 'Move man down-right', 'Move man down-right', 'Move man down-right', 'Push ball up']
```





### Test Case 6

**Test:**
```text
test case 6
```
**Input:**
```text
2,4
3,1
```
**Expected output:**

```text
['Move man down', 'Move man down', 'Move man down', 'Push ball right', 'Push ball right', 'Move man down', 'Push ball up-right', 'Push ball up-right']
```





### Test Case 7

**Test:**
```text
no solution
```
**Input:**
```text
0,1
0,2
```
**Expected output:**

```text
No Solution!
```

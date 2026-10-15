# Exercise 1 - Star Struck

## Task

A board of size `N x N` is given, where each cell of the board belongs to a unique colored region. The regions are labeled with numbers from `1` to `N` (the total number of regions), and multiple cells may belong to the same region.

### Example

A board of size `8 x 8`, where `N = 8`.

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/61d89139-2e81-4418-ab8c-89eb83891b46" />

Your task is to place `N` stars on the board, where each star is placed in a single cell of the board, such that:

1. `N` is the number of regions.
2. Each region contains at most 2 stars.
3. Stars that belong to **different regions** must not be placed in the same row or the same column.
4. Stars that belong to **the same region** must not be orthogonally adjacent (i.e. two stars must not be directly left, right, above, or below each other). It is allowed for these stars to be placed diagonally within the same region.
5. It is allowed for regions to contain no stars.

### Example

A valid filling of the board with stars.

<img width="253" height="252" alt="image" src="https://github.com/user-attachments/assets/01155eba-34fe-4571-a09f-d32e27b3c8c4" />


## Input

In the first line of the input, you are given an integer `N` — the size of the `N x N` board.

Then the board of size `N x N` is given, where each of the next `N` rows contains `N` numbers representing the region to which each cell belongs.

## Output

Print one valid filling of the board with the same structure, where the symbol `*` is printed instead of a number at positions where a star is placed.

If multiple valid solutions exist, it is sufficient to print any one of them.

## Implementation Requirements

Starter code is provided which creates a class for representing the problem. Then a solution is searched using `BacktrackingSolver`.

Your task is to add the variables and their domains, as well as to add the constraints (conditions) of the problem.

**Reminder:** In the given constraint module, the following constraints are already implemented as classes:

- `AllDifferentConstraint`
- `AllEqualConstraint`
- `MaxSumConstraint`
- `ExactSumConstraint`
- `MinSumConstraint`
- `InSetConstraint`
- `NotInSetConstraint`
- `SomeInSetConstraint`
- `SomeNotInSetConstraint`


# Задача 1 - Star Struck

## Опис на задачата

Дадена е табла со големина `N x N`, каде секоја ќелија на таблата припаѓа на единствен обоен регион. Регионите се означени со цифри од `1` до `N` (вкупниот број на региони), и повеќе ќелии може да припаѓаат на ист регион.

Пример. Табла со големина `8 x 8`, т.е. `К = 8`.

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/61d89139-2e81-4418-ab8c-89eb83891b46" />



Вашата задача е да поставите `N` ѕвезди на таблата, каде секоја ѕвезда се поставува во една ќелија од таблата, така што:

1. `N` е бројот на региони.
2. Секој регион содржи најмногу 2 ѕвезди.
3. Ѕвезди кои припаѓаат на **различни региони** не смеат да бидат поставени во иста редица или иста колона.
4. Ѕвезди кои припаѓаат на **ист регион** не смеат да бидат ортогонално соседни (т.е. не смеат две ѕвезди да бидат директно лево, десно, горе или долу меѓу себе). Дозволено е овие ѕвезди да бидат дијагонално поставени во истиот регион.
5. Дозволено е регионите да не содржат ѕвезди.

Пример. Валидно пополнување на таблата со ѕвезди.

<img width="253" height="252" alt="image" src="https://github.com/user-attachments/assets/2fd01378-bea0-4470-ad35-ab4f3ee5bf9a" />


## Влез

Во првиот ред од влезот се добива цел број `N` — големината на таблата. Потоа е зададена таблата со големина `N x N`, каде во секој од следните `N` редови се дадени `N` броеви кои ја означуваат припадноста на одредена ќелија на даден регион.

## Излез

Да се испечати едно валидно пополнување на таблата со иста структура, каде наместо број се печати симболот `*` на позициите каде што има ѕвезда. Доколку постојат повеќе валидни решенија, доволно е да се испечати кое било од нив.

## Имплементација

Даден е почетен код со кој е креирана класа за претставување на проблемот. Потоа се повикува наоѓање решение со `BacktrackingSolver`.

Ваша задача е да ги додадете променливите и нивните домени, како и да ги додадете ограничувањата (условите) на проблемот.

## Достапни ограничувања

Во дадениот модул `constraint` веќе се имплементирани следните ограничувања како класи:

- `AllDifferentConstraint`
- `AllEqualConstraint`
- `MaxSumConstraint`
- `ExactSumConstraint`
- `MinSumConstraint`
- `InSetConstraint`
- `NotInSetConstraint`
- `SomeInSetConstraint`
- `SomeNotInSetConstraint`

## Test Cases


### Test Case 1

**Input:**
```text
2
1 1
1 2
```
**Expected output:**

```text
* 1
1 *
```



### Test Case 2

**Input:**
```text
1
1
```
**Expected output:**

```text
*
```



### Test Case 3

**Input:**
```text
3
1 1 1
2 2 2
3 3 3
```
**Expected output:**

```text
1 1 1
2 * 2
* 3 *
```




### Test Case 4

**Input:**
```text
3
1 1 2
1 1 2
3 3 4
```
**Expected output:**

```text
No Solution!
```





### Test Case 5

**Input:**
```text
```
**Expected output:**

```text
```




### Test Case 6

**Input:**
```text
3
1 2 3
1 2 3
1 2 3
```
**Expected output:**

```text
1 2 *
1 * 3
1 2 *
```




### Test Case 7

**Input:**
```text
4
1 1 2 2
1 3 3 2
4 4 5 5
4 6 6 5
```
**Expected output:**

```text
No Solution!
```




### Test Case 8

**Input:**
```text
8
1 1 1 1 1 1 1 1
1 3 4 4 1 1 5 5
1 3 6 4 1 1 5 7
1 3 6 4 1 7 7 7
1 3 6 4 6 7 8 8
1 3 6 6 6 7 8 2
1 9 9 6 7 7 9 2
1 2 9 9 7 7 9 2
```
**Expected output:**

```text
1 1 1 1 1 1 1 1
* 3 4 4 1 1 5 5
1 3 6 * 1 1 5 7
* 3 6 4 1 7 7 7
1 3 6 4 * 7 8 8
1 3 6 6 6 * 8 2
1 9 * 6 7 7 * 2
1 * 9 9 7 7 9 *
```




### Test Case 9

**Input:**
```text
6
1 1 2 2 3 3
2 2 3 3 4 4
3 3 4 4 5 5
4 4 5 5 6 6
1 2 3 4 5 6
6 5 4 3 2 1
```
**Expected output:**

```text
* 1 2 2 3 3
2 * 3 3 4 4
3 3 * 4 5 5
4 4 5 * 6 6
1 2 3 4 * 6
6 5 4 3 2 *
```





### Test Case 10

**Input:**
```text
6
1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
1 1 1 1 1 1
```
**Expected output:**

```text
1 * 3 4 5 6
2 3 * 5 6 1
3 4 5 6 1 2
* 5 6 1 2 3
5 6 1 2 * 4
1 1 1 * 1 *
```




### Test Case 11

**Input:**
```text
8
1 1 1 1 2 2 2 2
1 3 3 1 2 3 3 2
1 4 3 3 3 3 2 2
1 4 5 3 3 6 2 2
1 5 5 7 7 6 6 2
1 1 1 7 7 2 2 2
1 8 1 1 1 2 8 2
1 8 8 8 8 8 8 2
```
**Expected output:**

```text
* 1 * 1 2 2 2 2
1 3 3 1 2 3 3 2
1 4 3 3 3 3 2 2
1 4 5 3 * 6 2 2
1 5 5 7 7 * 6 2
1 1 1 7 7 2 2 *
1 * 1 1 1 2 * 2
1 8 8 8 8 8 8 *
```

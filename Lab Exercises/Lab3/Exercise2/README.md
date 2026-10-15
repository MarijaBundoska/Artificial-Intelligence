# Exercise 2 - Hotel Room Assignment

## Problem Description

A hotel needs to assign available rooms to guests who have made reservations. Each reservation contains the name of the guest who made it, the total number of people who will stay in the room, and certain amenities that the room must satisfy. Each room has a limited capacity and provides a set of amenities.

The assignment should be made such that each room can be assigned to at most one guest. Some rooms may remain empty. Each guest can be accommodated in **at most one room** or can be **rejected**.

Additionally, a guest can be assigned to a room only if the room has sufficient capacity for that guest and contains all required amenities of the guest.

A guest **must not be unjustifiably rejected**, i.e., it is not allowed for a guest to remain unassigned if there exists a free room in which the guest could be accommodated (all requirements are satisfied and the capacity is sufficient).

## Input

As input, you are given a list of guests and a list of rooms.

- For each guest, the following is given:
  - A name as a unique identifier.
  - The number of people that will stay in one room.
  - Required amenities (`wifi`, `parking`, `breakfast`).

- For each room, the following is given:
  - Room ID.
  - Capacity (maximum number of guests).
  - The amenities available in that room.

## Output

As output, you need to print the **best assignment** in the format given in the examples. Only rooms that are assigned to guests should be printed.

Among all valid assignments, you need to find the one that maximizes the total number of accommodated guests. If there are multiple such assignments, it is sufficient to print any one of them.

## Optional Requirement

The output should be sorted by room ID. This requirement is not checked.

## Implementation

An initial code is provided which defines a class for representing the problem. Then, a solution is obtained using `BacktrackingSolver`.

**Your task is to add the variables, their domains, and the constraints (conditions) of the problem.**

## Available Constraints

The following constraints are already implemented in the `constraint` module as classes:

- `AllDifferentConstraint`
- `AllEqualConstraint`
- `MaxSumConstraint`
- `ExactSumConstraint`
- `MinSumConstraint`
- `InSetConstraint`
- `NotInSetConstraint`
- `SomeInSetConstraint`
- `SomeNotInSetConstraint`

## Passing Additional Arguments to a Constraint Function

To pass additional arguments to a constraint function in the `constraint` module, you can use a lambda function:

```python
problem.addConstraint(
    lambda var1, var2, ei=extra_info: func_name(var1, var2, ei),
    (var1, var2)
)
```


# Задача 2 - Распределување на гости во хотелски соби

## Опис на задачата

Хотел треба да ги распредели достапните соби на гости кои имаат направено резервации. Секоја резервација го содржи името на гостинот кој ја направил резервацијата, вкупниот број на лица кои ќе престојуваат во собата и одредени погодности кои собата мора да ги задоволува. Секоја соба има ограничен капацитет и располага со одредени погодности.

Распределбата треба да се направи така што секоја соба може да биде доделена на најмногу еден гостин. Некои соби може да останат празни. Секој гостин може да биде сместен во **најмногу една соба** или да биде **одбиен**. Дополнително, гостин може да биде доделен во соба само ако собата има доволен капацитет за тој гостин и ако ги содржи сите барани погодности на гостинот.

Гостин **не смее да биде неоправдано одбиен**, односно не е дозволено да постои гостин кој не е сместен, а постои слободна соба во која тој гостин може да биде сместен (ги исполнува сите барања и капацитетот е доволен).

## Влез

На влез добивате листа на гости и листа на соби.

- За секој гостин се зададени:
  - Име како единствен идентификатор.
  - Број на лица кои ќе престојуваат во една соба.
  - Барани погодности (`wifi`, паркинг, доручек).

- За секоја соба се зададени:
  - Реден број на собата.
  - Капацитет (максимален број на гости).
  - Погодности кои ги поседува таа соба.

## Излез

На излез е потребно да се испечати **најдоброто распоредување** во форматот кој е даден во тест примерите. Се печатат само собите кои се пополнети со гости.

Од сите валидни распоредувања треба да се најде распоредување кое го максимизира вкупниот број на сместени лица. Доколку постојат повеќе такви распоредувања, доволно е да се испечати кое било од нив.

## Опционално барање

Излезот да биде сортиран според редниот број на собата. Ова барање не се проверува.

## Имплементација

Даден е почетен код со кој е креирана класа за претставување на проблемот. Потоа се повикува наоѓање на решение со `BacktrackingSolver`.

**Ваша задача е да ги додадете променливите, нивните домени, како и ограничувањата (условите) на проблемот.**

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

## Предавање дополнителни аргументи на функција за ограничување

За предавање дополнителни аргументи на функција за ограничување во модулот `constraint`, можете да користите `lambda` функција:

```python
problem.addConstraint(
    lambda var1, var2, ei=extra_info: func_name(var1, var2, ei),
    (var1, var2)
)
```



## Test Cases


### Test Case 1

**Input:**
```text	
2
Patty 4 wifi-breakfast
Ann 1 parking
2
114 4 parking-breakfast-wifi
115 2 parking-wifi-breakfast-balcony
```
**Expected output:**

```text
Best assignment:
Patty->114
Ann->115
```




### Test Case 2

**Input:**
```text
1
Patty 4 parking-breakfast
1
205 4 wifi-parking-breakfast-balcony
```
**Expected output:**

```text
Best assignment:
Patty->205
```




### Test Case 3

**Input:**
```text
4
Chris 4 breakfast-wifi
Patty 2 breakfast-wifi
Ann 3 breakfast-parking-wifi-balcony
Hazel 4 balcony-wifi-parking
4
113 4 parking-breakfast
114 3 balcony-breakfast-wifi
213 4 parking-wifi-balcony
214 3 balcony-breakfast-wifi
```
**Expected output:**

```text
Best assignment:
Hazel->213
Patty->214
```




### Test Case 4

**Input:**
```text
6
Olive 2 breakfast-wifi-balcony-parking
Patty 4 breakfast-parking
Hazel 1 wifi-balcony
Chris 1 balcony-wifi
Ann 3 wifi-breakfast-parking
Marsha 3 wifi-breakfast
6
212 1 wifi-balcony
213 2 balcony-wifi-parking-breakfast
214 4 wifi-parking
215 3 breakfast-wifi-parking-balcony
216 4 parking-breakfast-wifi-balcony
217 4 parking-wifi-balcony-breakfast
```
**Expected output:**

```text
Best assignment:
Hazel->212
Olive->213
Marsha->215
Ann->216
Patty->217
```





### Test Case 5

**Input:**
```text
10
Barb 2 breakfast-parking
Patty 3 balcony-wifi
Maureen 4 wifi-breakfast
Ann 3 parking-wifi-breakfast
Marsha 4 breakfast-wifi-parking-balcony
Chris 1 breakfast-wifi-parking
Aida 4 breakfast-wifi-parking-balcony
Hazel 2 breakfast-wifi
Olive 3 wifi-breakfast-parking-balcony
Teri 4 parking-wifi
6
211 3 balcony-wifi
212 3 wifi-breakfast
311 4 parking-wifi-breakfast
312 3 breakfast-balcony
313 4 parking-breakfast
314 4 wifi-breakfast
```
**Expected output:**

```text
Best assignment:
Patty->211
Hazel->212
Teri->311
Barb->313
Maureen->314
```





### Test Case 6

**Input:**
```text
3
Patty 4 wifi-parking
Ann 3 breakfast-wifi
Hazel 2 parking-wifi-breakfast
15
205 3 wifi-parking-balcony
206 3 breakfast-parking-wifi
207 3 breakfast-wifi-parking-balcony
305 2 breakfast-wifi-parking
405 3 breakfast-wifi
406 3 parking-wifi
505 4 wifi-parking
506 3 breakfast-wifi-balcony
507 3 wifi-breakfast-parking-balcony
508 1 wifi-parking-balcony-breakfast
605 4 breakfast-wifi-balcony-parking
606 2 parking-wifi-breakfast
705 4 breakfast-wifi
706 3 wifi-parking-breakfast-balcony
805 2 breakfast-balcony-wifi-parking
```
**Expected output:**

```text
Best assignment:
Patty->605
Ann->706
Hazel->805
```





### Test Case 7

**Input:**
```text
12
guest_E 4 wifi-balcony-parking
guest_B 3 breakfast-wifi-parking-balcony
guest_H 4 parking-wifi
guest_L 3 wifi-balcony
guest_J 4 breakfast-wifi-parking
guest_G 4 wifi-parking
guest_F 4 wifi-breakfast-parking
guest_D 4 wifi-breakfast
guest_C 4 breakfast-wifi
guest_K 3 parking-balcony-wifi-breakfast
guest_I 1 wifi-parking
guest_A 4 wifi-balcony-parking-breakfast
4
104 3 wifi-parking-breakfast
105 4 wifi-balcony
106 2 balcony-breakfast-wifi-parking
107 4 balcony-wifi-breakfast
```
**Expected output:**

```text
Best assignment:
guest_L->105
guest_I->106
guest_D->107
```





### Test Case 8

**Input:**
```text
9
Chris 3 parking-wifi
Ann 2 wifi-parking-breakfast-balcony
Aida 2 wifi-breakfast-parking
Barb 1 breakfast-wifi-parking-balcony
Patty 1 wifi-breakfast
Olive 3 wifi-parking
Hazel 2 parking
Maureen 1 wifi-parking
Marsha 3 breakfast-parking-balcony-wifi
4
118 4 wifi-parking-breakfast-balcony
119 4 breakfast-balcony
218 4 balcony-wifi-parking-breakfast
219 2 parking
```
**Expected output:**

```text
Best assignment:
Olive->118
Marsha->218
Hazel->219
```





### Test Case 9

**Input:**
```text
2
guest_A 2 wifi
guest_B 2 wifi
2
101 2 wifi
102 2 wifi
```
**Expected output:**

```text
Best assignment:
guest_B->101
guest_A->102
```





### Test Case 10

**Input:**
```text
3
guest_A 4 wifi
guest_B 3 wifi
guest_C 3 wifi
2
101 4 wifi
102 3 wifi-parking
```
**Expected output:**

```text
Best assignment:
guest_A->101
guest_C->102
```

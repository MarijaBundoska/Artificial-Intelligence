## Exercise 2 – Minesweeper

### Problem Statement

This problem is based on the game Minesweeper.

Create a **function** that takes as input a list containing `#` and `-`, where each hash sign (`#`) represents a mine, and each dash (`-`) represents a field without a mine. The function should return a list where each dash is replaced with a number representing the number of mines in the neighboring fields of the current field (horizontally, vertically, and diagonally). The list returned as output should be created using the **list comprehension** approach.

From standard input, you are given the size of the field `N` (the field has dimensions `N × N`), as well as the representation of the field using `#` and `-`. You should represent the field as a list of lists where the elements are `#` and `-`. This list is the input to the previously defined function, and the output of the function should be printed to standard output.

**Hint:** The input is given row by row for each row of the field, while the individual elements are separated by three spaces. To separate the elements with three spaces, you can use the `split()` function defined for strings. To print the output, you can use the `join()` function defined for strings.


## Задача 2 – Minesweeper (Минско поле)

### Опис на задачата

Овој проблем се базира на играта Minesweeper.

Креирајте **функција** која како влез прима листа што содржи знаци `#` и `-`, каде што секој хаш-знак (`#`) претставува мина, а секоја цртичка (`-`) претставува поле без мина. Функцијата треба да врати листа во која секоја цртичка е заменета со број што го претставува бројот на мини во соседните полиња на тековното поле (хоризонтално, вертикално и дијагонално). Излезната листа треба да биде креирана со користење на пристапот **list comprehension**.

Од стандарден влез се внесува големината на полето `N` (полето има димензии `N × N`), како и приказот на полето со помош на знаците `#` и `-`.

Полето треба да се претстави како листа од листи, чии елементи се `#` и `-`. Оваа листа е влезен аргумент на претходно дефинираната функција, а резултатот од функцијата треба да се испечати на стандарден излез.

**Помош:** Влезните податоци се внесуваат ред по ред за секој ред од полето, при што поединечните елементи се одделени со три празни места. За разделување на елементите можете да ја користите функцијата `split()`, дефинирана за низи од знаци. За печатење на излезот можете да ја користите функцијата `join()`, исто така дефинирана за низи од знаци.

## Test Cases


### Test Case 1

**Input:**
```text
5
-   -   -   -   #
-   -   -   -   -
-   -   #   -   -
-   -   -   -   -
#   -   -   -   -
```
**Expected output:**

```text
0   0   0   1   #
0   1   1   2   1
0   1   #   1   0
1   2   1   1   0
#   1   0   0   0
```

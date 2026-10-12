## Exercise 1 – Weather Measurement Data

### Problem Statement

Weather measurement data for different cities are read from standard input. Each line contains the name of the city, the temperature measured on a certain day, and whether there was rain on that day (given as `"yes"` or `"no"`). The reading ends when the word `"end"` is entered.

For each city, all measured temperatures and the number of days with rain should be stored in a dictionary.

After all the data is read, for each city print the average temperature and the number of rainy days, sorted by the number of rainy days in descending order. If two cities have the same number of rainy days, they are ordered alphabetically by the city name.

The output format can be observed from the given test examples.

**Note:** In Python, you can use `sort()` or `sorted()` with the `key` parameter to define the sorting criteria. For example, if we are sorting tuples `x = (city_name, avg_temp, rainy_days)`, then we can first sort by the number of rainy days in descending order and then by the city name alphabetically using `key=lambda x: (-x[2], x[0])`.


# Вештачка интелигенција – Лабораториска вежба 1

Оваа папка ги содржи решенијата на задачите од првата лабораториска вежба по предметот Вештачка интелигенција на ФИНКИ.

---

## Задача 1 – Податоци за временски мерења

### Опис на задачата

Од стандарден влез се читаат податоци за временски мерења во различни градови. Секој ред го содржи името на градот, температурата измерена во одреден ден и дали имало или немало дожд во истиот ден (дадено како `"yes"` или `"no"`). Читањето завршува кога ќе се внесе зборот `"end"`.

За секој град треба да се зачуваат сите измерени температури и бројот на денови со дожд во речник.

По читањето на сите податоци, за секој град испечатете ја просечната температура и бројот на дождливи денови, сортирани според бројот на дождливи денови во опаѓачки редослед. Ако два града имаат ист број на дождливи денови, тие се подредуваат по азбучен ред според името на градот.

Форматот на излезот може да се воочи од дадените тест-примери.

**Забелешка:** Во Python можете да ги користите `sort()` или `sorted()` со параметарот `key` за дефинирање на критериумите за сортирање. На пример, ако сортираме торки `x = (име_на_град, просечна_температура, број_на_дождливи_денови)`, тогаш можеме прво да сортираме според бројот на дождливи денови во опаѓачки редослед, а потоа според името на градот по азбучен ред, користејќи `key=lambda x: (-x[2], x[0])`.


## Test Cases


### Test Case 1

**Input:**
```text
Skopje 24.5 yes
Bitola 22.1 no
Ohrid 20.0 yes
Skopje 25.3 no
Bitola 21.7 yes
Ohrid 19.8 yes
end
```
**Expected output:**

```text
Ohrid 19.9 2
Bitola 21.9 1
Skopje 24.9 1
```




### Test Case 2

**Input:**
```text
Tetovo 18.4 yes
Tetovo 20.1 yes
Tetovo 19.5 no
Gostivar 17.2 no
Gostivar 18.3 yes
Struga 21.0 no
Struga 20.5 no
end
```
**Expected output:**

```text
Tetovo 19.33 2
Gostivar 17.75 1
Struga 20.75 0
```




### Test Case 3

**Input:**
```text
Prilep 23.0 no
Prilep 24.0 no
Prilep 25.0 no
Kumanovo 22.0 yes
Kumanovo 23.0 yes
Kumanovo 24.0 yes
end
```
**Expected output:**

```text
Kumanovo 23.0 3
Prilep 24.0 0
```




### Test Case 4

**Input:**
```text
Skopje 24.5 yes
Bitola 22.3 no
Ohrid 20.1 yes
Tetovo 19.8 yes
Kumanovo 23.0 no
Strumica 26.2 yes
Prilep 21.4 no
Gostivar 18.7 yes
Struga 20.5 no
Kavadarci 24.1 no
Skopje 25.0 no
Bitola 21.9 yes
Ohrid 19.7 yes
Tetovo 20.3 no
Kumanovo 22.5 yes
Strumica 27.1 yes
Prilep 22.0 no
Gostivar 19.1 no
Struga 21.0 yes
Kavadarci 23.6 no
Skopje 23.8 yes
Bitola 22.7 no
Ohrid 20.4 no
Tetovo 21.0 yes
Kumanovo 23.4 no
Strumica 26.8 yes
Prilep 21.6 yes
Gostivar 18.9 yes
Struga 20.8 no
Kavadarci 24.3 yes
end
```
**Expected output:**

```text
Strumica 26.7 3
Gostivar 18.9 2
Ohrid 20.07 2
Skopje 24.43 2
Tetovo 20.37 2
Bitola 22.3 1
Kavadarci 24.0 1
Kumanovo 22.97 1
Prilep 21.67 1
Struga 20.77 1
```


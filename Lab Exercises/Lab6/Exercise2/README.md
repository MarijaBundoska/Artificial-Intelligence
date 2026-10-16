# Exercise 2 - Cryotherapy Treatment Classification Using Naive Bayes

## Problem Description

You are given a dataset for cryotherapy treatments. All included attributes are continuous, and it can be assumed that they follow a continuous distribution. Your task is to train a **Naive Bayes classifier** that predicts whether the treatment is successful or not (1 or 0), using the **first 85%** **of each class** of the dataset. You should compute the accuracy obtained on the remaining part of the dataset, and then make predictions on records received as input.

The starter code provides the dataset. As input, the program receives a single record for which a class prediction should be made. As output, the program should print the model's accuracy, the predicted class, and the probabilities of class membership.


# Задача 2 - Класификација на третмани со криотерапија со Наивен Баесов класификатор

## Опис на задачата

Дадено ни е податочно множество за третмани со криотерапија. Сите атрибути кои ги содржи се од непрекинат тип и може да се претпостави дека имаат непрекината распределба. Ваша задача е да истренирате **наивен баесов класификатор** кој ќе предвидува дали терапијата е успешна или не (1 и 0) користејќи ги **првите 85%** **од секоја класа** од даденото податочно множество. Треба да ја пресметате точноста која ја добивате над останатиот дел од податочното множество и потоа да направите предвидувања на записи кои ги примате на влез.

Во почетниот код имате дадено податочно множество. На влез се прима еден запис за кој треба да се направи предвидување на класата. На излез треба да се испечати точноста на моделот, класата на предвидување како и веројатностите за припадност во класите.



## Test Cases


### Test Case 1

**Test:**
```text
TC1
```
**Input:**
```text
1 20 4 3 1 6
```
**Expected output:**
```text
0.8571428571428571
1
[[0.00208097 0.99791903]]
```





### Test Case 2

**Test:**
```text
TC2
```
**Input:**
```text
1 20 4 3 1 6
```
**Expected output:**
```text
0.8571428571428571
1
[[0.00208097 0.99791903]]
```






### Test Case 3

**Test:**
```text
TC3
```
**Input:**
```text
1 34 11.25 1 3 150
```
**Expected output:**
```text
0.8571428571428571
0
[[0.99697507 0.00302493]]
```






### Test Case 4

**Test:**
```text
TC4
```
**Input:**
```text
2 21 10.75 7 1 35
```
**Expected output:**
```text
0.8571428571428571
1
[[0.13812339 0.86187661]]
```








### Test Case 5

**Test:**
```text
TC5
```
**Input:**
```text
2 41 7.75 5 2 20
```
**Expected output:**
```text
0.8571428571428571
0
[[0.78831244 0.21168756]]
```

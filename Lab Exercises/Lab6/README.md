# Exercise 1 - Solar Flare Classification Using Naive Bayes

## Problem Description

You are given a dataset for solar flare classification. All included attributes are categorical (the last column is the class attribute).

Your task is to train a **Naive Bayes classifier** that predicts solar flare classes using the **first X%** of the dataset. The percentage `X` is read from the standard input.

You should compute the accuracy obtained on the remaining part of the dataset, and then make predictions on records received as input.

## Input

The starter code provides the dataset.

As input, the program receives:
- The percentage `X` of the dataset to be used for training.
- A single record for which a class prediction should be made.

## Output

As output, the program should print:
- The model's accuracy on the remaining part of the dataset.
- The predicted class for the given record.
- The probabilities of class membership.

## Implementation

Train a **Naive Bayes classifier** using the first `X%` of the dataset, evaluate its accuracy on the remaining part of the dataset, and use the trained model to predict the class and class membership probabilities for the input record.


# Задача 1 - Класификација на соларни одблесоци со Наивен Баесов класификатор

## Опис на задачата

Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од категориски тип (последната колона е класен атрибут).

Ваша задача е да истренирате **наивен Баесов класификатор** кој ќе предвидува класи на соларен одблесок користејќи ги **првите X%** од даденото податочно множество. Процентот `X` се чита од стандарден влез.

Треба да ја пресметате точноста која ја добивате на останатиот дел од податочното множество и потоа да направите предвидувања на записи кои ги примате на влез.

## Влез

Во почетниот код имате дадено податочно множество.

На влез се примаат:
- Процентот `X` за поделба на податочното множество.
- Еден запис за кој треба да се направи предвидување на класата.

## Излез

На излез треба да се испечати:
- Точноста на моделот.
- Класата што ја предвидува моделот за дадениот запис.
- Веројатностите за припадност во класите.

## Имплементација

Потребно е да се истренира **наивен Баесов класификатор** користејќи ги првите `X%` од податочното множество, да се пресмета неговата точност на преостанатиот дел од податочното множество и да се предвиди класата и веројатностите за припадност во класите за дадениот запис.




## Test Cases


### Test Case 1

**Test:**
```text
TC1
```
**Input:**
```text
75
H R X 1 2 1 1 2 1 1
```
**Expected output:**
```text
0.8294797687861272
0
[[9.94855050e-01 4.57710457e-03 3.71407825e-04 9.29521929e-05
  3.34611214e-05 3.36218889e-05 7.71205438e-06 2.86906785e-05]]
```





### Test Case 2

**Test:**
```text
TC2
```
**Input:**
```text
75
H R X 1 2 1 1 2 1 1
```
**Expected output:**
```text
0.8294797687861272
0
[[9.94855050e-01 4.57710457e-03 3.71407825e-04 9.29521929e-05
  3.34611214e-05 3.36218889e-05 7.71205438e-06 2.86906785e-05]]
```





### Test Case 3

**Test:**
```text
TC3
```
**Input:**
```text
60
B X O 1 1 1 1 2 1 1
```
**Expected output:**
```text
0.8173598553345389
0
[[9.77941058e-01 2.03662205e-02 6.12553966e-05 8.18962050e-04
  8.79441217e-05 6.25847888e-04 9.70308698e-06 8.90094774e-05]]
```





### Test Case 4

**Test:**
```text
TC4
```
**Input:**
```text
90
D S I 1 3 1 1 2 1 1
```
**Expected output:**
```text
0.7553956834532374
0
[[7.89078069e-01 1.62154353e-01 2.93556921e-02 1.88386076e-02
  2.01521799e-04 2.69986709e-04 8.25712951e-05 1.91990549e-05]]
```





### Test Case 5

**Test:**
```text
TC5
```
**Input:**
```text
85
D S O 1 3 1 1 2 1 1
```
**Expected output:**
```text
0.7884615384615384
0
[[8.86994550e-01 1.04027606e-01 5.51382962e-03 3.19270262e-03
  3.22953582e-05 1.94703148e-04 3.96979816e-05 4.61518573e-06]]
```





### Test Case 6

**Test:**
```text
TC6
```
**Input:**
```text
50
E K C 2 2 2 2 2 2 1
```
**Expected output:**
```text
0.7884615384615384
0
[[8.86994550e-01 1.04027606e-01 5.51382962e-03 3.19270262e-03
  3.22953582e-05 1.94703148e-04 3.96979816e-05 4.61518573e-06]]
```





### Test Case 7

**Test:**
```text
TC7
```
**Input:**
```text
70
E A I 1 3 1 2 2 1 1
```
**Expected output:**
```text
0.8096385542168675
0
[[4.02622760e-01 1.22278921e-01 2.96872940e-01 1.15043444e-01
  5.11792242e-02 1.08606566e-02 8.52436920e-04 2.89617509e-04]]
```





### Test Case 8

**Test:**
```text
TC8
```
**Input:**
```text
80
D R I 1 3 1 1 2 1 1
```
**Expected output:**
```text
0.8122743682310469
0
[[8.43718865e-01 1.29064601e-01 2.09433190e-02 5.41770623e-03
  3.90055404e-04 3.48381748e-04 7.99104117e-05 3.71607197e-05]]
```

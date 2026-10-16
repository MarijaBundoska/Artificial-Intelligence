# Exercise 1 - Solar Flare Prediction Using a Decision Tree Classifier

## Problem Description

A dataset for solar flare prediction is given. All attributes in the dataset are categorical. Your task is to train a decision tree classifier that will predict solar flare classes using the last **X%** of the given dataset. You should calculate the accuracy obtained on the remaining **(100 - X)%** of the dataset.

The initial code already contains the dataset. The input consists of the split percentage value **X**. For example, if the value is 80, this means that you should use the last 80% of the dataset for training, and the first 20% for testing. Additionally, the variable **criterion** contains the value for the attribute selection criterion.

As output, print the accuracy, depth, and number of leaves of the constructed tree, as well as the features with the highest and lowest importance.

**To obtain the same results as in the test cases, when creating the classifier, set random_state=0.**


# Задача 1 - Предвидување на соларни одблесоци со дрво на одлука

## Опис на задачата

Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од категориски тип. Ваша задача е да истренирате класификатор - дрво на одлука кој ќе предвидува класи на соларен одблесок користејќи ги последните **X%** од даденото податочно множество. Треба да ја пресметате точноста која ја добивате над останатите **(100 - X)%** од податочното множество.

Во почетниот код имате дадено податочно множество. На влез се прима вредност за процентот на поделба **X**. На пример, ако вредноста е 80 значи дека ги користите последните 80% од множеството за тренирање, а првите 20% за тестирање. Дополнително во променливата **criterion** се вчитува вредност за критериумот за избор на најдобар атрибут.

На излез треба да се испечати точност, длабочина и број на листови на изграденото дрво, како и карактеристиките со најголема и најмала важност.

**За да ги добиете истите резултати како и во тест примерите, при креирање на класификаторот поставете random_state=0.**




## Test Cases


### Test Case 1

**Test:**
```text
TC1
```
**Input:**
```text
50
entropy
```
**Expected output:**
```text
Depth: 12
Number of leaves: 125
Accuracy: 0.7771345875542692
Most important feature: 0
Least important feature: 9
```





### Test Case 2

**Test:**
```text
TC2
```
**Input:**
```text
50
entropy
```
**Expected output:**
```text
Depth: 12
Number of leaves: 125
Accuracy: 0.7771345875542692
Most important feature: 0
Least important feature: 9
```





### Test Case 3

**Test:**
```text
TC3
```
**Input:**
```text
50
gini
```
**Expected output:**
```text
Depth: 12
Number of leaves: 122
Accuracy: 0.7916063675832128
Most important feature: 1
Least important feature: 9
```





### Test Case 4

**Test:**
```text
TC4
```
**Input:**
```text
60
entropy
```
**Expected output:**
```text
Depth: 12
Number of leaves: 137
Accuracy: 0.7554347826086957
Most important feature: 2
Least important feature: 9
```





### Test Case 5

**Test:**
```text
TC5
```
**Input:**
```text
60
gini
```
**Expected output:**
```text
Depth: 14
Number of leaves: 137
Accuracy: 0.7681159420289855
Most important feature: 2
Least important feature: 9
```





### Test Case 6

**Test:**
```text
TC6
```
**Input:**
```text
70
entropy
```
**Expected output:**
```text
Depth: 13
Number of leaves: 162
Accuracy: 0.8164251207729468
Most important feature: 0
Least important feature: 9
```





### Test Case 7

**Test:**
```text
TC7
```
**Input:**
```text
70
gini
```
**Expected output:**
```text
Depth: 14
Number of leaves: 169
Accuracy: 0.8067632850241546
Most important feature: 2
Least important feature: 9
```





### Test Case 8

**Test:**
```text
TC8
```
**Input:**
```text
80
entropy
```
**Expected output:**
```text
Depth: 13
Number of leaves: 200
Accuracy: 0.8478260869565217
Most important feature: 0
Least important feature: 7
```





### Test Case 9

**Test:**
```text
TC9
```
**Input:**
```text
80
gini
```
**Expected output:**
```text
Depth: 15
Number of leaves: 194
Accuracy: 0.8188405797101449
Most important feature: 2
Least important feature: 7
```





### Test Case 10

**Test:**
```text
TC10
```
**Input:**
```text
90
entropy
```
**Expected output:**
```text
Depth: 12
Number of leaves: 231
Accuracy: 0.7391304347826086
Most important feature: 0
Least important feature: 7
```





### Test Case 11

**Test:**
```text
TC11
```
**Input:**
```text
90
gini
```
**Expected output:**
```text
Depth: 14
Number of leaves: 228
Accuracy: 0.8188405797101449
Most important feature: 1
Least important feature: 7
```

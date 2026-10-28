import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    x_percent = int(input())
    criterion_value = input()

    X = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    encoder = OrdinalEncoder()
    X_encoded = encoder.fit_transform(X)

    num_samples = len(X_encoded)
    split_index = int(num_samples * (1 - x_percent / 100))

    train_X = X_encoded[split_index:]
    train_Y = Y[split_index:]
    test_X = X_encoded[:split_index]
    test_Y = Y[:split_index]

    classifier = DecisionTreeClassifier(criterion=criterion_value, random_state=0)
    classifier.fit(train_X, train_Y)

    predictions = classifier.predict(test_X)

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")
    print(f"Accuracy: {accuracy_score(test_Y, predictions)}")
    
    importances = classifier.feature_importances_
    print(f"Most important feature: {np.argmax(importances)}")
    print(f"Least important feature: {np.argmin(importances)}")

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)

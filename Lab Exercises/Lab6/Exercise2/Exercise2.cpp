import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


dataset_sample = [
    ['1', '35', '12', '5', '1', '100', '0'],
    ['1', '29', '7', '5', '1', '96', '1'],
    ['1', '50', '8', '1', '3', '132', '0'],
    ['1', '32', '11.75', '7', '3', '750', '0'],
    ['1', '67', '9.25', '1', '1', '42', '0']
]


if __name__ == "__main__":

    sample = input().split()

    data_array = np.array(dataset, dtype=float)

    X = data_array[:, :-1]
    Y = data_array[:, -1].astype(int)

    x_train_parts = []
    y_train_parts = []

    x_test_parts = []
    y_test_parts = []

    classes = np.unique(Y)

    for value in classes:

        positions = np.where(Y == value)[0]

        border = int(len(positions) * 0.85)

        x_train_parts.append(X[positions[:border]])
        y_train_parts.append(Y[positions[:border]])

        x_test_parts.append(X[positions[border:]])
        y_test_parts.append(Y[positions[border:]])

    x_train = np.vstack(x_train_parts)
    y_train = np.concatenate(y_train_parts)

    x_test = np.vstack(x_test_parts)
    y_test = np.concatenate(y_test_parts)

    model = GaussianNB()
    model.fit(x_train, y_train)

    predicted_values = model.predict(x_test)

    accuracy = accuracy_score(y_test, predicted_values)

    print(accuracy)

    sample_array = np.array(sample, dtype=float).reshape(1, -1)

    predicted_class = model.predict(sample_array)[0]
    probabilities = model.predict_proba(sample_array)

    print(int(predicted_class))
    print(probabilities)

    submit_train_data(x_train.tolist(), y_train.tolist())
    submit_test_data(x_test.tolist(), y_test.tolist())
    submit_classifier(model)
    submit_encoder(None)
    
    
    
    
    
    
    
    
# import os
# os.environ['OPENBLAS_NUM_THREADS'] = '1'

# from submission_script import *
# from dataset_script import dataset

# import numpy as np
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score


# dataset_sample = [
#     ['1', '35', '12', '5', '1', '100', '0'],
#     ['1', '29', '7', '5', '1', '96', '1'],
#     ['1', '50', '8', '1', '3', '132', '0'],
#     ['1', '32', '11.75', '7', '3', '750', '0'],
#     ['1', '67', '9.25', '1', '1', '42', '0']
# ]


# if __name__ == "__main__":

#     indexes = list(map(int, input().split()))

#     data_array = np.array(dataset, dtype=float)

#     X = data_array[:, :-1]
#     Y = data_array[:, -1].astype(int)

#     x_train_parts = []
#     y_train_parts = []

#     x_test_parts = []
#     y_test_parts = []

#     for value in np.unique(Y):

#         positions = np.where(Y == value)[0]

#         border = int(len(positions) * 0.75)

#         x_train_parts.append(X[positions[:border]])
#         y_train_parts.append(Y[positions[:border]])

#         x_test_parts.append(X[positions[border:]])
#         y_test_parts.append(Y[positions[border:]])

#     x_train = np.vstack(x_train_parts)
#     y_train = np.concatenate(y_train_parts)

#     x_test = np.vstack(x_test_parts)
#     y_test = np.concatenate(y_test_parts)

#     model = GaussianNB()
#     model.fit(x_train, y_train)

#     predicted_values = model.predict(x_test)

#     accuracy = accuracy_score(y_test, predicted_values)

#     print(accuracy)

#     for index in indexes:

#         current_sample = np.array(dataset[index][:-1], dtype=float).reshape(1, -1)

#         prediction = model.predict(current_sample)[0]

#         real_class = int(dataset[index][-1])

#         if int(prediction) == real_class:
#             print(True)
#         else:
#             print(False)

#     submit_train_data(x_train.tolist(), y_train.tolist())
#     submit_test_data(x_test.tolist(), y_test.tolist())
#     submit_classifier(model)
#     submit_encoder(None)

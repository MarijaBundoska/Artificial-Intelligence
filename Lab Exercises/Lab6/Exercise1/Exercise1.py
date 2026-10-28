import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from submission_script import *
from dataset_script import dataset

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
import numpy as np


if __name__ == "__main__":

    percentage = int(input())
    entry = input().split()

    split_index = int(len(dataset) * percentage / 100)

    training_set = dataset[:split_index]
    testing_set = dataset[split_index:]

    x_train_raw = [data[:-1] for data in training_set]
    y_train = [data[-1] for data in training_set]

    x_test_raw = [data[:-1] for data in testing_set]
    y_test = [data[-1] for data in testing_set]

    encoder = OrdinalEncoder()

    all_features = [data[:-1] for data in dataset]
    encoder.fit(all_features)

    x_train = encoder.transform(x_train_raw)
    x_test = encoder.transform(x_test_raw)

    model = CategoricalNB()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    acc = accuracy_score(y_test, predictions)

    encoded_entry = encoder.transform([entry])

    result = model.predict(encoded_entry)[0]
    probs = model.predict_proba(encoded_entry)

    ordered_classes = np.sort(model.classes_)
    class_indexes = [list(model.classes_).index(value) for value in ordered_classes]

    probs = probs[:, class_indexes]

    print(acc)
    print(result)
    print(probs)

    submit_train_data(x_train, y_train)
    submit_test_data(x_test, y_test)
    submit_classifier(model)
    submit_encoder(encoder)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# import os
# os.environ['OPENBLAS_NUM_THREADS'] = '1'

# from submission_script import *
# from dataset_script import dataset

# from sklearn.preprocessing import OrdinalEncoder
# from sklearn.naive_bayes import CategoricalNB
# from sklearn.metrics import accuracy_score
# import numpy as np


# if __name__ == "__main__":

#     threshold = 0.9
#     percentage = 80

#     entry = input().split()

#     split_index = int(len(dataset) * percentage / 100)

#     training_set = dataset[:split_index]
#     testing_set = dataset[split_index:]

#     x_train_raw = [row[:-1] for row in training_set]
#     y_train = [row[-1] for row in training_set]

#     x_test_raw = [row[:-1] for row in testing_set]
#     y_test = [row[-1] for row in testing_set]

#     encoder = OrdinalEncoder()

#     encoder.fit([row[:-1] for row in dataset])

#     x_train = encoder.transform(x_train_raw)
#     x_test = encoder.transform(x_test_raw)

#     model = CategoricalNB()
#     model.fit(x_train, y_train)

#     predictions = model.predict(x_test)
#     probabilities = model.predict_proba(x_test)

#     max_probabilities = np.max(probabilities, axis=1)

#     filtered_predictions = []
#     filtered_labels = []

#     counter = 0

#     for i in range(len(max_probabilities)):

#         if max_probabilities[i] >= threshold:

#             counter += 1

#             filtered_predictions.append(predictions[i])
#             filtered_labels.append(y_test[i])

#     if len(filtered_predictions) > 0:
#         acc = accuracy_score(filtered_labels, filtered_predictions)
#     else:
#         acc = 0

#     encoded_entry = encoder.transform([entry])

#     predicted_class = model.predict(encoded_entry)[0]

#     entry_probability = np.max(model.predict_proba(encoded_entry))

#     print(counter)
#     print(acc)
#     print(predicted_class)

#     if entry_probability >= threshold:
#         print(True)
#     else:
#         print(False)

#     submit_train_data(x_train, y_train)
#     submit_test_data(x_test, y_test)
#     submit_classifier(model)
#     submit_encoder(encoder)

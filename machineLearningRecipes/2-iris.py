
import numpy as np

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()

## Part 1
# print example data, learn dataset
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]

## Part 2
# separate testing data
test_indices = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_indices)
train_data = np.delete(iris.data, test_indices, axis=0)

# test data
test_target = iris.target[test_indices]
test_data = iris.data[test_indices]


## Part 3
# get classifier, predict labels for test data
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# classify test
#   test_target is expected, results should match
print test_target
print clf.predict(test_data)


## Part 4
# visualize the decision tree
# Check the vid https://www.youtube.com/watch?v=tNa99PG8hR8&index=2&list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal
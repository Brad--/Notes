from sklearn import datasets
iris = datasets.load_iris()

# Get data
# x = input, y = output. f(x) = y
x = iris.data
y = iris.target


# Separate test data
# from sklearn.cross_validation import train_test_split #deprecated
from sklearn.model_selection import train_test_split
# Neat!
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)


# Create classifier
#   Decision Tree Classifier
# from sklearn import tree
# classifier = tree.DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
print predictions

# Find accuracy
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

# cool stuff
#   https://playground.tensorflow.org
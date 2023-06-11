# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# 1) Load data (in this example we'll use the iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2) Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("X train")
print(X_train)

print("X test")
print(X_test)

print("Y train")
print(y_train)

print("Y test")
print(y_test)

# 3) Train the SVM model
clf = SVC(C=5,kernel='linear')
clf.fit(X_train, y_train)

# 4) Use the trained model to make predictions on the test set
y_pred = clf.predict(X_test)

print("SVM:")

# 5) Evaluate the performance of the model using a confusion matrix and accuracy metric
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

#confusion matrix
print("Confusion matrix:")

#accuracy score
print(cm)
print("Accuracy:", acc)


print(classification_report(y_test, y_pred))

# Use cross-validation to evaluate the model
scores = cross_val_score(classifier, iris.data, iris.target, cv=10)
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", scores.mean())

# 6) Use regularization to improve the model's performance
pipe = make_pipeline(StandardScaler(), classifier)
scores = cross_val_score(pipe, iris.data, iris.target, cv=10)
print("Cross-validation scores with regularization:", scores)
print("Mean cross-validation score with regularization:", scores.mean())








gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("Naive Bayes:")
print("Confusion matrix:")
print(cm)
print("Accuracy:", acc)

# Train and evaluate Neural Network model
nn = MLPClassifier()
nn.fit(X_train, y_train)
y_pred = nn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("Neural Network:")
print("Confusion matrix:")
print(cm)
print("Accuracy:", acc)

# Train and evaluate Logistic Regression model
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("Logistic Regression:")
print("Confusion matrix:")
print(cm)
print("Accuracy:", acc)

# Train and evaluate Random Forest model
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("Random Forest:")
print("Confusion matrix:")
print(cm)
print("Accuracy:", acc)

# Train and evaluate K-Nearest Neighbors model
knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("K-Nearest Neighbors:")
print("Confusion matrix:")
print(cm)
print("Accuracy:", acc)

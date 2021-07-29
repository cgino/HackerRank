
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression



def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place.
              It should not return anything.
    """

    # print(id_name_verified)
    # print(id_password)
    # print(id_name_verified['Id'].values)
    id_name_verified['Verified'] = id_password[id_name_verified['Id'].values == id_password[:, 0], -1]
    id_name_verified.rename(columns={'Verified': 'Password'}, inplace=True)

    pass

def train_and_predict(train_input_features, train_outputs, prediction_features):
    """
    :param train_input_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :param train_outputs: (numpy.array) A one-dimensional NumPy array where each element
                        is a number representing the species of iris which is described in
                        the same row of train_input_features. 0 represents Iris setosa,
                        1 represents Iris versicolor, and 2 represents Iris virginica.
    :param prediction_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :returns: (list) The function should return an iterable (like list or numpy.ndarray) of the predicted
                        iris species, one for each item in prediction_features
    """


    clf = make_pipeline(StandardScaler(), SVC(gamma='auto', kernel='rbf', probability=True))
    clf.fit(X_train, y_train)
    # pred = clf.predict(X_test)
    proba = clf.predict_proba(X_test)


    clf1 = RandomForestClassifier()
    clf1.fit(X_train, y_train)
    # pred1 = clf1.predict(X_test)
    proba1 = clf1.predict_proba(X_test)
    # print(proba1)

    clf2 = LogisticRegression(penalty='l2')
    clf2.fit(X_train, y_train)
    # pred2 = clf2.predict(X_test)
    proba2 = clf2.predict_proba(X_test)

    # Bagging to improve noise tolerance
    mean_prob = (proba + proba1 + proba2)/3
    mean_pred = np.argmax(mean_prob, axis=1)

    return mean_pred


if '__name__' == '__main__':
    id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
    id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
    login_table(id_name_verified, id_password)
    print(id_name_verified)

    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.3, random_state=0)

    y_pred = train_and_predict(X_train, y_train, X_test)
    print(y_pred)
    if y_pred is not None:
        print(metrics.accuracy_score(y_test, y_pred))






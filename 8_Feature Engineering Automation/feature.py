# Ref: https://towardsdatascience.com/practical-code-implementations-of-feature-engineering-for-machine-learning-with-python-f13b953d4bcd
import numpy as np
import pandas as pd
from feature_engine import discretisation as dsc
from feature_engine import encoding as ce
from feature_engine import outliers as outr
from feature_engine import transformation as vt
from feature_engine.imputation import MeanMedianImputer
from sklearn.model_selection import train_test_split


def load_titanic():
    data = pd.read_csv("https://www.openml.org/data/get_csv/16826755  /phpMYEkMl")
    data = data.replace("?", np.nan)
    data["cabin"] = data["cabin"].astype(str).str[0]
    data["pclass"] = data["pclass"].astype("O")
    data["embarked"].fillna("C", inplace=True)
    return data


# Load dataset
def load_titanic2():
    data = pd.read_csv("https://www.openml.org/data/get_csv/16826755/phpMYEkMl")
    data = data.replace("?", np.nan)
    data["cabin"] = data["cabin"].astype(str).str[0]
    data["pclass"] = data["pclass"].astype("O")
    data["embarked"].fillna("C", inplace=True)
    data["fare"] = data["fare"].astype("float")
    data["fare"].fillna(data["fare"].median(), inplace=True)
    data["age"] = data["age"].astype("float")
    data["age"].fillna(data["age"].median(), inplace=True)
    return data


def missing_inputation():
    # Load dataset
    data = pd.read_csv("creditApprovalUCI.csv")

    # Separate into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop("A16", axis=1), data["A16"], test_size=0.3, random_state=0
    )

    # Set up the imputer
    median_imputer = MeanMedianImputer(
        imputation_method="median", variables=["A2", "A3", "A8", "A11", "A15"]
    )
    # fit the imputer
    median_imputer.fit(X_train)

    # transform the data
    X_train = median_imputer.transform(X_train)
    X_test = median_imputer.transform(X_test)


def categorical_encoding():
    # Load dataset
    data = load_titanic()

    # Separate into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(["survived", "name", "ticket"], axis=1),
        data["survived"],
        test_size=0.3,
        random_state=0,
    )

    # set up the encoder
    encoder = ce.CountFrequencyEncoder(
        encoding_method="frequency", variables=["cabin", "pclass", "embarked"]
    )

    # fit the encoder
    encoder.fit(X_train)

    # transform the data
    train_t = encoder.transform(X_train)
    test_t = encoder.transform(X_test)


def discretization():
    # Load dataset
    data = data = pd.read_csv("houseprice.csv")

    # Separate into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(["Id", "SalePrice"], axis=1),
        data["SalePrice"],
        test_size=0.3,
        random_state=0,
    )

    # set up the discretisation transformer
    disc = dsc.DecisionTreeDiscretiser(
        cv=3,
        scoring="neg_mean_squared_error",
        variables=["LotArea", "GrLivArea"],
        regression=True,
    )

    # fit the transformer
    disc.fit(X_train, y_train)

    # transform the data
    train_t = disc.transform(X_train)
    test_t = disc.transform(X_test)


def outlier():
    # Load dataset
    data = load_titanic2()

    # Separate into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(["survived", "name", "ticket"], axis=1),
        data["survived"],
        test_size=0.3,
        random_state=0,
    )

    # set up the capper
    capper = outr.Winsorizer(
        capping_method="gaussian", tail="right", fold=3, variables=["age", "fare"]
    )

    # fit the capper
    capper.fit(X_train)

    # transform the data
    train_t = capper.transform(X_train)
    test_t = capper.transform(X_test)


def variable_transformation():
    # Load dataset
    data = data = pd.read_csv("houseprice.csv")

    # Separate into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(["Id", "SalePrice"], axis=1),
        data["SalePrice"],
        test_size=0.3,
        random_state=0,
    )

    # set up the variable transformer
    tf = vt.BoxCoxTransformer(variables=["LotArea", "GrLivArea"])

    # fit the transformer
    tf.fit(X_train)

    # transform the data
    train_t = tf.transform(X_train)
    test_t = tf.transform(X_test)


if __name__ == "__main__":
    categorical_encoding()

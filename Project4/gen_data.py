import numpy as np


def best_4_lin_reg(seed=1489683273):
    np.random.seed(seed)

    # Create X values
    X = np.random.random((100, 5))

    # Linear relation with noise
    Y = (
        2 * X[:, 0]
        + 3 * X[:, 1]
        - 1 * X[:, 2]
        + np.random.normal(0, 0.01, 100)
    )

    return X, Y


def best_4_dt(seed=1489683273):
    np.random.seed(seed)

    # Create X values
    X = np.random.random((100, 5))

    # Non-linear relation (Decision Tree friendly)
    Y = np.where(
        X[:, 0] > 0.5,
        X[:, 1] ** 2,
        np.sin(X[:, 2] * 3)
    )

    return X, Y


def author():
    return  "paras123"
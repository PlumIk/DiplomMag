from abc import ABC, abstractmethod

import numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor


class ModelWrapper(ABC):
    @abstractmethod
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'ModelWrapper':
        pass

    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        pass


class GBMModel(ModelWrapper):
    def __init__(self):
        self._model = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'GBMModel':
        self._model = HistGradientBoostingRegressor(l2_regularization=1,
                                                    learning_rate=0.01,
                                                    loss='absolute_error',
                                                    max_bins=128,
                                                    max_iter=100,
                                                    max_leaf_nodes=1024,
                                                    min_samples_leaf=64,
                                                    random_state=42,
                                                    verbose=9,
                                                    )
        self._model = self._model.fit(X, y)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)


if __name__ == '__main__':
    model = GBMModel()
    X = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [1, 2, 2]])
    y = np.array([1.0, 2.5, 3.5])
    model = model.fit(X, y)
    sample1 = np.array([[1, 2, 3]])
    sample2 = np.array([[2, 3, 3]])
    print(model.predict(sample2))
    print(model.predict(sample1))

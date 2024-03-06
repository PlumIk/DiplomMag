import numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor

from common.Parameters.Paremeter import Parameter


class GradientFunction:
    def rebuildDunction(self, data):
        self.model = HistGradientBoostingRegressor(l2_regularization=1,
                                                   learning_rate=0.01,
                                                   loss='absolute_error',
                                                   max_bins=128,
                                                   max_iter=100,
                                                   max_leaf_nodes=1024,
                                                   min_samples_leaf=64,
                                                   random_state=42,
                                                   verbose=9,
                                                   )
        matrix = []
        targets = []
        for parameters in data:
            line = []
            targets.append(parameters.getTarget())
            for parameter in parameters.parameters:
                line.append(parameter.getValue())
            matrix.append(line)

        X = np.array(matrix)
        Y = np.array(targets)
        self.model = self.model.fit(X, Y)

    def getTarget(self, data) -> float:
        sample = np.array(data).reshape(1, -1)
        print(self.model.predict(sample)[0])
        return float(self.model.predict(sample)[0])

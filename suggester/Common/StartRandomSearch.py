import optuna

from common.Enums.ParameterTypes import ParameterTypes
from common.Enums.RangeTypes import RangeTypes
from common.Parameters.Paremeter import Parameter
from suggester.Common.SuggesterBase import SuggesterBase

currentParameters = list()
study = None
currentTarget = 0
result = list()


class StartRandomSearch(SuggesterBase):
    def __init__(self):
        self._study = optuna.create_study()
        self._current_target = None
        self._current_params = None
        self._result = None

    def step(self, target, parameters: list[Parameter]) -> list[Parameter]:
        self._study = optuna.create_study()
        self._current_target = None
        self._current_params = None
        self._result = None
        self._current_params = parameters
        self._current_target = target
        self._study.optimize(self.get_objective(), n_trials=1)
        return self._result

    def get_objective(self):
        def objective(trial):
            self._result = []
            for parameter in self._current_params:
                value = None
                if parameter.getType() is ParameterTypes.IntType:
                    if parameter.getRangeType() is RangeTypes.RangesRange:
                        value = trial.suggest_int(parameter.getName(), parameter.getRange()[0], parameter.getRange()[1])
                    elif parameter.getRangeType() is RangeTypes.DescreteRange:
                        value = trial.suggest_int(parameter.getName(), 0, len(parameter.getRange()))
                elif parameter.getType() is ParameterTypes.NumberType:
                    if parameter.getRangeType() is RangeTypes.RangesRange:
                        value = trial.suggest_float(parameter.getName(), parameter.getRange()[0],
                                                    parameter.getRange()[1])
                    elif parameter.getRangeType() is RangeTypes.DescreteRange:
                        value = trial.suggest_int(parameter.getName(), 0, len(parameter.getRange()))
                        value = parameter.getRange()[value]
                elif parameter.getType() is ParameterTypes.StringType:
                    value = trial.suggest_int(parameter.getName(), 0, len(parameter.getRange()))
                    value = parameter.getRange()[value]
                self._result.append(parameter.createCopy(value))
            return self._current_target
        return objective

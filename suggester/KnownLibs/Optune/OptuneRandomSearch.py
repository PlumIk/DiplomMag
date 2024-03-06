import optuna

from common.Enums.ParameterTypes import ParameterTypes
from common.Enums.RangeTypes import RangeTypes
from common.Parameters.Paremeter import Parameter
from suggester.Common.SuggesterBase import SuggesterBase


class OptuneRandomSearch(SuggesterBase):

    def __init__(self, function):
        self._study = optuna.create_study()
        self._current_target = None
        self._current_params = None
        self._result = None
        self._function = function

    def step(self, target, parameters: list[Parameter]) -> list[Parameter]:
        self._current_params = parameters
        self._current_target = target
        self._study.optimize(self.get_objective(), n_trials=10)
        result = []
        for parameter in parameters:
            newParameter = parameter.createCopy(self._study.best_params.get(parameter.getName()))
            result.append(newParameter)
        return result

    def get_objective(self):
        def objective(trial):
            result = []
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
                result.append(value)
            return self._function.getTarget(result)
        return objective

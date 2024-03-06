from common.Enums.RangeAttributes import RangeAttributes
from common.Enums.RangeTypes import RangeTypes
from common.Enums.SuggesterTypes import SuggesterTypes
from common.Parameters.IntegerParameter import IntegerParameter
from common.ParametersContexst import ParametersContexst
from suggester.Common.DataBase import DataBase
from suggester.Common.StartRandomSearch import StartRandomSearch
from suggester.Preparing import work as mainWork


def work():
    test1()

def test1():
    one = IntegerParameter("1", RangeTypes.RangesRange, 1, RangeAttributes.readWriteAllowed, [0, 100])
    context = ParametersContexst(SuggesterTypes.RandomSearch, 100, [one])
    data = DataBase(context)
    initTarget = data.currentParameters.target
    for _ in range(data.config.startIters):
        predictedParameters = StartRandomSearch().step(initTarget, data.currentParameters.parameters)
        target = predictedParameters[0].getValue() % 50 + 1
        newData = ParametersContexst(data.currentParameters.suggesterType, target, predictedParameters)
        data.setNewProbParameters(newData)
    data.initFunction()
    for _ in range(500):
        predictedParameters = mainWork(data)
        line = []
        for parameter in predictedParameters:
            line.append(parameter.getValue())
        data.setPsevdoTarget(data.function.getTarget(line))
        target = predictedParameters[0].getValue() % 50 + 1
        newData = ParametersContexst(data.currentParameters.suggesterType, target, predictedParameters)
        data.setNewProbParameters(newData)
    print(data.getBest())
# for _ in range(10):
#   predictedParameters = mainWork(data)
#  predictedParameters.setTarget(predictedParameters[0].getValue() % 50)
#  data.setNewParameters(predictedParameters)

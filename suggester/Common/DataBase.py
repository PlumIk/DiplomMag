from common.ParametersContexst import ParametersContexst
from suggester.Function.GradientFunction import GradientFunction
from suggester.MainWork.ConfigData import ConfigData


class DataBase:
    def __init__(self, parameters: ParametersContexst):
        self.config = ConfigData()
        self.currentParameters = parameters
        self.allParameters = [parameters]
        self.countedTarget = -1
        self.countedIter = 0

    def setNewProbParameters(self, parameters: ParametersContexst):
        self.allParameters.append(parameters)
        self.currentParameters = parameters
        if self.countedTarget > 0:
            if abs(self.currentParameters.getTarget() - self.countedTarget) / self.currentParameters.getTarget() > self.config.loss:
                self.function.rebuildDunction(self.allParameters)
                self.countedIter = 0
            elif self.countedIter > self.config.iterations:
                self.function.rebuildDunction(self.allParameters)
                self.countedIter = 0
            else:
                self.countedIter += 1

    def initFunction(self):
        self.function = GradientFunction()
        self.function.rebuildDunction(self.allParameters)

    def setPsevdoTarget(self, countedTarget: float):
        self.countedTarget = countedTarget

    def getBest(self):
        best = self.allParameters[0]
        bestTarget = best.getTarget()
        for parameters in self.allParameters:
            if parameters.getTarget() < bestTarget:
                best = parameters
                bestTarget = best.getTarget()
        return best
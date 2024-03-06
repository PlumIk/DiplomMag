from common.Enums.SuggesterTypes import SuggesterTypes
from common.Parameters.Paremeter import Parameter


class ParametersContexst:

    def __init__(self, suggesterType: SuggesterTypes, target: float, parameters: list[Parameter]):
        self.suggesterType = suggesterType
        self.target = target
        self.parameters = parameters

    def countTarget(self) -> float:
        self.target = 1

    def setTarget(self, value: float):
        self.target = value

    def getTarget(self) -> float:
        return self.target

    def getParameters(self) -> list[Parameter]:
        return self.parameters

    def getSuggesterType(self) -> SuggesterTypes:
        return self.suggesterType

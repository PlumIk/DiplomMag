from common.Enums.ParameterTypes import ParameterTypes
from common.Enums.RangeTypes import RangeTypes


class Parameter:
    def getValue(self):
        return self.value

    def getRange(self):
        return self.range

    def getType(self) -> ParameterTypes:
        return self.type

    def getName(self) -> str:
        return self.name

    def getRangeType(self) -> RangeTypes:
        return self.rangeType

    def createCopy(self, value) -> 'Parameter':
        pass
from common.Enums.ParameterTypes import ParameterTypes
from common.Enums.RangeAttributes import RangeAttributes
from common.Enums.RangeTypes import RangeTypes
from common.Parameters.Paremeter import Parameter


class IntegerParameter(Parameter):
    def __init__(self, name: str, rangeType: RangeTypes, value: int, rangeAttributes: RangeAttributes, range: list):
        self.name = name
        self.rangeType = rangeType
        self.value = value
        self.rangeAttributes = rangeAttributes
        self.range = range
        self.type = ParameterTypes.IntType

    def createCopy(self, value) -> 'Parameter':
        return IntegerParameter(self.name, self.rangeType, value, self.rangeAttributes, self.range)

from common.Enums.ParameterTypes import ParameterTypes
from common.Enums.RangeAttributes import RangeAttributes
from common.Parameters.Paremeter import Parameter


class StringParameter(Parameter):
    def __init__(self, name: str, value: str, rangeAttributes: RangeAttributes, range: list):
        self.name = name
        self.value = value
        self.rangeAttributes = rangeAttributes
        self.range = range
        self.type = ParameterTypes.StringType

    def createCopy(self, value) -> 'Parameter':
        return StringParameter(value, self.rangeAttributes, self.range)
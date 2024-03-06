from enum import Enum


class RangeAttributes(Enum):
    nothingAllowed = 0
    readOnlyAllowed = 1
    writeOnlyAllowed = 2
    readWriteAllowed = 3

    def getAllowed(self, readAllowed: bool, writeAllowed:bool):
        if readAllowed and writeAllowed:
            return self.readWriteAllowed
        if readAllowed:
            return self.readOnlyAllowed
        if writeAllowed:
            return self.writeOnlyAllowed
        return self.nothingAllowed

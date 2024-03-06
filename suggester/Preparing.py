from common.Enums.SuggesterTypes import SuggesterTypes
from suggester.Common.DataBase import DataBase
from suggester.KnownLibs.Optune.OptuneRandomSearch import OptuneRandomSearch


def work(data: DataBase):
    currentSuggester = data.currentParameters.getSuggesterType()
    result = list()
    if currentSuggester is SuggesterTypes.RandomSearch:
        result = OptuneRandomSearch(data.function).step(data.currentParameters.getTarget(), data.currentParameters.getParameters())
    return result

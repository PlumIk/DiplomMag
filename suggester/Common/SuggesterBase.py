from common.Parameters.Paremeter import Parameter


class SuggesterBase:
    def step(self, target, parameters: list[Parameter]) -> list[Parameter]:
        pass
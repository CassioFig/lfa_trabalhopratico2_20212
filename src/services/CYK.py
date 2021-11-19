from utils.GrammarRead import GrammarReader

class CYK:
    def __init__(self):
        self.__grammar = GrammarReader().execute()

    def __loadTable(self, length: int, string: str) -> list[list]:
        table = []
        for i in range(length):
            table.append([[] for j in range(length)])

        for i in range(length):
            for variable, values in self.__grammar.items():
                if string[i] in values:
                    table[i][i].append(variable)
        return table

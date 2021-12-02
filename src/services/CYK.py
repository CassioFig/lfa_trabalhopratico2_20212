from utils.GrammarRead import GrammarReader
from utils.PrintTable import PrintTable

class CYK:
    def __init__(self):
        self.__grammar = GrammarReader().execute()

    def testString(self, string: str):
        length = len(string)

        table = self.__loadTable(length, string)
        print(table)
        table = self.__execute(table, length)

        PrintTable(table, string).execute()

        if self.__isValid(table):
            print('String aceita!')
        else:
            print('String recusada!')

    def __loadTable(self, length: int, string: str) -> list[list]:
        table = []
        for i in range(length):
            table.append([[] for j in range(length)])

        for i in range(length):
            for variable, values in self.__grammar.items():
                if string[i] in values:
                    table[i][i].append(variable)
        return table

    def __execute(self, table, length: int):
        for i in range(1, length):
            for j in range(length - i):
                for k in range(i):
                    for variable, values in self.__grammar.items():
                        for value in values:
                            if len(value) == 2:
                                if value[0] in table[j][j+k] and value[1] in table[j+k+1][j+i]:
                                    table[j][j+i].append(variable)
        return table

    def __isValid(self, table):
        firstVariable = list(self.__grammar.keys())[0]
        if firstVariable in table[0][-1]:
            return True
        return False

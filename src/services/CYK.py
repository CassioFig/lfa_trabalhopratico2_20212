from utils.GrammarRead import GrammarReader
from utils.PrintTable import PrintTable

class CYK:
    def __init__(self):
        self.__grammar = GrammarReader().execute()

    def testString(self, string: str):
        length = len(string)

        table = self.__loadTable(length, string)
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

        print('--' * 14)
        print('   Etapa: 1')
        print('--' * 14)
        for i in range(length):
            for variable, values in self.__grammar.items():
                if string[i] in values:
                    table[i][i].append(variable)
                    print(f'A variável {variable} contém a letra {string[i]}, posição (1, {i + 1}): {self.__removeRepeated(table[i][i])}')
        return table

    def __execute(self, table, length: int):
        for i in range(1, length):
            print('--' * 14)
            print(f'   Etapa: {i + 1}')
            print('--' * 14)
            for j in range(length - i):
                for k in range(i):
                    for variable, values in self.__grammar.items():
                        for value in values:
                            if len(value) == 2:
                                if value[0] in table[j][j+k] and value[1] in table[j+k+1][j+i]:
                                    table[j][j+i].append(variable)
                                    print(f'A variação {value} está presente em {variable}, posição ({j + 1},{(j+i) + 1}): {self.__removeRepeated(table[j][j+i])}')
        return table

    def __isValid(self, table):
        firstVariable = list(self.__grammar.keys())[0]
        if firstVariable in table[0][-1]:
            return True
        return False

    def __removeRepeated(self, array):
        aux = []
        for value in array:
            if value not in aux:
                aux.append(value)
        return aux

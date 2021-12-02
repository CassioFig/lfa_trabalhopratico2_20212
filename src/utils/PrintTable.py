class PrintTable:
    def __init__(self, table, string):
        self.table = table
        self.string = string

    def execute(self):
        print('--' * 14)
        print('         Tabela')
        print('--' * 14)

        count = 0
        length = len(self.table) - 1
        for i in range(len(self.table)):
            aux = []
            for j in range(length, len(self.table)):
                if (j <= len(self.table)):
                    if len(self.table[count][j]) == 0:
                        aux.append(['-'])
                    else:
                        aux.append(self.__removeRepeated(self.table[count][j]))
                    count += 1
                else:
                    break
            print(aux)
            count = 0
            length -= 1

        self.__printString()
        print('--' * 14)

    def __removeRepeated(self, array):
        aux = []
        for value in array:
            if value not in aux:
                aux.append(value)
        return aux

    def __printString(self):
        aux = []
        for letter in self.string:
            aux.append(letter)
        print(aux)
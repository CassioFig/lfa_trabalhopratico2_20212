import re

class GrammarReader:
    def __init__(self) -> None:
        self.__file = "src/grammar.txt"
            
    def execute(self) -> dict:
        grammar = {}
        with open(self.__file, 'r', encoding='utf-8') as file:
            for row in file:
                values = re.findall(r'\w+', row)
                grammar[values[0]] = values[1::]
        return grammar
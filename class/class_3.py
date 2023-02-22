"""class otrezok:
    def __init__(self, a, b):
        self.a = a
        self.b = b



class Otrezok(otrezok):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c

    def Sun(self):
        return  self.a + self.b + self.c

a = int(input("Введите длинну отрезка  a: "))
b = int(input("Введите длинну отрезка  b: "))
c = int(input("Введите длинну отрезка  c:"))
obj = Otrezok(a, b, c)
print("Длинна всех отрезков:", obj.Sun())

"""


def letters_num():
    return f"{len(letters)}  букв"


class ALphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
lang = "В Англиский алфавите"
print(letters, lang, letters_num())




class EngAlphabet(ALphabet):
    def __init__(self):
        super().__init__(lang, letters)
    def proverka(self):
        self.proverka()
        if a == letters:
            return "True"
        if a != letters:
            return "False"
        if b == letters:
            return "True"
        if b != letters:
            return "False"

a = input("Введите букву:")
b = input("Введите букву:")
print(proverka())


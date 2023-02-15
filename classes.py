class Person:
    name = str()
    surname = str()
    qualify = int()
    sex = str()
    def __init__(self, name, surname, qualify = 1, sex='male'):
        self.name = name
        self.surname = surname
        self.qualify = qualify
        self.sex = sex

    def prints(self):
        ls = [self.name, self.surname, str(self.qualify)]
        return str(' '.join(ls))

if __name__ == '__main__':
    a = Person("Sultan", "Kurbanov", 13)


    print(a.prints())
    input('>')


class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length


a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
obj = rectangle(a, b)
print("Площадь прямоугольника:", obj.area())

print()


class rectangle ():
    def __init__(self, breadth_1, breadth_2, length):
        self.breadth_1= breadth_1
        self.breadth_2 = breadth_2
        self.length = length

    def area(self):
        return self.breadth_1 * self.length * self.breadth_2


a = int(input("Введите 1-ю сторону треугольника: "))
b = int(input("Введите 2-ю сторону треугольника: "))
c = int(input("Введите 3-ю сторону треугольника: "))
obj = rectangle(a, b, c)
print("Площадь треугольника:", obj.area())

print()

from sys import stdin


class matrix():
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def str(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = matrix(a)
print(m.str())

exec(stdin.read())

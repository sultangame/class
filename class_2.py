"""class Person(object):
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age
    def move(self):
        return f'{self.fullname} идет  в/'
f'школу и Ему(ей) 13 год(а) '

    def talk(self):
        return f"Данный момент {self.fullname} разговаривает с боТом!"


    if __name__ == "__main__":
        sultan = Person("Sultan", 13)
        print(sultan.move())
        print(sultan.talk())"""


class Dog(object):
    def __init__(self, name, age, colour, breed ):
        self.name = name
        self.age = age
        self.colour = colour
        self.breed = breed
    def sposobnosty(self):
        return f"моя собака по  кличке {self.name} подчиняется командам , он хоррошо надресерован"

    def description(self):
        return f"он {self.colour} цвета" \
               f" он из породы  {self.breed} " \
               f" ему  {self.age} года"
    def is_play(self):
        return f"{self.name} любит гулять и играть"


if __name__ == "__main__":
    My_dog = Dog("Шарик", 2, "черного", "авчарок")
    print(My_dog.sposobnosty())
    print(My_dog.description())




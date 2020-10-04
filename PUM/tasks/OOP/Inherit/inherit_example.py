class Pet:

    def __init__(self, name):
        self.name = name

    def say(self):
        return self.name

# определили класс Dog как наследника класса Pet
class Dog(Pet):

    def __init__(self, name, breed):
        # super() - обращение к классу предка, в данном случае - класс Pet
        # таким образом заполняем атрибут name с помощью уже написанного метода __init__ у класса Pet
        super().__init__(name)
        self.breed = breed

    def say(self):
        return super().say() + " : waw"

# определили класс FightingDog как наследника класса Dog
class FightingDog(Dog):

    def __init__(self, name, breed, is_angry):
        # использование __init__ класса Dog
        super().__init__(name, breed)
        self.__is_angry = is_angry

    def feed(self):
        self.__is_angry = False

    def step_on_tail(self):
        self.__is_angry = True

    def say(self):
        if self.__is_angry:
            # super() можно использовать также и для других методов класса предка
            # в данном случае используем уже написанный метод say() класса Dog
            return super().say() + 10*"waw"
        else:
            return super().say()

# определили класс Crocodile как наследника класса Pet
class Crocodile(Pet):

    def __init__(self, name, weight):
        # использование __init__ класса Pet
        super().__init__(name)
        self.weight = weight

    def say(self):
        return super().say() + " : rrrrr"

    # метод say переопределяется у всех потомков класса Pet
    # вызов метода выглядит одинаковым для объектов всех созданных нами классов,
    # однако исполняемый код разный (полиморфизм)


# Работа с созданной иерархией

a = FightingDog("Мухтар", "Овчарка", False)
b = Dog("Тузик", "Мопс")
с = Crocodile("Ник", 100)

zoo = [a, b, c]

for animal in zoo:
    print(animal.say())
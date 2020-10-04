# определение класса
class Robot:
    # определение магического метода __init__, вызывается при создании объектов класса
    def __init__(self, name, build_year):
        # переменная принадлежащая классу - АТРИБУТ класса
        # добавляем атрибуты класса name и build_year
        self.name = name
        self.build_year = build_year

    # функция принадлежащая классу - МЕТОД класса
    def say_hi(self):
        print('Привет, меня зовут {}'.format(self.name))

    # self - аргумент, представляющий объект класса, вызывающий метод или обращающийся к атрибуту
    # вспоминаем аналогию со списком

# создание трёх объектов класса Robot
# вызов Robot("Alex", 1979) соответствует вызову методу __init__("Alex", 1979) класса Robot
a = Robot("Alex", 1979)
b = Robot("Marvin", 2005)
c = Robot("Alex", 2017)

# создаём список объектов класса
robot_list = [a, b, c]

# вызов метода say_hi() для каждого робота в списке
for robot in robot_list:
    robot.say_hi()
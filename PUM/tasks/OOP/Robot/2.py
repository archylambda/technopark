class Robot:
    
    def __init__(self, name, build_year):
        # "закрыли" атрибуты класса добавив к началу названия атрибута 2 подчеркивающие черты
        # например, следующий код теперь выдаст ошибку (если вставить после 39 строки):
        # >> print(a.__name)
        # такие атрибуты называются ПРИВАТНЫМИ
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        print('Привет, меня зовут {}'.format(self.__name))

    # однако чтобы взаимодествовать с приватными атрибутами добавим
    # соответствующие методы

    # получить имя робота
    def get_name(self):
        return self.__name

    # изменить имя робота, только если name - не пустая строка
    def set_name(self, name):
        if name != '':
            self.__name = name

    # получить год создания робота
    def get_by(self):
        return self.__build_year

    # изменить год создания робота, только если год создания > 0
    def set_by(self, by):
        if by > 0:
            self.__build_year = by

    # Теперь мы можем контролировать работу с атрибутами объекта извне, например, проверять новое имя робота или его
    # год создания перед тем как изменить соотвествующий атрибут у объекта. Вы сами решаете, как будут работать с
    # объектами ваших классов, например, мы можем запретить изменять атрибут name, убрав метод set_name(name).
    # Но все также можно будет получить имя робота используя метод get_name().

a = Robot("Alex", 1979)
b = Robot("Marvin", 2005)
c = Robot("Alex", 2017)

robot_list = [a, b, c]

# модифицированный цикл из прошлого задания, обратите внимание как мы теперь работаем с атрибутами объектов в списке
for robot in robot_list:
    robot.say_hi()
    if (robot.get_name() == "Alex"):
        robot.set_by(2000)    
    print('Год моего создания {}'.format(robot.get_by()))

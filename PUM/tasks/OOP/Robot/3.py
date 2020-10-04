class Robot:
    
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print('Привет, меня зовут {}'.format(self.__name))
        else:
            print('Привет, я робот без имени')

    # аналог get_name() из прошлого задания, будет вызываться при обращении
    # >> print(a.name)
    @property
    def name(self):
        return self.__name

    # аналог set_name(name) из прошлого метода, будет вызываться при присваивании атриубуту значения:
    # >> a.name = 'Martin'
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def build_year(self):
        return self.__build_year

    @build_year.setter
    def build_year(self, by):
        self.__build_year = by

    # магический метод, меняющий внутреннее представление объектов класса
    # пример: вывод на экран список robot_list
    # print(robot_list)
    def __repr__(self):
        return "Robot('" + str(self.__name) + "', " + str(self.__build_year) + ")"

    # магический метод, меняющий строкое представление объекта
    # пример: вывод на экран объекта класса
    # >> print(a)
    def __str__(self):
        return "Name: " + str(self.__name) + ", Build Year: " + str(self.__build_year)

    @classmethod
    def copy(cls, self):
        return cls(self.__name, self.__build_year)

def andrew_gen(robot_list):
    res = []
    for robot in robot_list:
        tmp = Robot.copy(robot)
        tmp.name = "Andrew"
        res.append(tmp)

    return res

a = Robot("Alex", 1979)
b = Robot("Marvin", 2005)
c = Robot("Alex", 2017)
d = Robot()

robot_list = [a, b, c, d]

for robot in robot_list:
    if (robot.name == "Alex"):
        robot.build_year = 2000    
    print(robot)
#1 Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight:
    __traffic_light_color = "Светофор"
    def running(self):
        while True:
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(3)
            break
a = TrafficLight()
a.running()

from time import sleep
class TrafficLight:
    __light = ['red', 'yellow', 'green']
    def running(self):
        print('now', self.__light[0])
        sleep(7)
        print('now', self.__light[1])
        sleep(2)
        print('now', self.__light[2])
        sleep(3)
a = TrafficLight()
a.running()



#2 Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def calc(self):
        return f'Масса асфальта {(self._lenght * self._width * 25 * 0.05) / 1000} тонн'
road1 = Road(5000, 20)
print(road1.calc())

#3 Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'oklad': int(wage), 'premia': int(bonus)}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return f'доход: {self._income["oklad"] + self._income["premia"]}'
worker1 = Position('Петр', 'Петров', 'Водитель', 10000, 7000)
print(worker1.get_full_name())
print(worker1.get_total_income())

#4 Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'New car: {self.name} color: {self.color} police ? {self.is_police}')
    def go(self):
        print(f'Car: {self.name} go')
    def stop(self):
        print(f'Car: {self.name} stop')
    def turn(self, direction):
        print(f'Car: {self.name} turn {"left" if direction == 0 else "right"}')
    def show_speed(self):
        print(f'Car: {self.name} goes with speed {self.speed}')
class Towncar(Car):
    def show_speed(self):
        print(f' Car: {self.name} goes with speed {self.speed} {"- Outlaw speed" if self.speed > 60 else "- Speed is normal"}')

class Workcar(Car):
    def show_speed(self):
        print(f' Car: {self.name} goes with speed {self.speed} {"- Outlaw speed" if self.speed > 40 else "- Speed is normal"}')

class Sportcar(Car):
    pass
class Policecar(Car):
    def __init__(self, name, color, speed, is_police = True):
        super().__init__(name, color, speed, is_police)
t_c = Towncar(50, 'yellow', '\nbus')
t_c.turn(0)
t_c.show_speed()

w_c = Workcar(70, 'black', '\ntrack')
w_c.turn(1)
w_c.show_speed()

p_c = Policecar(120, 'white', 'police')
p_c.stop()
p_c.show_speed()
print(p_c.is_police)

#5 Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'запуск отрисовки'
class Pen(Stationery):
    def draw(self):
        return f'запуск отрисовки {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'запуск отрисовки {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'запуск отрисовки {self.title}'

pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())

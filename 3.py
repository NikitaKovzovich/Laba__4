# 1. Реализуйте базовый класс Car.
# 2. У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# 3. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# 4. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# 5. Для классов TownCar и WorkCar переопределите метод show_speed.
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"\n{self.name} поехала.")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")

class SportCar(Car):
   pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = True)


town_car = TownCar(55, "red","Toyota")
sport_car = SportCar(120, "blue", "Ferrari")
work_car = WorkCar(45, "yellow", "Ford")
police_car = PoliceCar(80,"black","Police Car")


town_car.go()
town_car.show_speed()
town_car.turn("налево")
town_car.stop()

sport_car.go()
sport_car.show_speed()
sport_car.turn("направо")
sport_car.stop()

work_car.go()
work_car.show_speed()
work_car.turn("направо")
work_car.stop()

police_car.go()
police_car.show_speed()
police_car.turn("налево")
police_car.stop()
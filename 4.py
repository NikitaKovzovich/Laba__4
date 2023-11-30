# 1. CarRental, представляющий систему аренды автомобилей.
# 2. В классе определены доступные автомобили с их ценой за день и количеством доступных единиц.
# 3. Конструктор класса CarRental принимает тип автомобиля и длительность аренды.
# 4. Метод rent_car позволяет арендовать заданное количество автомобилей определенного типа на указанный срок.
# 5. При аренде выводится информация о количестве автомобилей, типе, длительности аренды и общей стоимости.
# 6. После каждой аренды уменьшается доступность выбранного типа автомобиля.
# 7. Метод display_available_cars выводит информацию о доступных автомобилях и их характеристиках.
# 8. Метод show_rental_prices отображает цены на аренду для всех типов автомобилей.

class CarRental:
    available_cars = {
        "Седан": {"rental_price": 2000, "availability": 5},
        "Внедорожник": {"rental_price": 3000, "availability": 3},
        "Хэтчбек": {"rental_price": 1800, "availability": 7},
    }

    def __init__(self, car_type, rental_duration):
        self.car_type = car_type
        self.rental_duration = rental_duration

    def rent_car(self, num_of_cars):
        if self.car_type in CarRental.available_cars:
            if self.rental_duration > 0 and num_of_cars > 0:
                total_cost = self.rental_duration * CarRental.available_cars[self.car_type]["rental_price"] * num_of_cars

                if self.rental_duration == 1:
                    print(
                        f"\nВы арендовали {num_of_cars} автомобиль(ей) типа {self.car_type} на {self.rental_duration} день.")
                else:
                    print(
                        f"\nВы арендовали {num_of_cars} автомобиль(ей) типа {self.car_type} на {self.rental_duration} дней.")

                print(f"Стоимость аренды составляет {total_cost} рублей.")

                # Уменьшаем доступность автомобиля после аренды
                CarRental.available_cars[self.car_type]["availability"] -= num_of_cars
            else:
                print("Длительность аренды и количество автомобилей должны быть больше 0.")
        else:
            print("Выбранный тип автомобиля не доступен.")

    @staticmethod
    def display_available_cars():
        print("\nДоступные автомобили:")
        for index, (car_type, details) in enumerate(CarRental.available_cars.items(), start=1):
            print(f"{index}. {car_type}: Цена аренды - {details['rental_price']} рублей, Доступно - {details['availability']} шт.")

    @classmethod
    def show_rental_prices(cls):
        for car_type, details in cls.available_cars.items():
            print(f"{car_type}: {details['rental_price']} рублей за день.")


while True:
    CarRental.display_available_cars()

    chosen_car_index = int(input("\nВыберите номер автомобиля из списка (0 - завершить аренду): "))

    if chosen_car_index == 0:
        break

    if 1 <= chosen_car_index <= len(CarRental.available_cars):
        chosen_car_type = list(CarRental.available_cars.keys())[chosen_car_index - 1]

        num_of_cars_to_rent = int(input("Укажите количество автомобилей для аренды: "))
        rental_duration = int(input("Укажите длительность аренды (в днях): "))

        rental_instance = CarRental(chosen_car_type, rental_duration)
        rental_instance.rent_car(num_of_cars_to_rent)

        CarRental.show_rental_prices()
    else:
        print("Некорректный номер автомобиля.")

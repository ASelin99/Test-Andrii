import random


class Car:
    def __init__(self, model: str, color: str, economy: int):
        self.model = model
        self.color = color
        self.economy = economy
        self.mileage = 0
        self.fuel = 100

    def drive(self, distance):
        fuel = distance / self.economy
        if fuel <= self.fuel:
            self.mileage += distance
            self.fuel -= fuel
        else:
            print("Not enough fuel")

    def fuel_up(self):
        self.fuel = min(self.fuel + 20, 100, 200)

    def distance_left(self):
        return self.fuel / self.economy


def generate_random_cars(num_cars):
    models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
    colors = ["White", "Gray", "Black", "Red", "Brown"]
    cars = []

    for _ in range(num_cars):
        model = random.choice(models)
        color = random.choice(colors)
        economy = random.randint(10, 20)
        car = Car(model, color, economy)
        cars.append(car)
    return cars


def drive_and_refuel(cars, distance_1, distance_2):
    for car in cars:
        car.drive(distance_1)
        car.fuel_up()
        car.drive(distance_2)


def car_with_highest_fuel(cars):
    car_with_highest_fuel = max(cars, key=lambda car: car.fuel)
    return car_with_highest_fuel


def print_car_description(car):
    print(f"Car with highest fuel: Model - {car.model}, Color - {car.color}, Fuel reserve - {car.fuel}%")


cars = generate_random_cars(10)

drive_and_refuel(cars, 200, 100)

car_with_highest_fuel = car_with_highest_fuel(cars)

print_car_description(car_with_highest_fuel)

from car import Car


def main():
    my_car = Car("Car", 42)
    my_car.drive(0)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
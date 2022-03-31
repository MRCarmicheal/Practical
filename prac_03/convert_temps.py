import random


def main():
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_output.txt", "w")
    for line in input_file:
        result = convert_celsius_to_fahrenheit(float(line))
        print(result, file=output_file)
    input_file.close()
    output_file.close()


def create_input_file(quantity):
    temperatures_file = open("temps_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temperatures_file)
    temperatures_file.close()


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
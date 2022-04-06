
import random
MINIMUM_number = 1
MAXIMUM_number = 45


def main():
    number_picks = int(input("How many quick picks? "))
    while number_picks < 0:
        print("That makes no sense!")
        number_picks = int(input("How many quick picks? "))

    for i in range(number_picks):
        quick_pick = []
        for j in range(0, 6):
            number = random.randint(MINIMUM_number, MAXIMUM_number)
            while number in quick_pick:
                number = random.randint(MINIMUM_number, MAXIMUM_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
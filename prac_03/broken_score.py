import random


def main():
    score = random.randint(1, 100)
    result = determine_status(score)
    print(result)
    with open("result.txt", "a+") as f:
        f.write(result)


def determine_status(score):
    if score < 0 or score > 100:
        return "\n{} is Invalid score".format(score)
    elif score >= 90:
        return "\n{} is Excellent score".format(score)
    elif score >= 50:
        return "\n{} is Pass score".format(score)
    else:
        return "\n{} is Bad score".format(score)


main()



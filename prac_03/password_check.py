

def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Enter password: ")
    return password


def print_asterisks(number):
    print('*' * len(number))


main()
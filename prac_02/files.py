out_file = open("name.text", "w")
name = input("What is your name?")
print(name, file=out_file)
out_file.close()

in_file = open("name.text", "r")
name = in_file.read().strip()
print("your name is ", name)
in_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1+number2)
in_file.close()

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()

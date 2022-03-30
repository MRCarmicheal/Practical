number = int(input("Number of items : "))
sum = 0
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items :"))
for i in range(number):
    price = float(input("Price of item: "))
    sum += price
if sum > 100:
    sum = sum * 0.9
print("Total price for", number, "items is $", sum)



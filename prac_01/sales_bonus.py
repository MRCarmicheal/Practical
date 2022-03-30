
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print("Bonus is :{:.2f}".format(bonus))
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Bonus is :{:.2f}".format(bonus))
    pass
    sales = float(input("Enter sales: $"))

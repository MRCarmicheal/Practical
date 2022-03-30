
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero")
print("Finished.")

# 1 when input isn't number will be display ValueError
# 2 when numberator is 0 will be display ZeroDivisonError


score = float(input("Enter score: "))
if 90 <= score < 100:
    print("Excellent")
elif 50 <= score < 90:
    print("pass")
elif 50 > score > 0:
    print("Bad")
else:
    print("Invalid score")

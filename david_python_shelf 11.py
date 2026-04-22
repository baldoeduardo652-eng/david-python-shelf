def classify_score():
    num = int(input("Enter a score: "))

    if 90 <= num <= 100:
        print("Excellent")
    elif 75 <= num <= 89:
        print("Good")
    elif 0 <= num <= 74:
        print("Needs improvement")
    else:
        print("Invalid score")



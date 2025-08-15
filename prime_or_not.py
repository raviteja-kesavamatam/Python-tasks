number = int(input("Enter your number :"))
if number > 1:
    for i in range(2, number):
        if number % 1 == 0:
            print("Not Prime")
        break
    else:
        print("Prime Number")
else:
    print("Not Prime")

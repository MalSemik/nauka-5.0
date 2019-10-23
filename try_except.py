def ask():
    while True:
        try:
            number = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            result = number **2

            print(f"Thank you, your number squared is: {result}")
            break
ask()
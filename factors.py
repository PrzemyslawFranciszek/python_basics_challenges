good_input = True
while good_input:
    user_number = int(input("Please input positive integer number to find factors: "))
    if user_number > 0:
        for factor in range(1, user_number + 1):
            if (user_number % factor == 0):
                print(f"{factor} is a factor of {user_number}")
        good_input = False
    else:
        print(f"{user_number} is not a positive integer. ")

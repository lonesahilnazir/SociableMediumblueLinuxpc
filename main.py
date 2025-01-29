    action = str(input())

    if action == "odd_num_check":
        number = int(input())
        if number % 2 == 0:
            print("no")
        else:
            print("yes")

    elif action == "perfect_square_check":
        number = int(input())
        if number < 0:
            print("no")
        else:
            is_sq = False
            x = 0
            while x * x <= number:
                if x * x == number:
                    is_sq = True
                else:
                    is_sq = False
                x += 1
            print("yes" if is_sq else "no")

    elif action == "vowel_check":
        text = str(input())
        if any(char in "aeiouAEIOU" for char in text):
            print("yes")
        else:
            print("no")

    elif action == "divisibility_check":
        number = int(input())
        if number % 2 == 0 and number % 3 == 0:
            print("divisible by 2 and 3")
        elif number % 2 == 0:
            print("divisible by 2")
        elif number % 3 == 0:
            print("divisible by 3")
        else:
            print("not divisible by 2 and 3")

    elif action == "palindrominator":
        text = str(input())
        print(text+text[:-1][::-1])

    elif action == "simple_interest":
        principal_amount = int(input())
        n_years = int(input())
        if n_years < 10:
            print(round(principal_amount * 5 * n_years / 100))
        else:
            print(round(principal_amount * 8 * n_years / 100))

    else:
        print("Invalid Operation")
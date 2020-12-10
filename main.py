secret_number = 777
print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


def guess_function():
    guess_number = int(input("Guess a three int number : "))
    right = False
    while not right:
        if guess_number != secret_number:
            print("Ha ha! You're stuck in my loop!")
            return guess_function()
        else:
            print("Well done, muggle! You are free now")
            right = True


guess_function()

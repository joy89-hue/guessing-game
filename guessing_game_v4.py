import random

highest = 1000
secret_number = random.randint(1, highest)
# print(secret_number) # TODO: Remove after testing
guess = 0   # initialise to any number that doesn't equal to  answer
print("Please guess a number between 1 and {}".format(highest))

while guess != secret_number:
    guess = int(input("Enter: "))
    if guess == 0:
        break
    if guess == secret_number:
        print("Well done, you guessed correctly!")
        break
    else:
        if guess < secret_number:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input("Enter: "))
        # if guess == secret_number:
        #     print("Well done, you guessed correctly!")
        # else:
        #     print("Sorry, you can't made it")

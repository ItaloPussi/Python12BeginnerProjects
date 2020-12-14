import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != "c":
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = high

        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)??").lower()

        if(feedback == "h"):
            high = guess -1
        elif(feedback == 'l'):
            low = guess + 1

    print(f"The computer won! The number is {guess}")

print("The computer will find out your number between 1 and 100000\n")
computer_guess(100000)
        
#...........................
import random
secret_number = random.randint(1, 100)

guess = 0

while guess != secret_number:
    guess = int(input("TEBAK ANGKA BRE MASUKIN ANGKA "))

    if guess < secret_number:
        print("TOO HIGH BRE")
 
    elif guess > secret_number:
        print("TOO LOW BREE")

    else:
        print("CONGRATULATIONS BRE. YOU BENAR")



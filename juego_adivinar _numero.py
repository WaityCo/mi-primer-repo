import random

random_number = random.randint(1, 100)
print(random_number)

playing = True

while  playing:
    guess = int(input("Ingresa el número"))
    if guess == random_number:
        print("Ganaste")
        playing = False
    elif guess > random_number:
        print("El número debe ser menor")
    elif guess < random_number:
        print("El número debe ser mayor")


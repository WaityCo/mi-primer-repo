# number = int(input("Ingrese un numero "))

# for n in range(1, number + 1):
#    print(n)   

for n in range(1, 101):
    print(n)
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

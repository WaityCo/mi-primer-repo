a = int(input("Ingrese un numero"))
b = int(input("Ingrese otro numero numero"))

def min(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return "Los numeros son iguales"
    
print(min(a, b))

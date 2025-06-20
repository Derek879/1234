def MN (a, b):
    if a > b:
        return f"El numero mayor es {a}"
    else:
        return f"El numero mayor es {b}"

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(MN(num1, num2))
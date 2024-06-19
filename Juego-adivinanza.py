import random


numero_secreto = random.randint(1,101)
adivinado = False
cant_max_intentos = 5
cant_intentos = 0

print("Bienvenido al juego de adividar el numero secreto!")

while not adivinado and cant_intentos < cant_max_intentos:
    numero = input("Introduce un numero del 1 al 99: ")   #TODO: convertir en numero
    numero = int(numero)

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    
    cant_intentos +=1

if not cant_intentos < cant_max_intentos:
    print("¡Game over! No has podido adivinar en la cantidad máxima de intentos")




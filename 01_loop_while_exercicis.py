###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
n=10
while n>=1:
    print(n)
    n-=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
n = 1
suma = 0
while n <= 20:
    if n % 2 == 0:
        suma += n
    n += 1

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero = int(input("Introdueix un número enter positiu: "))

if numero < 1:
    print("El número ha de ser positiu")
else:
    factorial = 1
    n = 1

    while n <= numero:
        factorial = factorial * n
        n = n + 1

    print(f"El factorial de {numero} és {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
while True:
    contrasenya = input("Introdueix una contrasenya: ")
    if len(contrasenya) >= 8:
        break
    print("La contrasenya ha de tenir almenys 8 caràcters")

print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix un número: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

n = int(input("Introdueix un número enter positiu N: "))

if n < 1:
    print("El número ha de ser positiu")
else:
    candidat = 2

    while candidat <= n:
        es_primer = True
        divisor = 2

        while divisor < candidat:
            if candidat % divisor == 0:
                es_primer = False
            divisor = divisor + 1

        if es_primer:
            print(candidat)

        candidat = candidat + 1
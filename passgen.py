"""Module providing a function printing python version."""

# importacion de módulos
import string
import random

### GENERADOR DE CONTRASEÑAS ###


def passgen():
    # INPUT PARA PREGUNTAR AL USUARIO LA LONGITUD DE SU CONTRASEÑA
    longitud = int(input("Ingrese el tamaño de la contraseña: "))

    # VARIABLE PARA TENER A DISPOSICIÓN DISTINTOS CARACTERES

    # ascci_letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    # digits: 0123456789

    # punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # VARIABLE CONTRASEÑA
    # Uso de .join para concatenar caracteres aleatorios usando el metodo random.choice
    # Para la longitud uso un for donde el limite es la longitud expresada por el usuario
    contraseña = "".join(random.choice(caracteres) for i in range(longitud))

    print(f"La contraseña generada es: {contraseña}")


passgen()

import csv
from storage import client_route

def user_authenticate():
    usuario = input("Insert your username: ")
    password = input("Insert your password: ")
    with open(client_route, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for row in lector:
            if row['username'] == usuario and row['password'] == password:
                    return True
    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
    return user_authenticate()
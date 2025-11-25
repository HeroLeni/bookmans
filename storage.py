import csv

#route to the csv of the books
route_books = "csv/books.csv"
#route to the clients
client_route = "csv/clients.csv"

#it reads the files from the csv
def read_csv(route):
    with open(route, newline='', encoding='utf-8') as file:
        lector = csv.DictReader(file)
        return [dict(row)for row in lector]

#it writes into the files
def write_csv(route, camps, data):
    with open(route, mode ="w", newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=camps)
        escritor.writeheader
        for row in data:
            escritor.writerow(row)

#adds new rows
def add_row(route, camps, row):
    with open(route, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=camps)
        escritor.writerow(row)


#it modifies the data or eliminates it from
def modify_csv(route, thing, data, id_delete,camp="id"):
    new_list = [row for row in data if row[camp] != id_delete]
    write_csv(route, thing, new_list)
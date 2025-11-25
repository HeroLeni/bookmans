from storage import read_csv,write_csv,add_row,modify_csv,route_books

book_thing = [
    "book_id",
    "title",
    "author",
    "category",
    "price", 
    "stock_quantity",
    "most_sold", 
    "quantity_sold"
]

def obtain_id_book():
    book = read_csv(route_books)
    if not book:
        return "001"
    ids = [int(v['book_id'][:]) for v in book if v['book_id'].startswith('V')]
    max_id = max(ids) if ids else 0
    return f"v{str(max_id + 1).zfill(3)}"

def register_books():
    new_book = obtain_id_book()
    print(f"assigned an ID {new_book}")
    data = {
        "book_id": new_book,
        "title": input("insert the title of the book: "),
        "author": input("insert the author of the book: "),
        "category": input("insert the category of the book: "),
        "price": input("insert the price of the book: "), 
        "stock_quantity": input("Insert the stock of the book: "),
        "most_sold": input("is this book the most sold? yes or no? "),
        "quantity_sold": input("insert the most sold after book: ")
    }
    add_row(route_books, book_thing, data)
    print("Book succesfully registered")


def list_books():
    books = read_csv(route_books)
    for books in books:
        print(tuple(books[c] for c in book_thing))

def check_books():
    books = read_csv(route_books)
    search = input("insert the id of the book: ")
    for books in books:
        if books["book_id"] == search:
            print("the searched book: ")
            print(books)
            return
        print("the book is not registered")

def modify_books():
    book = read_csv(route_books)
    search_id = input("introduce the ID for the book: ")
    for books in book:
        if books["book_id"] == search_id:
            print("the real data at the moment", book)
            for camp in book_thing[1:]:
                new = input(f"new value for {camp}(For the moment: {book[camp]}): ")
                if new:
                    books[camp] = new
                modify_csv(route_books, book_thing, books)
                print("the book has been modified")
                return
            print("this id doesn't exist")

def delete_books():
    books = read_csv(route_books)
    id_delete = input("ID of the book to delete: ")
    new = [v for v in books if v["book_id"] != id_delete]
    if len(new) < len(books):
        modify_csv(route_books, book_thing, new, id_delete)
        print("Book eliminated.")
    else:
        print("this id doesn't exist.")

def top_sell():
    seller = read_csv(route_books)
    for books in books:
        if seller not in books:
            return None
        total_units = sum(p["quantity"] for p in books)
        total_value = sum((lambda p: ["price"] * p["quantity"])(p) for p in books)
        most_expensive_book = max(books, key=lambda p: p["price"])
        most_sold_book = max(books, key=lambda p: p["quantity"])
        most_sold_author = max(books, key=lambda p: p["author"])
        return {
            "total_units": total_units,
            "total_value": total_value,
            "most_expensive_book": most_expensive_book,
            "most_sold_book": most_sold_book,
            "most_sold_author": most_sold_author
        }
    
def sell_buk():
    selling = read_csv(route_books)
    for books in books:
        if selling not in books:
            return None
        id_book = input("insert the id for the book: ")
        id_book = obtain_id_book
        if id_book in route_books:
            quantity = input("how many books do you want?: ")
            new_quantity = quantity - "stock_quantity"
            write_csv(new_quantity)
            print(f"done, bought {quantity} of books")
            print(f"there are {new_quantity} of books left")
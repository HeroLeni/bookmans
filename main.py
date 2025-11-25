from auth import user_authenticate
from book import register_books
from book import check_books
from book import modify_books
from book import delete_books
from book import top_sell
from book import sell_buk

def main_menu():
    while True:
        print("1. register books")
        print("2. check books")
        print("3. modify books")
        print("4. delete books")
        print("5. top sellers")
        print("6. buy a buk")
        print("7. exit")
        opcion_menu = input("enter an option from the menu (1-7): ")

        match opcion_menu:
            case "1":
                register_books()
            case "2":
                check_books()
            case "3":
                modify_books()
            case "4":
                delete_books()
            case "5":
                top_sell()
            case "6":
                sell_buk()
            case "7":
                print("Good bye m8")
                break
            case _:
                print("Error, not valid option")

is_a_customer = user_authenticate()
if is_a_customer:
    print("welcom to bookmans")
    main_menu()
else:
    print("error, password or username are incorrect")



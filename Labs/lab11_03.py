import os


def menu(options):
    for key, value in options.items():
        print(f"{key}. {value}")

    user_input = input("Choose an option.")
    return int(user_input)


def borrow_book():
    pass


def return_book():
    pass


def add_book():
    pass


def remove_book():
    pass


def main():
    library = {}
    role_menu = {1: "Admin", 2: "Member"}
    admin_options = {1: "Add new book", 2: "Remove book", 0: "Exit"}
    admin_actions = {1: add_book, 2: remove_book}
    member_options = {1: "Borrow a book", 2: "Return a book", 0: "Exit"}
    member_actions = {1: borrow_book, 2: return_book}
    choice = -1

    role_choice = menu(role_menu)

    while choice != 0:
        os.system("clear")
        if role_choice == 1:
            choice = menu(admin_options)
            if choice in admin_actions:
                admin_actions[choice]()
        elif role_choice == 2:
            choice = menu(member_options)
            if choice in member_actions:
                member_actions[choice]()


if __name__ == "__main__":
    main()

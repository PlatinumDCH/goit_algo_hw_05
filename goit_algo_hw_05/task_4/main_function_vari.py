def input_error(expected_args):
    def decorator(func):
        def wrapper(phone_book, args):
            if expected_args == 0:
                return func(phone_book, args)

            if len(args) == 0:
                return "Please enter arguments for the command"

            if len(args) != expected_args:
                return f"Command expected {expected_args} arguments"

            return func(phone_book, args)

        return wrapper

    return decorator


def parse_input(user_input: str):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(2)
def add_contact(phone_book, args):
    name, phone = args
    phone_book[name] = phone
    return "Contact added."


@input_error(2)
def change_contact(phone_book, args):
    name, phone = args
    if name in phone_book:
        phone_book[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."


@input_error(1)
def delete_contact(phone_book, args):
    name = args[0]
    if name in phone_book:
        del phone_book[name]
        return "Contact deleted."
    else:
        return "Contact not found."


@input_error(1)
def show_phone(phone_book, args):
    name = args[0]
    if name in phone_book:
        return f"{phone_book[name]}"
    else:
        return "Contact not found."


def greting():
    return "Hello, how can I help you?"


@input_error(0)
def show_all(phone_book, args):
    if phone_book:
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def show_command():
    help_text = (
        "Available commands:\n"
        "1. add <name> <phone> - Add a new contact.\n"
        "2. change <name> <new_phone> - Change an existing contact's phone number.\n"
        "3. phone <name> - Show the phone number of a contact.\n"
        "4. all - Show all contacts.\n"
        "5. help - Show this help message.\n"
        "6. del - Delete a contact.\n"
        "7. hello - greets the user.\n"
        "8. close / exit - Exit the program."
    )
    print(help_text)


def main():
    phone_book = {}
    while True:
        user_input = input("Enter a command: ").strip()
        cmd, *args = parse_input(user_input)

        if cmd == "add":
            print(add_contact(phone_book, args))
        elif cmd == "change":
            print(change_contact(phone_book, args))
        elif cmd == "phone":
            print(show_phone(phone_book, args))
        elif cmd == "all":
            show_all(phone_book, [])
        elif cmd == "help":
            show_command()
        elif cmd == "del":
            print(delete_contact(phone_book, args))
        elif cmd == "hello":
            print(greting())
        elif cmd in ["close", "exit"]:
            print("Goodbye!")
            break
        else:
            print('Invalid command. Type "help" for a list of available commands.')


if __name__ == "__main__":
    print("Welcome to the CLI assistant")
    main()

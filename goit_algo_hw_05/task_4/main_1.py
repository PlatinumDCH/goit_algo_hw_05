class CommandHandler:
    def __init__(self, contact_book):
        self.contact_book = contact_book

    def input_error(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except KeyError:
                print("Error: Contact not found.")
            except ValueError:
                print("Error: Invalid value provided.")
            except IndexError:
                print("Error: Missing arguments.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        return wrapper

    @input_error
    def add_contact(self, name, phone):
        self.contact_book[name] = phone
        print("Contact added.")

    @input_error
    def change_contact(self, name, phone):
        if name not in self.contact_book:
            raise KeyError
        self.contact_book[name] = phone
        print("Contact updated.")

    @input_error
    def show_phone(self, name):
        print(self.contact_book[name])

    @input_error
    def show_all(self):
        if self.contact_book:
            for name, phone in self.contact_book.items():
                print(f"{name}: {phone}")
        else:
            print("Contact book is empty.")

    @input_error
    def help_command(self):
        help_text = (
            "Available commands:\n"
            "1. hello - Greet the bot.\n"
            "2. add <name> <phone> - Add a new contact.\n"
            "3. change <name> <phone> - Change an existing contact's phone.\n"
            "4. phone <name> - Show the phone number of a contact.\n"
            "5. all - Show all contacts.\n"
            "6. help - Show this help message.\n"
            "7. close / exit - Exit the program."
        )
        print(help_text)


class CLI:
    def __init__(self):
        self.contact_book = {}
        self.command_handler = CommandHandler(self.contact_book)

    def greeting(self):
        print("Welcome to the assistant bot!")

    def run_command(self, command, args):
        commands = {
            "hello": lambda: print("How can I help you?"),
            "add": lambda: self.check_arguments(
                args, 2, self.command_handler.add_contact
            ),
            "change": lambda: self.check_arguments(
                args, 2, self.command_handler.change_contact
            ),
            "phone": lambda: self.check_arguments(
                args, 1, self.command_handler.show_phone
            ),
            "all": lambda: self.command_handler.show_all(),
            "help": lambda: self.command_handler.help_command(),
            "close": lambda: print("Good bye!"),
            "exit": lambda: print("Good bye!"),
        }

        command_func = commands.get(command)
        if command_func:
            command_func()
        else:
            print("Invalid command.")

    def check_arguments(self, args, expected_length, func):
        if len(args) != expected_length:
            print(f"Enter the command and {expected_length} argument(s).")
        else:
            func(*args)


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def main():
    cli_bot = CLI()
    cli_bot.greeting()
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            cli_bot.run_command(command, args)
            break

        cli_bot.run_command(command, args)


if __name__ == "__main__":
    main()

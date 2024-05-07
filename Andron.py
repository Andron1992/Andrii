
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid input value. Please provide correct arguments."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Invalid input value. Please provide correct arguments."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    if not user_input:
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(contacts, name, phone_number):
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone_number
    return "Contact added."
@input_error
def change_contact(contacts, name, new_phone_number):
    if name not in contacts:
        return "Contact not found."
    contacts[name] = new_phone_number
    return "Contact updated."

@input_error
def show_phone(contacts, name):
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    all_contacts = "\n".join([f"{name}: {contacts[name]}" for name in contacts])
    return all_contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)


        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: add [ім'я] [номер телефону]")
                continue
            name, phone_number = args
            print(add_contact(contacts, name, phone_number))
        elif command == "change":
            if len(args) != 2:
                print("Invalid number of arguments. Usage: change [ім'я] [новий номер телефону]")
                continue
            name, new_phone_number = args
            print(change_contact(contacts, name, new_phone_number))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid number of arguments. Usage: phone [ім'я]")
                continue
            name = args[0]
            print(show_phone(contacts, name))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
        main()


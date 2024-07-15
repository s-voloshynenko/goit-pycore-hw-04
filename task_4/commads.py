def add_contact(args: list, contacts: dict) -> str:
    try:
        validate_arguments_length(args, 2)
        name, phone = args

        if name in contacts:
            return "Contact is already exist. Use \"change\" command to update the contact."

        contacts[name] = phone

        return "Contact added."
    except ValueError as e:
        return str(e)

def change_contact(args: list, contacts: dict) -> str:
    try:
        validate_arguments_length(args, 2)
        name, phone = args

        if name not in contacts:
            return "Contact doesn't exist"

        contacts[name] = phone

        return "Contact updated."
    except ValueError as e:
        return str(e)

def show_phone(args: list, contacts: dict) -> str:
    try:
        validate_arguments_length(args, 1)
        name = args[0]

        if name not in contacts:
            return "Contact doesn't exist"

        return contacts[name]
    except ValueError as e:
        return str(e)

def all_contacts(contacts: dict) -> str:
    if not contacts:
        return "Contacts dictionary is empty."

    command_output = "Contacts list:"

    for name, phone in contacts.items():
        command_output += f"\n{name}: {phone}"

    return command_output

# utils
def validate_arguments_length(args: list[str], desired_len: int):
    if len(args) != desired_len:
        raise ValueError(f"not enough values to unpack (expected {desired_len}, got {len(args)})")
    return

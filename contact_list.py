contact_list = []

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        while True:
            name = input("Enter the contact's name: ").title()
            if any(contact[0] == name for contact in contact_list):
                print("A contact with this name already exists. Please try again!")
                continue
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            address = input("Enter the contact's address: ")
            contact_list.append([name, phone, email, address])
            print("Contact added successfully!")
            break

    elif option == 2:
        print("\nContact List:")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact[0]} - {contact[1]}")

    elif option == 3:
        search_query = input("Enter the name or phone number to search: ").lower()
        matching_contacts = [contact for contact in contact_list if search_query in contact[0].lower() or search_query in contact[1].lower()]
        if not matching_contacts:
            print("No matching contacts found!")
        else:
            print("\nSearch Results:")
            for contact in matching_contacts:
                print(f"{contact[0]} - {contact[1]}")

    elif option == 4:
        print("\nContact List:")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact[0]} - {contact[1]}")
        contact_index = int(input("Enter the index of the contact to update: ")) - 1
        if contact_index < 0 or contact_index >= len(contact_list):
            print("Invalid contact index!")
            continue
        contact = contact_list[contact_index]
        while True:
            update_field = input("Enter the field to update (name, phone, email, address): ").lower()
            if update_field == "name":
                contact[0] = input("Enter the new name: ").title()
            elif update_field == "phone":
                contact[1] = input("Enter the new phone number: ")
            elif update_field == "email":
                contact[2] = input("Enter the new email address: ")
            elif update_field == "address":
                contact[3] = input("Enter the new address: ")
            else:
                print("Invalid field! Please try again!")
                continue
            print("Contact updated successfully!")
            break

    elif option == 5:
        print("\nContact List:")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact[0]} - {contact[1]}")
        contact_index = int(input("Enter the index of the contact to delete: ")) - 1
        if contact_index < 0 or contact_index >= len(contact_list):
            print("Invalid contact index!")
            continue
        del contact_list[contact_index]
        print("Contact deleted successfully!")

    elif option == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please try again!")
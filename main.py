contacts = []

class ContactsList:
    def __init__(self):
        print('================')
        print('  Contact List  ')
        print('================')
        self.menu()

    def menu(self):
        print('please make a selection')
        print('1) View Contacts')
        print('2) Add Contact')
        print('3) Delete Contact')
        print('4) Print')
        print('5) Exit')
        user_input = eval(input())
        self.menu_switch(user_input)

    def menu_switch(self, user_input):
        if user_input == 1:
            self.view()
        elif user_input == 2:
            self.add_contact()
        elif user_input == 3:
            self.delete_contact()
        elif user_input == 4:
            self.print_contacts()
        elif user_input == 5:
            print('Goodbye')
            exit()
        else:
          print('Invalid Input')
          self.menu()

    def view(self):
        global contacts
        for index, contact in enumerate(contacts):
            new_contact = enumerate(contact['first_name'])
            print(new_contact)
    
    def add_contact(self):
        global contacts
        contact = {
            'first_name': '', 
            'last_name': '', 
            'phone': '',
            'address': '',
            'note': '',
        }
        contact['first_name'] = input('First Name:')
        contact['last_name'] = input('Last Name:')
        contact['phone'] = input('Phone:')
        contact['address'] = input('Address:')
        contact['note'] = input('Notes:')
        print('Do you wish to save this contact? y/n')
        self.contact_review(contact)
        save_contact = input('(y/n)')
        save_contact = save_contact.lower()
        if save_contact == 'y':
            print('Your contact has been saved')
            contacts.append(contact)
            contact = {}
            self.menu()
        elif save_contact == 'n':
            print('Contact has been deleted')
            contact = {}
            self.menu()
        else:
            print('Invalid Input')
            self.menu()

    def contact_review(self, contact):
        print(f"First Name:{contact['first_name']}")
        print(f"Last Name:{contact['last_name']}")
        print(f"Phone:{contact['phone']}")
        print(f"Address:{contact['address']}")
        print(f"Notes:{contact['note']}")

contact_list = ContactsList()
contact_list.menu()

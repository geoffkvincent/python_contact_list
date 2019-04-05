  # import pdb; pdb.set_trace()
from termcolor import colored, cprint
contacts = [
    {'first_name': 'Geoff', 'last_name': 'Vincent', 'phone': '555-1234', 'note': 'not a very cool guy' },
    {'first_name': 'Mike', 'last_name': 'Coker', 'phone': '535-1234', 'note': 'very cool guy' },
    {'first_name': 'Max', 'last_name': 'Crebs', 'phone': '595-1254', 'note': 'very cool guy' },
]

class ContactsList:
    def __init__(self):
        cprint('========================', 'magenta')
        cprint('      Contact List  ', 'magenta')
        cprint('========================', 'magenta')
        self.menu()

    def menu(self):
        cprint('Please make a selection:', 'yellow')
        cprint('========================', 'magenta')
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
        cprint('=========================', 'magenta')
        print('Enter index to see details')
        for index, contact in enumerate(contacts, start=1):
            print(index, contact['first_name'])
        user_input = int(input())
        for index, contact in enumerate(contacts, start=1):
            if index == user_input:
                for i in contact:
                    cprint('=========', 'magenta')
                    print(contact[i])
                    cprint('=========', 'magenta')
    
    def add_contact(self):
        global contacts
        contact = {
            'first_name': '', 
            'last_name': '', 
            'phone': '',
            'note': '',
        }
        contact['first_name'] = input('First Name:')
        contact['last_name'] = input('Last Name:')
        contact['phone'] = input('Phone:')
        contact['note'] = input('Notes:')
        print('=====================================')
        print('Do you wish to save this contact? y/n')
        print('=====================================')
        self.contact_review(contact)
        save_contact = input('(y/n)')
        save_contact = save_contact.lower()
        if save_contact == 'y':
            print('===========================')
            print('Your contact has been saved')
            print('===========================')
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
        print(f"Notes:{contact['note']}")

contact_list = ContactsList()
contact_list.menu()

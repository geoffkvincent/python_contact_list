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
        print('3) Print')
        print('4) Exit')
        cprint('=========================', 'magenta')
        user_input = int(input())
        cprint('=========================', 'magenta')
        self.menu_switch(user_input)

    def menu_switch(self, user_input):
        if user_input == 1:
            self.view()
        elif user_input == 2:
            self.add_contact()
        elif user_input == 3:
            self.print_contacts()
        elif user_input == 4:
            print('Goodbye')
            exit()
        else:
          cprint('Invalid Input', 'red')
          self.menu()

    def view(self):
        global contacts
        cprint('Enter index to see details', 'yellow')
        cprint('=========================', 'magenta')
        for index, contact in enumerate(contacts, start=1):
            name = contact['first_name']
            print(f"{index}. {name}")
        cprint('=========================', 'magenta')
        user_input = int(input())
        cprint('=========================', 'magenta')
        for index, contact in enumerate(contacts, start=1):
            if index == user_input:
                contact_select = contact
                for i in contact_select:
                    print(contact[i])
                cprint('==========================', 'magenta')
                cprint('1) Edit  2) Delete  3) Menu', 'yellow')
                cprint('==========================', 'magenta')
                view_option = int(input('Enter the number of desired option: '))
                self.view_switch(view_option, contact_select)

    def view_switch(self, view_option, contact_select):
        if view_option == 1:
            self.edit_contact(contact_select)
        elif view_option == 2:
            self.delete_contact(contact_select)
        elif view_option == 3:
            self.menu()
        else:
            cprint('Invalid Input', 'red')
            self.menu()

    def edit_contact(self, contact_select):
        cprint('=========================', 'magenta')
        cprint('Enter index to edit field', 'yellow')
        cprint('=========================', 'magenta')
        contact_select = contact_select.items()
        for index, (k,v) in enumerate(contact_select, 1):
            print(f"{index}.{k}: {v}")
        edit_option = int(input())
        for index, (k,v) in enumerate(contact_select, 1):
            if index == edit_option:
                edit_select = f"{k}: {v}"
                print(edit_select)
                contact_update = input('Enter updated info:')
                contact_select['k'] = contact_update

    def delete_contact(self, contact_select):
        print(contact_select)
                
    def add_contact(self):
        global contacts
        contact = {
            'first_name': '', 
            'last_name': '', 
            'phone': '',
            'note': '',
        }
        cprint('=====================================','magenta')
        contact['first_name'] = input('First Name:')
        contact['last_name'] = input('Last Name:')
        contact['phone'] = input('Phone:')
        contact['note'] = input('Notes:')
        cprint('=====================================', 'magenta')
        cprint('Do you wish to save this contact? y/n', 'yellow')
        cprint('=====================================', 'magenta')
        self.contact_review(contact)
        save_contact = input('(y/n)')
        save_contact = save_contact.lower()
        if save_contact == 'y':
            cprint('===========================', 'magenta')
            print('Your contact has been saved')
            cprint('===========================', 'magenta')
            contacts.append(contact)
            contact = {}
            self.menu()
        elif save_contact == 'n':
            cprint('Contact has been deleted', 'red')
            contact = {}
            self.menu()
        else:
            cprint('Invalid Input', 'red')
            self.menu()

    def contact_review(self, contact):
        print(f"First Name:{contact['first_name']}")
        print(f"Last Name:{contact['last_name']}")
        print(f"Phone:{contact['phone']}")
        print(f"Notes:{contact['note']}")

contact_list = ContactsList()
contact_list.menu()

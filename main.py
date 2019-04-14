  # import pdb; pdb.set_trace()
from termcolor import colored, cprint
contacts = [
    {'first_name': 'Geoff', 'last_name': 'Vincent', 'phone': '555-1234', 'note': 'not a very cool guy' },
    {'first_name': 'Mike', 'last_name': 'Coker', 'phone': '535-1234', 'note': 'very cool guy' },
    {'first_name': 'Max', 'last_name': 'Crebs', 'phone': '595-1254', 'note': 'very cool guy' },
]
import time
import os

class ContactsList:
    def __init__(self):
        self.menu()

    def menu(self):
        os.system('clear')
        cprint('========================', 'magenta')
        cprint('      Contact List  ', 'magenta')
        cprint('========================', 'magenta')
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
            time.sleep(1)
        elif user_input == 2:
            self.add_contact()
        elif user_input == 3:
            self.print_contacts()
        elif user_input == 4:
            cprint('Goodbye', 'yellow')
            exit()
        else:
          cprint('Invalid Input', 'red')
          self.menu()

    def view(self):
        os.system('clear')
        global contacts
        cprint('Enter index to see details', 'yellow')
        cprint('=========================', 'magenta')
        for index, contact in enumerate(contacts, start=1):
            name = contact['first_name']
            print(f"{index}) {name}")
        back_option = index +1
        cprint(f'{back_option}) Back', 'yellow')
        cprint('=========================', 'magenta')
        user_input = int(input())
        cprint('=========================', 'magenta')
        if user_input == back_option:
            self.menu()
        for index, contact in enumerate(contacts, start=1):
            if index == user_input:
                contact_select = contact
                for i in contact_select:
                    print(contact[i])
                cprint('==========================', 'magenta')
                cprint('1) Edit  2) Delete  3) Menu', 'yellow')
                cprint('==========================', 'magenta')
                view_option = int(input('Enter index of desired option: '))
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
        os.system('clear')
        cprint('=========================', 'magenta')
        cprint('Enter index to edit field', 'yellow')
        cprint('=========================', 'magenta')
        for index, (k, v) in enumerate(contact_select.items(), 1):
            print(f"{index}) {k}:  {v}")
        cprint('=========================', 'magenta')
        edit_option = int(input())
        cprint('=========================', 'magenta')
        for index, (k,v) in enumerate(contact_select.items(), 1):
            if index == edit_option:
                edit_select = f"{k}: {v}"
                print(edit_select)
                contact_update = input('Enter updated info:')
                cprint('=========================', 'magenta')
                cprint(f"{v} has been updated to {contact_update}.", 'yellow')
                cprint('=========================', 'magenta')
                edit_confirm = input('Save changes? (y/n) : ')
                if edit_confirm == 'y':
                    cprint('=========================', 'magenta')
                    contact_select[f"{k}"] = contact_update
                    print("Your contact has been updated")
                    cprint('=========================', 'magenta')
                    self.view()
                elif edit_confirm == 'n':
                    cprint('=========================', 'magenta')
                    print('Update disregarded')
                    cprint('=========================', 'magenta')
                    self.view()
                else:
                    cprint('=========================', 'magenta')
                    cprint('Invalid Input', 'red')
                    self.edit_contact(contact_select)

    def delete_contact(self, contact_select):
        os.system('clear')
        global contacts
        cprint('Are you sure?(y/n): ', 'red')
        delete_confirm = input()
        if delete_confirm == 'y':
            contacts.remove(contact_select)
            cprint('Your contact has been deleted', 'red')
        elif delete_confirm == 'n':
            self.view()
        else:
            cprint('Invalid Input', 'red')
            self.view()

                
    def add_contact(self):
        os.system('clear')
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
        cprint('=====================================', 'magenta')
        cprint('Do you wish to save this contact? y/n', 'yellow')
        cprint('=====================================', 'magenta')
        self.contact_review(contact)
        save_contact = input('(y/n)')
        save_contact = save_contact.lower()
        if save_contact == 'y':
            cprint('====================', 'magenta')
            print('Your contact has been saved')
            cprint('====================', 'magenta')
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

    def print_contacts(self):
        os.system('clear')
        global contacts
        file = open('contacts.txt', 'w+')
        confirm = input('Print contacts?(y/n): ')
        if confirm == 'y':
            for contact in contacts:
                for c in contact:
                    file.write(f'{contact[c]}\n')
                file.write('\n')
                file.write('\n')
            file.close()
            cprint('Contacts printed.')
            cprint('====================', 'magenta')
            cprint('1) View file\n2) Delete file\n3) Menu', 'yellow')
            cprint('====================', 'magenta')
            user_input = int(input())
            cprint('====================', 'magenta')
            if user_input == 1:
                os.system('open contacts.txt')
                self.menu()
            elif user_input == 2:
                os.remove('contacts.txt')
                cprint('File has been deleted', 'red')
                self.menu()
            elif user_input == 3:
                self.menu()
            else:
                cprint('Invalid Input', 'red')
                self.menu()
        else:
            self.menu()

contact_list = ContactsList()
contact_list.menu()



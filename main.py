contacts = []
contact = {}

class Contacts:
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
        user_input = input()
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
            exit()
        else:
          print('Invalid Input')
          self.menu()


    def view(self):
    
    def add_contact(self):
        global contact['first_name'] = input('First Name:')
        global contact['last_name'] = input('Last Name:')
        global contact['phone'] = input('Phone:')
        global contact['address'] = input('Address:')
        global contact['notes'] = input('Notes:')
        print('Do you wish to save this contact? y/n')
        save_contact = input()
        

    def delete_contact(self):

    def print_contacts(self):



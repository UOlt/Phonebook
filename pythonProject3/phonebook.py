# Найти контакт, удалить контакт, добавить контакт, показать все контакты
# Найти контакт по имени и фамилии и номеру телефону
class Contacts:                         # Creating class
    def __init__(self):                 # Constructing model phonebook's
        self.phonebook = []             # Creating list of contacts

    def contactcreate(self, name, surname, phonenumber):            # Creating method
        contact = [name, surname, phonenumber]                      # Creating list of forms creating contacts
        self.phonebook.append(contact)                              # Adding contact in end phonebook

    def contactnumremoving(self, phonenumber):
        for contact in self.phonebook:
            if contact[2] == phonenumber:
                self.phonebook.remove(contact)

    def printcontacts(self):                                        # Creating method
        for contact in self.phonebook:                              # Creating cycle in self.phonebook
            print(contact[0] + ' ' + contact[1] + ' ' + contact[2]) # Showing all contacts

    def foundcontactname(self, name):           # Creating method
        countc = 0                              # Creating variable 'countc' to score contacts
        for contact in self.phonebook:          # Creating cycle in self.phonebook ) In cycle creating variable contact
            if name == contact[0]:              # Condition
                countc = countc + 1             # Increase variable 'countc' to 1
                print(contact[0] + " " + contact[1] + " " + contact[2])     # Showing contacts
        if countc == 0:
            print('No contact...')  # Printing report: Contact not found

    def foundcontactsurname(self, surname):
        countc = 0
        for contact in self.phonebook:
            if surname == contact[1]:
                countc = countc + 1
                print(contact[0] + " " + contact[1] + " " + contact[2])  # Showing contacts
        if countc == 0:
            print('No contact...')

    def foundcontactnumber(self, phonenumber):
        countc = 0
        for contact in self.phonebook:
            if phonenumber == contact[2]:
                countc = countc + 1
                print(contact[0] + " " + contact[1] + " " + contact[2])  # Showing contacts
        if countc == 0:
            print('No contact...')

contacts = Contacts()       # Creating examplyare class
#contacts.contactcreate('Andrey', 'Shamanov', '89643781390')
#contacts.contactcreate('Nikita', 'Gerferipov', '89257036358')
#contacts.contactcreate('Possiuuys', 'Tiktoker', '1246488558')
#contacts.contactcreate('Floppa', 'Tiktoker', '837184747374')
#contacts.foundcontactnumber('837184747374')
#contacts.foundcontactsurname('Tiktoker')

print('Welcome to Phonebook CNS!')          # Printing welcome alert

while True:         # Infinity cycle
    command = input('Choose 1 is 4 actions: create, found, delete, exit\n')         # Input: Choose action
    if command.upper() == 'CREATE':         # Condition
        command1 = input('To create contact: <name> <surename> <phoneNumber>\n')          # Input: Format create contact and saving text, for typed user
        newcn = command1.split(' ')
        contacts.contactcreate(newcn[0], newcn[1], newcn[2])
        print('Contact successefly created!')

    # Found contact:
    elif command.upper() == 'FOUND':
        command2 = input('To found contact write contact phone number\n')
        contacts.foundcontactnumber(command2)

    # Delete contact:
    elif command.upper() == 'DELETE':
        command3 = input('To delete contact write contact phone number\n')
        contacts.contactnumremoving(command3)
        print('Contact successefly deleted!')

    # Exit program:
    elif command.upper() == 'EXIT':
        command4 = input('Do you want are sure to quit from program?(Y-yes, N-no)\n')
        if command4.upper() == 'Y':
            exit()
        else:
            print('Exit canceled')
            continue
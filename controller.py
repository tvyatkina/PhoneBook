
from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
import Model
import View

def greeting():
    print("Здравствуйте!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    father_name = input("Введите отчество: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, father_name, phone_number, note]

sep = ";"

def choice_todo():
    print("Что делаем:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - удаление контакта;\n\
    4 - изменение контакта;\n\
    5 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        import_data(input_data(), sep)
    elif ch == '2':
        contacts = export_data()
        print_data(contacts)
    elif ch == '3':
        contacts = remove_contact()
        print('\nКонтакт удален\n')
    elif ch == '4':
        contacts = change_contact()
    else:
        word = input("Введите данные для поиска: ")
        contacts = export_data()
        item = search_data(word, contacts)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*105)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(15), item[4].center(30))
        else:
            print("Данные не обнаружены")

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-фамилия, 1-имя, 2-отчество, 3-телефон, 4-примечание): '))

    contact = Model.phonebook.pop(choice)
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()
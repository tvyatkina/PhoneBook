# модуль экспорта данных 
import Model

def export_data():
    with open(Model.path, 'r') as data:
        contacts = []
        t = []
        for line in contacts:
            if ';' in line:
                temp = line.strip().split(';')
                contacts.append(temp)    
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    contacts.append(t)
                    t= []
    return contacts
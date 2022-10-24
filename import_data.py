# модуль 
import Model

def import_data(contacts, sep=None):
    with open(Model.path, 'w') as data:
        if sep == None:
            for i in contacts:
                data.write(f"{i}\n")
            data.write(f"\n")
        else:
            data.write(sep.join(data))
            data.write(f"\n")
# модуль экспорта данных 
import Model

def export_data():
    with open(Model.path, 'r') as file:
        data = []
        t = []
        for line in file:
            if ';' in line:
                temp = line.strip().split(';')
                data.append(temp)    
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data
import csv 

def read_csv(path):
    with open(path, 'r') as csvfile: # se abre el doc con permiso de solo lectura
        reader = csv.reader(csvfile, delimiter=',') # la manera de crear un lector
        header = next(reader) # aqui se consigue el nombre de las columnas (la primer fila)
        data = [] # se crea para guardar los diccionarios q se crean en la linea 10
        for row in reader: # leer fila por fila / renglon por renglon
            iterable = zip(header, row) # unir columna y fila
            country_dict = {key: value for key, value in iterable} # se transforma a una lista de diccionarios
            data.append(country_dict)
        return data
            


if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data[0])

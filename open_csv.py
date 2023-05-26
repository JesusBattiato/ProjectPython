import csv

def read_csv(path, delim):
    with open(path, 'r',encoding='UTF8') as csvfile:
        reader = csv.reader(csvfile, delimiter = delim)
        if path == './inflacionMundial.csv': #este archivo tiene un decodificacion diferente y de esta forma logre que funcione el codigo
            i = 0
            while i < 5: #filas vacias en el archivo
                header = next(reader)
                i = i+1
        else:
            header = next(reader)
        
        data = []
        for row in reader:
            
            iter = zip(header, row)
            
            dict = {key: value for key,value in iter } 
            data.append(dict)
    return data
        

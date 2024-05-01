import csv
import os

# Obtener el directorio actual
current_directory = os.getcwd()

# Ruta relativa al archivo usuarios.csv dentro de la carpeta data
file_path = os.path.join(current_directory, 'data', 'usuarios.csv')


def register(name, email, password):
    # Guardar los datos en un archivo CSV
    with open(file_path, mode='r', newline='') as users:
        reader = csv.reader(users)
        for row in reader:
            if email == row[1]:
                return [False]
        else: 
            if name and email and password != '':
                access = True
            else:
                access = False
            if access:
                    with open('usuarios.csv', mode='a', newline='') as users:
                            writer = csv.writer(users)
                            writer.writerow([name, email.lower(), password])
                            return [True, access]
            else:
                users.close()
                return [True, access]

            
def login(email, password):
    # Verificar las credenciales en el archivo CSV
    with open(file_path, mode='r', newline='') as users:
        reader = csv.reader(users)
        for row in reader:
            if email == row[1] and password == row[2]:
                users.close()
                return True
        else:
            users.close()
            return False

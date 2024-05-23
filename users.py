#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MODULO DE USUARIOS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import csv
import os

# Obtener el directorio actual
current_directory = os.getcwd()

# Registro de usuarios
def register(name, email, password):
    """Save the user data in the CSV file to complete the register.

    Args:
        name (str): User name to register
        email (str): User email to register
        password (str): User password to register

    Returns:
        list : [True, True] if the data is saved successfully
        list : [True, False] if the data is not saved successfully
        list : [False] if the email is already registered
    """
    # Especiicar la ruta relativa al archivo users.csv 
    file_path = os.path.join(current_directory, 'data', 'db', 'users.csv')
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
                    with open(file_path, mode='a', newline='') as users:
                            writer = csv.writer(users)
                            writer.writerow([name, email.lower(), password])
                            users.close()
                    with open(os.path.join(current_directory, 'data', 'db', 'usersData.csv'), mode='a', newline='') as users:
                            writer = csv.writer(users, delimiter=';')
                            writer.writerow([name, email.lower(), 'N/A', 'N/A', 'N/A'])
                            users.close()
                            return [True, access]
            else:
                users.close()
                return [True, access]

# Inicio de sesión
def login(email, password):
    """Check the credentials in the CSV file to auth the login.

    Args:
        email (str): User email
        password (str): User password

    Returns:
        True : if the credentials are correct
        False : if the credentials are incorrect
    """
    # Especificar la ruta relativa al archivo users.csv
    file_path = os.path.join(current_directory, 'data', 'db', 'users.csv')
    # Verificar las credenciales en el archivo CSV
    with open(file_path, mode='r', newline='') as users:
        reader = csv.reader(users)
        for row in reader:
            if email == row[1] and password == row[2]:
                users.close()
                return True, row[0]
        else:
            users.close()
            return False, None

# Actualizar datos del perfil de usuario
def update_profile_data(name, email, cellphone, address, ocupation):
    """Update user data in the CSV file based on the email provided.

    Args:
        name (str): New user name
        email (str): User email
        cellphone (str): New user cellphone
        address (str): New user address
        ocupation (str): New user ocupation or set user ocupation

    Returns:
        True : if the data is updated successfully
    """
    # Especificar la ruta relativa al archivo userData.csv
    file_path = os.path.join(current_directory, 'data', 'db', 'usersData.csv')
    with open(file_path, mode='r', newline='') as users:
        reader = csv.reader(users, delimiter=';')
        data = list(reader)
        # Buscar el correo electrónico en el archivo CSV
        for row in data:
            if email == row[1]:
                if name:
                    row[0] = name
                if cellphone:
                    row[2] = cellphone
                if address:
                    row[3] = address
                if ocupation:
                    row[4] = ocupation
                break
            else:
                continue
        # Actualizar los datos en el archivo CSV
        with open(file_path, mode='w', newline='') as users:
            writer = csv.writer(users, delimiter=';') # Especificar el delimitador
            writer.writerows(data)
            return True
        
# Obtener datos del perfil de usuario
def get_user_data(email):
    """Get user data from the CSV file based on the email provided.

    Args:
        email (str): user email

    Returns:
        row : list with the user data if the email is found
        None : if the email is not found
    """
    # Especificar la ruta relativa al archivo userData.csv
    file_path = os.path.join(current_directory, 'data', 'db', 'usersData.csv')
    # Abrir el archivo CSV y buscar el correo electrónico
    with open(file_path, mode='r', newline='') as users:
        reader = csv.reader(users, delimiter=';') # Especificar el delimitador
        for row in reader:
            if email == row[1]:
                users.close()
                return row # Devolver los datos del usuario
        else:
            users.close()
            return None

def get_img_status(email):
    if email:
        file_path = os.path.join(current_directory, 'data', 'images', f'{email}.png')
        if os.path.exists(file_path):
            return True
        else:
            return False
    else:
        return False

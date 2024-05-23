import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import numpy as np

def file_path(carpeta = None, archivo = None):
    # Obtener el directorio actual
    current_directory = os.getcwd()
    carpeta = carpeta.lower()
    archivo = archivo.lower()
    if carpeta and archivo:
        if type(carpeta) == str or type(archivo) == str:
            file_path = os.path.join(current_directory, 'data' , carpeta, archivo)
            return file_path
    
def load_data():
    df = pd.read_csv(file_path('db', 'usersData.csv'), delimiter=';', index_col=0)
    return df

def get_jobs_data():
    df = load_data()
    jobs_list = df['job'].tolist()
    new_jobs_list = [element.lower() for element in jobs_list]
    return new_jobs_list

def count_jobs():
    jobs_list = get_jobs_data()
    jobs_dict = {}
    for job in jobs_list:
        if job not in jobs_dict:
            jobs_dict[job] = 1
        else:
            jobs_dict[job] += 1
    return jobs_dict

def exportGraphics(choice, create_img=False):
    """La función exportGraphic genera una gráfica según la elección del usuario

    Args:
        choice (str): Será la elección del usuario pasada desde el front-end
        create_img (bool): Indicador para crear o no la imagen

    Returns:
        3 valores : 
        - Verdadero si no hubo problemas de comunicación, 
        - Verdadero si la imagen se genera, 
        - Ruta de la imagen generada
    """

    if choice == '1':
        jobs_dict = count_jobs()
        jobs = list(jobs_dict.keys())
        values = list(jobs_dict.values())
        file = file_path('images', 'Occupations.png')
        # Make a graphic with the occupations of the users
        if create_img:
            plt.figure(figsize=(12, 7))
            sns.set_theme(style='darkgrid')
            sns.barplot(x=jobs, y=values, palette='viridis', width=0.3)
            plt.title('Ocupaciones de los usuarios')
            plt.ylabel('Cantidad de usuarios')
            plt.xticks(rotation=0)
            plt.savefig(file)  
            return True, True, file
        else:
            return True, False, file  # Asegurarse de que siempre se retorne la ruta del archivo
    
    elif choice == '2':
        df = load_data()
        users_list = df['email'].tolist()
        number_of_users = len(users_list)
        file = file_path('images', 'NumberOfUsers.png')
        # Make a graphic with the number of registered users
        if create_img:
            x = ['Minimo de usuarios', 'Media de usuarios', 'Maximo de usuarios']
            y = [0, number_of_users / 2, number_of_users]
            plt.plot(x, y, linewidth=5, color='#4CAF50')
            plt.title('Número de usuarios registrados')
            plt.grid(axis='y')
            plt.savefig(file)
            return True, True, file  # Ajustar el retorno para incluir siempre la ruta del archivo
        else:
            return True, False, file
    
    else:
        return False, False, None
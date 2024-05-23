#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MODULO DE TRABAJOS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import json

# Obtener el directorio actual
current_directory = os.getcwd()

# Ruta relativa al archivo data.json dentro de la carpeta data
file_path = os.path.join(current_directory, 'data' , 'db', 'data.json')
    
def load_data():
    """Load the data from the JSON file.

    Returns:
        dict : data from the JSON file
    """
    # Cargar el JSON con los datos de los trabajos
    data = json.load(open(file_path, encoding='utf-8'))
    return data

def unzip_data():
    """Unzip the data from the JSON file.

    Returns:
        dict : dict of jobs from the JSON file
    """
    trabajos = load_data()["jobs"]
    dict_trabajos = trabajos[0]
    return dict_trabajos

def get_keys():
    """Get the keys from the JSON file.

    Returns:
        list : list of keys of the jobs dict from the JSON file
    """
    # Establecer las claves del JSON
    json_keys = []
    data = unzip_data()
    for key in data:
        if key not in json_keys:
            json_keys.append(key)
    return json_keys

def get_job_category(category: str):
    """Get the job category from the input.

    Args:
        category (str): user input for the job category search

    Returns:
        str : job category
        None : if the category is not found
    """
    category_lower = category.lower()
    if category_lower in ['software', 'desarollo', 'programacion', 'developer', 'programador']:
        return "software"
    elif category_lower in ['arquitectura', 'arquitecto', 'diseño', 'construccion', 'arquitecta', 'diseñadora', 'constructora']:
        return "arquitectura"
    elif category_lower in ['ingenieria', 'ingeniero', 'engineer', 'ingeniera', 'civil', 'ingeniero civil', 'ingeniera civil', 'ingeniero mecanico', 'ingeniera mecanica', 'ingeniero electromecanico', 'ingeniera electromecanica', 'ingeniero industrial', 'ingeniera industrial', 'ingeniero quimico', 'ingeniera quimica']:
        return "ingenieria"
    elif category_lower in ['rrhh', 'recruiter', 'recursos humanos', 'reclutador', 'human resources', 'rrhh', 'rh', 'it recruiter', 'recruiter it', 'recruiter rrhh', 'recruiter recursos humanos', 'reclutadora', 'profesor', 'docente', 'docente universitario', 'docente secundario', 'docente primario', 'docente inicial', 'docente de idiomas', 'docente de matematicas', 'docente de historia', 'docente de geografia', 'docente de literatura', 'docente de fisica', 'docente de quimica', 'docente de biologia', 'docente de educacion fisica', 'docente de educacion artistica', 'docente de educacion sexual', 'docente de educacion civica', 'docente de educacion etica', 'docente de educacion ciudadana', 'catedratico', 'catedratica']:
        return "rrhh"
    elif category_lower in ['medicina', 'doctor', 'medico', 'enfermero', 'enfermera', 'cirujano', 'medico general', 'medica general', 'medico clinico', 'medica clinica', 'medico pediatra', 'medica pediatra', 'medico traumatologo', 'medica traumatologa', 'medico oftalmologo', 'medica oftalmologa', 'medico ginecologo', 'medica ginecologa', 'medico obstetra', 'medica obstetra', 'medico cirujano', 'cardiologo', 'cardiologa', 'neurologo', 'neurologa', 'neurocirujano', 'neurocirujana', 'neurologo infantil', 'neurologa infantil', 'neurologo adulto', 'neurologa adulta', 'neurologo geriatrico', 'neurologa geriatrica', 'neurologo clinico', 'neurologa clinica', 'neurologo hospitalario', 'neurologa hospitalaria', 'neurologo pediatra', 'neurologa pediatra', 'residente', 'residenta', 'medico residente', 'medica residente', 'residente de medicina', 'residenta de medicina', 'residente de enfermeria', 'residenta de enfermeria', 'residente de cirugia', 'residenta de cirugia', 'residente de cardiologia', 'residenta de cardiologia', 'residente de neurologia', 'residenta de neurologia', 'residente de neurocirugia', 'residenta de neurocirugia']:
        return "medicina"
    elif category_lower in ['marketing', 'marketing digital', 'marketing online', 'marketing de contenidos', 'marketing estrategico', 'marketing de productos', 'marketing de servicios', 'marketing de marca', 'marketing de empresa', 'marketing de negocio', 'marketing de ventas', 'marketing de publicidad', 'marketing de promocion', 'marketing de posicionamiento', 'marketing de marca', 'marketing de empresa', 'marketing de negocio', 'marketing de ventas', 'marketing de publicidad', 'marketing de promocion', 'marketing de posicionamiento', 'marketing de marca', 'marketing de empresa', 'assistant', 'asistente', 'asistente administrativo', 'asistente de direccion', 'asistente de gerencia', 'asistente de marketing', 'asistente de ventas', 'asistente de publicidad', 'asistente de promocion', 'asistente de posicionamiento', 'asistente de marca', 'asistente de empresa', 'influencer', 'influencer de marca', 'influencer de empresa', 'influencer de negocio', 'influencer de ventas', 'influencer de publicidad', 'influencer de promocion', 'influencer de posicionamiento', 'influencer de marca', 'influencer de empresa', 'influencer de negocio', 'influencer de ventas', 'influencer de publicidad', 'influencer de promocion', 'influencer de posicionamiento', 'influencer de marca', 'influencer de empresa', 'influencer de negocio', 'seo', 'sem', 'smm', 'smo', 'manager', 'community manager', 'social media manager', 'bussines manager', 'marketing manager', 'marketing digital manager', 'marketing online manager', 'marketing de contenidos manager', 'marketing estrategico manager', 'marketing de productos manager', 'especialista', 'especialista en marketing', 'especialista en marketing digital', 'especialista en marketing online', 'especialista en marketing de contenidos', 'especialista en marketing estrategico', 'especialista en marketing de productos', 'especialista en marketing de servicios', 'especialista en marketing de marca', 'especialista en marketing de empresa', 'especialista en marketing de negocio', 'especialista en marketing de ventas', 'especialista en marketing de publicidad']:
        return "marketing"
    else:
        return None
    
def get_job_data(categoria: str):
    """Get the job data from the JSON file based on the category provided.

    Args:
        categoria (str): job category

    Returns:
        list : list of jobs from the JSON file based on the category provided
    """
    # Cargar el JSON con los datos de los trabajos
    data = unzip_data()
    keys = get_keys()
    for key in keys:
        if categoria == key:
            return data[key]  # Devolver los trabajos de la categoría especificada

def create_json(categoria):
    """Create a JSON file with the jobs of the specified category.

    Args:
        categoria (str): job category
    """
    # Crear un archivo JSON con los trabajos de la categoría especificada
    # Crear la ruta completa al archivo dentro de la carpeta "data"
    files_path = os.path.join(os.getcwd(), 'data', 'json')
    os.makedirs(files_path, exist_ok=True)  # Crear la carpeta si no existe
    file_path = os.path.join(files_path, f"{categoria}.json")
    # Guardar la lista como JSON en el archivo especificado
    with open(file_path, "w", encoding='utf-8') as outfile:
        json.dump(get_job_data(categoria), outfile, indent=4)
    print(f"JSON guardado exitosamente como {categoria}.json.")

def create_json_files():
    """Create JSON files with the jobs of each category."""
    # Crear archivos JSON con los trabajos de cada categoría
    categorias = ["software", "arquitectura", "ingenieria", "rrhh", "medicina", "marketing"]
    for categoria in categorias:
        create_json_files(categoria)

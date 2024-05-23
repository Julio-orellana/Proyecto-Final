import users
import jobs
import data
import os
import json
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'b_5#y2L"F4Q8z@n\xec]/'  # Clave secreta para la cookie de sesión

# Rutas para renderizar las páginas HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def app_page():
    if 'email' in session:  # Verificar si el usuario está autenticado
        if session['email'] == "admin@correo.com":
            return render_template('app.html', admin=True)
        else:
            return render_template('app.html', admin=False)
    else:
        return redirect(url_for('login_page'))  # Redirigir al inicio de sesión si no está autenticado

@app.route('/login')
def login_page():
    return render_template('login.html')

# Ruta para manejar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulariO
    email = request.form.get('email')
    password = request.form.get('password')

    login_successful, user_name = users.login(email.lower(), password)
    # Verificar las credenciales
    if login_successful:
        session['email'] = email  # Establecer la cookie de sesión
        session['name'] = user_name
        return redirect(url_for('app_page'))  # Redirigir a la página principal
    else:
        error_message = "Credenciales incorrectas. Intente de nuevo."
        return render_template("login.html", error=error_message)

# Ruta para manejar el registro de usuarios
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    register_successful = users.register(name, email.lower(), password)

    if register_successful[0]:
        # Establecer la cookie de sesión
        session['email'] = email
        session['name'] = name
        # Enviar una respuesta JSON al frontend
        if register_successful[1]:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Todos los campos son requeridos'})
    else:
        return jsonify({'success': False, 'message': 'El correo electronico ya está registrado'})

# Ruta para cerrar sesión
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('email', None)  # Eliminar la cookie de sesión
    session.pop('name', None)
    return redirect(url_for('index'))  # Redirigir al inicio o a la página que desees

@app.route('/profile')
def profile():
    if 'email' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('login_page'))

# Ruta para enviar los datos de los trabajos
@app.route('/app', methods=['POST'])
def send_job_data():
    """Send the job data to the frontend.

    Returns:
        json : if the user has already signed in send the job data to the frontend
    """
    # Verificar si el usuario está autenticado
    if 'email' in session:
        category = request.form.get('searchInput')
        key = jobs.get_job_category(category)
        # Realizar validaciones para enviar los datos de los trabajos en formato JSON
        if key == 'software':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        elif key == 'arquitectura':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        elif key == 'ingenieria':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        elif key == 'rrhh':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        elif key == 'medicina':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        elif key == 'marketing':
            current_directory = os.getcwd()
            file = os.path.join(current_directory, 'data', 'json', f'{key}.json')
            data = jobs.get_job_data(key)
            print(f'Enviando {key}.json a la app')
            with open(file, 'r') as f:
                trabajos = json.load(f)
            return jsonify(trabajos)
        else:
            return "Categoria no encontrada"
    else:
        return redirect(url_for('login_page'))
    
# Ruta para enviar los datos del usuario
@app.route('/profile', methods=['POST'])
def send_user_data():
    """Send the user data to the frontend.

    Returns:
        json : if the user has already signed in send user data to the frontend
        redirect : if the user has not signed in redirect to the login page
    """
    if 'email' in session:
        email = session['email']
        data = users.get_user_data(email)
        return jsonify(data)
    else:
        return redirect(url_for('login_page'))

# Ruta para actualizar los datos de perfil del usuario
@app.route('/edit-profile', methods=['POST'])
def update_profile():
    """Update the user data in the CSV file based on the email provided.

    Returns:
        json : if the user has already signed in update the user data in the CSV file
        redirect : if the user has not signed in redirect to the login page
    """
    if 'email' in session:
        name = request.form.get('name')
        email = session['email']
        cellphone = request.form.get('phone')
        address = request.form.get('address')
        ocupation = request.form.get('ocupation')
        users.update_profile_data(name, email, cellphone, address, ocupation)
        print('Datos actualizados correctamente')
        return jsonify({'success': True})
    else:
        return redirect(url_for('login_page'))
    
@app.route('/show_data', methods=['POST'])
def show_data():
    """Send the user data to the frontend.

    Returns:
        json : if the user has already signed in send the user data to the frontend
        redirect : if the user has not signed in redirect to the login page
    """
    if 'email' in session:
        email = session['email']
        data = users.get_user_data(email)
        return jsonify(data)
    else:
        return redirect(url_for('login_page'))
    
@app.route('/save_cv', methods=['POST'])
def save_file():
    """Save the file in the data/pdf folder.

    Returns:
        redirect : if the file is saved correctly redirect to the profile page
    """
    email = session['email']

    # return request.files

    # Verifica si se envió un archivo en la solicitud
    if 'fileInputCv' not in request.files:
        return 'No se ha enviado ningún archivo'

    file = request.files['fileInputCv']

    # Verifica si se ha seleccionado un archivo
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No se ha seleccionado ningún archivo'})
    
    file_path = os.path.join(os.getcwd(), 'data', 'pdf', f'{email}.pdf')
    # Guarda el archivo como "email.pdf"
    print(f'Guardando archivo en {file_path}')
    file.save(file_path)
    # Redirige a la página de perfil si el archivo se guardó correctamente
    return jsonify({'success': True})

@app.route('/get_cv/<email>')
def get_cv(email):
    """Get the file from the data/pdf folder.

    Args:
        emails (str): email of the user to get the file

    Returns:
        send file : if the file is found return the file
        str : if the file is not found return a message
    """
    file_path = os.path.join(os.getcwd(), 'data', 'pdf', f'{email}.pdf')
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='application/pdf')
    else:
        return "No se encontró el archivo PDF", 404
    
@app.route('/get_user_img/<email>')
def get_user_img(email):
    """Get the image from the data/img folder.

    Args:
        emails (str): email of the user to get the image

    Returns:
        send file : if the image is found return the image
        str : if the image is not found return a message
    """

    file_path = os.path.join(os.getcwd(), 'data', 'images', f'{email}.png')
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='image/png')
    else:
        return "No se encontró la imagen", 404

# Ruta para verificar el estado de la aplicación
@app.route('/healthcheck')
def healthcheck():
    """Check the status of the application.

    Returns:
        html : the status of the application
    """
    return render_template('status.html')

# Ruta para la página de análisis de datos
@app.route('/analytics')
def analytics_page():
    if 'email' in session and session['email'] == "admin@correo.com":
        return render_template('analytics.html')
    else:
        return "<body><script>alert('No tienes permiso para acceder a esta página. Regirigiendo a la app...');\nwindow.location.href= '/app';</script>"

@app.route('/show_analytics', methods=['POST'])
def analytics():
    choice = request.form.get('userchoice')  # Obtiene la elección del usuario
    print(f'Elección del usuario: {type(choice)}')
    if choice in ['1', '2']:  # Verifica que la elección sea válida
        access, saved_img, file_path = data.exportGraphics(choice, False)  # Cambiar a True para generar la imagen
        if access:
            print(f"Archivo: {file_path}")
            if os.path.exists(file_path) and file_path.endswith('.png'):
                print(f'Enviando {file_path} a la app')
                return send_file(file_path, mimetype='image/png')
            else:
                return "No se encontró la imagen o no es un archivo PNG"
        else:
            return "No se pudo guardar la imagen"
        
    return "Opción no válida, intente de nuevo"
    
@app.route('/img_status', methods=['POST'])
def img_status():
    email = session['email']
    status = users.get_img_status(email)
    return jsonify({'status': status})

@app.route('/save_img', methods=['POST'])
def save_img():
    """Save the file in the data/images folder.

    Returns:
        redirect : if the file is saved correctly redirect to the profile page
    """
    email = session['email']
    # Verifica si se envió un archivo en la solicitud
    if 'fileInput' not in request.files:
        return 'No se ha enviado ningún archivo'

    file = request.files['fileInput']

    # Verifica si se ha seleccionado un archivo
    if file.filename == '':
        return 'No se ha seleccionado ningún archivo'
    file_path = os.path.join(os.getcwd(), 'data', 'images', f'{email}.png')
    # Guarda el archivo como "email.png"
    print(f'Guardando imagen en {file_path}')
    file.save(file_path)
    # Redirige a la página de perfil si el archivo se guardó correctamente
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True, port=1500)

import users
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'tu_clave_secreta'  # Clave secreta para la cookie de sesión

# Rutas para renderizar las páginas HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def app_page():
    if 'email' in session:  # Verificar si el usuario está autenticado
        return render_template('app.html')
    else:
        return redirect(url_for('login_page'))  # Redirigir al inicio de sesión si no está autenticado

@app.route('/login')
def login_page():
    return render_template('login.html')

# Ruta para manejar el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario
    email = request.form.get('email')
    password = request.form.get('password')

    login_successful = users.login(email.lower(), password)

    # Verificar las credenciales
    if login_successful:
        session['email'] = email  # Establecer la cookie de sesión
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
    return redirect(url_for('index'))  # Redirigir al inicio o a la página que desees

if __name__ == '__main__':
    app.run(debug=True, port=1500)

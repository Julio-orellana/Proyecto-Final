const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function login() {
    var email = document.querySelector('.form-container.sign-in input[type="email"]').value;
    var password = document.querySelector('.form-container.sign-in input[type="password"]').value;
    console.log(email, password);

    var formData = {
        email: email,
        password: password
    };

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
}

const registerForm = document.querySelector('.form-container.sign-up form');

registerForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Evitar el envío del formulario por defecto

    // Obtener los valores del formulario
    const name = document.getElementById('name').value;
    const email = document.getElementById('emailRegister').value;
    const password = document.getElementById('passwordRegister').value;

    // Crear un objeto FormData con los datos del formulario
    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('password', password);

    // Enviar los datos al backend usando fetch
    fetch('/register', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Registro exitoso. Inicie sesión para continuar.');
            window.location.href = '/login'; // Redirigir al usuario a la página de inicio de sesión
        } else {
        var message = data.message;
        alert(message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error en el servidor, Por favor vuelva a intentarlo mas tarde.');
    });
});


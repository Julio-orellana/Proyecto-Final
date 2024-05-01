document.addEventListener('DOMContentLoaded', function() {
    const logoutBtn = document.getElementById('logoutBtn');  // ID del botón de cerrar sesión en tu HTML

    logoutBtn.addEventListener('click', function() {
        // Enviar una solicitud POST para cerrar sesión
        fetch('/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            // Redirigir a la página de inicio después de cerrar sesión
            window.location.href = '/';
        })
        .catch(error => {
            console.error('Error al cerrar sesión:', error);
        });
    });
});

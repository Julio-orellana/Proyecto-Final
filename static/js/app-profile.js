document.addEventListener('DOMContentLoaded', function() {
    const editBtn = document.getElementById('editBtn');
    const editInfoContainer = document.getElementById('edit-info-container');
    const infoContainer = document.getElementById('info-container');
    const saveBtn = document.querySelector('#edit-info-container button[type="submit"]');

    // Al hacer clic en el botón Editar
    editBtn.addEventListener('click', function() {
        // Cambiar las clases para mostrar el formulario de edición y ocultar la información estática
        editInfoContainer.classList.remove('hidden');
        infoContainer.classList.add('hidden');
        infoContainer.classList.remove('visible');
    });

    // Al hacer clic en el botón Guardar
    saveBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Detener la acción predeterminada del formulario
        // Agregar lógica adicional aquí para enviar los datos del formulario mediante Fetch si es necesario
        fetch('/edit-profile', {
            method: 'POST',
            body: new FormData(editInfoContainer.querySelector('form'))
        })
        .then(response => response.text())
        .then(result => {
          //console.log(result); // Mostrar la respuesta del servidor
          window.location.href = '/profile';
        })
        .catch(error => {
         console.error('Error:', error);
         });
                 // Cambiar las clases para ocultar el formulario de edición y mostrar la información estática actualizada
        editInfoContainer.classList.add('hidden');
        infoContainer.classList.remove('hidden');
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');
    const uploadForm = document.getElementById('uploadForm');

    // Cuando se haga clic en el botón de subir
    uploadButton.addEventListener('click', function() {
        const fileInput = document.getElementById('fileInputCv')
        const files = fileInput.files;

        // console.log(files, fileInput);
        
        // Verificar si se seleccionó al menos un archivo
        if (files.length === 0) {
            alert('Por favor, seleccione al menos un archivo.');
        }

        // Crear un objeto FormData para enviar el archivo
        // const formData = new FormData(uploadForm);
        const formData = new FormData()
        formData.append('fileInputCv', files[0])

        // console.log(formData)
        
        // Lógica para enviar el formulario con el archivo adjunto
        fetch('/save_cv', {
            method: 'POST',
            body: formData
        })
        //then(response => response.text())
        .then(result => {
            //console.log(result); // Mostrar la respuesta del servidor
            window.location.href = '/profile';
        })
        .catch(error => {
            console.error('Error:', error);
          
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const editCvBtn = document.getElementById('editCvBtn');
    const cvForm = document.getElementById('cv-form');
    const cvContainer = document.getElementById('cv-container');
  
    // Al hacer clic en el botón Editar
    editCvBtn.addEventListener('click', function() {
      // Cambiar las clases para mostrar el formulario de edición y ocultar el contenedor del CV
      cvForm.classList.remove('hidden');
      cvContainer.classList.add('hidden');
      cvContainer.classList.remove('visible');
    });
  
    // Al hacer clic en el botón Subir
    const uploadButton = document.getElementById('uploadButton');
    uploadButton.addEventListener('click', function() {
      // Aquí puedes agregar tu lógica para subir el archivo seleccionado
  
      // Después de subir el archivo, puedes cambiar las clases para ocultar el formulario de edición y mostrar el contenedor del CV actualizado
      cvForm.classList.add('hidden');
      cvContainer.classList.remove('hidden');
      cvContainer.classList.add('visible');
    });
     // Al hacer clic en el botón Subir
     const cancelButton = document.getElementById('cancelButton');
     cancelButton.addEventListener('click', function() {
       // Aquí puedes agregar tu lógica para subir el archivo seleccionado
   
       // Después de subir el archivo, puedes cambiar las clases para ocultar el formulario de edición y mostrar el contenedor del CV actualizado
       cvForm.classList.add('hidden');
       cvContainer.classList.remove('hidden');
       cvContainer.classList.add('visible');
     });
  });

  document.addEventListener("DOMContentLoaded", function() {
    fetch('/show_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data) {
            document.getElementById("name-content").textContent = data[0];
            document.getElementById("email-content").textContent = data[1];
            document.getElementById("phone-content").textContent = data[2];
            document.getElementById("address-content").textContent = data[3];
            document.getElementById("ocupation-content").textContent = data[4];
        } else {
            alert('Aun no has ingresado tu información personal, por favor hazlo en la sección de editar perfil')
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.addEventListener('DOMContentLoaded', function() {
  const logoutBtn = document.getElementById('logoutBtn');  // ID del botón de cerrar sesión en tu HTML

  logoutBtn.addEventListener('click', function() {
      alert('Sesión cerrada exitosamente');  // Mostrar un mensaje de alerta al usuario
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

document.addEventListener('DOMContentLoaded', function() {
  const imgContainer = document.getElementById('upload-img-container');
  const uploadButton = document.getElementById('uploadImageButton');
  const fileInput = document.getElementById('fileInput');
  const uploadForm = document.getElementById('uploadImageForm');

  // Check the image status on load
  fetch('/img_status', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.status === false) {
          console.log(data);
          imgContainer.classList.remove('hidden');
          imgContainer.classList.add('visible');
          uploadForm.classList.remove('hidden');
          uploadForm.classList.add('visible');
      } else {
          console.log(data);
          imgContainer.classList.remove('visible');
          imgContainer.classList.add('hidden');
          uploadForm.classList.remove('visible');
          uploadForm.classList.add('hidden');
      }
  });

  // Upload image on button click
  uploadButton.addEventListener('click', function() {
      alert('Tu imagen ha sido cambiada permanentemente\nPara cambiar tu imagen de perfil, contacta a soporte tecnico.')
      const formData = new FormData();
      formData.append('fileInput', fileInput.files[0]);

      fetch('/save_img', {
          method: 'POST',
          body: formData
      })
      .then(response => response.text())
      .then(data => {
          window.location.href = '/profile';
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });
});

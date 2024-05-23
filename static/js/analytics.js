document.addEventListener('DOMContentLoaded', function() {
    const usersBtn = document.getElementById('usersBtn');
    const usersResults = document.getElementById('users-results');
    const jobsContent = document.getElementById('jobs');

    usersBtn.addEventListener('click', function(event) {
        event.preventDefault();
        usersResults.classList.remove('hidden');
        jobsContent.classList.remove('visible');
        jobsContent.classList.add('hidden');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const jobsBtn = document.getElementById('jobsBtn');
    const jobsResults = document.getElementById('jobs-results');
    const usersContent = document.getElementById('users');

    jobsBtn.addEventListener('click', function(event) {
        event.preventDefault();
        jobsResults.classList.remove('hidden');
        usersContent.classList.remove('visible');
        usersContent.classList.add('hidden');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".userchoice");
    const userChoiceInput = document.getElementById("userChoice");
    const usersResults = document.getElementById("users-results");
    const jobsResults = document.getElementById("jobs-results");
    const userform = document.querySelector(".choice");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const choice = userChoiceInput.value.trim();
        
        if (choice === "1" || choice === "2") {
            fetch("/show_analytics", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `userchoice=${choice}`
            })
            .then(response => {
                if (response.ok) {
                    return response.blob(); // Para manejar la imagen devuelta por el servidor
                } else {
                    throw new Error("Ocurrió un error en la solicitud");
                }
            })
            .then(blob => {
                const imgUrl = URL.createObjectURL(blob);
                const img = document.createElement("img");
                img.src = imgUrl;
                img.alt = "Gráfica de análisis";
                img.id = "analytics-img";

                // Limpiar resultados anteriores
                usersResults.innerHTML = "";
                jobsResults.innerHTML = "";

                if (choice === "1") {
                    usersResults.appendChild(img);
                    usersResults.classList.remove("hidden");
                    jobsResults.classList.add("hidden");
                    userform.classList.add("hidden");
                    userform.classList.remove("visible");

                    // Agregar botón de volver
                    const backButton = document.createElement("button");
                    backButton.id = "backButton";
                    backButton.textContent = "Volver";
                    backButton.addEventListener("click", function() {
                        usersResults.classList.add("hidden");
                        userform.classList.remove("hidden");
                    });
                    usersResults.appendChild(backButton);
                } else if (choice === "2") {
                    jobsResults.appendChild(img);
                    jobsResults.classList.remove("hidden");
                    usersResults.classList.add("hidden");
                    userform.classList.add("hidden");
                    userform.classList.remove("visible");

                    // Agregar botón de volver
                    const backButton = document.createElement("button");
                    backButton.textContent = "Volver";
                    backButton.id = "backButton";
                    backButton.addEventListener("click", function() {
                        jobsResults.classList.add("hidden");
                        userform.classList.remove("hidden");
                    });
                    jobsResults.appendChild(backButton);
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Hubo un problema al procesar su solicitud. Por favor, inténtelo de nuevo.");
            });
        } else {
            alert("Opción no válida, intente de nuevo");
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const backBtn = document.getElementById('backBtn');

    backBtn.addEventListener('click', function() {
        window.location.href = '/app';
    });
});




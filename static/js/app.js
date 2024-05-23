document.addEventListener('DOMContentLoaded', function() {
    const searchBtn = document.getElementById('searchBtn');
    const searchResults = document.getElementById('search-results');

    searchBtn.addEventListener('click', function(event) {
        event.preventDefault();
        searchResults.classList.remove('hidden');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const resetBtn = document.getElementById('resetBtn');
    const searchResults = document.getElementById('search-results');
    const searchContent = document.querySelector('#search-results .search-results-content');

    resetBtn.addEventListener('click', function(event) {
        event.preventDefault();
        // Clear the search results content and hide the search results section when the reset button is clicked
        while (searchContent.firstChild) {
            searchContent.removeChild(searchContent.firstChild);
        }
        searchResults.classList.add('hidden');
    });
});

// Asynchronous function to handle the search request to the server
document.addEventListener('DOMContentLoaded', async function() {
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.querySelector('#search-results .search-results-content'); // Updated selector
    const jobDetails = document.querySelector('job-details');

    // Add an event listener to the search button to handle the search request to the server
    searchBtn.addEventListener('click', async function(event) {
        event.preventDefault(); 
        const category = searchInput.value.trim();
        const response = await fetch('/app', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({ searchInput: category }),
        });

        if (response.ok) {
            const Jobs = await response.json();
            // console.log(data);
            // Validate that the received JSON is not null or undefined
            if (Jobs !== null && Jobs !== undefined) {
                const searchContent = document.querySelector('#search-results .search-results-content');  // Updated selector
                // Clear the search results content before displaying the new results
                while (searchContent.firstChild) {
                    searchContent.removeChild(searchResults.firstChild);
                }
                // Iterate over each job and display the info in the HTML
                Jobs.forEach(job => {
                    const jobSection = document.querySelector('#search-results .search-results-content'); // Updated selector
                    const jobElement = document.createElement('div');
                    
                    jobElement.classList.add('jobs-results');
                    jobElement.innerHTML = `
                    <div class="job-details">
                        <br />
                        <span><h2>Puesto: ${job.name}</h2></span>
                        <span><h4>Compania: ${job.company}</h4></span>
                        <span><p>Nivel del puesto: ${job.level}</p></span>
                        <span><p>Tiempo de trabajo: ${job.time}</p></span>
                        <span><p>Modalidad del puesto: ${job.mode}</p></span>
                        <button class="infoBtn"><a href="${job.url}" alt="${job.company}">Mas Informacion</a></button>
                        <hr />
                    </div>
                    `;

                    jobSection.appendChild(jobElement);
                });
            searchResults.classList.remove('hidden');
            jobDetails.classList.remove('hidden');
        }  // if the JSON is null or undefined, display an error message in the HTML
            else {
                const jobSection = document.querySelector('#search-results .search-results-content') // Updated selector
                const jobElement = document.createElement('div');
                jobElement.textContent = 'No se encontraron trabajos con la categoría ingresada. Por favor, intenta con otra categoría.';
                jobSection.appendChild(jobElement);
                console.error('Error al obtener los datos del servidor');
            }
        } 
        else {
            console.error('Error al obtener los datos del servidor');
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const logoutBtn = document.getElementById('logoutBtn');  // Get the logout button element by ID
    const nav = document.querySelector('.navbar ul');  // Get the unordered list element in the navbar
    logoutBtn.addEventListener('click', function() {
        alert('Sesión cerrada exitosamente');  // Display an alert to the user when the logout button is clicked
        // Send a POST request to the server to log out the user
        fetch('/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            nav.removeChild(nav.firstChild);  // Remove the last child element from the unordered list
            // Redirect the user to the home page after logging out
            window.location.href = '/';
        })
        .catch(error => {
            console.error('Error al cerrar sesión:', error);
        });
    });
});



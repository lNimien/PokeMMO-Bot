document.addEventListener("DOMContentLoaded", function() {
    var inicioBtn = document.getElementById("inicioBtn");
    var descargarBtn = document.getElementById("descargarBtn");
    var discordBtn = document.getElementById("discordBtn");
    var youtubeBtn = document.getElementById("youtubeBtn");
    var registrarseBtn = document.getElementById("registrarseBtn");

    inicioBtn.addEventListener("click", function() {
        mostrarContenidoInicio();
    });

    descargarBtn.addEventListener("click", function() {
        mostrarContenidoDescarga();
    });

    registrarseBtn.addEventListener("click", function() {
        mostrarContenidoRegistro();
    });

    discordBtn.addEventListener("click", function() {
        console.log("Clic en Discord");
    });

    youtubeBtn.addEventListener("click", function() {
        console.log("Clic en YouTube");
    });


    function mostrarContenidoInicio() {
        document.getElementById("contenido").innerHTML = `
            <div class="container inicio-container">
                <img src="static/imgs/Logo.png" alt="Logo" class="logo">
                <div class="info">
                    <h1>PokeMMO Bot</h1>
                    <p>Descarga nuestro bot para automatizar acciones en el juego PokeGame.</p>
                    <p>Características:</p>
                    <ul>
                        <li>Automatiza acciones continuas en el juego.</li>
                        <li>Utiliza un motor visual para leer texto en la pantalla.</li>
                        <li>Devuelve datos útiles para mejorar tu experiencia de juego.</li>
                    </ul>
                    <p>Sistema operativo compatible: Windows 7/8.1/10/11</p>
            </div>
        `;
    }


    function mostrarContenidoDescarga() {
        document.getElementById("contenido").innerHTML = `
            <div class="container">
                <!-- Contenido de descarga -->
                <h1>Descargar nuestra aplicación</h1>
                <p>Aquí puedes encontrar enlaces y detalles para descargar nuestra aplicación.</p>
            </div>
        `;
    }

    function mostrarContenidoRegistro() {
        document.getElementById("contenido").innerHTML = `
            <div class="container">
                <img src="static/imgs/Logo.png" alt="Logo">
                <form action="/" method="POST">
                    <input type="username" name="username" placeholder="Nombre">
                    <input type="email" name="email" placeholder="Email">
                    <input type="password" name="password" placeholder="Contraseña">
                    <button type="submit">Registrarse</button>
                </form>
                <p class="mensaje"></p>
            </div>
        `;
    }

    mostrarContenidoInicio();
});



window.onload = function () {
    document.querySelector('form').addEventListener('submit', function (event) {
        event.preventDefault();

        let username = document.querySelector('input[name="username"]').value;
        let email = document.querySelector('input[name="email"]').value;
        let password = document.querySelector('input[name="password"]').value;

        let mensaje = document.querySelector('.mensaje');

        if (username.trim() === '' || email.trim() === '' || password.trim() === '') 
        {
            mensaje.innerHTML = '<strong>Por favor, complete todos los campos.</strong>';
        } 
        else if (!email.includes('@')) 
        {
            mensaje.innerHTML = '<strong>Ingrese un correo electrónico válido.</strong>';
        } 
        else 
        {
            fetch('/', 
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, email, password })
            })
            .then(response => response.text())
            .then(data => {
                mensaje.innerText = data; // Mostrar respuesta del servidor
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
};

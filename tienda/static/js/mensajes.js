setTimeout(function() {
    var mensajes = document.getElementsByClassName('alert');
    for (var i = 0; i < mensajes.length; i++) {
        mensajes[i].style.display = 'none';
    }
}, 3000); // Desaparecer después de 2 segundos
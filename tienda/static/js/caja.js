
document.getElementById("aceptar").addEventListener("click", function() {
    var fecha = document.getElementById('fecha').value;
    var opcion = document.getElementById('opcion').value;
    var monto = document.getElementById('monto').value;
    Swal.fire({
        title: 'Finalizar Transferencia?',
        text: "No podrás revertir esto!",
        icon: 'warning',
        width: '300px',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si',
        cancelButtonText: 'No'
        }).then((result) => {
        if (result.isConfirmed) {
            enviarDatos(fecha, opcion, monto);
        }
    });

// Función para enviar los datos a Flask con AJAX
function enviarDatos(fecha, opcion, monto) {
    
    var xhr = new XMLHttpRequest();
    var url = './transferir'; // La URL de la vista de Flask que manejará los datos
    var data = {
        fecha: fecha,
        opcion: opcion,
        monto: monto
    };
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Aquí puedes manejar la respuesta de Flask si es necesario
            resultados.innerHTML = "Datos enviados a Flask con éxito.";
            location.reload();
            }
        };
        xhr.send(JSON.stringify(data));
    }
});
        

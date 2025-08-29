document.getElementById("ing").addEventListener('submit', function(event) {
	event.preventDefault();

//aqui obtengo lo valores de los inpput del formulario
	const correo = document.getElementById('correo').value;
	const clave = document.getElementById('clave').value;


	//VERIFICACION DE CREDENCIALES
	const userCorrecto = "uru@gmail.com";
	const claveCorrecto = "146";

	const userCorrecto1 = "david@gmail.com";
	const claveCorrecto1 = "1234";

	if (correo == userCorrecto && clave == claveCorrecto) {
		alert('Bievenid@ Señor@ Admin');
	window.location.href = 'http://127.0.0.1:5000/home_admin.html';
	 }

	else if(correo == userCorrecto1 && clave == claveCorrecto1) {
		alert('Bievenid@ Señor@ Admin');
	window.location.href = 'http://127.0.0.1:5000/home_admin.html';
	 }
	 else{
    window.location.href = 'home_usuario.html';
}



}
);
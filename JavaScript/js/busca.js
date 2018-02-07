var botaoAdicionar = document.querySelector("#buscar-paciente");

botaoAdicionar.addEventListener("click", function(event) {

	var xhr = new XMLHttpRequest();

	xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes");

	xhr.addEventListener("load", function() {

		if (xhr.status == "200") {
			var response = xhr.responseText;
			var pacientes = JSON.parse(response);
			addJsonData(pacientes);
		} else {
			alert("Não foi possível carregar os dados. Erro: " + xhr.status);
			console.log(xhr.responseText);
		}

		

	});

	xhr.send();

});

function addJsonData(pacientes) {

	var pacienteTr = [pacientes.length];
	for (var i = 0; i < pacientes.length; i++) {
		pacienteTr[i] = getRowStructure(pacientes[i]);
	}

	var tabela = document.querySelector("#tabela-pacientes");

	for (var j = 0; j < pacienteTr.length; j++) {
		tabela.appendChild(pacienteTr[j]);	
	}

	updateTable();

}
var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

updateTable();

var botaoAdicionar = document.querySelector("#adicionar-paciente");

botaoAdicionar.addEventListener("click", function(event) {
	event.preventDefault();
	
	var form = document.querySelector("#form-adiciona");

	var paciente = getFormFields(form);

	if (validateForm(paciente)) {
		pacienteTr = getRowStructure(paciente);

		var tabela = document.querySelector("#tabela-pacientes");

		tabela.appendChild(pacienteTr);

		updateTable();

		form.reset();
	} else {
		//logErro();
	}

	

});

function updateTable() {

	var pacientes = document.querySelectorAll(".paciente");

	for (var i = 0; i < pacientes.length; i++) {

		var paciente = pacientes[i];

		var tdPeso = paciente.querySelector(".info-peso");
		var peso = tdPeso.textContent;

		var tdAltura = paciente.querySelector(".info-altura");
		var altura = tdAltura.textContent;

		var tdImc = paciente.querySelector(".info-imc");

		var pesoEhValido = true;
		var alturaEhValida = true;

		if (peso <= 0 || peso >= 1000) {
		    console.log("Peso inválido!");
		    pesoEhValido = false;
		    tdImc.textContent = "Peso inválido";
		    paciente.classList.add("invalido");
		} else if (altura <= 0 || altura >= 3.00) {
		    console.log("Altura inválida!");
		    alturaEhValida = false;
		    tdImc.textContent = "Altura inválida";
		    paciente.classList.add("invalido");
		}

		if (pesoEhValido && alturaEhValida) {
		    var imc = peso / (altura * altura);
		    tdImc.textContent = imc.toFixed(2);
		}

	}

}

function getFormFields(form) {

	var paciente = {
		nome: form.nome.value,
		peso: form.peso.value,
		altura: form.altura.value,
		gordura: form.gordura.value,
		imc: calculaImc(form.peso.value, form.altura.value)
	}
	return paciente;
}


function calculaImc(peso, altura) {
	return peso / (altura * altura);
}

function getRowStructure(paciente) {

	var pacienteTr = document.createElement("tr");
	pacienteTr.classList.add("paciente");

	pacienteTr.appendChild(getTdStructure(paciente.nome, "info-nome"));
	pacienteTr.appendChild(getTdStructure(paciente.peso, "info-peso"));
	pacienteTr.appendChild(getTdStructure(paciente.altura, "info-altura"));
	pacienteTr.appendChild(getTdStructure(paciente.gordura, "info-gordura"));
	pacienteTr.appendChild(getTdStructure(paciente.imc.toFixed(2), "info-imc"));

	return pacienteTr;
}

function getTdStructure(dado, classe) {

	var td = document.createElement("td");
	td.textContent = dado;
	td.classList.add(classe);

	return td;
}

function validateForm(paciente) {

	if (paciente.nome.length < 3) return false;
	else if (paciente.peso < 2 || paciente.peso > 400) return false;	
	else if (paciente.altura < 0.1 || paciente.altura > 2.5) return false;
	else if (paciente.gordura < 0 || paciente.gordura > 100) return false;
	else return true;

}

function logErro() {
	alert("Não foi possível cadastrar usuário");
}
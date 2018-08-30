var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

updateTable();

var botaoAdicionar = document.querySelector("#adicionar-paciente");

var tabela = document.querySelector("table");

tabela.addEventListener("dblclick", function(event) {
	if (event.target.tagName == 'TD') {
        event.target.parentNode.classList.add("fadeOut");
		setTimeout(function() {
			event.target.parentNode.remove();
		}, 500);
    }
});

botaoAdicionar.addEventListener("click", function(event) {
	resetForm();

	event.preventDefault();
	
	var form = document.querySelector("#form-adiciona");

	var paciente = getFormFields(form);

	var bools = validateForm(paciente);

	if (bools[0] && bools[1] && bools[2] && bools[3]) {
		pacienteTr = getRowStructure(paciente);

		var tabela = document.querySelector("#tabela-pacientes");

		tabela.appendChild(pacienteTr);

		updateTable();

		form.reset();
	} else {
		logErro(bools);
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

	var booleans = [false, false, false, false];
	if (paciente.nome.length > 2) booleans[0] = true;
	if (paciente.peso > 2 && paciente.peso < 400 && paciente.peso.length > 0) booleans[1] = true;	
	if (paciente.altura > 0.1 && paciente.altura < 2.5 && paciente.altura.length > 0) booleans[2] = true;
	if (paciente.gordura >= 0 && paciente.gordura <= 100 && paciente.gordura.length > 0) booleans[3] = true;
	return booleans;

}

function logErro(bools) {
	
	var wNome = document.querySelector("#w-nome");
	var wPeso = document.querySelector("#w-peso");
	var wAltura = document.querySelector("#w-altura");
	var wGordura = document.querySelector("#w-gordura");

	if (!bools[0]) {
		wNome.classList.add("f-show");
		nome.classList.add("form-error");
	}
	if (!bools[1]) {
		wPeso.classList.add("f-show");
		peso.classList.add("form-error");
	}
	if (!bools[2]) {
		wAltura.classList.add("f-show");
		altura.classList.add("form-error");
	}
	if (!bools[3]) {
		wGordura.classList.add("f-show");
		gordura.classList.add("form-error");
	}

}

function resetForm() {

	var wNome = document.querySelector("#w-nome");
	var wPeso = document.querySelector("#w-peso");
	var wAltura = document.querySelector("#w-altura");
	var wGordura = document.querySelector("#w-gordura");

	wNome.classList.remove("f-show");
	nome.classList.remove("form-error");
	wPeso.classList.remove("f-show");
	peso.classList.remove("form-error");
	wAltura.classList.remove("f-show");
	altura.classList.remove("form-error");
	wGordura.classList.remove("f-show");
	gordura.classList.remove("form-error");

}
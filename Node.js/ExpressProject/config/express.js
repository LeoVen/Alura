// Esse código fica fora do module.exports para que (ele seja sempre o mesmo[?]) e o 
// module.export apenas retorna o app (que ja foi definido para todas as chamadas do require[?])
var app = require('express')();
app.set("view engine", "ejs"); // Usando ejs
app.set("views", "./app/views") // Dizer que a pasta views está na pasta app agora, e não na raiz do projeto
								// Raiz do projeto = onde o arquivo que inicia tudo está

// usamos module.exports para exportar um modulo
module.exports = function() {
	console.log("Modulo sendo carregado");
	return app;
}

// Configurações do Express
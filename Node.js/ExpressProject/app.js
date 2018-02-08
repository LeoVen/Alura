var app = require('./config/express')(); // Configurações do Express
var r = require('./app/routes/routes')(app); // Configurações de rotas

// Listen na porta 3000
app.listen(3000, function() {
	console.log("Server Running...");
});
// usamos module.exports para exportar um modulo
module.exports = function(app) {

	app.get('/', function(request, response) {
		response.render("index");
	});

	app.get('/main', function(request, response) {
		var oracle = require('oracledb');
		var dbConfig = require('./dbconfig.js');
		var conn = oracle.

		response.render("main/m");
	});
}
/* Definindo rotas. Se buscarmos /main, a resposta será main/m por exemplo
*/
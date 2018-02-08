// usamos module.exports para exportar um modulo
module.exports = function(app) {

	app.get('/', function(request, response) {
		response.render("index");
	});

	app.get('/main', function(request, response) {
		response.render("main/m");
	});
}
/* Definindo rotas. Se buscarmos /main, a resposta será main/m por exemplo
*/
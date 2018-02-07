var http = require('http');

var server = http.createServer(function(request, response) {

	switch(request.url) {
		case "/produtos":
			response.writeHead(200, {'Content-Type':'text-html'});
			response.end("<!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <title>Alura</title> </head> <body> <h1>Minha Página</h1> </body> </html>");
			break;
		default:
			response.writeHead(200, {'Content-Type':'text-html'});
			response.end("<!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <title>Alura</title> </head> <body> <h1>Home</h1> <a href='/produtos'>Outra página</a></body> </html>");
			break;
	}
	
}).listen(3000, "localhost");

console.log("Subindo serviço");


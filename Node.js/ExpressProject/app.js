var express = require('express');
var app = express();

app.get('/produtos', function(request, response) {
	response.send("<!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <title>Alura</title> </head> <body> <h1>Home</h1> <a href='/produtos'>Outra página</a></body> </html>");
});

app.listen(3000, function() {
	console.log("Server Running");
});
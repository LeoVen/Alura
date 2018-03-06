<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Empresas</title>
</head>
<body>
	
	<h1>Resultado da Busca</h1>
	<c:forEach var="empresa" items="${empresas }">
		<li>${empresa.id } : ${empresa.nome }</li>
	</c:forEach>
	<br>
	<a href="/gerenciador"><button>Voltar</button></a>

</body>
</html>
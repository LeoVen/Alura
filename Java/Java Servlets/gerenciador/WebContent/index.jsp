<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<body>
	<h1>Bem vindo ao nosso gerenciador de empresas!</h1>
	<c:if test="${not empty usuarioLogado }">
		Logado como ${usuarioLogado.email }
	</c:if>
	<br>
	<br>
	<hr>
	<h3>Fazer Login</h3>
	<form action="login" method="POST">
		<label for="email">Email</label>
		<input type="text" name="email">
		<label for="senha">Senha</label>
		<input type="password" name="senha">
		<button type="submit">Login</button>
	</form>
	<form action="logout" method="POST">
		<button type="submit" value="Deslogar">Logout</button>
	</form>
	<br>
	<hr>
	<h3>Cadastre Nova Empresa</h3>
	<form action="novaEmpresa" method="POST">
		<label for="nome">Nome</label>
		<input type="text" name="nome" id="nome">
		<input type="submit" value="Enviar">
	</form>
	<br>
	<hr>
	<h3>Buscar Empresa</h3>
	<form action="/gerenciador/index" method="POST">
		<input type="hidden" name="tarefa" value="GetEmpresas">
		<label for="filtro">Filtro</label>
		<input type="text" name="filtro">
		<button type="submit">Buscar</button>
	</form>


</body>
</html>
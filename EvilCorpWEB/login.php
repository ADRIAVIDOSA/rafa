<!DOCTYPE html>
<html>
<head>
<h1><a href="index.php">Evil Corp</a></h1>
<div class="top-right">
</div>
	<title>Login</title>
	<link rel="stylesheet" href="clients.css">
</head>
<body>
	<h2>Inicio de sesión</h2>
	<form action="register.php" method="post">
		<label for="email">Correo electrónico:</label>
		<input type="email" name="email" required><br>
		<label for="password">Contraseña:</label>
		<input type="password" name="password" required><br>

		<input type="submit" value="Login">
	</form>
</body>
</html>

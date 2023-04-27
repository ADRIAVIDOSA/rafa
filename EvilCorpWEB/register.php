<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
if (sizeof($_POST) > 0) {
	require("./db.php");
	$rol       	= "client";
	$name 		= $_POST["name"];
	$surname1 	= $_POST["surname1"];
	$surname2 	= $_POST["surname2"];
	$birthday 	= $_POST["birthday"];
	$email 		= $_POST["email"];
	$phone 		= $_POST["phone"];
	$country 	= $_POST["country"];
	$address 	= $_POST["address"];
	$password 	= $md5(_POST["password"]);

	//INSERT INTO users (rol, name, surname1, surname2, birthday, email, phone, country, address, password)
	$stmt = $conn->prepare("INSERT INTO users
		(rol, name, surname1, surname2, birthday, email, phone, country, address, password) VALUES (
			:rol,
			:name,
			:surname1,
			:surname2,
			:birthday,
			:email,
			:phone,
			:country,
			:address,
			:password
		);");
	$stmt->bindParam(":rol", $rol);
	$stmt->bindParam(":name", $name);
	$stmt->bindParam(":surname1", $surname1);
	$stmt->bindParam(":surname2", $surname2);
	$stmt->bindParam(":birthday", $birthday);
	$stmt->bindParam(":email", $email);
	$stmt->bindParam(":phone", $phone);
	$stmt->bindParam(":country", $country);
	$stmt->bindParam(":address", $address);
	$stmt->bindParam(":password", $password);

	$result = $stmt->execute();
	print_r($result);
}

 
?>

<!DOCTYPE html>
<html>

<head>
	<h1><a href="index.php">Evil Corp</a></h1>
	<div class="top-right">
	</div>
	<title>Registro de usuario</title>
	<link rel="stylesheet" href="clients.css">
</head>

<body>
	<h2>Registro de usuario</h2>
	<form action="register.php" method="post">
		<label for="name">Nombre:</label>
		<input type="text" name="name" required><br>

		<label for="surname1">Primer Apellido:</label>
		<input type="text" name="surname1" required><br>

		<label for="surname2">Segundo Apellido:</label>
		<input type="text" name="surname2" required><br>

		<label for="birthday">Fecha de Nacimiento:</label>
		<input type="date" name="birthday" required><br>

		<label for="email">Correo electrónico:</label>
		<input type="email" name="email" required><br>

		<label for="phone">Teléfono (sin prefijo):</label>
		<input type="tel" name="phone" required><br>

		<label for="country">País (nombre completo):</label>
		<input type="text" name="country" required><br>

		<label for="address">Dirección de domicilio:</label>
		<input type="text" name="address" required><br>

		<label for="password">Contraseña:</label>
		<input type="password" name="password" required><br>

		<input type="submit" value="Registrarse">
	</form>
</body>

</html>

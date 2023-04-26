<?php
//Conexión a la base de datos
$servername = "localhost";
$username = "tu_usuario";
$password = "tu_contraseña";
$dbname = "usersdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("Conexión fallida: " . mysqli_connect_error());
}

//Verificar si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  //Validar campos
  $name = mysqli_real_escape_string($conn, $_POST['name']);
  $surname1 = mysqli_real_escape_string($conn, $_POST['surname1']);
  $surname2 = mysqli_real_escape_string($conn, $_POST['surname2']);
  $birthday = mysqli_real_escape_string($conn, $_POST['birthday']);
  $email = mysqli_real_escape_string($conn, $_POST['email']);
  $phone = mysqli_real_escape_string($conn, $_POST['phone']);
  $country = mysqli_real_escape_string($conn, $_POST['country']);
  $address = mysqli_real_escape_string($conn, $_POST['address']);
  $password = mysqli_real_escape_string($conn, $_POST['password']);

  //Validar correo electrónico
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "El correo electrónico no es válido";
    exit;
  }

  //Validar contraseña
  if (!preg_match("/^[a-zA-Z0-9]{8,}$/", $password)) {
    echo "La contraseña debe tener al menos 8 caracteres alfanuméricos";
    exit;
  }

  //Hashear la contraseña
  $hashed_password = password_hash($password, PASSWORD_DEFAULT);

  //Insertar datos en la base de datos
  $sql = "INSERT INTO users (name, surname1, surname2, birthday, email, phone, country, address, password)
  VALUES ('$name', '$surname1', '$surname2', '$birthday', '$email', '$phone', '$country', '$address', '$hashed_password')";

  if (mysqli_query($conn, $sql)) {
    echo "Registro exitoso";
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }

  mysqli_close($conn);
}
?>

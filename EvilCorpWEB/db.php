<?php
$host = "localhost";
$user = "ecorp";
$pass = "Ecorp";
$dbnm = "usersdb";

try {
    $conn = new PDO("mysql:host=$host;dbname=$dbnm", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (\Throwable $th) {
    die("Error en la conexion con la base de datos. Revise ./db.php");
}
INSERT INTO users
	(name, surname1, surname2, rol, birthday, email, password, phone, country, address)
VALUES
	('Juan', 'García', 'Martínez', 'Paciente', '1990-05-05', 'juan@gmail.com', '123456', 987654321, 'España', 'Calle Mayor, 1'),
	('María', 'Sánchez', 'Fernández', 'Paciente', '1988-10-12', 'maria@gmail.com', 'abcdef', 666555444, 'España', 'Avenida del Sol, 20'),
	('Pedro', 'López', 'González', 'Médico', '1975-03-22', 'pedro@gmail.com', 'qwerty', 987654321, 'México', 'Calle Reforma, 15');

INSERT INTO doctors
	(doctor)
VALUES
	('Dr. García'),
	('Dra. Martínez');

INSERT INTO medicines
	(medicament, production_cost, sell_cost)
VALUES
	('Paracetamol', 0.50, 1.00),
	('Ibuprofeno', 0.80, 1.50),
	('Amoxicilina', 1.20, 2.50),
	('Omeprazol', 1.00, 2.00);

INSERT INTO diseases
	(disease, symptoms, description, deadly)
VALUES
	('Gripe', 'Fiebre, dolor de cabeza, tos, fatiga', 'Infección viral que afecta las vías respiratorias', FALSE),
	('Diabetes', 'Sed, aumento de la micción, visión borrosa, fatiga', 'Trastorno metabólico que afecta la regulación de azúcar en sangre', FALSE),
	('Cáncer de pulmón', 'Tos persistente, dolor en el pecho, dificultad para respirar', 'Crecimiento anormal de células en los pulmones', TRUE),
	('Hipertensión', 'Dolor de cabeza, visión borrosa, fatiga, mareos', 'Aumento persistente de la presión arterial', FALSE);

INSERT INTO diagnoses
	(diagnosis, id_doctor, id_user, id_disease)
VALUES
	('El paciente tiene gripe', 1, 1, 1),
	('La paciente tiene diabetes', 2, 2, 2),
	('El paciente tiene hipertensión', 1, 3, 4),
	('El paciente tiene cáncer de pulmón', 2, 1, 3),
	('La paciente tiene hipertensión', 2, 2, 4),
	('El paciente tiene diabetes', 1, 3, 2);

INSERT INTO treatments
	(id_diagnosis)
VALUES
	(1),
	(2),
	(3),
	(4),
	(5);

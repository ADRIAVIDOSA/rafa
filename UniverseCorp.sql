CREATE TABLE Civilizations (
	id INT PRIMARY KEY,
	name VARCHAR(50),
	planet VARCHAR(50),
	dead BOOLEAN DEFAULT false
);

INSERT INTO Civilizations (id, name, planet)
VALUES 
	(1, 'Civilization 1', 'Planet A'),
	(2, 'Civilization 2', 'Planet B'),
	(3, 'Civilization 3', 'Planet B'),
	(4, 'Civilization 4', 'Planet C'),
	(5, 'Civilization 5', 'Planet C'),
	(6, 'Civilization 6', 'Planet C');

CREATE VIEW PeopleCountByPlanet AS
SELECT planet, COUNT(*) AS count
FROM Civilizations
GROUP BY planet;

CREATE VIEW MedicineRevenueByPlanet AS
SELECT planet, SUM(revenue) AS medicine_revenue
FROM Medicines
GROUP BY planet;

ALTER TABLE Civilizations
ADD COLUMN dead BOOLEAN DEFAULT false;

CREATE USER grimreaper;
GRANT SELECT, UPDATE ON Civilizations TO grimreaper;

CREATE FUNCTION GetRandomIndividualFromPlanet(planet_param VARCHAR(50)) RETURNS VARCHAR(50)
AS $$
DECLARE
	individual VARCHAR(50);
BEGIN
	SELECT name INTO individual
	FROM Civilizations
	WHERE planet = planet_param
	ORDER BY random()
	LIMIT 1;

	RETURN individual;
END;
$$ LANGUAGE plpgsql;

CREATE PROCEDURE KillUser(user_param VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
	IF EXISTS (SELECT 1 FROM Civilizations WHERE name = user_param AND dead = true) THEN
		RAISE NOTICE 'You cannot kill % again.', user_param;
	ELSE
		UPDATE Civilizations
		SET dead = true
		WHERE name = user_param;

		RAISE NOTICE 'HA MUERTO... %', user_param;
	END IF;
END;
$$;

SET ROLE grimreaper;
SELECT GetRandomIndividualFromPlanet('Planet A');
CALL KillUser('Civilization 1');

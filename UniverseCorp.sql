CREATE TABLE civilizations (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    planet VARCHAR(50),
    dead BOOLEAN DEFAULT false
);

INSERT INTO civilizations (id, name, planet)
VALUES 
    (1, 'Civilization 1', 'Planet A'),
    (2, 'Civilization 2', 'Planet B'),
    (3, 'Civilization 3', 'Planet B'),
    (4, 'Civilization 4', 'Planet C'),
    (5, 'Civilization 5', 'Planet C'),
    (6, 'Civilization 6', 'Planet C');

CREATE VIEW people_count_by_planet AS
SELECT planet, COUNT(*) AS count
FROM civilizations
GROUP BY planet;

CREATE VIEW medicine_revenue_by_planet AS
SELECT planet, SUM(revenue) AS medicine_revenue
FROM medicines
GROUP BY planet;

ALTER TABLE civilizations
ADD COLUMN dead BOOLEAN DEFAULT false;

CREATE USER grimreaper;
GRANT SELECT, UPDATE ON civilizations TO grimreaper;

DELIMITER $$
CREATE FUNCTION get_random_individual_from_planet(planet_param VARCHAR(50))
RETURNS VARCHAR(50)
BEGIN
    DECLARE random_individual VARCHAR(50);
    SELECT name INTO random_individual
    FROM civilizations
    WHERE planet = planet_param
    ORDER BY RAND()
    LIMIT 1;
    RETURN random_individual;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE kill_user(user_param VARCHAR(50))
BEGIN
    DECLARE user_name VARCHAR(50);
    SET user_name = (SELECT name FROM civilizations WHERE name = user_param);

    IF EXISTS (SELECT 1 FROM civilizations WHERE name = user_param AND dead = true) THEN
        SELECT CONCAT(
            'No puedes matar otra vez a "',
            user_name,
            '".'
        ) AS Resultado;
    ELSE
        UPDATE civilizations
        SET dead = true
        WHERE name = user_param;
        SELECT CONCAT(
            'HA MUERTO... "',
            user_name,
            '".'
        ) AS Resultado;
    END IF;
END$$
DELIMITER ;

SET @user_role = 'grimreaper';
SET @planet = 'Planet A';
SELECT get_random_individual_from_planet(@planet);
CALL kill_user('Civilization 1');

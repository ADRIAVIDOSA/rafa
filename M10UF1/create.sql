USE usersdb;

CREATE TABLE IF NOT EXISTS medicines (
    id_medicine INT UNSIGNED NOT NULL AUTO_INCREMENT,
    medicament VARCHAR(192) NOT NULL,
    production_cost DECIMAL(9,2) NOT NULL,
    sell_cost DECIMAL(9,2) NOT NULL,
    PRIMARY KEY (id_medicine)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS treatments (
    id_treatment BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_diagnosis BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_treatment),
    FOREIGN KEY (id_diagnosis) REFERENCES diagnoses(id_diagnosis) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS doctors (
    id_doctor INT UNSIGNED NOT NULL AUTO_INCREMENT,
    doctor VARCHAR(32) NOT NULL,
    PRIMARY KEY (id_doctor)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS diagnoses (
    id_diagnosis BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    diagnosis TEXT NOT NULL,
    id_doctor INT UNSIGNED NOT NULL,
    id_user BIGINT UNSIGNED NOT NULL,
    id_disease INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_diagnosis),
    FOREIGN KEY (id_doctor) REFERENCES doctors(id_doctor) ON DELETE CASCADE,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE,
    FOREIGN KEY (id_disease) REFERENCES diseases(id_disease) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS diseases (
    id_disease INT UNSIGNED NOT NULL AUTO_INCREMENT,
    disease VARCHAR(64) NOT NULL,
    symptoms TEXT NOT NULL,
    description TEXT NOT NULL,
    deadly BOOLEAN NOT NULL,
    PRIMARY KEY (id_disease)
) ENGINE=InnoDB;
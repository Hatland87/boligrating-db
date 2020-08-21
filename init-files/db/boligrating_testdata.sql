CREATE SCHEMA IF NOT EXISTS boligrating_testdata;

CREATE TABLE IF NOT EXISTS boligrating_testdata.leiligheter (
    id BIGINT NOT NULL PRIMARY KEY, 
    veinavn VARCHAR(100) NOT NULL,
    nummer SMALLINT NOT NULL,
    bokstav VARCHAR(2),
    nummer_bokstav VARCHAR(10) NOT NULL,
    bruksenhetsnummer VARCHAR(5),
    postnummer SMALLINT NOT NULL,
    poststed VARCHAR(50) NOT NULL,
    kommunenavn VARCHAR(50) NOT NULL,
    FULLTEXT(veinavn, nummer_bokstav, poststed, kommunenavn)
);

CREATE TABLE IF NOT EXISTS boligrating_testdata.adresser (
    id BIGINT NOT NULL PRIMARY KEY, 
    veinavn VARCHAR(100) NOT NULL,
    nummer SMALLINT NOT NULL,
    bokstav VARCHAR(2),
    nummer_bokstav VARCHAR(10) NOT NULL,
    postnummer SMALLINT NOT NULL,
    poststed VARCHAR(50) NOT NULL,
    kommunenavn VARCHAR(50) NOT NULL,
    FULLTEXT(veinavn, nummer_bokstav, poststed, kommunenavn)
);

CREATE TABLE IF NOT EXISTS boligrating_testdata.reviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    dato_review DATETIME NOT NULL,
    adresse_id INT NOT NULL REFERENCES adresser(bruksenhetid),

    karakter_total TINYINT NOT NULL,
    karakter_bygg TINYINT NOT NULL,
    karakter_pris TINYINT NOT NULL,
    karakter_utleier TINYINT NOT NULL,

    navn_utleier VARCHAR(100) NOT NULL,
    kontrakt_oppsigelsestid ENUM('1', '2', '3', '3+', 'ingen') NOT NULL,
    depositumskonto TINYINT NOT NULL,
    leiepris INT NOT NULL,
    depositum INT NOT NULL,

    leie_fra DATE NOT NULL,
    leie_til DATE NOT NULL,
    bo_alene TINYINT NOT NULL,
    telefonnummer_reviewer VARCHAR(11) NOT NULL,
    godkjent TINYINT NOT NULL
);
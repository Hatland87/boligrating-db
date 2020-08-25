CREATE VIEW Adresse_Leilighet AS
SELECT 
a.id as adresseID,
l.id as leilighetID,
a.veinavn,
l.bruksenhetsnummer as leilighetnummer,
a.nummer_bokstav as bolignummer,
a.postnummer,
a.poststed,
a.kommunenavn
FROM adresser a
LEFT JOIN leiligheter l 
ON l.veinavn = a.veinavn 
AND l.nummer_bokstav = a.nummer_bokstav
AND l.postnummer = a.postnummer
AND l.poststed = a.poststed
AND l.kommunenavn = a.kommunenavn;
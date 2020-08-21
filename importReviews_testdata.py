import mysql.connector

file = open('./data/test/matrikkelenAdresseLeilighetsniva.csv', encoding="utf8")

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)
cursor = cnx.cursor()

query = "INSERT INTO boligrating_testdata.leiligheter(dato_review, adresse_id, karakter_total, karakter_bygg, karakter_pris, karakter_utleier, navn_utleier, kontrakt_oppsigelsestid, depositumskonto, leiepris, depositum, leie_fra, leie_til, bo_alene, telefonnummer_reviewer, godkjent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for l in file:
    line = l.split(';')
    if line[2] == 'vegadresse' and line[15] != '':
        try:
            data = (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15])
            cursor.execute(query, data)
            cnx.commit()
        except:
            print("Did not write to database")
            print(line)

cursor.close()
cnx.close()
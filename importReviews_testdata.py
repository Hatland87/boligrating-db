from db import cnx, cursor

file = open('./data/test/reviews.csv', encoding="utf8")

query = "INSERT INTO boligrating_testdata.reviews(dato_review, adresse_id, karakter_total, karakter_bygg, karakter_pris, karakter_utleier, navn_utleier, kontrakt_oppsigelsestid, depositumskonto, leiepris, depositum, leie_fra, leie_til, bo_alene, telefonnummer_reviewer, godkjent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for l in file:
    line = l.split(';')
    if line[0] != 'dato_reviews':
        if line[2] == '':
            line[2] = None
        data = (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16])
        cursor.execute(query, data)
        cnx.commit()

cursor.close()
cnx.close()
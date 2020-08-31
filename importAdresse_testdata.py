from db import cnx, cursor

file = open('./data/test/matrikkelenVegadresse.csv', encoding="utf8")

query = "INSERT INTO boligrating_testdata.adresser(id, veinavn,nummer,bokstav,nummer_bokstav, postnummer, poststed, kommunenavn) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        
for l in file:
    line = l.split(';')
    if line[3] == 'vegadresse':
        data = (line[0],line[7],line[8],line[9],line[8] + line[9],line[19],line[20],line[2])
        cursor.execute(query, data)
        cnx.commit()

cursor.close()
cnx.close()

from db import cnx, cursor

file = open('./data/real/matrikkelenAdresseLeilighetsniva.csv', encoding="utf8")

query = "INSERT INTO boligrating.leiligheter(id, veinavn, nummer, bokstav, nummer_bokstav, bruksenhetsnummer, postnummer, poststed, kommunenavn) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
for l in file:
    line = l.split(';')
    if line[2] == 'vegadresse' and line[15] != '':
        try:
            data = (line[14], line[6], line[7], line[8], line[7] + line[8], line[15], line[21],line[22],line[1])
            cursor.execute(query, data)
            cnx.commit()
        except:
            print("Did not write to database")
            print(line)

cursor.close()
cnx.close()

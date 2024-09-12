import mysql.connector

def lentoasema_tyypit(maakoodi, tyyppi):
    sql = f'SELECT type FROM airport WHERE iso_country = "{maakoodi}" AND type = "{tyyppi}"'
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    airport_data = kursori.fetchall()
    lukumaara = 0
    for i in airport_data:
        lukumaara = lukumaara + 1
    return lukumaara

yhteys = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='flight_game',
         user='kayttaja',
         password='sala_sana',
         autocommit=True
         )

ab = input("Syötä maakoodi: ")
pienet = lentoasema_tyypit(ab,"small_airport")
keskikokoiset = lentoasema_tyypit(ab,"medium_airport")
suuret = lentoasema_tyypit(ab, "large_airport")
helikopteri = lentoasema_tyypit(ab,"heliport")
suljettu = lentoasema_tyypit(ab,"closed")

print(f"Pieniä lentoasemia on {pienet} kappaletta.")
print(f"Keskikokoisia lentoasemia on {keskikokoiset} kappaletta.")
print(f"Suuria lentoasemia on {suuret} kappaletta.")
print(f"Helikopterikenttiä on {helikopteri} kappaletta.")
print(f"Lentoasemista {suljettu} kappaletta on suljettu.")

import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    airport_data = kursori.fetchall()
    return airport_data

yhteys = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='flight_game',
         user='riikkoo',
         password='2001Riikka',
         autocommit=True
         )

icao_koodi = input("Anna ICAO-koodi: ")

lentoaseman_tiedot = get_airport_by_icao(icao_koodi)

print(f"Tämän lentoaseman nimi on '{lentoaseman_tiedot[0][0]}' "
      f"ja sijaintikunta '{lentoaseman_tiedot[0][1]}'.")
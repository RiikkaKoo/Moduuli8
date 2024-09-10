import mysql.connector
from geopy import distance

def lentoasema_koordinaatit(icao):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
    #print(sql)
    kursori = yhteys.cursor() #(dictionary=True)
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

eka = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
eka_sijainti = lentoasema_koordinaatit(eka)
#print(eka_sijainti)
lat_long_1 = eka_sijainti[0][0],eka_sijainti[0][1]
#print(lat_long_1)

toka = input("Anna toisen lentoaseman ICAO-koodi: ")
toka_sijainti = lentoasema_koordinaatit(toka)
#print(toka_sijainti)
lat_long_2 = toka_sijainti[0][0],toka_sijainti[0][1]
#print(lat_long_2)

print()
print(f"Näiden lentoasemien välinen etäisyys on {distance.distance(lat_long_1, lat_long_2).km:.4f} kilometriä.")
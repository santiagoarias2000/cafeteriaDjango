import pandas as pd
import psycopg2
from location import Coffee


class DataBase_Coffee:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='bichis162332',
            database='cafe_db',
            port='5432'
        )
        self.cursor = self.connection.cursor()
        print('DataBase connection')

    def get_seeCafe(self):
        sql = 'select  id, name, address, city, state, zip, lat, lon from coffee_shops'
        try:
            self.cursor.execute(sql)
            caffes = self.cursor.fetchall()
            return caffes
        except Exception as e:
            raise

    def get_save(self):

        sql = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (1, 'cafeteria1', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql1 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (2, 'cafeteria del bosque', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql2 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (3, 'cafeteria del sur', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql3 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (4, 'cafeteria del norte', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql4 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (5, 'cafeteria del maldonado', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql5 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (6, 'cafeteria de los muiscas', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql6 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (7, 'cafeteria de los hongos', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql7 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (8, 'cafeteria del santan ines', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql8 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (9, 'cafeteria del centro', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"
        sql9 = "insert into coffee_shops (id, name, address, city, state, zip, lat, lon) values (10, 'cafeteria del surinama', 'direccion', 'tunja', 'aa', 'zip', 222, 222)"

        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            self.cursor.execute(sql4)
            self.cursor.execute(sql5)
            self.cursor.execute(sql6)
            self.cursor.execute(sql7)
            self.cursor.execute(sql8)
            self.cursor.execute(sql9)
            self.connection.commit()
        except Exception as e:
                raise

    def get_search(self, lag, lon, ran):
        sql = "SELECT* FROM coffee_shops WHERE ST_DWithin(geom, ST_MakePoint('{}','{}')::geography, {})".format(lag,lon, ran)
        try:
            self.cursor.execute(sql)
            cafe_search = self.cursor.fetchone()
            return cafe_search
        except Exception as e:
            raise



data = DataBase_Coffee()
print('Coffes Shops')
coffe_shop = int(input('1) See data. 2) Save data. 3) Search data.'))

if coffe_shop == 1:
    count = 1
    while count < 4:
        print('.')
        count = count + 1
    coffes = data.get_seeCafe()
    for cofe in coffes:
        print(cofe)


if coffe_shop == 2:
    count = 1
    while count < 4:
        print('.')
        count = count + 1
    coffes = data.get_save()
    print('Save data')

if coffe_shop == 3:
    lag = float(input('Data of lag:'))
    lon = float(input('Data of lon:'))
    ran = float(input('Data of ran:'))
    count = 1
    while count < 4:
        print('.')
        count = count + 1
    coffes = data.get_search(lag, lon, ran)
    print(coffes)








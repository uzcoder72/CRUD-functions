from datetime import datetime
from typing import Optional
import psycopg2
db_name = 'n47'
password = '123'
host = 'localhost'
port = 5432
user = 'postgres'
def create_table():
    global connection, connection, connection, cursor, connection, connection, cursor
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(120) NOT NULL,
            image VARCHAR(300),
            is_liked BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error creating table:", error)


def insert_products_data(name, image, is_liked):
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        insert_query = '''
        INSERT INTO Products (name, image, is_liked)
        VALUES (%s, %s, %s);
        '''
        cursor.execute(insert_query, (name, image, is_liked))
        connection.commit()
        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error inserting data:", error)

def select_data():
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        select_query = '''
        SELECT id, name, image, is_liked, created_at, updated_at
        FROM Products;
        '''
        cursor.execute(select_query)
        records = cursor.fetchall()

        for record in records:
            print(record)

    except (Exception, psycopg2.Error) as error:
        print("Ma'lumotlarni olishda xatolik:", error)


def update_data(id, new_name, is_liked):
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        update_query = f'''
        UPDATE Products
        SET name = '{new_name}', is_liked = {is_liked}
        WHERE id = {id};
        '''
        cursor.execute(update_query)
        connection.commit()
        print(f"Ma'lumot {id} raqamli mahsulot uchun yangilandi!")

    except (Exception, psycopg2.Error) as error:
        print("Ma'lumotni yangilashda xatolik:", error)


def delete_data(id):
    try:
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        delete_query = f'''
        DELETE FROM Products
        WHERE id = {id};
        '''
        cursor.execute(delete_query)
        connection.commit()
        print(f"Ma'lumot {id} raqamli mahsulotni o'chirildi!")

    except (Exception, psycopg2.Error) as error:
        print("Ma'lumotni o'chirishda xatolik:", error)
conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='123',
                        host='localhost',
                        port=5432)
cur = conn.cursor()
class Product:
    def __init__(self,
                 name: str,
                 image: Optional[str] = None,
                 is_liked: bool = False,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None
                 ):
        self.name = name
        self.image = image
        self.is_liked = is_liked
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    @staticmethod
    def get_all():
        select_product_all = '''select * from products;'''
        cur.execute(select_product_all)
        rows = cur.fetchall()
        for i in rows:
            print(i)

    def save(self):
        insert_product_obj = '''insert into products (name,image,is_liked,created_at,updated_at) values (%s,%s,%s,%s,%s);'''
        data = (self.name, self.image, self.is_liked, self.created_at, self.updated_at)
        cur.execute(insert_product_obj, data)
        conn.commit()


iphone = Product('Iphone', 'Image', True)
iphone.save()
(Product.get_all())

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def select_one_data(self):
        try:
            connection = psycopg2.connect(
                host=host,
                database=db_name,
                user=user,
                password=password
            )
            cursor = connection.cursor()

            select_query = f'''
            SELECT id, name, image, is_liked, created_at, updated_at
            FROM Products
            WHERE id = {self.user_id};
            '''
            cursor.execute(select_query)
            record = cursor.fetchone()

            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Error fetching data:", error)

User = User(1)
User.select_one_data()

# create_table()
# insert_products_data('Telefon','https/photo.com',True)
# insert_products_data('Changyutgich','https/photocha.com',True)
# insert_products_data('Televizor','https/tvcha.com',False)
# update_data(2,'Muzlatgich',False)
# delete_data(3)
# select_data()
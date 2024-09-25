import pymysql

db = pymysql.connect(
    host='localhost',
    user='mann',
    password='mann02',
    database='test'
)

cursor = db.cursor()

def create_table():
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS menu (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item VARCHAR(100) NOT NULL,
                price DECIMAL(5,2) NOT NULL)'''
    )
    print("Table created successfully.")

def insert_record(item_name, price):
    cursor.execute("INSERT INTO menu (item, price) VALUES (%s, %s)", (item_name, price))
    db.commit()
    print(f"Inserted: {item_name} - ${price}")

def retrieve_records():
    cursor.execute("SELECT * FROM menu")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Item: {row[1]}, Price: ${row[2]:.2f}")

create_table()

insert_record("cake", 1.80)
insert_record("pasta", 2.40)
insert_record("pizza", 4.25)
insert_record("mojito", 1.2)

retrieve_records()

cursor.close()
db.close()
import csv
import mysql.connector


engine = create_engine('mysql+mysqlconnector://root:MySQL@localhost:3306/openblockschema')

mysql_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MySQL',
    database='openblockschema'
)
cursor = mysql_conn.cursor()
csv_file_path = './openblocklabs-dataset.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        insert_query = f"INSERT INTO dataset (date, wallet_address, point_value, year, month, day) VALUES ('{row['date']}', '{row['wallet_address']}', {float(row['point_value'])}, {int(row['year'])}, {int(row['month'])}, {int(row['day'])})"
        cursor.execute(insert_query)

mysql_conn.commit()

engine.dispose()

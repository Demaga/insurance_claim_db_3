import cx_Oracle
import csv

dsn_tns = cx_Oracle.makedsn('DESKTOP-QCKCHB8', '1521', service_name='XE')
connection = cx_Oracle.connect(user='Demaga', password='31415Bog', dsn=dsn_tns)

cursor = connection.cursor()

tables = ["customer", "education", "incident", "policy", "collision_type", "state", "incident_type"]

for table in tables:
    file = table + ".csv"
    query = "SELECT * FROM {}".format(table)
    cursor.execute(query)
    with open(file, "w", encoding = "utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        row = cursor.fetchone()
        while row != None:
            writer.writerow(list(row))
            row = cursor.fetchone()

cursor.close()
connection.commit()
connection.close()
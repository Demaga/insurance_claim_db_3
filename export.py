import csv
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('DESKTOP-QCKCHB8', '1521', service_name='XE')
connection = cx_Oracle.connect(user='Demaga', password='31415Bog', dsn=dsn_tns)

cursor = connection.cursor()

tables = ["customer", "education", "incident", "policy", "collision_type", "state", "incident_type"]

for t in tables:
    file = t + ".csv"
    query = "SELECT * FROM {}".format(t)
    cursor.execute(query)
    with open(file, "w", encoding = "utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        r = cursor.fetchone()
        while r != None:
            writer.writerow(list(row))
            r = cursor.fetchone()

cursor.close()
connection.commit()
connection.close()

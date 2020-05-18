import cx_Oracle
import csv
import datetime 

dsn_tns = cx_Oracle.makedsn('DESKTOP-QCKCHB8', '1521', service_name='XE')
connection = cx_Oracle.connect(user='Demaga', password='31415Bog', dsn=dsn_tns)
cursor = connection.cursor()

csv_data = dict()


with open('insurance_claims.csv', encoding='utf-8') as f:
	i = 0
	while i < 5:
		print(f.readline())
		i = i + 1


with open('insurance_claims.csv', encoding='utf-8') as f:
	headers = ['age', 'policy_number', 'policy_bind_date',
				'insured_zip', 'insured_sex',
				'insured_education_level',
				'capital-gains', 'capital-loss',
				'incident_date', 'incident_type',
				'collision_type']

	reader = csv.reader(f)
	all_headers = next(reader)

	headers_names = []
	headers_indeces = []

	i = 0
	for header in all_headers:
		if header in headers:
			headers_names.append(header)
			headers_indeces.append(i)
		i = i + 1

	k = 0
	while k < 10:
		line = f.readline()
		line = line.split(',')
		new_line = ''
		z = 0
		for i in headers_indeces:
			if z != 0:
				new_line += ',' + line[i]
			else:
				new_line += line[i]
				z = 1
		print(new_line)
		k += 1


with open('insurance_claims.csv', encoding='utf-8') as f:
	headers = ['age', 'policy_number', 'policy_bind_date',
				'insured_zip', 'insured_sex', 'policy_state',
				'insured_education_level',
				'capital-gains', 'capital-loss',
				'incident_date', 'incident_type',
				'collision_type']

	reader = csv.reader(f)
	all_headers = next(reader)

	headers_names = []
	headers_indeces = []

	i = 0
	for header in all_headers:
		if header in headers:
			headers_names.append(header)
			headers_indeces.append(i)
		i = i + 1

	print(headers_names)


	states = []
	incident_types = []
	collision_types = []
	education_types = []

	k = 0
	for line in f:
		line = line.split(',')
		new_line = ''
		z = 0
		for i in headers_indeces:
			if z != 0:
				new_line += ',' + line[i]
			else:
				new_line += line[i]
				z = 1

		k = k + 1

		new_list = new_line.split(',')

		new_list[2] = new_list[2].split('-')
		new_list[2] = datetime.datetime(int(new_list[2][2]), int(new_list[2][1]), int(new_list[2][0]))
		new_list[9] = new_list[9].split('-')
		new_list[9] = datetime.datetime(int(new_list[9][2]), int(new_list[9][1]), int(new_list[9][0]))


		state = new_list[3]
		if state not in states:
			states.append(state)
			cursor.execute(
			"""INSERT INTO
					STATE(state_name)
				VALUES
					(:state_name)
				""", state_name=state)
		incident_type = new_list[10]
		if incident_type not in incident_types:
			incident_types.append(incident_type)
			cursor.execute(
				"""INSERT INTO
						INCIDENT_TYPE(incident_type_name)
					VALUES
						(:incident_type_name)
					""", incident_type_name=incident_type)
		collision_type = new_list[11]
		if collision_type not in collision_types:
			collision_types.append(collision_type)
			cursor.execute(
				"""INSERT INTO
						COLLISION_TYPE(collision_type_name)
					VALUES
						(:collision_type_name)
					""", collision_type_name=new_list[11])
		education_type = new_list[6]
		if education_type not in education_types:
			education_types.append(education_type)
			cursor.execute(
				"""INSERT INTO
						EDUCATION(education_type_name)
					VALUES
						(:education_type_name)
					""", education_type_name=new_list[6])
		cursor.execute(
			"""INSERT INTO
					POLICY(policy_number, bind_date, state_name)
				VALUES
					(:policy_number, :policy_bind_date, :state_name)
				""", policy_number=new_list[1], policy_bind_date=new_list[2], state_name=new_list[3])
		cursor.execute(
			"""INSERT INTO
					CUSTOMER(age, zip, sex, education_type_name, policy_number)
				VALUES
					(:age, :zip, :sex, :education_type_name, :policy_number)
				""", age=new_list[0], zip=new_list[4], sex=new_list[5],
					education_type_name=new_list[6], policy_number=new_list[1])
		cursor.execute(
			"""INSERT INTO
					incident(capital_gains, capital_loss, policy_number, incident_type_name, collision_type_name, incident_date)
				VALUES
					(:capital_gains, :capital_loss, :policy_number, :incident_type_name, :collision_type_name, :incident_date)
				""", capital_gains=new_list[7], capital_loss=new_list[8], policy_number=new_list[1],
					incident_type_name=new_list[10], collision_type_name=new_list[11],
					incident_date=new_list[9])

		print("successfuly inserted")



	cursor.close()
	connection.commit()
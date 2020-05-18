import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import re
import chart_studio
import chart_studio.dashboard_objs as dashboard


chart_studio.tools.set_credentials_file(username = 'demaga1234', api_key = 'jAF9Tt02z1oeefyO7mj2')

def fileId_from_url(url):
    raw_fileID = re.findall("~[A-z0-9]+/[0-9]+", url)[0][1:]
    return raw_fileID.replace('/', ':')

 
dsn_tns = cx_Oracle.makedsn('DESKTOP-QCKCHB8', '1521', service_name='XE')
connection = cx_Oracle.connect(user='Demaga', password='31415Bog', dsn=dsn_tns)


##################################################################
# TOTAL NUMBER OF CLIENTS BY EDUCATION - BAR CHART
##################################################################
cursor = connection.cursor()
 
cursor.execute("""
SELECT
    education_type_name,
    COUNT(education_type_name) as education_count   
FROM 
    customer_education_incident
GROUP BY
    education_type_name""")
 

degrees = []
count = []
 

print("\nClients by education level")
for row in cursor:
    print(row[0] + ": " + str(row[1]))
    degrees.append(row[0])
    count.append(row[1])

 
data = [go.Bar(
            x=degrees,
            y=count
    )]
 
layout = go.Layout(
    title='Total # of clients with a corresponding degree',
    xaxis=dict(
        title='Degree',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='# of clients',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
 
clients_education = py.plot(fig, filename='clients_education')
 
 
##################################################################
# CAPITAL LOSS BY SEX - PIE CHART
##################################################################
cursor.execute("""
SELECT
    sex,
    SUM(capital_loss)
FROM (
    SELECT
        capital_loss,
        sex,
        policy_number
    FROM
        customer_education_incident
)
GROUP BY
    sex
""")
 

sex = []
total_loss = []
 

print("\nCapital loss by sex")
for row in cursor:
    print(row[0] + ": " + str(row[1]))
    sex.append(row[0])
    total_loss.append(abs(row[1]))

 
data = [go.Pie(
            labels=sex,
            values=total_loss
    )]
 
layout = go.Layout(
    title='Total amount of clients\' capital loss by sex',
    xaxis=dict(
        title='Degree',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='# of clients',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
 
capital_loss_by_sex = py.plot(fig, filename='capital_loss_by_sex')
 



##################################################################
# CAPITAL LOSS BY SEX - PIE CHART
##################################################################
cursor.execute("""
SELECT 
    COUNT(incident_date),
    incident_date
FROM 
    customer_education_incident
GROUP BY
    incident_date
""")
 

incident_dates = []
number_of_incidents = []
 

print("\nDynamic of incidents")
for row in cursor:
    incident_date = row[1]
    incident_date = incident_date.date()
    print(str(incident_date) + ": " + str(row[0]))
    incident_dates.append(incident_date)
    number_of_incidents.append(row[0])

incident_dates.sort() 

incidents_by_date = go.Scatter(
    x=incident_dates,
    y=number_of_incidents,
    mode='lines+markers'
)
data = [incidents_by_date]
layout = go.Layout(title='Dynamic of the amount of incidents by day',
    xaxis=dict(
        range=[incident_dates[0], incident_dates[-1]],
        title='Day',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='# of incidents',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ))
fig = go.Figure(data=data, layout=layout)
dynamic_of_incidents = py.plot(fig, filename='dynamic_of_incidents')



dboard = dashboard.Dashboard()

clients_education_id = fileId_from_url(clients_education)
capital_loss_by_sex_id = fileId_from_url(capital_loss_by_sex)
dynamic_of_incidents_id = fileId_from_url(dynamic_of_incidents)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': clients_education_id,
    'title': 'Clients\' education level'
}
 
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': capital_loss_by_sex_id,
    'title': 'Total capital loss by sex'
}
 
box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': dynamic_of_incidents_id,
    'title': 'Dynamic of incidents by date'
}
 
 
dboard.insert(box_1)
dboard.insert(box_2, 'below', 1)
dboard.insert(box_3, 'left', 2)
 

py.dashboard_ops.upload(dboard, 'Insurance Claims Data')

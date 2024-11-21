import mysql.connector
import json

def handler(context, event):
    mydb = mysql.connector.connect(
        host="10.4.110.208",
        user="root",
        password="test",
        database="dzhw",
        port="3306"
    )
    cur = mydb.cursor()
    cur.execute('''SELECT * FROM users''')
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    cur.close()
    return context.Response(body=json.dumps(json_data, default = str),
							headers={},
							content_type='text/plain',
							status_code=200)

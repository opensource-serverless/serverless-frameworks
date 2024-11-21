import mysql.connector
import json

def main():
    mydb = mysql.connector.connect(
        host="vmserverless0.dzhw.local",
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
    return json.dumps(json_data, default = str)
import functions_framework
import pymysql

import json
import time

@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)

    map = dict()
    map["message"] = ""

    if request_json and 'action' in request_json and request_json['action']=="put":
        try:
            conn = pymysql.connect(
                host="34.95.142.61",
                port = 3306,
                user="root",
                password="cU`6mrvPVFjqF&p0",
                db="Blog",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("insert into Messages (message,autor,date) values ('{}','{}','{}');".format(message, autor, date))
                    conn.commit()
                    map["message"] = "put executed successfully"

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    elif request_json and 'action' in request_json and request_json['action'] == "get":
        try:
            conn = pymysql.connect(
                host="34.95.142.61",
                port = 3306,
                user="root",
                password="cU`6mrvPVFjqF&p0",
                db="Blog",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:                    
                    cursor.execute("select * from Messages ORDER BY date DESC")
                    rows = cursor.fetchall()
                    
                    if rows:                        
                        for row in rows:
                            row["date"] = row["date"].strftime("%m/%d/%Y, %H:%M:%S")
                    
                    map["message"] = "get executed successfully"
                    map["results"] = rows

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    else:
        map["message"] = "action missing or with wrong value!"

    return json.dumps(map)
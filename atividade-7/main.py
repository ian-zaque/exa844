import functions_framework
import pymysql

import json
import time

@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)

    map = {}
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

    elif request_args and 'action' in request_args and request_json['action']=="get":
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
                    
                    cursor.execute("select * from Messages where author = f{autor}")
                    
                    rows = cursor.fetchall()
                    map["message"] = "get executed successfully"
                    map["results"] = rows

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    else:
        map["message"] = "action missing or with wrong value!"

    return json.dumps(map)
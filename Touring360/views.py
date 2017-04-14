from django.http import HttpResponse
#Importing needed modules of PyMySQL
from pymysql import connect, err, sys, cursors


#Doing our connection
conn = connect(host='mysqldb.criblyzj9wkn.us-west-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='password',
                        db='DatabaseProjectDB');




def index(request):
    cursor = conn.cursor(cursors.DictCursor);
    user = 'sometourist@mail.com'
    cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
    data = cursor.fetchall()
    return HttpResponse(data)

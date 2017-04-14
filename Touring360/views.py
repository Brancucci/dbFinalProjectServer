from django.http import HttpRequest
from django.http import HttpResponse
#Importing needed modules of PyMySQL
from django.http import JsonResponse
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

"""
to get:
try --- request.content.key

to respond:
>>> from django.http import JsonResponse
>>> response = JsonResponse({'foo': 'bar'})
>>> response.content
b'{"foo": "bar"}'
"""


def login(request):
    user = request.GET.email
    password = request.GET.password
    cursor = conn.cursor(cursors.DictCursor);
    cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
    data = cursor.fetchall()
    print(data)
    if not data[0].password == password:
        #wrong password
        pass
    else:
        # user password matches password
        return HttpResponse(JsonResponse({
            'notFound': False,
            'wrongPassword': False,
            'success': True,
            'user': data[0]}))

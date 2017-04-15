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
    return HttpResponse("My home page!!")

    """
    if request.method == 'GET':
        cursor = conn.cursor(cursors.DictCursor);
        user = request.GET['email']
        cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
        data = cursor.fetchall()

        return HttpResponse("Testing: " + data[0]["email"] + " password" + data[0]["password"])
    elif request.method == 'POST':
        user = request.POST['email']
        password = request.POST['password']
        cursor = conn.cursor(cursors.DictCursor);
        cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", str(user))
        data = cursor.fetchall()
        return HttpResponse(data)
    else:
        return HttpResponse("failure")

    conn.close()

"""
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
    user = ""
    if request.method == 'GET':
        cursor = conn.cursor(cursors.DictCursor);
        try:
            user = request.GET['email']
            password = request.GET['password']
            cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
            data = cursor.fetchall()
        except KeyError:
            return HttpResponse("Key Error")
        else:
            if data:
                if data[0]["password"] != password:
                    # wrong password
                    return HttpResponse(JsonResponse({
                        'notFound': False,
                        'wrongPassword': True,
                        'success': False,
                    }))
                else:
                    # user password matches password
                    return HttpResponse(JsonResponse({
                        'notFound': False,
                        'wrongPassword': False,
                        'success': True,
                        }))
            else:
                return HttpResponse(JsonResponse({
                    'notFound': True,
                    'wrongPassword': False,
                    'success': False,
                }))










from django.http import HttpRequest
from django.http import HttpResponse
#Importing needed modules of PyMySQL
from django.http import JsonResponse
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from pymysql import connect, err, sys, cursors


#Doing our connection
conn = connect(host='mysqldb.criblyzj9wkn.us-west-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='password',
                        db='DatabaseProjectDB');


def index(request):
    return HttpResponse("My home page")

    # if request.method == 'POST':
    #     try:
    #         body_unicode = request.body.decode('utf-8')
    #         body = json.loads(body_unicode)
    #         user = body['email']
    #         password = body['password']
    #         cursor = conn.cursor(cursors.DictCursor);
    #         cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", str(user))
    #         data = cursor.fetchall()
    #     except KeyError:
    #         return HttpResponse("Key Error")
    #     else:
    #         if data:
    #             if data[0]["password"] != password:
    #                 # wrong password
    #                 return HttpResponse(JsonResponse({
    #                     'notFound': False,
    #                     'wrongPassword': True,
    #                     'success': False,
    #                 }))
    #             else:
    #                 # user password matches password
    #                 return HttpResponse(JsonResponse({
    #                     'notFound': False,
    #                     'wrongPassword': False,
    #                     'success': True,
    #                     }))
    #         else:
    #             return HttpResponse(JsonResponse({
    #                 'notFound': True,
    #                 'wrongPassword': False,
    #                 'success': False,
    #             }))
    #
    #     return HttpResponse(data)
    # else:
    #     return HttpResponse("Was not a post method")

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

@method_decorator(csrf_exempt)
def login(request):
    user = ""
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = body['email']
            password = body['password']
            cursor = conn.cursor(cursors.DictCursor);
            cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
            data = cursor.fetchall()
        except KeyError:
            return HttpResponse("Key error 1")
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
    else:
        return HttpResponse("You must pass parameters (A body) to this url")




            # try:
            #     user = request.GET['email']
            #     password = request.GET['password']
            #     cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
            #     data = cursor.fetchall()
            # except KeyError:
            #     return HttpResponse("Key Error 2")
            # else:
            #     if data:
            #         if data[0]["password"] != password:
            #             # wrong password
            #             return HttpResponse(JsonResponse({
            #                 'notFound': False,
            #                 'wrongPassword': True,
            #                 'success': False,
            #             }))
            #         else:
            #             # user password matches password
            #             return HttpResponse(JsonResponse({
            #                 'notFound': False,
            #                 'wrongPassword': False,
            #                 'success': True,
            #                 }))
            #     else:
            #         return HttpResponse(JsonResponse({
            #             'notFound': True,
            #             'wrongPassword': False,
            #             'success': False,
            #         }))










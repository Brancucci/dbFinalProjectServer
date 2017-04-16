from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
import json
import time
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pymysql import connect, err, sys, cursors


#our connection
conn = connect(host='mysqldb.criblyzj9wkn.us-west-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='password',
                        db='DatabaseProjectDB');


def index(request):
    return HttpResponse("My home page")


@method_decorator(csrf_exempt)
def login(request):
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


@method_decorator(csrf_exempt)
def register(request):
    if request.method == 'POST':
        # get the body of the post request
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = body['email']
            password = body['password']
            phone = body['phone']
            city = body['city']
            country = body['country']
            address = body['address']
            firstName = body['firstName']
            lastName = body['lastName']
            date = time.strftime("%Y-%m-%d")
        except KeyError:
            return HttpResponse(JsonResponse({
                'error': True,
                'taken': False,
                'success': False,
            }))
        else:
            # check user exists
            cursor = conn.cursor(cursors.DictCursor);
            cursor.execute("SELECT * FROM `USERS` WHERE `email` = %s", user)
            data = cursor.fetchall()
            if data:
                #user already exists
                return HttpResponse(JsonResponse({
                    'error': False,
                    'taken': True,
                    'success': False,
                }))
            else:
                # Create a new record
                sql = "INSERT INTO USERS (email, password, signup_date, phone, city, country, address, first_name, last_name) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (user, password, date, phone, city, country, address, firstName, lastName))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                conn.commit()
                return HttpResponse(JsonResponse({
                    'error': False,
                    'taken': False,
                    'success': True,
                }))
    else:
        return HttpResponse("You must pass parameters (A body) to this url")


@method_decorator(csrf_exempt)
def search_city(request):
    if request.method == 'GET':
        startDate = ""
        endDate = ""
        try:
            startDate = request.GET['start_available_date']
            endDate = request.GET['end_available_date']
        except KeyError as e:
            print(e)
            pass
        try:
            cursor = conn.cursor(cursors.DictCursor);
            city = request.GET['city']
            if startDate:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `city` = %s AND `start_available_date` <= %s AND `end_available_date` >= %s",
                               (city, startDate, endDate))
            else:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `city` = %s", city)
            data = cursor.fetchall()
        except KeyError as e:
            print(e)
            return HttpResponse(JsonResponse({
                'error': True,
                'found': False,
            }))
        else:
            if not data:
                # no results
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': False,
                }))
            else:
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': True,
                    'results': data,
                }))
    else:
        return HttpResponse("You cannot pass parameters to this call")


@method_decorator(csrf_exempt)
def search_country(request):
    if request.method == 'GET':
        startDate = ""
        endDate = ""
        try:
            startDate = request.GET['start_available_date']
            endDate = request.GET['end_available_date']
        except KeyError as e:
            print(e)
            pass
        try:
            cursor = conn.cursor(cursors.DictCursor);
            country = request.GET['country']
            if country == 'US' or country == 'USA' or country == 'us' or country == 'usa':
                country = 'United States'
            if startDate:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `country` = %s AND `start_available_date` <= %s AND `end_available_date` >= %s",
                               (country, startDate, endDate))
            else:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `country` = %s", country)
            data = cursor.fetchall()
        except KeyError as e:
            print(e)
            return HttpResponse(JsonResponse({
                'error': True,
                'found': False,
            }))
        else:
            if not data:
                # no results
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': False,
                }))
            else:
                # return results
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': True,
                    'results': data,
                }))


@method_decorator(csrf_exempt)
def search_city_country(request):
    if request.method == 'GET':
        startDate = ""
        endDate = ""
        try:
            startDate = request.GET['start_available_date']
            endDate = request.GET['end_available_date']
        except KeyError as e:
            print(e)
            pass
        try:
            cursor = conn.cursor(cursors.DictCursor);
            city = request.GET['city']
            country = request.GET['country']
            if country == 'US' or country == 'USA' or country == 'us' or country == 'usa':
                country = 'United States'
            if startDate:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `city` = %s AND `country` = %s AND `start_available_date` <= %s AND `end_available_date` >= %s",
                               (city, country, startDate, endDate))
            else:
                cursor.execute("SELECT * FROM `HOSTS` WHERE `city` = %s AND `country` = %s", (city, country))
            data = cursor.fetchall()
        except KeyError as e:
            print(e)
            return HttpResponse(JsonResponse({
                'error': True,
                'found': False,
            }))
        else:
            if not data:
                # no results
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': False,
                }))
            else:
                # return results
                return HttpResponse(JsonResponse({
                    'error': False,
                    'found': True,
                    'results': data,
                }))











#Importing needed modules of PyMySQL
from pymysql import connect, err, sys, cursors


#Doing our connection
conn = connect(host='mysqldb.criblyzj9wkn.us-west-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='password',
                        db='DatabaseProjectDB');

# #Setting cursors and defining type of returns we need from Database, here it's gonna be returning as dictionary data
# cursor = conn.cursor(cursors.DictCursor);
# cursor.execute("SELECT * FROM `HOSTS`")
# data = cursor.fetchall()
# print(data)

# user = "donjajo"
# cursor.execute( "SELECT * FROM `test_user` WHERE `user_name` = %s", ( user ) )
# data = cursor.fetchall()
# print( data )

"""
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
"""
# cursor.execute( "INSERT INTO `test_user` ( `user_name`, `user_email` ) VALUES( 'donjajo', 'donjajo@example.com' ) ")

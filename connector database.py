import mysql.connector
try:
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='25k8809faris'
    )
    mycursor=mydb.cursor()
    mycursor.execute('Create database kerala45')
except mysql.connector.Error as err:
    print('Something went wrong:{}'.format(err))

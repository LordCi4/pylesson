import mysql.connector



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sr lordhellum',
    database='appdata'
)



class store:


    def prnt(self):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM store")
        s = mycursor.fetchall()

        print('Producto  marca   precio')
        for x in s:

            print(x[1]," ",  x[2]," ",  x[3])

str = store()

str.prnt()


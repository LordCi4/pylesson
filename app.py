import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sr lordhellum',
    database='appdata'
)



class store:
    def __init__(self, product, brand, price):

        self.product = product
        self.brand = brand
        self.price = price


    def valdt(self):
        mycursor = mydb.cursor()


        mycursor.execute('INSERT IGNORE INTO store (product, brand, price) '
            'VALUES (%s, %s, %s)', (self.product, self.brand, self.price))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")





class storePnt:
    def prnt(self):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM store")
        s = mycursor.fetchall()

        print('<------------------------------------->')
        print('Producto  marca   precio')

        for x in s:

            print(x[1]," ",  x[2]," ",  x[3])

    def plus(self):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT SUM(price) FROM store")
        s = mycursor.fetchall()

        print('<------------------------------------->')
        for row in s:
            total = "total es: "
            print('{}'.format(total), row[0])


#SCRIPT PARA GUARDAR LA COMPRA  EN LA BASE DE DATOS
pro = input("porducto: ")
brn = input("marca: ")
prc = input("precio: ")

str = store(pro, brn, prc)
str.valdt()

#SCRIPT PARA IMPRIMIR LA FACTURA Y EL TOTAL DE LOS PRECIOS
st = storePnt()

st.prnt()
st.plus()










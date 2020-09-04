import sqlite3


def createCustomerTable():  #function to create the data base and its values 
    con=sqlite3.connect('property.db') #connects to the property database or creates it if doesnt exist
    cursor=con.cursor()#alloes for database manipulation
    cursor.execute("PRAGMA foreign_keys = ON")


    #creates a table called bookings if doesnt exist and then creates these fields into the table
    cursor.execute('CREATE TABLE IF NOT EXISTS Customer(\
            idc integer PRIMARY KEY AUTOINCREMENT,\
            first_name text,\
            surname text,\
            birth_date text,\
            phone_number text,\
            email text)')
          
    con.commit() #adds the table and fields to the database
    con.close() #closes the database

def addCustomerData(first_name='',surname='',birth_date='',phone_number='',email=''):#function to add the data entered into the data base
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
 
    cursor.execute('INSERT INTO Customer (first_name,surname,birth_date,phone_number,email) VALUES (?,?,?,?,?)',(\
        first_name,surname,birth_date,phone_number,email)) 
    con.commit() #adds the data to the database

    con.close() ##closes the database

def createCustomerBookingTable():
    con=sqlite3.connect('property.db') #connects to the property database or creates it if doesnt exist
    cursor=con.cursor()#alloes for database manipulation
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('CREATE TABLE IF NOT EXISTS CustomerBooking(\
            cust_id integer NOT NULL,\
            cust_flat text NOT NULL,\
            FOREIGN KEY (cust_id) REFERENCES Customer(idc) ON DELETE CASCADE,\
            FOREIGN KEY (cust_flat) REFERENCES Bookings(flat_name) ON DELETE CASCADE ON UPDATE CASCADE,\
            PRIMARY KEY (cust_id,cust_flat) )')

    con.commit()
    con.close()
        
def addCustomerBooking(cust_id,cust_flat):
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
 
    cursor.execute('INSERT INTO CustomerBooking (cust_id,cust_flat) VALUES (?,?)',(cust_id,cust_flat))
    con.commit()
    con.close()

def getCustomerName():

    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the flat name and status from the status table
    cursor.execute(f'SELECT idc,first_name,surname FROM Customer')
    name_list=cursor.fetchall()
    names=[]
    for i in name_list:
        name=[]
        name.append(str(i[0])+' '+i[1] +' '+i[2])

        names.append(name)

        
    con.close()
    return names

def getCustomerID(first_name,surname):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the flat name and status from the status table
    cursor.execute('SELECT idc FROM Customer WHERE first_name=? AND surname=?',(first_name,surname,))
    cust_id=cursor.fetchall()
    cust_id=cust_id[0][0]
    
    con.close()
    return cust_id

def getCustomerData(id,first_name,surname):
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('SELECT Bookings.flat_name FROM (Property INNER JOIN Bookings ON Property.flat_name = Bookings.flat_name) \
    INNER JOIN (Customer INNER JOIN CustomerBooking ON Customer.idc = CustomerBooking.cust_id) ON \
    Bookings.flat_name = CustomerBooking.cust_flat WHERE Customer.idc=? AND Customer.first_name=? AND \
    Customer.surname=?',(id,first_name,surname,))

    cust_flats=cursor.fetchall()

    cursor.execute('SELECT birth_date,phone_number,email FROM Customer WHERE first_name=? AND surname=?',(first_name,surname,))
    cust_data=cursor.fetchall()
    con.close()
    return cust_flats,cust_data

def deleteBookingWithCustomer(first_name,surname,id):

    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('DELETE FROM Bookings WHERE EXISTS (SELECT CustomerBooking.cust_flat\
    FROM Property INNER JOIN (Customer INNER JOIN CustomerBooking ON Customer.idc = CustomerBooking.cust_id) ON \
    Property.flat_name = CustomerBooking.cust_flat\
    WHERE Customer.first_name=? AND Customer.surname=? AND Customer.idc=? AND Bookings.flat_name=Property.flat_name)',(first_name,surname,id))

    con.commit()
    con.close()

   
def updateCustomerData(id,first_name,surname,birth_date,phone_number,email):
    con=sqlite3.connect('property.db') #updates the row
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('UPDATE Customer SET first_name=?,surname=?,birth_date=?,phone_number=?,email=? WHERE idc=?',\
        (first_name,surname,birth_date,phone_number,email,id)) #updates the fields using these data variables
  
    con.commit()
    con.close()


def searchCustomerData(string,variable):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute(f'SELECT * FROM Customer WHERE {string}',\
            (variable)) #this looks for all rows in the table that are equal to the data

    except:
        pass
                                                                                           
    #returns values that meet this criteria
    row=cursor.fetchall()
    con.close()

   
    return row
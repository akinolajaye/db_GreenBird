import sqlite3

import datetime


def createBookingTable():  #function to create the data base and its values 
    con=sqlite3.connect('property.db') #connects to the property database or creates it if doesnt exist
    cursor=con.cursor()#alloes for database manipulation
    cursor.execute("PRAGMA foreign_keys = ON")


    #creates a table called bookings if doesnt exist and then creates these fields into the table
    cursor.execute('CREATE TABLE IF NOT EXISTS Bookings(\
            idb integer PRIMARY KEY AUTOINCREMENT,\
            duration integer,\
            start_date text,\
            end_date text,\
            num_of_people integer,\
            flat_name text UNIQUE,\
            rent_due_date text,\
            FOREIGN KEY (flat_name) REFERENCES Property(flat_name) ON DELETE CASCADE ON UPDATE CASCADE)')
          
    con.commit() #adds the table and fields to the database
    con.close() #closes the database


def addBookingsData(duration='',start_date='',end_date='',num_of_people='',\
    flat_name='',rent_due_date=''):#function to add the data entered into the data base
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
 
    cursor.execute('INSERT INTO Bookings (duration,start_date,end_date,num_of_people,\
    flat_name,rent_due_date) VALUES (?,?,?,?,?,?)',(\
        duration,start_date,end_date,num_of_people,flat_name,rent_due_date)) 
    con.commit() #adds the data to the database

    con.close() ##closes the database

def searchBookingsData(string,variables):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    #add for names
    try:
        cursor.execute(f'SELECT Bookings.*,Customer.first_name,Customer.surname FROM Bookings JOIN Customer \
        JOIN CustomerBooking ON Bookings.flat_name=CustomerBooking.cust_flat AND Customer.idc=CustomerBooking.cust_id WHERE {string}',\
           variables) #this looks for all rows in the table that are equal to the data
                      
    except:
        pass
    #Create a string thaat generates sentence

    bookings=cursor.fetchall()#fetches and stores the row

    bookings_list=[]
    for i in range(len(bookings)):
        books=[]
        for j in range(len(bookings[i])):
            books.append(bookings[i][j])

        first_name=books.pop(-2)
        surname=books.pop(-1)
        name=first_name+' '+surname
        books.insert(1,name)
        bookings_list.append(books)    

    con.close()
    
    return bookings_list #the rows are returened to be used in the gui



def updateBookingsData(id,duration,start_date,num_of_people,flat_name,rent_due_date):
    con=sqlite3.connect('property.db') #updates the row
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('UPDATE Bookings SET duration=?,start_date=?,num_of_people=?,\
    flat_name=?,rent_due_date=?,phone_number=?,email=? WHERE idb=?',\
        (duration,start_date,num_of_people,flat_name,rent_due_date,phone_number,email,id)) #updates the fields using these data variables
  
    con.commit()
    con.close()

def getNumOccpts(flat_name):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the number of occupants
    cursor.execute('SELECT num_of_people FROM Bookings WHERE flat_name=?',(flat_name,))
    occpts=cursor.fetchall()
    occpts=occpts[0][0]
    con.close()

    return occpts

def getFlatName():
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the flat name and status from the status table
    cursor.execute('SELECT flat_name,status FROM Property')
    flat=cursor.fetchall()
    con.close()

    return flat

def getAvailableFlats():
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('SELECT flat_name FROM Bookings')
    booked_flats=cursor.fetchall()

    cursor.execute('SELECT flat_name FROM Property')
    all_flats=cursor.fetchall()

    con.close()



    booked_flats_list=[]
    for i in booked_flats:
        booked_flats_list.append(i[0])

    all_flats_list=[]
    for i in all_flats:
        all_flats_list.append(i[0])

    available_flats=[]

    for i in range(len(all_flats_list)):
        if all_flats_list[i] not in booked_flats_list:

            available_flats.append(all_flats_list[i])


    return available_flats

def getRentPrice(flat_name): #gets the rent price based on flat name
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('SELECT rent_price FROM Property WHERE flat_name=?',(flat_name,))
    price=cursor.fetchall()
    price=price[0][0]
    con.close()
    
    return price

def getAllFlats():
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets all flat names of those that have been booked
    cursor.execute('SELECT flat_name FROM Bookings')
    flats=cursor.fetchall()
    con.close()

    flat_list=[]
    for i in flats:
        flat_list.append(i[0])

    return flat_list


def viewData():
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute(f'SELECT Bookings.*,Customer.first_name,Customer.surname FROM Bookings JOIN Customer \
    JOIN CustomerBooking ON Bookings.flat_name=CustomerBooking.cust_flat AND Customer.idc=CustomerBooking.cust_id') #the * means all and so this selects all rows from the table property
    bookings=cursor.fetchall()#fetches and stores the row


    bookings_list=[]
    for i in range(len(bookings)):
        books=[]
        for j in range(len(bookings[i])):
            books.append(bookings[i][j])

        first_name=books.pop(-2)
        surname=books.pop(-1)
        name=first_name+' '+surname
        books.insert(1,name)
        bookings_list.append(books)




        
    

    con.close()
    
    return bookings_list #the rows are returened to be used in the gui
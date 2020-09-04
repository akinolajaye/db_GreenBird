import sqlite3


#=======================================================================Create Property and Status Databas============================================================================   
def createPropertyTable():#function to create the data base and its values
    con=sqlite3.connect('property.db')#connects to the property database or creates it if doesnt exist

    cursor =con.cursor() #allows for database manipulation
    cursor.execute("PRAGMA foreign_keys = ON")

    #creates a table called property if doesnt exist and puts these values into the table
    cursor.execute(f'CREATE TABLE IF NOT EXISTS Property(\
            idp INTEGER PRIMARY KEY AUTOINCREMENT,\
            flat_name text UNIQUE,\
            flat_num integer,\
            post_code text,\
            town text,\
            city text,\
            bathrooms text,\
            bedrooms text,\
            rent_price integer)')
    con.commit()#adds the table and fields to the database
    con.close()#closes the database
        

#=======================================================================Add to Data bases==================================================================================================================

def addPropertyData(flat_name,flat_num,post_code,town,city,bathrooms,bedrooms,rent_price):#function to add the data entered into the data base
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
 
    cursor.execute(f'INSERT INTO Property (flat_name,flat_num,post_code,town,city,bathrooms,bedrooms,rent_price) VALUES (?,?,?,?,?,?,?,?)',\
        (flat_name,flat_num,post_code,town,city,bathrooms,bedrooms,rent_price)) #adds each variable to the fields in the database
    con.commit() #adds the data to the database
          
      
##=======================================================================Database Functions========================================================================================

def viewData(table):
    con=sqlite3.connect('property.db')#connects to property database
    cursor =con.cursor()#initiates a cursor from sql which allows access and manipulation of data in sql table and rows
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute(f'SELECT * FROM {table}') #the * means all and so this selects all rows from the table property
    row=cursor.fetchall()#fetches and stores the row
    con.close()
    return row #the rows are returened to be used in the gui

def deleteData(id,table,sqlid):
    try:
        con=sqlite3.connect('property.db')
        cursor =con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(f'DELETE FROM {table} WHERE {sqlid}=?',(id,))#a parameter id is passed into the function to specify the data row to be deleted based on the primary key
        con.commit()
        con.close()
    except:
        pass

    return
   
def searchPropertyData(string,variable):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute(f'SELECT * FROM Property WHERE {string}',\
            (variable)) #this looks for all rows in the table that are equal to the data

    except:
        pass
                                                                                           
    #returns values that meet this criteria
    row=cursor.fetchall()
    con.close()

   
    return row

def updatePropertyData(id,flat_name,flat_num,post_code,town,city,bathrooms,bedrooms,rent_price):
    con=sqlite3.connect('property.db') #updates the row
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('UPDATE Property SET flat_name=?,flat_num=?,post_code=?,town=?,\
    city=?,bathrooms=?,bedrooms=?,rent_price=? WHERE idp=?',\
        (flat_name,flat_num,post_code,town,city,bathrooms,bedrooms,rent_price,id)) #updates the fields using these data variables
  
    con.commit()
    con.close()


def getLocation(flat_name):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the location information from property
    cursor.execute('SELECT flat_name,flat_num,post_code,town,city FROM Property WHERE flat_name=?',(flat_name,))
    location=cursor.fetchall()
    location=location[0]
    con.close()

    return location

def getFlatInfo(flat_name):


    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the location information from property
    cursor.execute('SELECT * FROM Property WHERE flat_name=?',(flat_name,))
    flat_info=cursor.fetchall()

    return flat_info

def getAllFlats():
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #gets the flat name and status from the status table
    cursor.execute('SELECT flat_name FROM Property')
    flats=cursor.fetchall()
    con.close()

    flat_list=[]
    for i in flats:
        flat_list.append(i[0])

    return flat_list
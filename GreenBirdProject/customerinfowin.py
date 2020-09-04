import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk
from tkinter import scrolledtext as st
from editdatbwin import EditDatabase
import customersql as cdbsql
import bookingsdatabasesql as bdbsql
import propertydatabasesql as pdbsql

class CustomerInfo(EditDatabase):
    def __init__(self,win,id,first_name,surname):
        self.win=win#so that win can be used in other function
        self.id,self.first_name,self.surname=id,first_name,surname
        self.customer_info_window=tk.Toplevel(win)#creates a instance of the tkinter module in the form of a new window
        self.customer_info_window.geometry('500x500')#sets a default size for the window when opened
        self.customer_info_window.resizable(0,0)
        self.createWidgets()
        self.insertCustInfo()
        

    def tupleToArray(self,table):
        new_table=[]
        for i in range(len(table)):###changes the 2d list format  from a list with tuples to a list with arrays which then allows it to be edidted eg from [(x,y)] to [[x,y]]
            t=[]
            for j in range(len(table[i])):
                t.append(table[i][j])            
            new_table.append(t)
        return new_table


    def createWidgets(self):
        
        name=self.first_name+' '+self.surname
        
        self.list_box_frame=ttk.LabelFrame(self.customer_info_window,text=name,style='MF.TLabelframe')
        self.list_box_frame.pack()
        self.createListBox(self.list_box_frame,100,12)#creates list box)
        self.listboxCommand()


    def listboxCommand(self):
        self.display_box.bind('<<ListboxSelect>>',\
            lambda event:self.SelectProperty(event))#performs the command when data is selected on the listbox


    def getCustInfo(self):
        cust_flats,cust_data=cdbsql.getCustomerData(self.id,self.first_name,self.surname)
        
        cust_flats=self.tupleToArray(cust_flats)
        cust_data=self.tupleToArray(cust_data)

        for i in range(len(cust_data)):
            cust_data[i][0]= 'Birth Date: '+cust_data[i][0]
            cust_data[i][1]= 'Phone Number: '+cust_data[i][1]
            cust_data[i][2]= 'Email: '+cust_data[i][2]
        
        return cust_flats,cust_data

    def insert(self,table):
        for i in range(len(table)):
            for j in range(len(table[i])):
               
                self.display_box.insert(tk.END,table[i][j])
        self.display_box.insert(tk.END,'')

    def insertCustInfo(self):
        
        cust_flats,cust_data=self.getCustInfo()
        cust_data[0].insert(0,'Customer info:')
        cust_flats.insert(0,['Flats Leased:'])
        
        self.insert(cust_flats)
        self.insert(cust_data)

    def SelectProperty(self,event):#*
        global sd#stands for searched data
        try:
            search=self.display_box.curselection()[0] #returns an index that is used to specify the location of the data on the listbox line i.e first line will be 0 
           
            sd =self.display_box.get(search) #returns a list of data displayed on the list box
            flat_name=sd
            flats=pdbsql.getAllFlats()
            if flat_name in flats:
                PropertyInfo(self.win,flat_name)
                
              
        except Exception as err:
            print(err)

        return


    

class PropertyInfo(CustomerInfo):
    def __init__(self,win,flat_name):
        self.flat_name=flat_name
        self.property_info_window=tk.Toplevel(win)#creates a instance of the tkinter module in the form of a new window
        self.property_info_window.geometry('500x500')#sets a default size for the window when opened
        self.property_info_window.resizable(0,0)
        self.createWidgets()
        self.insertPropertyInfo()

    def createWidgets(self):
        
       
        self.list_box_frame=ttk.LabelFrame(self.property_info_window,text=self.flat_name,style='MF.TLabelframe')
        self.list_box_frame.pack()
        self.createListBox(self.list_box_frame,100,12)#creates list box)
        

    def getFlatInfo(self):
        flats=pdbsql.getFlatInfo(self.flat_name)
        flats=self.tupleToArray(flats)

        for i in range(len(flats)):
            flats[i][1]= 'Flat Name: '+str(flats[i][1])
            flats[i][2]= 'Flat Num: '+str(flats[i][2])
            flats[i][3]= 'Post Code: '+str(flats[i][3])
            flats[i][4]= 'Town: '+str(flats[i][4])
            flats[i][5]= 'City: '+str(flats[i][5])
            flats[i][6]= 'Bathroom(s): '+str(flats[i][6])       
            flats[i][7]= 'Bedroom(s): '+str(flats[i][7])
            flats[i][8]= 'Renting Price: £'+str(flats[i][8])

        

        
        return flats


    def insertPropertyInfo(self):
        flats=self.getFlatInfo()
        flats[0][0]='Property info:'
        self.insert(flats)



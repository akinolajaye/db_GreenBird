import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk
from editdatbwin import EditDatabase
import datetime
from tkinter import scrolledtext as st
import customersql as cdbsql
import re
from tkinter import messagebox as mbx #imports a module that allows the use of pop up message boxes


class Customer(EditDatabase): #inherits from editdatabase
    def __init__(self,win):
        self.customer_window=tk.Toplevel(win)#creates a instance of the tkinter module in the form of a new window
        self.customer_window.geometry('900x370')#sets a default size for the window when opened
        self.customer_window.resizable(0,0)
        self.createStyle()
        self.createWidgets()
        self.array=[self.first_name_entry,self.surname_entry,self.birth_date_entry,self.phone_number_entry,self.email_entry]#creates a list that holds all entrys

    def createFrame(self):

        main_frame =ttk.LabelFrame(self.customer_window,text ='GreenBird Properties Bookings')#creaetes a main frame that holds all frames
        main_frame.pack(anchor ='w',fill='both')

       
        #self.data_frame=ttk.Frame(main_frame,style ='DF.TLabelframe')#creates a frame that holdd the data widgets and frames
        #self.data_frame.pack(side=tk.TOP,pady=6)
        self.data_display_frame=ttk.LabelFrame(main_frame,text='Customers:',style ='DEF.TLabelframe')#creates a labeled frame that will hold all displayed data
        self.data_display_frame.pack(side=tk.RIGHT,anchor ='nw')  
        
        self.data_entry_frame=ttk.LabelFrame(main_frame,text ='Customer Details:',style ='DEF.TLabelframe')#creates a labeled frame that will hold all data entries
        self.data_entry_frame.pack(side=tk.TOP,anchor='nw')
 
        self.button_frame=ttk.Frame(main_frame)#creates a button frame that will hold all buttons in the mainframe
        self.button_frame.pack(side=tk.LEFT)  
        
    def createLabels(self):

        #creates a label
        first_name_lbl=ttk.Label(self.data_entry_frame,text='First Name: ',style ='DEF.TLabel')
        first_name_lbl.grid(row=0,column=0)

        surname_lbl=ttk.Label(self.data_entry_frame,text='Surname:',style ='DEF.TLabel')
        surname_lbl.grid(row=1,column=0)

        birth_date_lbl=ttk.Label(self.data_entry_frame,text='Date Of Birth (dd/mm/yyyy):',style ='DEF.TLabel')
        birth_date_lbl.grid(row=2,column=0)

        phone_number_lbl=ttk.Label(self.data_entry_frame,text='Phone Number:',style ='DEF.TLabel')
        phone_number_lbl.grid(row=3,column=0)
        

        email_lbl=ttk.Label(self.data_entry_frame,text='Email: ',style ='DEF.TLabel')
        email_lbl.grid(row=4,column=0) 

    def createEntrys(self):

        first_name=tk.StringVar()# declares variables types
        surname=tk.StringVar()
        birth_date=tk.StringVar()
        phone_number=tk.StringVar()
        email=tk.StringVar() 



        #creates entries

        self.first_name_entry=ttk.Entry(self.data_entry_frame,textvariable =first_name,width=25,font =('calibri',15))
        self.first_name_entry.grid(row=0,column=1) 


        self.surname_entry=ttk.Entry(self.data_entry_frame,textvariable =surname,width=25,font =('calibri',15),)
        self.surname_entry.grid(row=1,column=1)

        self.birth_date_entry=ttk.Entry(self.data_entry_frame,textvariable =birth_date,width=25,font =('calibri',15))
        self.birth_date_entry.grid(row=2,column=1) 

        self.phone_number_entry=ttk.Entry(self.data_entry_frame,textvariable =phone_number,width=25,font =('calibri',15))
        self.phone_number_entry.grid(row=3,column=1) 


        self.email_entry=ttk.Entry(self.data_entry_frame,textvariable =email,width=25,font =('calibri',15))
        self.email_entry.grid(row=4,column=1)
    
    def createButtons(self):

        #creates click buttons
        add_datab=ttk.Button(self.button_frame,text='Add Customer',command =self.addCustomerData)
        add_datab.grid(row=0,column=0)

        search_datab=ttk.Button(self.button_frame,text='Search Customer',command=self.searchCustomerDatabase)
        search_datab.grid(row=0,column=1)

        display_datab=ttk.Button(self.button_frame,text='Display Customers',command=lambda:self.displayTable('Customer'))
        display_datab.grid(row=1,column=0)

        clear_datab=ttk.Button(self.button_frame,text='Clear',command=lambda:self.clearData(self.array))
        clear_datab.grid(row=1,column=1)

        delete_datab=ttk.Button(self.button_frame,text='Delete',command =self.delete)
        delete_datab.grid(row=2,column=0)

        update_datab=ttk.Button(self.button_frame,text='Update',command =self.updateCustomerDatabase)
        update_datab.grid(row=2,column=1)


        exitb=ttk.Button(self.button_frame,text='Exit',command=lambda:self._exit(self.customer_window))
        exitb.grid(row=3,column=0)

        for i in self.button_frame.winfo_children():
            i.configure(style= 'B.TButton')

    def createWidgets(self):
      
        self.createFrame()
        self.createLabels()
        self.createEntrys()
        self.createListBox(self.data_display_frame,35,10)
        self.listboxCommand()
        self.createButtons()

        for i in self.data_entry_frame.winfo_children():
            i.grid_configure(pady=5,sticky='w') 

    def listboxCommand(self):


        self.display_box.bind('<<ListboxSelect>>',lambda event :self.recordDisplayIndex(event,self.array))
    
    def addCustomerData(self):

        valid,empty=self.customerValid()

        if valid and not empty:
           
            cdbsql.addCustomerData(self.first_name_entry.get().upper(),self.surname_entry.get().upper(),self.birth_date_entry.get(),\
                self.phone_number_entry.get(),self.email_entry.get().upper()) #adds data from entrys and puts in sql database
            self.displayTable('Customer')

    def delete(self):


        cdbsql.deleteBookingWithCustomer(self.first_name_entry.get(),self.surname_entry.get(),self.sd[0])
        self.deleteData('Customer','idc')#deletes the row selected 


    def validEmailCheck(self):
        email=self.email_entry.get()
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
        else:

            return True

    def validNameCheck(self):
        first_name=self.first_name_entry.get()
        surname=self.surname_entry.get()

        if not re.match(r"[A-Za-z]+$",first_name):
            return False
        elif not re.match(r"[A-Za-z]+$",surname):
            return False
        else:
            return True

    def validateDate(self,date_text):
        try:
            date_text=date_text.split('/')
            date=date_text[0]+'-'+date_text[1]+'-'+date_text[2]
            datetime.datetime.strptime(date, '%d-%m-%Y')
            return True
        except:

            return False 

    def validPhonenumber(self):
        number=self.phone_number_entry.get()
        if not re.match(r"[0][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",number):
            return False
        else:

            return True



    def customerValid(self):
        valid=False
        empty=True

        empty=self.emptyEntryCheck(5)
        if empty:
            mbx.showerror('Error','Fill out all remaining fields!')
            return valid,empty

        if self.validNameCheck():
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for first name or surname \nname should have no special characters or white space!')
            return valid,empty

        if self.validateDate(self.birth_date_entry.get()):
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for birth date should be DD/MM/YYYY!')
            return valid,empty

        if self.validPhonenumber():
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for phone number!')
            return valid,empty

        if self.validEmailCheck():
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for email!')
            return valid,empty


        return valid,empty

    def updateCustomerDatabase(self):
        #updates data by inserting entry values into the the sql database

        cdbsql.updateCustomerData(self.sd[0],self.first_name_entry.get().upper(),self.surname_entry.get().upper(),\
            self.birth_date_entry.get(),self.phone_number_entry.get(),self.email_entry.get().upper())
        self.displayTable('Customer')


    def getSqlCommand(self):

        sql_string=''
        sql_variables=[]

        if self.first_name_entry.get().isspace() or self.first_name_entry.get()=='':
            pass
        else:
            sql_string+='first_name=? '
            sql_variables.append(self.first_name_entry.get().upper())

        if self.surname_entry.get().isspace() or self.surname_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='surname=? '
            else:
                sql_string+='AND surname=? '

            sql_variables.append(self.surname_entry.get().upper())

        if self.birth_date_entry.get().isspace() or self.birth_date_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='birth_date=? '
            else:
                sql_string+='AND birth_date=? '
            sql_variables.append(self.birth_date_entry.get())


        if self.phone_number_entry.get().isspace() or self.phone_number_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='phone_number=? '
            else:
                sql_string+='AND phone_number=? '
            sql_variables.append(self.phone_number_entry.get())

        if self.email_entry.get().isspace() or self.email_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='email=? '
            else:
                sql_string+='AND email=? '
            sql_variables.append(self.email_entry.get().upper())


        return sql_string,sql_variables
       
    def searchCustomerDatabase(self):
        self.display_box.delete(0,tk.END)
        #uses entry values as search criteria

        sql_string,sql_variables=self.getSqlCommand()

        for i in cdbsql.searchCustomerData(sql_string,sql_variables):
            self.display_box.insert(tk.END,i) #inserts different data into display box based on index
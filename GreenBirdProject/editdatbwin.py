import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk #imports a variant of the tk module that gives a more modern look for the gui
from tkinter import scrolledtext as st #imports the scrolled text widget
import propertydatabasesql as pdbsql #imports the sql data base file
from tkinter import messagebox as mbx #imports a module that allows the use of pop up message boxes
import bookingsdatabasesql as bdbsql #imports the sql data base file
import re

class EditDatabase(): #edit database class created

    def __init__(self,win): # win from greenbird menu module is passed as a parameter for the main parent window
        self.edit_data_window=tk.Toplevel(win)#creates a instance of the tkinter module in the form of a new window
        self.edit_data_window.geometry('1090x420')#sets a default size for the window when opened      
        self.edit_data_window.resizable(0,0)#makes the window non resizable
        self.createStyle() #calls the create style function
        self.createWidgets() #calls the create widgets function
        self.entry_ary=[self.flat_name_entry,self.flat_num_entry,self.post_code_entry,self.town_entry,self.city_entry,self.bathrooms_entry,\
                self.bedrooms_entry,self.rent_price_entry]#creates an array that holds the variables of all entries
      
#====================================================================Creates a style for differnt widgets===============================================================================================
    def createStyle(self):       
        self.database_style=ttk.Style()#calls the module for creating a format style for widgets
        self.database_style.configure('MF.TLabelframe.Label',font =('calibri light',15)) #creates a style for label
        self.database_style.configure('DEF.TLabelframe.Label',font =('calibri light',15))
        self.database_style.configure('DF.TLabelframe')
        self.database_style.configure('B.TButton',font =('calibri',13),height=3,width=16)
        self.database_style.configure('DEF.TLabel',font=('calibri light',14))
        self.database_style.configure('DEF.TEntry',font=('calibri',14))
       
    def createFrame(self):
        self.main_frame =ttk.LabelFrame(self.edit_data_window,text ='GreenBird Properties Database Management')#creaetes a main frame that holds all frames
        self.main_frame.pack(anchor ='w',fill='both')

       
        self.data_frame=ttk.Frame(self.main_frame,style ='DF.TLabelframe')#creates a frame that holdd the data widgets and frames
        self.data_frame.pack(side=tk.TOP,fill='x',pady=6)

        self.data_entry_frame=ttk.LabelFrame(self.data_frame,text ='Property Info:',style ='DEF.TLabelframe')#creates a labeled frame that will hold all data entries
        self.data_entry_frame.pack(side=tk.LEFT,anchor ='nw')
        

        self.data_display_frame=ttk.LabelFrame(self.data_frame,text='Property Details:',style ='DEF.TLabelframe')#creates a labeled frame that will hold all displayed data
        self.data_display_frame.pack(side=tk.RIGHT,anchor ='w')
        
        self.button_frame=ttk.Frame(self.main_frame)#creates a button frame that will hold all buttons in the mainframe
        self.button_frame.pack(side=tk.BOTTOM,fill='x') 

    def createLabels(self):
 
        flat_name_lbl=ttk.Label(self.data_entry_frame,text='Flat Name: ',style ='DEF.TLabel') #creates a label
        flat_name_lbl.grid(row=0,column=0) #determines the position of a label on the grid

        flat_num_lbl=ttk.Label(self.data_entry_frame,text='Flat No.: ',style ='DEF.TLabel')
        flat_num_lbl.grid(row=1,column=0)

        post_code_lbl=ttk.Label(self.data_entry_frame,text='Post Code: ',style ='DEF.TLabel')
        post_code_lbl.grid(row=2,column=0)

        town_lbl=ttk.Label(self.data_entry_frame,text='Town: ',style ='DEF.TLabel')
        town_lbl.grid(row=3,column=0)

        city_lbl=ttk.Label(self.data_entry_frame,text='City: ',style ='DEF.TLabel')
        city_lbl.grid(row=4,column=0)

        bathrooms_lbl=ttk.Label(self.data_entry_frame,text='No. of Bathrooms: ',style ='DEF.TLabel')
        bathrooms_lbl.grid(row=5,column=0)

        bedrooms_lbl=ttk.Label(self.data_entry_frame,text='No. of Bedrooms: ',style ='DEF.TLabel')
        bedrooms_lbl.grid(row=6,column=0)

        rent_price_lbl=ttk.Label(self.data_entry_frame,text='Renting Price(£): ',style ='DEF.TLabel')
        rent_price_lbl.grid(row=7,column=0)

    def createEntrys(self):

        valid =self.data_entry_frame.register(self.intEntryValidation)#declares the function that will be used as a validation for entries requiring integers
        flat_name=tk.StringVar()#declares the variable for the entry as a string
        flat_num=tk.IntVar() #declares the variable for the entry as a integer
        post_code=tk.StringVar()
        town=tk.StringVar() 
        city=tk.StringVar()
        bathrooms=tk.StringVar()
        bedrooms=tk.StringVar()      
        rent_price=tk.IntVar()       
#=============================================================Labels and Data entry ======================================================================================
        self.flat_name_entry=ttk.Entry(self.data_entry_frame,textvariable =flat_name,width=40,font =('calibri',15)) #creates a data entry widget
        self.flat_name_entry.grid(row=0,column=1)#positions the entry on the grid

        self.flat_num_entry=ttk.Entry(self.data_entry_frame,textvariable =flat_num,width=40,font =('calibri',15),\
            validate ='key',validatecommand=(valid,'%P'))#creates a data entry widget and sets the function valid as the validate command
        self.flat_num_entry.grid(row=1,column=1)

        self.post_code_entry=ttk.Entry(self.data_entry_frame,textvariable =post_code,width=40,font =('calibri',15))
        self.post_code_entry.grid(row=2,column=1)
     
        self.town_entry=ttk.Entry(self.data_entry_frame,textvariable =town,width=40,font =('calibri',15))
        self.town_entry.grid(row=3,column=1)


        self.city_entry=ttk.Entry(self.data_entry_frame,textvariable =city,width=40,font =('calibri',15))
        self.city_entry.grid(row=4,column=1)

        self.bathrooms_entry=ttk.Entry(self.data_entry_frame,textvariable =bathrooms,width=40,font =('calibri',15),\
            validate ='key',validatecommand=(valid,'%P'))
        self.bathrooms_entry.grid(row=5,column=1)

        self.bedrooms_entry=ttk.Entry(self.data_entry_frame,textvariable =bedrooms,width=40,font =('calibri',15),\
            validate ='key',validatecommand=(valid,'%P'))
        self.bedrooms_entry.grid(row=6,column=1)


        self.rent_price_entry=ttk.Entry(self.data_entry_frame,textvariable =rent_price,width=40,font =('calibri',15),\
            validate ='key',validatecommand=(valid,'%P'))
        self.rent_price_entry.grid(row=7,column=1)  

        for i in self.data_entry_frame.winfo_children(): #creates a for loop for each widget in the data entry frame
            i.grid_configure(pady=5,sticky='w') #configures the padding and position of each widget

    def createButtons(self):

#==========================================================================Buttons=======================================================================================

        self.add_datab=ttk.Button(self.button_frame,text='Add New',command =self.addPropertyData) #creates a button that when clicked performs the command addpropertydata
        self.add_datab.grid(row=0,column=0) #positions the button on the grid within its frame

        self.search_datab=ttk.Button(self.button_frame,text='Search',command =self.searchPropertyDatabase)
        self.search_datab.grid(row=0,column=1)

        self.display_datab=ttk.Button(self.button_frame,text='Display',command =self.displayTable)
        self.display_datab.grid(row=0,column=2)

        self.clear_datab=ttk.Button(self.button_frame,text='Clear',command= lambda:self.clearData(self.entry_ary))#lambda allows parameters to be passed into the command
        self.clear_datab.grid(row=0,column=3)

        self.delete_datab=ttk.Button(self.button_frame,text='Delete',command =self.delete)
        self.delete_datab.grid(row=0,column=4)

        self.update_datab=ttk.Button(self.button_frame,text='Update',command =self.updatePropertyDatabase)
        self.update_datab.grid(row=0,column=5)

        self.exitb=ttk.Button(self.button_frame,text='Exit',command =lambda:self._exit(self.edit_data_window))
        self.exitb.grid(row=0,column=6)

        for i in self.button_frame.winfo_children(): #creates a for loop for each widget in button frame
            i.configure(style= 'B.TButton')#gives each button the style b.tbutton

    def listboxCommand(self):
        self.display_box.bind('<<ListboxSelect>>',\
            lambda event:self.recordDisplayIndex(event,self.entry_ary))#performs the command when data is selected on the listbox

    def createWidgets(self):
#=========================================Frames================================================================================      
        self.createFrame()
        self.createLabels()
        self.createEntrys()
        self.createButtons()
        self.createListBox(self.data_display_frame,100,12)
        self.listboxCommand()

    def createListBox(self,frame,w,h):

           #===========================================================Listbox======================================================================================================
        self.display_box=tk.Listbox(frame,width=w,height=h,font =('arial',15)) #creates a list box that will display data and allow it to  be selected
        
        yscroll_bar=st.Scrollbar(frame,orient =tk.VERTICAL,command =self.display_box.yview) #creates a vertical scrollbar
        
        xscroll_bar=st.Scrollbar(frame,orient =tk.HORIZONTAL,command =self.display_box.xview) #creates a horizontal scrollbar
        self.display_box.configure(xscrollcommand =xscroll_bar.set)#sets the horizontal scroll bar onto the list box
        self.display_box.configure(yscrollcommand =yscroll_bar.set)#sets the vertical scroll bar onto the listbox
        yscroll_bar.pack(fill='y',side=tk.RIGHT)#puts the horizontal scroll bar onto the righ
        xscroll_bar.pack(fill='x',side=tk.BOTTOM) #puts the horizontal scroll bar onto the left

        self. display_box.pack(side=tk.TOP, fill='both', expand=1)#organis the list box the the top of the window and expands within its frame

    def _exit(self,arg):
        exit =mbx.askyesno('GreenBird Properties Database Management System',\
            'Confirm if you want to exit')#message box that asks yes or no to exit window
        if exit >0:
            arg.destroy() #exits the window

        return

#======================================================================================functions==================================================================================

    def clearData(self,arg): #removes all data from the data entry widgets *
        for i in range(len(arg)):
            arg[i].delete(0,tk.END) #tk END refers to the end of the string and 0 the begining thus removing the whole string

    def addPropertyData(self):

        valid,empty=self.databaseValid()#returns true or false for values valid and empty
        #adds the data entered in the entry into the property  database
        if valid and not empty:
            pdbsql.addPropertyData(self.flat_name_entry.get().upper(),self.flat_num_entry.get(),self.post_code_entry.get().upper(),self.town_entry.get().upper(),\
                self.city_entry.get().upper(),self.bathrooms_entry.get(),self.bedrooms_entry.get(),self.rent_price_entry.get()) #calls sql function to add to database
            self.displayTable()#displays the values on the database

    def displayTable(self,table='Property'):######*
        self.display_box.delete(0,tk.END)#empties the list box
        for i in pdbsql.viewData(table):#calls sql function that returns all data values as an array
            self.display_box.insert(tk.END,i) #the value returned from the sql function is then printed on the display box

    def recordDisplayIndex(self,event,arg):#*
        #global self.sd#stands for search data
        try:
            search=self.display_box.curselection()[0] #returns an index that is used to specify the location of the data on the listbox line i.e first line will be 0 
           
            self.sd =self.display_box.get(search) #returns a list of data displayed on the list box
                 
            for i in range(1,(len(arg)+1)):

                arg[i-1].delete(0,tk.END)
                arg[i-1].insert(tk.END,self.sd[i])#inserts each data in the list into entry

            
        except Exception as err:
            pass


  

    def delete(self):

        self.deleteData('Property','idp')#deletes the row selected 

    def deleteData(self,table,sqlid):
        pdbsql.deleteData(self.sd[0],table,sqlid)#deletes data selected
        self.displayTable(table)#displays data on list box
        
    def getSqlCommand(self):#generates a sql command based on if values have been typed into entry widgets

        sql_string='' #used to dynamiclly add sql command
        sql_variables=[] #will hold the value for each entry widget that has been typed into

        if self.flat_name_entry.get().isspace() or self.flat_name_entry.get()=='':
            pass
        else:
            sql_string+='flat_name=? '
            sql_variables.append(self.flat_name_entry.get().upper())

        if self.flat_num_entry.get().isspace() or self.flat_num_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='flat_num=? '
            else:
                sql_string+='AND flat_num=? '

            sql_variables.append(self.flat_num_entry.get())

        if self.post_code_entry.get().isspace() or self.post_code_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='post_code=? '
            else:
                sql_string+='AND post_code=? '
            sql_variables.append(self.post_code_entry.get().upper())

        if self.town_entry.get().isspace() or self.town_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='town=? '
            else:
                sql_string+='AND town=? '
            sql_variables.append(self.town_entry.get().upper())

        if self.city_entry.get().isspace() or self.city_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='city=? '
            else:
                sql_string+='AND city=? '
            sql_variables.append(self.city_entry.get().upper())


        if self.bathrooms_entry.get().isspace() or self.bathrooms_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='bathrooms=? '
            else:
                sql_string+='AND bathrooms=? '

            sql_variables.append(self.bathrooms_entry.get())


        if self.bedrooms_entry.get().isspace() or self.bedrooms_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='bedrooms=? '
            else:
                sql_string+='AND bedrooms=? '

            sql_variables.append(self.bedrooms_entry.get())

        if self.rent_price_entry.get().isspace() or self.rent_price_entry.get()=='':
            pass
        else:
            if sql_string=='':
                sql_string+='rent_price=? '
            else:
                sql_string+='AND rent_price=? '

            sql_variables.append(self.rent_price_entry.get())



        return sql_string,sql_variables


    def searchPropertyDatabase(self,):


        self.display_box.delete(0,tk.END)#empties display box

        sql_string,sql_variables=self.getSqlCommand()

        for i in pdbsql.searchPropertyData(sql_string,sql_variables):

            self.display_box.insert(tk.END,i,str('')) #looks for correlating data from entry and inserts it into displaybox 
        
    def updatePropertyDatabase(self):
        #updates data by inserting entry values into the the sql database
        pdbsql.updatePropertyData(self.sd[0],self.flat_name_entry.get().upper(),self.flat_num_entry.get(),\
            self.post_code_entry.get().upper(),self.town_entry.get().upper(),\
            self.city_entry.get().upper(),self.bathrooms_entry.get(),\
            self.bedrooms_entry.get(),self.rent_price_entry.get())
        self.displayTable()


    def intEntryValidation(self,inp):

        
        if inp.isdigit(): #checks that data entered is only an integer
            return True
        elif inp is '': #or if data is embty
            return True
        else:
            return False

    def validateName(self,name):
        
        if not re.match(r"^[A-Za-z]+\s*[A-Za-z]*$",name):
            return False

        else:

            return True

    def emptyEntryCheck(self,entry_start_index):
        entrys=self.data_entry_frame.winfo_children()

        for i in range(entry_start_index,len(entrys)): #starts at 5 because widgets before that are labels and we only want entry widgets
            if entrys[i].get() =='': #checks if an entry is empty
                empty=True
                return empty
            else:
                empty=False

        return empty

    def validPostCodeCheck(self):

        post_code=self.post_code_entry.get()
        if not re.match(r"^[A-Za-z]+[A-Za-z]*[0-9][0-9]\s*[0-9][A-Za-z][A-Za-z]",post_code):
            return False
        else:
            return True
        
    def FlatNameAvailabiltyValidate(self):

        flats=pdbsql.getAllFlats()#gets all flats 
        if self.flat_name_entry.get().upper() in flats: #checks if the flat has been booked

            return False
        else: 

            return True

    def databaseValid(self):
        valid=False
        empty=True

        empty=self.emptyEntryCheck(8)
        if empty:
            mbx.showerror('Error','Fill out all remaining fields!')
            return valid,empty


        if self.FlatNameAvailabiltyValidate():
            valid=True
        else:
            valid=False
            mbx.showerror('Error',f'{self.flat_name_entry.get()} is in the database already!')
            return valid,empty

        if self.validPostCodeCheck():
            valid=True
        else:
            valid=False
            mbx.showerror('Error',f'Incorrect format for post code!')
            return valid,empty

        if self.validateName(self.flat_name_entry.get()):
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for flat name!')
            return valid,empty

        if self.validateName(self.town_entry.get()):
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for town!')
            return valid,empty

        if self.validateName(self.city_entry.get()):
            valid=True
        else:
            valid=False
            mbx.showerror('Error','Incorrect format for city!')
            return valid,empty

        return valid,empty

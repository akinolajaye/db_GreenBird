import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk
from tkinter import scrolledtext as st

from customerinfowin import CustomerInfo
from bookcustomerswin import BookCustomers
from editdatbwin import EditDatabase
import customersql as cdbsql
import datetime

class CustomersBooked(BookCustomers):#inherits from book customers

    def __init__(self,win):
        self.win=win
        self.createStyle()
        self.createWidgets(win)
        self.insertNameIntoListbox()

    def createWidgets(self,win):
        self.list_box_frame=ttk.LabelFrame(win,text='Flats in Use',style='MF.TLabelframe')
        self.list_box_frame.pack()
        self.createListBox(self.list_box_frame,100,12)#creates list box)
        self.listboxCommand()



    def listboxCommand(self):
        self.display_box.bind('<<ListboxSelect>>',\
            lambda event:self.SelectCustomer(event))#performs the command when data is selected on the listbox
    


    def insertNameIntoListbox(self): #inserts the newly created array with descriptive strings into the list box
        name=cdbsql.getCustomerName()
        for i in range(len(name)):
            for j in range(len(name[i])):
                self.display_box.insert(tk.END,name[i][j])

            self.display_box.insert(tk.END,'')


    def SelectCustomer(self,event):#*
        global sd#stands for searched data
        try:
            search=self.display_box.curselection()[0] #returns an index that is used to specify the location of the data on the listbox line i.e first line will be 0 
           
            sd =self.display_box.get(search) #returns a list of data displayed on the list box
            name=sd.split(' ')
            CustomerInfo(self.win,name[0],name[1],name[2])
                
           

            
        except Exception as err:
            print(err)

        return






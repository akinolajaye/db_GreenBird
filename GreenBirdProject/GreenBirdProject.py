import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk
import checkstatuswin as cs
import bookcustomerswin as bc
import editdatbwin as ed

from tkinter import messagebox as mbx

import bookingsdatabasesql as bdbsql
import customersql as cdbsql
import propertydatabasesql as pdbsql #imports the sql data base file

class Menu():
    
    def __init__(self):
        self.win=tk.Tk() #creates an instance of the tkinter module by calling its constructor
        self.win.title('GreenBird Properties')#creates the window titlw
        self.win.configure(bg='light grey')#sets the window background colour
        self.win.geometry('300x250')#sets the size of the windows
        self.win.resizable(0,0)#set the window to a non resizble state


        pdbsql.createPropertyTable()#creates the property table
        bdbsql.createBookingTable()#creates the bookings table
        cdbsql.createCustomerTable()
        cdbsql.createCustomerBookingTable()
        self.createMenu()#calls the createMenu window
        

    def _exit(self):
        close =mbx.askyesno('GreenBird Properties Database Management System',\
            'Confirm if you want to exit')#message box that asks yes or no to exit window
        if close >0:
            self.win.quit()
            self.win.destroy() #exits the window
            exit()

        return

    def clickcs(self):
        cs.CheckStatus(self.win)#calls the checkstatus class

    def clickbc(self):
        bc.BookCustomers(self.win) #calls the book customers class
        
    def clicked(self):
        ed.EditDatabase(self.win)#calls the dit database class
        
    def createMenu(self):

        menu_style=ttk.Style()
        menu_style.configure('My.TFrame',background ='light grey')#creats a style of frame to set the background
        menu_style.configure('My.Tbutton',background='light grey')#sets a style for button to set the background
        menu_style.configure('My.TLabel',background='light grey',font=('Calibri light',20))#sets style for label sets backgrounf and font


        start_menu =ttk.Frame(self.win, style ='My.TFrame')#creates a frame widget that will contain other widgets
        
        label=ttk.Label(start_menu,text='Menu:',style = 'My.TLabel') #creates a text label
        label.grid()#places the label in the specified location on the gui in grid form

        book_cutsomersb=ttk.Button(start_menu,text ='Book in Customers',\
            style ='My.TButton',command=self.clickbc)#creats a click button that performs the command by callig the function it references
                                                     #calls function clickbc
                                                                                   
        book_cutsomersb.grid()#places the button in the next available space on the grid

        check_statusb=ttk.Button(start_menu,text='Check Status',\
            style ='My.TButton',command=self.clickcs)#calls function clickcs
        check_statusb.grid()#
        


        edit_databaseb=ttk.Button(start_menu,text= 'Edit Database',\
            style ='My.TButton',command=self.clicked)#calls function clicked
        edit_databaseb.grid()

        exitb=ttk.Button(start_menu,text='Exit',command=self._exit,style ='My.TButton')#calls the function exit
        exitb.grid()

        for i in start_menu.winfo_children(): # a for loop which loops through all widgets in the startmenu frame
            i.grid_configure(pady=5,padx=50)#configures all the widgets and specifes the padding along x and y


        start_menu.pack()#organises the position of the frame in the window


if __name__=='__main__':

    menu=Menu() #creates an instance of menu class
    menu.win.mainloop() #mainloop is a tkinter function that runs the tkinter module



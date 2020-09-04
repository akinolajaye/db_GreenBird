import tkinter as tk #imports the tkinter module which allow gui programming
from tkinter import ttk
import customerbooked as cb


class CheckStatus():
    def __init__(self,win):
        self.check_status_window=tk.Toplevel(win)#creates a instance of the tkinter module in the form of a new window
        self.check_status_window.geometry('500x500')#sets a default size for the window when opened
        self.createWidgets(self.check_status_window)


    def createWidgets(self,win):
        cb.CustomersBooked(win)





        
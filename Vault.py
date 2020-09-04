def updateRevenue(new_revenue,flat_name):
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    date=getCurrentDate()
    rev=getRevenueAtDate()
    old_revenue=getRentPrice(flat_name)
    cursor.execute('UPDATE Finances SET revenue=? WHERE date=?',(rev-int(old_revenue)+int(new_revenue),date,))#######add an update to minus when deleting
    con.commit()

    
    con.close() 


def getRentPrice(flat_name):

    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('SELECT rent_price FROM Property WHERE flat_name=?',(flat_name,))
    price=cursor.fetchall()
    price=int(price[0][0])
    con.close()
    return price


    def insertOccintoEntry(self):
        x=self.occ_frame.winfo_children()
        occupant=fasql.getOcc()
        
        
        
        for i in range(1,len(x)):
            if str(occupant[i-1][0]).isdigit():
                occ=int(occupant[i-1][0])

            else:
                occ=str(occupant[i-1][0])

            
            x[i].insert(0,occ)
            

        for i in self.occ_frame.winfo_children():
            if isinstance(i,ttk.Entry):
                i.config(state='readonly')


    def insertPriceintoEntry(self):
        x=self.rev_frame.winfo_children()
        revenue=fasql.getRevenue()
        count=0
        
        
        for i in range(1,len(x)):
            if str(revenue[i-1][0]).isdigit():
                rev=int(revenue[i-1][0])
            else:
                rev=str(revenue[i-1][0])

            x[i].insert(0,rev)
            

        for i in self.rev_frame.winfo_children():
            if isinstance(i,ttk.Entry):
                i.config(state='readonly')




def addPriceAtMonth(revenue):
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    date=changeDateForRange()
    rev=getRevenueAtDate()
    cursor.execute('UPDATE Finances SET revenue=? WHERE date=?',(int(revenue)+rev,date,))#######add an update to minus when deleting

    con.commit()
    
    con.close()


   
def deleteRevenue(revenue):
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    date=changeDateForRange()
    rev=getRevenueAtDate()
    cursor.execute('UPDATE Finances SET revenue=? WHERE date=?',(rev-int(revenue),date,))#######add an update to minus when deleting

    con.commit()
    
    con.close()   







def getRevenueAtDate():
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    date=changeDateForRange()
    cursor.execute('SELECT revenue FROM Finances WHERE date=?',(date,))
    rev=cursor.fetchall()####################
    rev=int(rev[0][0])
    con.close()
    return rev

def addOccAtMonth():
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")
    date=changeDateForRange()
    
    occ=getOccAtMonth()

    cursor.execute('UPDATE Finances SET occupant=? WHERE date=?',(occ,date,))

    con.commit()
    con.close()



def getOccAtMonth():
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('SELECT COUNT (*) FROM Bookings WHERE')
    occ=cursor.fetchall()

    occ=occ[0][0]

    con.close()

    return occ
    


    def createTotalRevenueTable(self):
        rev_frame=self.rev_frame.winfo_children()
        total_table=[]
      
   
        for i in range(1,len(self.months)+1):
            try:
                


                total_table.append(rev_frame[i].get())
                   
           

            except:
                total_table.append(0)

            


        print(total_table)

        return(total_table)


    def insertOccupants(self):

        occ_entry=self.occ_frame.winfo_children()
        

        for i in range(1,len(occ_entry)):
            try:
               occupants=self.addOccupants(self.months[i-1])
               occ_entry[i].insert(0,occupants)

            except:
                pass

       




        return

    def addOccupants(self,month):
        flats=[]
        total=0
        actual_occupants=0
        occupants=fasql.getOcc(month)

        

        
        for i in range(len(occupants)):
            flat=occupants[i][1]
            flats.append(flat) 
            total+=int(occupants[i][0])
            


        print(flats)
        for i in range(len(occupants)):

             
             try:
                if occupants[i][1]!=occupants[i+1][1]:
                    x=flats.count(occupants[i][1])

                    actual_occupants+=x

             except:
                pass





            



            #actual_occupants+=x
            

            

  



        print(actual_occupants)
        #print(total)
           
        
            
        

        return total


def getOcc(month):
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()#
    cursor.execute("PRAGMA foreign_keys = ON")

    date=getDate(month)
    cursor.execute('SELECT occupant,flat_name FROM Finances WHERE date=?',(date,))
    occ=cursor.fetchall()
    con.close()
    return occ






def getRevenueTable():

    revenue_table=[]
    con=sqlite3.connect('property.db')#connects to the property database
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('SELECT revenue FROM Finances')
    revenue=cursor.fetchall()
    con.close()

    for i in range(len(revenue)):
        revenue_table.append(int(revenue[i][0]))
  
    
    return revenue_table




    def updateBookingsDatabase(self):

        search=self.display_box.curselection()[0]#creates a list of item indexes [0] is the id

        sd =self.display_box.get(search)
        bdbsql.updateBookingsData(sd[0],self.name_entry.get(),self.duration_entry.get(),self.num_of_people_entry.get(),\
            self.phone_number_entry.get(),self.email_entry.get())

        self.display_box.delete(0,tk.END)
        self.display_box.insert(tk.END,self.name_entry.get(),self.duration_entry.get(),self.num_of_people_entry.get(),\
            self.flat_name_entry.get(),self.rent_price_entry.get(),self.phone_number_entry.get(),self.email_entry.get())

def rentPriceAvailable(array,flat_name):
    array.set('')
    array['values']=''
    rent_price=getRentPrice(flat_name) #gets the rent price based on the flat name

    for i in range(len(rent_price)):
    
        array['values']=int(rent_price[0][0]) #puts the rent price into the combobox
    


def updateBookingsData(id,name,duration,start_date,end_date,num_of_people,phone_number,email):
    con=sqlite3.connect('property.db')
    cursor =con.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #updates data 
    cursor.execute('UPDATE Bookings SET flat_name=?,duration=?,start_date=?,end_date=?,num_of_people=?,phone_number=?,email=? WHERE idb=?',\
        (name,duration,start_date,end_date,num_of_people,phone_number,email,id))

    con.commit()
    con.close()


        self.graph_frame=ttk.Frame(win)#cretaes a frame for graph button
        self.graph_frame.pack(anchor='w')

        self.graph_lbl1=ttk.Label(self.graph_frame,text='Create Graph in Order of Month:')
        self.graph_lbl1.grid(row=0,column=0)
        self.graphb=ttk.Button(self.graph_frame,text='Create',command=lambda:self.createGraph(self.months),style='B.TButton') #calls creategraph when button pressed
        self.graphb.grid(row=0,column=1)

        self.graph_lbl1=ttk.Label(self.graph_frame,text='Create Graph in Order of Revenue:')
        self.graph_lbl1.grid(row=1,column=0)
        self.graphb=ttk.Button(self.graph_frame,text='Create',\
            command=self.showOrderedGraph,style='B.TButton') #calls creategraph when button pressed
        self.graphb.grid(row=1,column=1)
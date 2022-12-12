from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class DonationManagement:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "Donation Management System")
        self.root.geometry("1700x700+0+0")
        
        #DONATOR INFO
        Donor_ID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Sex = StringVar()
        Phonenumber = StringVar()
        Address = StringVar()
        Email = StringVar()
        
        #ORGANIZATION INFO
        Organization_ID = StringVar()
        Organization_Name = StringVar()
        
        #DONATED ITEMS
        Donation_ID = StringVar()
        Donation_Type = StringVar()
        Item_Description = StringVar()
        Quantity = StringVar()
        
        #Extra
        Search = StringVar()
        
#-----------------------------------------------------------------------------------------------

        MainFrame = Frame(self.root, bd = 10, width = 1400, height = 1000)
        MainFrame.grid()
        
        #pwede magdagdag ng image
        
        TitleFrames = Frame(MainFrame, bd = 7, width = 1380, height = 100)
        TitleFrames.grid(row = 0, column = 0)
        
        SearchFrame = Frame(MainFrame, bd = 5, padx = 5, width = 1340, height = 50)
        SearchFrame.grid(row = 1, column = 0)
        
        MidFrame = Frame(MainFrame, bd = 5, width = 1340, height = 800)
        MidFrame.grid(row = 2, column = 0)
        
        MemberDetailsFrame = Frame(MidFrame, bd = 5, width = 1340, height = 300, padx = 6, pady = 4)
        MemberDetailsFrame.grid(row = 0, column = 0)
        
        TreeviewFrame = Frame(MidFrame, bd = 5, width = 1340, height = 400, padx = 2)
        TreeviewFrame.grid(row = 1, column = 0)
        
        ButtonFrame = Frame(MidFrame, bd = 7, width = 1340, height = 50)
        ButtonFrame.grid(row = 2, column = 0)
        
        #------------------------------------------------------------------------------
        self.IblTitle = Label (TitleFrames, font = ('arialbold', 40 , 'bold'), text = "Donation Management System",bd = 7)
        self.IblTitle.grid(row = 0, column = 0, padx=422)
        #------------------------------------------------------------------------------
        #------------------------------------------------------------------------------
        
        #DONORID
        self.lblDonor_ID = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Donor ID",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblDonor_ID.grid(row = 0, column = 0, sticky=W, padx=5)
        
        self.txtDonor_ID = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Donor_ID)
        self.txtDonor_ID.grid(row = 0, column = 1)
        
        #FIRSTNAME
        self.lblFirstname = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Firstname",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblFirstname.grid(row = 1, column = 0, sticky=W, padx=5)
        
        self.txtFirstname = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Firstname)
        self.txtFirstname.grid(row = 1, column = 1)
        
        #LASTNAME
        self.lblLastname = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Lastname",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblLastname.grid(row = 2, column = 0, sticky=W, padx=5)
        
        self.txtLastname = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Lastname)
        self.txtLastname.grid(row = 2, column = 1)
        
        #SEX
        self.lblSex = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Sex",bd = 7,
                                 anchor='w', justify = LEFT)
        self.lblSex.grid(row = 3, column = 0, sticky=W, padx=5)
       
        self.txtSex = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                 textvariable = Sex)
        self.txtSex.grid(row = 3, column = 1)
        
        #PHONENUMBER
        self.lblPhonenumber = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Phone Number",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblPhonenumber.grid(row = 4, column = 0, sticky=W, padx=5)
        
        self.txtPhonenumber = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Phonenumber)
        self.txtPhonenumber.grid(row = 4, column = 1)
        
        #ADDRESS
        self.lblAddress = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Address",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblAddress.grid(row = 5, column = 0, sticky=W, padx=5)
        
        self.txtAddress = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Address)
        self.txtAddress.grid(row = 5, column = 1)
        
        #ADDRESS
        self.lblEmail = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Email",bd = 7,
                                  anchor='w', justify = LEFT)
        self.lblEmail.grid(row = 6, column = 0, sticky=W, padx=5)
        
        self.txtEmail = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=36, justify = LEFT, 
                                  textvariable = Email)
        self.txtEmail.grid(row = 6, column = 1)
        
        #------------------------------------------------------------------------------
        #ORGANIZATION ID
        self.lblOrganization_ID = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "ORGANIZATION INFORMATION",bd = 7)
        self.lblOrganization_ID.grid(row = 0, column = 5, sticky=W, padx=5)
        
        self.lblOrganization_ID = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Organization ID",bd = 7)
        self.lblOrganization_ID.grid(row = 1, column = 4, sticky=W, padx=5)
        
        self.txtOrganization_ID = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=35, justify = LEFT, 
                                  textvariable = Organization_ID)
        self.txtOrganization_ID.grid(row = 1, column = 5)
        
        #ORGANIZATION NAME
        self.lblOrganization_Name = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Organization Name",bd = 7)
        self.lblOrganization_Name.grid(row = 2, column = 4, sticky=W, padx=5)
        
        self.txtOrganization_Name = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=35, justify = LEFT, 
                                  textvariable = Organization_Name)
        self.txtOrganization_Name.grid(row = 2, column = 5)
        
        #------------------------------------------------------------------------------
        #DONATION TYPE
        self.lblDonation_Type = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "DONATED ITEM INFORMATION",bd = 7)
        self.lblDonation_Type.grid(row = 0, column = 7, sticky=W, padx=5)
        
        
        self.lblDonation_ID = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Donation ID",bd = 7)
        self.lblDonation_ID.grid(row = 1, column = 6, sticky=W, padx=5)
        
        self.txtDonation_ID = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=35, justify = LEFT, 
                                  textvariable = Donation_ID)
        self.txtDonation_ID.grid(row = 1, column = 7)
        
        
        self.lblDonation_Type = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Donation Type",bd = 7)
        self.lblDonation_Type.grid(row = 2, column = 6, sticky=W, padx=5)
        
        self.cboDonation_Type = ttk.Combobox (MemberDetailsFrame, font = ('arial', 12 , 'bold'), width=38, 
                                  state = 'readonly', textvariable = Donation_Type)
        self.cboDonation_Type['values'] =('Cash','Food','Clothes','Hygiene Essentials','School Essentials', 'Toys and Games')
        self.cboDonation_Type.current(0)
        self.cboDonation_Type.grid(row = 2, column =7)
        
        #ITEM NAME
        self.lblItem_Description = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Item Description",bd = 7)
        self.lblItem_Description.grid(row = 3, column = 6, sticky=W, padx=5)
        
        self.txtItem_Description = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=35, justify = LEFT, 
                                  textvariable = Item_Description)
        self.txtItem_Description.grid(row = 3, column = 7)
        
        #QUANTITY
        self.lblQuantity = Label (MemberDetailsFrame, font = ('arial', 12 , 'bold'), text = "Quantity",bd = 7)
        self.lblQuantity.grid(row = 4, column = 6, sticky=W, padx=5)
        
        self.txtQuantity = Entry (MemberDetailsFrame, font = ('arial', 12 , 'bold'),bd=5, width=35, justify = LEFT, 
                                  textvariable = Quantity)
        self.txtQuantity.grid(row = 4, column = 7)
        
        #============================DATABASE CONNECTION=================================
        
        #+++++ADDON FUNCTION
        def combine_funcs(*funcs):
            def inner_combined_func(*args, **kwargs):
                for f in funcs:
  
                    f(*args, **kwargs)
  
            return inner_combined_func
        
        #+++++
        
        
        def  addNew_donor():
            if Donor_ID.get() == "" or Firstname.get() == "" or Lastname.get() =="":
                tkinter.messagebox.showerror("Error check input", "Enter correct members details")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur = sqlCon.cursor()
                cur.execute("insert into donor values (%s, %s, %s, %s, %s, %s, %s)",(
                    
                Donor_ID.get(),
                Firstname.get(),
                Lastname.get(),
                Sex.get(),
                Phonenumber.get(),
                Address.get(),
                Email.get(),
                ))
                
                sqlCon.commit()
                ShowRecord()
                ShowRecord1()
                ShowRecord2()
                sqlCon.close()
                
                
        def  addNew_item():
                 sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                 cur = sqlCon.cursor()
                 cur.execute("insert into item values (%s, %s, %s, %s)",(
                     
                 Donation_ID.get(),
                 Donation_Type.get(),
                 Item_Description.get(),
                 Quantity.get(),
                 ))
                 
                 sqlCon.commit()
                 ShowRecord()
                 ShowRecord1()
                 ShowRecord2()
                 sqlCon.close()
                         
                
        def  addNew_organization():
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur = sqlCon.cursor()
                cur.execute("insert into organization values (%s, %s, %s, %s)",(
                Organization_ID.get(),
                Organization_Name.get(),
                Donor_ID.get(),
                Donation_ID.get(),
                
                ))
                
                sqlCon.commit()
                ShowRecord()
                ShowRecord1()
                ShowRecord2()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")    
                
        
        def ShowRecord():
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur= sqlCon.cursor()
                cur.execute("select * from donor")
                result = cur.fetchall()
                if len(result)!=0:
                    self.donation_records.delete(*self.donation_records.get_children())
                    for row in result:
                        self.donation_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()
        
        def ShowRecord1():
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur= sqlCon.cursor()
                cur.execute("select * from organization")
                result = cur.fetchall()
                if len(result)!=0:
                    self.donation_records1.delete(*self.donation_records1.get_children())
                    for row in result:
                        self.donation_records1.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()
                
        def ShowRecord2():
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur= sqlCon.cursor()
                cur.execute("select * from item")
                result = cur.fetchall()
                if len(result)!=0:
                    self.donation_records2.delete(*self.donation_records2.get_children())
                    for row in result:
                        self.donation_records2.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()
                
        def DonatorsInfo(ev):
            viewInfo = self.donation_records.focus()
            learnerData = self.donation_records.item(viewInfo)
            row = learnerData['values']
            
            Donor_ID.set(row[0])
            Firstname.set(row[1])
            Lastname.set(row[2])
            Sex.set(row[3])
            Phonenumber.set(row[4])
            Address.set(row[5])
            Email.set(row[6])
        
        def DonatorsInfo1(ev):
            viewInfo = self.donation_records1.focus()
            learnerData = self.donation_records1.item(viewInfo)
            row = learnerData['values']
            
            Organization_ID.set(row[0])
            Organization_Name.set(row[1])
            
        def DonatorsInfo2(ev):
            viewInfo = self.donation_records2.focus()
            learnerData = self.donation_records2.item(viewInfo)
            row = learnerData['values']
            
            Donation_ID.set(row[0])
            Donation_Type.set(row[1])
            Item_Description.set(row[2])
            Quantity.set(row[3])
            
        
       
        
       
        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
            cur = sqlCon.cursor()
            cur.execute("update donor set firstname=%s, lastname=%s, sex=%s, phonenumber=%s, address=%s, email=%s where donorid=%s",(
        
            Firstname.get(),
            Lastname.get(),
            Sex.get(),
            Phonenumber.get(),
            Address.get(),
            Email.get(),
            Donor_ID.get()
            
            ))
            sqlCon.commit()
            ShowRecord()
            ShowRecord1()
            ShowRecord2()
            sqlCon.close()
            
            
        def update1():
             sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
             cur = sqlCon.cursor()
             cur.execute("update organization set organizationname=%s where organizationid=%s",(
         
             Organization_Name.get(),
             Organization_ID.get()
             
             
             ))
             sqlCon.commit()
             ShowRecord()
             ShowRecord1()
             ShowRecord2()
             sqlCon.close()
             
        
        def update2():
             sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
             cur = sqlCon.cursor()
             cur.execute("update item set donationtype=%s, itemdescription=%s, quantity=%s where donationid=%s",(
         
             Donation_Type.get(),
             Item_Description.get(),
             Quantity.get(),
             Donation_ID.get()
             
             
             ))
             sqlCon.commit()
             ShowRecord()
             ShowRecord1()
             ShowRecord2()
             sqlCon.close()
             tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Updated")
             
        
        def deleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
            cur = sqlCon.cursor()
            cur.execute("delete from donor where donorid=%s", Donor_ID.get())

            sqlCon.commit()
            ShowRecord()
            ShowRecord1()
            ShowRecord2()
            sqlCon.close()
            
        
        def deleteDB1():
            sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
            cur = sqlCon.cursor()
            cur.execute("delete from organization where organizationid=%s", Organization_ID.get())

            sqlCon.commit()
            ShowRecord()
            ShowRecord1()
            ShowRecord2()
            sqlCon.close()
            
            
        def deleteDB2():
            sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
            cur = sqlCon.cursor()
            cur.execute("delete from item where donationid=%s", Donation_ID.get())

            sqlCon.commit()
            ShowRecord()
            ShowRecord1()
            ShowRecord2()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
            
        def Reset():
            Donor_ID.set("")
            Firstname.set("")
            Lastname.set("")
            Sex.set("")
            Phonenumber.set("")
            Address.set("")
            Email.set("")
            Organization_ID.set("")
            Organization_Name.set("")
            Donation_ID.set("")
            Donation_Type.set("Cash")
            Item_Description.set("")
            Quantity.set("")
            Search.set("")
            
        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def searchDG():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur = sqlCon.cursor()
                cur.execute("select * from donor where donorid='%s'"%Search.get())
                
                row = cur.fetchone()
                
                Donor_ID.set(row[0])
                Firstname.set(row[1])
                Lastname.set(row[2])
                Sex.set(row[3])
                Phonenumber.set(row[4])
                Address.set(row[5])
                Email.set(row[6])
                
                
                
                sqlCon.commit()
            except:
                
                Search.set("")
                
            sqlCon.close()
        
        def searchDG1():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur = sqlCon.cursor()
                cur.execute("select * from organization where donorid='%s'"%Search.get())
                
                row = cur.fetchone()
                
                
                Organization_ID.set(row[0])
                Organization_Name.set(row[1])
                
                
                
                sqlCon.commit()
            except:
                
                Search.set("")
                
            sqlCon.close()
        
        
        def searchDG2():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="group4database", database="final_donation_database")
                cur = sqlCon.cursor()
                cur.execute("select * from item where donationid='%s'"%Search.get())
                
                row = cur.fetchone()
                
                
                Donation_ID.set(row[0])
                Donation_Type.set(row[1])
                Item_Description.set(row[2])
                Quantity.set(row[3])
                
                
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record")
                Search.set("")
                
            sqlCon.close()
        #================================================================================
        
        scroll_y=Scrollbar(TreeviewFrame, orient =VERTICAL)
        
        self.donation_records=ttk.Treeview(TreeviewFrame,height =5,columns= ("donorid", "firstname", "lastname", "sex", "phonenumber",
        "address", "email"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.donation_records1=ttk.Treeview(TreeviewFrame,height =5,columns= ("organizationid", "organizationname",), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.donation_records2=ttk.Treeview(TreeviewFrame,height =5,columns= ("donationid", "donationtype", "itemdescription", "quantity"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.donation_records.heading("donorid", text="Donor ID")
        self.donation_records.heading("firstname", text="Firstname")
        self.donation_records.heading("lastname", text="LastName")
        self.donation_records.heading("sex", text="Sex")
        self.donation_records.heading("phonenumber", text="Phone Number")
        self.donation_records.heading("address", text="Address")
        self.donation_records.heading("email", text="Email")
        self.donation_records1.heading("organizationid", text="Organization ID")
        self.donation_records1.heading("organizationname", text="Organization Name")
        self.donation_records2.heading("donationid", text="Donation ID")
        self.donation_records2.heading("donationtype", text="Donation Type")
        self.donation_records2.heading("itemdescription", text="Item Description")
        self.donation_records2.heading("quantity", text="Quantity")
        
        self.donation_records['show']='headings'
        self.donation_records1['show']='headings'
        self.donation_records2['show']='headings'
        
        self.donation_records.column("donorid", width=120)
        self.donation_records.column("firstname", width=120)
        self.donation_records.column("lastname", width=120)
        self.donation_records.column("sex", width=120)
        self.donation_records.column("phonenumber", width=120)
        self.donation_records.column("address", width=120)
        self.donation_records.column("email", width=120)
        self.donation_records1.column("organizationid", width=120)
        self.donation_records1.column("organizationname", width=120)
        self.donation_records2.column("donationid", width=120)
        self.donation_records2.column("donationtype", width=120)
        self.donation_records2.column("itemdescription", width=120)
        self.donation_records2.column("quantity", width=120)
        
        
        self.donation_records.pack(side=LEFT, expand=1)
        self.donation_records.bind("<ButtonRelease-1>",DonatorsInfo)
        ShowRecord()
        
        self.donation_records1.pack(side=LEFT, expand=1)
        self.donation_records1.bind("<ButtonRelease-1>",DonatorsInfo1)
        ShowRecord1()
        
        self.donation_records2.pack(side=LEFT, expand=1)
        self.donation_records2.bind("<ButtonRelease-1>",DonatorsInfo2)
        ShowRecord2()
        
        #----------------------------httt--------------------------------------------
        self.IblSearchTitle = Label (SearchFrame, font = ('arialbold', 16 , 'bold'), text = "Search Donor ID",bd = 7)
        self.IblSearchTitle.grid(row = 0, column = 0, padx=42)
        
        self.txtSearch = Entry (SearchFrame, font = ('arial', 16 , 'bold'), width=33, justify='right',
                                  textvariable = Search)
        self.txtSearch.grid(row = 0, column = 2)
        
        self.btnSearch = Button(SearchFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        height = 1, text="Search", bg="white", command=combine_funcs(searchDG, searchDG1, searchDG2)).grid(row=0, column=3, padx=1)
        
        
        #----------------------------httt--------------------------------------------
        #BUTTONS
        self.btnAddNew_donor = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 12,
        height = 1, text="Add New", command=combine_funcs(addNew_donor, addNew_item, addNew_organization)).grid(row=0, column=0, padx=2)
        
        #self.btnShowRecord = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        #height = 1, text="Show Record", command=combine_funcs(ShowRecord, ShowRecord1, ShowRecord2)).grid(row=0, column=1, padx=1)
        
        self.btnUpdate = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        height = 1, text="Update", command=combine_funcs(update, update1, update2)).grid(row=0, column=2, padx=2)
        
        self.btnDelete = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        height = 1, text="Delete", command=combine_funcs(deleteDB1, deleteDB2, deleteDB)).grid(row=0, column=3, padx=1)
        
        self.btnReset = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        height = 1, text="Reset", command=Reset).grid(row=0, column=4, padx=2)
        
        self.btnExit = Button(ButtonFrame, pady=1, padx=29, bd=4, font = ('arial', 16, 'bold'), width = 9,
        height = 1, text="Exit", command=iExit).grid(row=0, column=5, padx=1)
        
        
        
if __name__ =='__main__':
    root = Tk()
    application = DonationManagement(root)
    root.mainloop()
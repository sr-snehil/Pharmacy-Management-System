import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox



from tkinter import messagebox

from PIL import ImageTk, Image


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System-By Snehil")
        self.root.geometry("1366x768+0+0")
        
        # ===============MAIN VARIABLES==================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEfect_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar() 
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        # ===============RIGHT DATAFRAME VARIABLES==================
        self.addmed_var=StringVar()
        self.refmed_var=StringVar()
        
        
# ==================================HEADING===================================
        lbltitle=Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg="WHITE",
                       fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1= Image.open("E:\\PHARMA\\images\\download.png")
        img1=img1.resize((60,60),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=18,y=25)
        # ===============================DATAFRAME==================================
        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1368, height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=850,height=350)
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                  fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=860,y=5,width=450,height=350)
        
        # ==========================BUTTON FRAME====================================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1368,height=65)
        
        # ==========================BUTTON ADD====================================
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Add Medicine",bg="darkgreen",font=("arial",12,"bold"),fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateMed=Button(ButtonFrame,command=self.Update,text="UPDATE",bg="darkgreen",font=("arial",12,"bold"),fg="white")
        btnUpdateMed.grid(row=0,column=1)
        
        btnDeleteMed=Button(ButtonFrame,command=self.Delete,text="DELETE",bg="red",font=("arial",12,"bold"),fg="white")
        btnDeleteMed.grid(row=0,column=2)
        
        btnRestMed=Button(ButtonFrame,command=self.Reset,text="RESET",bg="darkgreen",font=("arial",12,"bold"),fg="white")
        btnRestMed.grid(row=0,column=3)
        
        btnExitMed=Button(ButtonFrame,command=self.root.destroy,text="EXIT",bg="red",font=("arial",12,"bold"),fg="white")
        btnExitMed.grid(row=0,column=4)
        
        # ==================================SEARCH BY=========================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By: ",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref_no","medName","LotNo")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)
        
        searchBtn=Button(ButtonFrame,command=self.Search_data,text="SEARCH",bg="darkgreen",font=("arial",12,"bold"),fg="white")
        searchBtn.grid(row=0,column=8)
        
        btnShowAll=Button(ButtonFrame,command=self.fetch_mainData,text="SHOW ALL",bg="red",font=("arial",12,"bold"),fg="white")
        btnShowAll.grid(row=0,column=9)
        
        # =============================label and entry======================
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No ",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                            host='localhost', database='mydata',
                            auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        s="select Ref from pharma"
        my_cursor.execute(s)
        row=my_cursor.fetchall()
        
        comrefno=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",12,"bold"),state="readonly")
        comrefno["values"]=row
        comrefno.grid(row=0,column=1)
        comrefno.current(0)
        
        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name ",padx=2)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtCmpName.grid(row=1,column=1)
        
        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)
        
        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Covid-19 Vaccine","Tablet","Liquid","Capsules","Vaccine","Drops","Inhalers","Injections")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)
        
        # =====================ADD MEDICINE=====================
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        my_cursor=conn.cursor()
        s="select MedRef from pharma"
        my_cursor.execute(s)
        med=my_cursor.fetchall()
        
        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=("arial",12,"bold"),state="readonly")
        comMedicineName["values"]=med
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)
        
        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot Number",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtLotNo.grid(row=4,column=1)
        
        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtIssueDate.grid(row=5,column=1)
        
        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses: ",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtUses.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects ",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEfect_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtSideEffect.grid(row=8,column=1)
        
        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec and Warning ",padx=2,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtPrecWarning.grid(row=0,column=3)
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtDosage.grid(row=1,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price ",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtPrice.grid(row=2,column=3)
        
        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtProductQt.grid(row=3,column=3)
        
        
        # ===================DataFrameRight================
        
        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Number",padx=2,pady=6)
        lblrefno.grid(row=0,column=2,sticky=W)
        txtrefno=Entry(DataFrameRight,textvariable=self.refmed_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtrefno.grid(row=0,column=3)
        
        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblmedName.grid(row=1,column=2,sticky=W)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,bd=2,relief=RIDGE,width=29,font=("arial",13,"bold"),bg="white")
        txtmedName.grid(row=1,column=3)
        
        # ====================SIDE FRAME IN RIGHT FRAME================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE)
        side_frame.place(x=0,y=80,width=250, height=220)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1 >",self.Medget_cursor)
        
        # ================MEDICINE ADD BUTTON================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=280,y=80,width=100, height=160)
        
        btnAddmed=Button(down_frame,text="ADD",bg="lime",font=("arial",12,"bold"),fg="white",pady=4,width=8,command=self.AddMed)
        btnAddmed.grid(row=0,column=0)
        
        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",bg="purple",font=("arial",12,"bold"),fg="white",pady=4,width=8)
        btnUpdatemed.grid(row=1,column=0)
        
        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",bg="red",font=("arial",12,"bold"),fg="white",pady=4,width=8)
        btnDeletemed.grid(row=2,column=0)
        
        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",bg="orange",font=("arial",12,"bold"),fg="white",pady=4,width=8)
        btnClearmed.grid(row=3,column=0)
                # ============================DETAILS FRAME======================
        
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1368, height=180)
        
        # ===========MAIN TABLE AND SCROLLING==========================
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1300, height=150)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","warning","dosage","price","productqt"),
                                         xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("reg",text="Referece No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Medcine Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effects")
        self.pharmacy_table.heading("warning",text="Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QT")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetchdata_med()
        self.fetch_mainData()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
#======================ADD MEDICINE FUNCTIONALITY DECLARATION=====================
    def AddMed(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                            host='localhost', database='mydata',
                            auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        s="insert into pharma(Ref,MedRef) values (%s,%s)"
        b1=(self.refmed_var.get(),self.addmed_var.get())
        my_cursor.execute(s,b1)
                                                                            
        conn.commit()
        self.fetchdata_med()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")
    def fetchdata_med(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                            host='localhost', database='mydata',
                            auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        s="select * from pharma"
        my_cursor.execute(s)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])
    def UpdateMed(self):
        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(user='root', password='snehilraj292',
                                host='localhost', database='mydata',
                                auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            s="UPDATE pharma SET MedRef=%s where Ref=%s"
            XX=self.refmed_var.get()
            b1=(XX,self.addmed_var.get())
            my_cursor.execute(s,b1)
            conn.commit()
            self.fetchdata_med()
            conn.close()
            
            messagebox.showinfo("Success","Medicine Has been updated")
            
    def DeleteMed(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                                host='localhost', database='mydata',
                                auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        s="delete from pharma where Ref=%s"
        b1=(self.refmed_var.get(),)
        my_cursor.execute(s,b1)
        conn.commit()
        self.fetchdata_med()
        conn.close()
        
    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")
        
        
        
# =============================MAIN TABLE========================FFSDGV=           
    def add_data(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                            host='localhost', database='mydata',
                            auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharmacy values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.ref_var.get(),
                                                                                                   self.cmpName_var.get(),
                                                                                                   self.typeMed_var.get(),
                                                                                                   self.medName_var.get(),
                                                                                                   self.lot_var.get(),
                                                                                                   self.issuedate_var.get(),
                                                                                                   self.expdate_var.get(),
                                                                                                   self.uses_var.get(),
                                                                                                   self.sideEfect_var.get(),
                                                                                                   self.warning_var.get(),
                                                                                                   self.dosage_var.get(),
                                                                                                   self.price_var.get(),
                                                                                                   self.product_var.get()
        ))
                                                                                                   
                                                                                                   
        conn.commit()
        self.fetch_mainData()
        conn.close()
        messagebox.showinfo("success","Data Has been added")

    def fetch_mainData(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                            host='localhost', database='mydata',
                            auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,eve=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEfect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10])
        
        self.price_var.set(row[11]),
        self.product_var.set(row[12]),
        
    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(user='root', password='snehilraj292',
                                host='localhost', database='mydata',
                                auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set CmpName=%s,TypeMed=%s,medName=%s,LotNo=%s,IssueDate=%s,Expdate=%s,uses=%s,Sideeffect=%s,warning=%s,dosage=%s,Price=%s,product=%s where Ref_no=%s",(
                                                                                                   
                                                                                                   self.cmpName_var.get(),
                                                                                                   self.typeMed_var.get(),
                                                                                                   self.medName_var.get(),
                                                                                                   self.lot_var.get(),
                                                                                                   self.issuedate_var.get(),
                                                                                                   self.expdate_var.get(),
                                                                                                   self.uses_var.get(),
                                                                                                   self.sideEfect_var.get(),
                                                                                                   self.warning_var.get(),
                                                                                                   self.dosage_var.get(),
                                                                                                   self.price_var.get(),
                                                                                                   self.product_var.get(),
                                                                                                   self.ref_var.get()
        ))
            conn.commit()
            self.fetch_mainData()
            conn.close()
            
            messagebox.showinfo("Success","Record Has been updated")
        
        
    def Delete(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                                host='localhost', database='mydata',
                                auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        s="delete from pharmacy where Ref_no=%s"
        b1=(self.ref_var.get(),)
        my_cursor.execute(s,b1)
        conn.commit()
        self.fetch_mainData()
        conn.close()
        messagebox.showinfo("Deleted","Info Deleted Succesfully")
        
    def Reset(self):
       # self.ref_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
       # self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEfect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.product_var.set("")
        
    def Search_data(self):
        conn=mysql.connector.connect(user='root', password='snehilraj292',
                                host='localhost', database='mydata',
                                auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE "+str(self.searchTxt_var.get()))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        


if __name__ == "__main__":
    root = Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()


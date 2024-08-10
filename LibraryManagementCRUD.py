from tkinter import*
from tkinter import ttk 
import mysql.connector
import datetime
from tkinter import messagebox
import tkinter
  
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        #variable
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.rollno_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.latereturnfine=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        # =================================Data Frame Left==================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblmember = Label(DataFrameLeft,bg="powder blue",textvariable=self.member_var,text="Member type:",font=("arial",12,"bold"),width=27)
        lblmember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1,sticky=W)

        lblprn_no=Label(DataFrameLeft,text="PRN NO:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblprn_no.grid(row=1,column=0,sticky=W)
        txtprn_no=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.prn_var,width=22)
        txtprn_no.grid(row=1,column=1)

        lblprn_no=Label(DataFrameLeft,text="ID NO:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblprn_no.grid(row=2,column=0,sticky=W)
        txtprn_no=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.rollno_var,width=22)
        txtprn_no.grid(row=2,column=1)

        lblF_name=Label(DataFrameLeft,text="First Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblF_name.grid(row=3,column=0,sticky=W)
        txtF_name=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=22)
        txtF_name.grid(row=3,column=1)

        lblL_name=Label(DataFrameLeft,text="Last Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblL_name.grid(row=4,column=0,sticky=W)
        txtL_name=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=22)
        txtL_name.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,text="Address:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address_var,width=22)
        txtAddress.grid(row=5,column=1)

        lbl_Postcode=Label(DataFrameLeft,text="Postcode:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Postcode.grid(row=6,column=0,sticky=W)
        txt_Postcode=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=22)
        txt_Postcode.grid(row=6,column=1)

        lbl_Mobile=Label(DataFrameLeft,text="Mobile No:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Mobile.grid(row=7,column=0,sticky=W)
        txt_Mobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=22)
        txt_Mobile.grid(row=7,column=1)

        lbl_Bookid=Label(DataFrameLeft,text="Book Id:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Bookid.grid(row=8,column=0,sticky=W)
        txt_Bookid=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=22)
        txt_Bookid.grid(row=8,column=1)
# -------------------------------------------------------------------------------------


        lbl_Booktitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Booktitle.grid(row=0,column=2,sticky=W)
        txt_Booktitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=22)
        txt_Booktitle.grid(row=0,column=3)

        lbl_Authorname=Label(DataFrameLeft,text="Author Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Authorname.grid(row=1,column=2,sticky=W)
        txt_Authorname=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=22)
        txt_Authorname.grid(row=1,column=3)

        lbl_DateBorrowed=Label(DataFrameLeft,text="Date Borrowed:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DateBorrowed.grid(row=2,column=2,sticky=W)
        txt_DateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=22)
        txt_DateBorrowed.grid(row=2,column=3)

        lbl_DueDate=Label(DataFrameLeft,text="Due Date:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DueDate.grid(row=3,column=2,sticky=W)
        txt_DueDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=22)
        txt_DueDate.grid(row=3,column=3)

        lbl_DaysOnBooks=Label(DataFrameLeft,text="Days On Books:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DaysOnBooks.grid(row=4,column=2,sticky=W)
        txt_DaysOnBooks=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=22)
        txt_DaysOnBooks.grid(row=4,column=3)

        lbl_LateReturnFine=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_LateReturnFine.grid(row=5,column=2,sticky=W)
        txt_LateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine,width=22)
        txt_LateReturnFine.grid(row=5,column=3)

        lbl_DateOverDate=Label(DataFrameLeft,text="Date over Date:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_DateOverDate.grid(row=6,column=2)
        txt_DateOverDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=22)
        txt_DateOverDate.grid(row=6,column=3)

        lbl_ActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_ActualPrice.grid(row=7,column=2)
        txt_ActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice,width=22)
        txt_ActualPrice.grid(row=7,column=3)

        
        # =================================Data Frame Right==================================================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        

        self.txtbox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16)
        self.txtbox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["wings of fire","Narcopolis","The Great Indian Novel","Combat Of Shadows","The White Tiger","Atomic habits","The Complete Adventures Of Feluda ","Ikigai",
                   "The Glass Palace","Gitanjali","Train to Pakistan","Harry Potter","Kung Fu Panda","The Hobbit","Data Science","SQL","Mongodb"
                ,"Cold war","Mahabahrat","Ramayan","The Room On The Roof","C programming","DataStructures And Algorithms","Java Programming","C++ Programming"]
        
        def SelectBook(event=""):
            value= str(listBox.get(listBox.curselection()))
            x=value
            if(x=="wings of fire"):
                self.bookid_var.set("BKID1010")
                self.booktitle_var.set("Wings of fire")
                self.author_var.set("A.P.J Abdul Kalam")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.109")
                
            elif(x=="Narcopolis"):
                self.bookid_var.set("BKID1011")
                self.booktitle_var.set("Narcopolis")
                self.author_var.set("Jeet Thayil")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.345")

            elif(x=="The Great Indian Novel"):
                self.bookid_var.set("BKID1012")
                self.booktitle_var.set("The Great Indian Novel")
                self.author_var.set("Shashi Tharoor")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.350")
                
            elif(x=="Combat Of Shadows"):
                self.bookid_var.set("BKID1013")
                self.booktitle_var.set("Combat Of Shadows")
                self.author_var.set("Manohar Malgonkar")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.295")
                
            elif(x=="The White Tiger"):
                self.bookid_var.set("BKID1014")
                self.booktitle_var.set("The White Tiger")
                self.author_var.set("Aravind Adiga")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.352")
                
            elif(x=="Atomic habits"):
                self.bookid_var.set("BKID1015")
                self.booktitle_var.set("Atomic habits")
                self.author_var.set("James Clear")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.459")
                
            elif(x=="The Complete Adventures Of Feluda "):
                self.bookid_var.set("BKID1016")
                self.booktitle_var.set("The Complete Adventures Of Feluda ")
                self.author_var.set("Satyajit Ray")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.399")
                
            elif(x=="Ikigai"):
                self.bookid_var.set("BKID1017")
                self.booktitle_var.set("Ikigai")
                self.author_var.set("Francesc Miralles and Hector Garcia")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.349")
                
            elif(x=="The Glass Palace"):
                self.bookid_var.set("BKID1018")
                self.booktitle_var.set("The Glass Palace")
                self.author_var.set("Amitav Ghosh")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.499")
                
            elif(x=="Gitanjali"):
                self.bookid_var.set("BKID1019")
                self.booktitle_var.set("Gitanjali")
                self.author_var.set("Rabindranath Tagore")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.94")
                
            elif(x=="Train to Pakistan"):
                self.bookid_var.set("BKID1020")
                self.booktitle_var.set("Train to Pakistan")
                self.author_var.set("Khushwant Singh")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.164")
                
            elif(x=="Harry Potter"):
                self.bookid_var.set("BKID1021")
                self.booktitle_var.set("Harry Potter")
                self.author_var.set("J. K. Rowling")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.345")
                
            elif(x=="Kung Fu Panda"):
                self.bookid_var.set("BKID1022")
                self.booktitle_var.set("Kung Fu Panda")
                self.author_var.set("Jonathan Aibel, Glenn Berger and Dan Harmon")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.2611")
            
            elif(x=="The Hobbit"):
                self.bookid_var.set("BKID1023")
                self.booktitle_var.set("The Hobbit")
                self.author_var.set("John Ronald Reuel Tolkien")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.359")
                
            elif(x=="Cold war"):
                self.bookid_var.set("BKID1024")
                self.booktitle_var.set("Cold war")
                self.author_var.set("John Lewis Gaddis")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.746")
                
            elif(x=="Mahabahrat"):
                self.bookid_var.set("BKID1025")
                self.booktitle_var.set("Mahabahrat")
                self.author_var.set("Vyasa")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.147")
                
            elif(x=="Ramayan"):
                self.bookid_var.set("BKID1026")
                self.booktitle_var.set("Ramayan")
                self.author_var.set("Valmiki")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.670")
                
            elif(x=="The Room On The Roof"):
                self.bookid_var.set("BKID1027")
                self.booktitle_var.set("The Room On The Roof")
                self.author_var.set("Valmiki")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.670")
                
            elif(x=="C programming"):
                self.bookid_var.set("BKID1028")
                self.booktitle_var.set("C programming")
                self.author_var.set("Brian Kernighan")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.3971")
                
            elif(x=="DataStructures And Algorithms"):
                self.bookid_var.set("BKID1029")
                self.booktitle_var.set("DataStructures And Algorithms")
                self.author_var.set("Ronald Rivest")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.1790")
                
            elif(x=="Java Programming"):
                self.bookid_var.set("BKID1030")
                self.booktitle_var.set("Java Programming")
                self.author_var.set("")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.799")
                
            elif(x=="C++ Programming"):
                self.bookid_var.set("BKID1031")
                self.booktitle_var.set("C++ Programming")
                self.author_var.set("Bjarne Stroustrup")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.7414")
                
            elif(x=="Data Science"):
                self.bookid_var.set("BKID1032")
                self.booktitle_var.set("Data Science")
                self.author_var.set("")
                d1=datetime.datetime.today("Data Science")
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.1575")
                
            elif(x=="SQL"):
                self.bookid_var.set("BKID1033")
                self.booktitle_var.set("SQL")
                self.author_var.set("Alan Beaulieu")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.1475")
                
            elif(x=="Mongodb"):
                self.bookid_var.set("BKID1034")
                self.booktitle_var.set("Mongodb")
                self.author_var.set("Kristina Chodorow and Michael Dirolf")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.2")
                self.dateoverdue.set("No")
                self.finalprice.set("Rs.1850")
            
           # listbox
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ===============================Buttons Frame========================================
        FrameButton=LabelFrame(self.root,text="",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=17,pady=6)
        FrameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(FrameButton,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(FrameButton,text="Show Data",command=self.show_data,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(FrameButton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(FrameButton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(FrameButton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(FrameButton,text="Exit",command=self.Exit, font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=6)


        # ===============================Database Information Frame========================================
        FrameDetails=Frame(self.root,bg="powder blue",bd=12,relief=RIDGE,padx=20)
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        

        self.library_table=ttk.Treeview(Table_frame,column=("Member","prnno","RollNo","firstname","lastname","address"
                                                            ,"postcode","mobile","bookid","booktitle","author","dateborrowed"
                                                            ,"datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll,yscrollcommand=yscroll)
    
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member",text="Member Type")
        self.library_table.heading("prnno",text="PRN N0.")
        self.library_table.heading("RollNo",text="RollNo")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("postcode",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="latereturnfine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Member",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("RollNo",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
       
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username= "root",password="ubuntu", database="books")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.rollno_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook.get(),
                                                                                                            self.latereturnfine.get(),
                                                                                                            self.dateoverdue.get(),
                                                                                                            self.finalprice.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted")
        

    def update(self):
        conn=mysql.connector.connect(host="localhost",username= "root",password="ubuntu", database="books")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Address=%s,PostCode=%s, Mobile=%s where prnno=%s",(self.address_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.prn_var.get() ))
      
        conn.commit()
        self.fetch_data()
        
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been updated")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username= "root",password="ubuntu", database="books")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library;")
        rows = my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        print("Cursor Function is called")
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.rollno_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address_var.set(row[5])
        self.postcode_var.set(row[6])
        self.mobile_var.set(row[7])
        self.bookid_var.set(row[8])
        self.booktitle_var.set(row[9])
        self.author_var.set(row[10])
        self.dateborrowed_var.set(row[11])
        self.datedue_var.set(row[12])
        self.daysonbook.set(row[13])
        self.latereturnfine.set(row[14])
        self.dateoverdue.set(row[15])
        self.finalprice.set(row[16]) 
        
        
        
    def show_data(self):
        self.txtbox.insert(END,"Member Type: "+self.member_var.get() + "\n")
        self.txtbox.insert(END,"PRN No. "+self.prn_var.get() + "\n")
        self.txtbox.insert(END,"ID No. "+self.rollno_var.get() + "\n")
        self.txtbox.insert(END,"First Name: "+self.firstname_var.get() + "\n")
        self.txtbox.insert(END,"Last Name: "+self.lastname_var.get() + "\n")
        self.txtbox.insert(END,"Address: "+self.address_var.get() + "\n")
        self.txtbox.insert(END,"Post Code: "+self.postcode_var.get() + "\n")
        self.txtbox.insert(END,"Mobile No: "+self.mobile_var.get() + "\n")
        self.txtbox.insert(END,"Book ID: "+self.bookid_var.get() + "\n")
        self.txtbox.insert(END,"Book Title:"+self.booktitle_var.get() + "\n")
        self.txtbox.insert(END,"Author: "+self.author_var.get() + "\n")
        self.txtbox.insert(END,"Date Borrowed: "+self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END,"Date Due: "+self.datedue_var.get() + "\n")
        self.txtbox.insert(END,"Days on Book: "+self.daysonbook.get() + "\n")
        self.txtbox.insert(END,"Late Fine: "+self.latereturnfine.get() + "\n")
        self.txtbox.insert(END,"Date Over Due: "+self.dateoverdue.get() + "\n")
        self.txtbox.insert(END,"Final Price: "+self.finalprice.get() + "\n")
    
    def reset(self):
        self.member_var.set("")
        self.rollno_var.set("")
        # self.title_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.latereturnfine.set("")
        self.dateoverdue.set("")
        self.finalprice.set("")
        self.txtbox.delete("1.0",END)
        
        
    def Exit(self):
        Exit = messagebox.askyesno("Library Management System", "Do you want to exit?")
        if Exit>0:
            self.root.destroy()
            return
        
        
    def delete(self):
        if self.prn_var.get() == "" or self.rollno_var.get() == "":
            messagebox.showerror("Error", "First select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username= "root",password="ubuntu", database="books")
            my_cursor=conn.cursor()
            query = "delete from library where PRNNo = %s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted")
            
            
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
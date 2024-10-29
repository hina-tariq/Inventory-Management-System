from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==========title===================
        image = Image.open("Images/logo1.png")
        resized_image = image.resize((100, 70))
        self.icon_title = ImageTk.PhotoImage(resized_image)
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="blue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #==========button logout==============
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #============clock=================
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #=====================ProductFrame============================
        self.var_search = StringVar()
        ProductFrame1 = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle = Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="Gray15",fg="white").pack(side=TOP,fill=X)

        ProductFrame2 = Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90 )

        lbl_search = Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search = Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search = Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search = Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all = Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        cart_Frame = Frame(ProductFrame1,bd=3,relief=RIDGE)
        cart_Frame.place(x=2,y=140,width=398,height=380)

        scrolly = Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID No.")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Qty")
        self.CartTable.heading("status",text="Status")


        self.CartTable["show"] = "headings"

        self.CartTable.column("pid",width=90)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=100)
        self.CartTable.column("qty",width=100)
        self.CartTable.column("status",width=100)       
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        lbl_note = Label(ProductFrame1,text="Enter 0 Quantity to remove product from the Cart",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #=====================CustomerFrame============================
        self.var_name = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle = Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name = Label(CustomerFrame,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=35)
        txt_name = Entry(CustomerFrame,textvariable=self.var_name,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=150)
       
        lbl_contact = Label(CustomerFrame,text="Contact No.",font=("times new roman",15,"bold"),bg="white").place(x=270,y=35)
        txt_contact = Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)
       
        Cal_Cart_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

        Cal_Frame = Frame(Cal_Cart_Frame,bd=2,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
  
        cart_Frame = Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)

        scrolly = Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID No.")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Qty")
        self.CartTable.heading("status",text="Status")
        self.CartTable["show"] = "headings"
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=20)
        self.CartTable.column("status",width=90)       
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()
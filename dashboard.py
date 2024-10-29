from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #=============title============
        # Open the image, resize it, and then convert it to ImageTk format
        image = Image.open("Images/logo1.png")
        
        # Resize the image to your desired dimensions (e.g., 100x70)
        resized_image = image.resize((100, 70))

        # Convert the resized image to a Tkinter-compatible image
        self.icon_title = ImageTk.PhotoImage(resized_image)
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="blue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #==========button logout==============
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #============clock=================
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #============Left Menu===============
        self.MenuLogo = Image.open("Images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200,200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X) 

        self.icon_side = Image.open("Images/arrow.png")
        self.icon_side = self.icon_side.resize((20,20))
        self.icon_side = ImageTk.PhotoImage(self.icon_side)

        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="green").pack(side=TOP,fill=X)
        btn_employee = Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)        
        btn_category = Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_products = Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #==============content================
        self.lbl_employee = Label(self.root,text="Total Employee\n [0]",bd=5,relief=RIDGE,bg="sea green",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=120,height=150,width=300)
        self.lbl_supplier = Label(self.root,text="Total Supplier\n [0]",bd=5,relief=RIDGE,bg="sea green",fg="white",font=("goudy old style",20,"bold")).place(x=650,y=120,height=150,width=300)
        self.lbl_category = Label(self.root,text="Total Category\n [0]",bd=5,relief=RIDGE,bg="sea green",fg="white",font=("goudy old style",20,"bold")).place(x=1000,y=120,height=150,width=300)
        self.lbl_product = Label(self.root,text="Total Product\n [0]",bd=5,relief=RIDGE,bg="sea green",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=300,height=150,width=300)
        self.lbl_sales = Label(self.root,text="Total Sales\n [0]",bd=5,relief=RIDGE,bg="sea green",fg="white",font=("goudy old style",20,"bold")).place(x=650,y=300,height=150,width=300)


        #================footer================
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by Hina Tariq\nFor any Technical Issue Contact: 9234xxxx01",font=("times new roman",12),bg="grey",fg="white").pack(side=BOTTOM, fill=X)

#======================================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
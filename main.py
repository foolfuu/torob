from tkinter import *
from tkinter import messagebox
p12 = []
pa1 = {}
pa2 = {}
pa3 = {}
#{a:b}
#{b:c}
#{c:d}
import random

def error(x,y):
    messagebox.showinfo(x , y)

root = Tk()

#main
def Main():
    def Mosh():
        def back():
            mo.destroy()
            Main()
        erfun.destroy()
        mo = Tk()
        mo.geometry("1140x700+100+50")
        mo.title("Khayam")
        mo.resizable(False , False)
        mo.config(bg = "black")
        a = Button(mo,text = "back",font = ('Times',25),bg = '#40A2D8',fg = 'red',bd = 5,command = back).place(x = 650 , y = 480)
        Label(mo,text = "Price",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 400,y = 190)
        pri = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);pri.place(x = 550 , y = 130)

        Label(mo,text = "Asthma",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 340,y = 110)
        ast = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);ast.place(x = 550 , y = 210)

        Label(mo,text = "Manufacturer",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 215,y = 270)
        man = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);man.place(x = 550 , y = 290)

        Label(mo,text = "Company",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 290,y = 350)
        comp = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);comp.place(x = 550 , y = 365)
        def checked():
            pr = pri.get()
            Ast = ast.get()
            ma = man.get()
            Comp = comp.get()
            if len(pr) == 0 or len(Ast) == 0 or len(ma) == 0 or len(Comp) == 0 : error("Error" , "Please complete all")
            else:
                pa1[pr]=Ast
                pa2[Ast] = ma
                pa3[ma] = Comp
                p12.append(pr)
                back()


        Button(mo,text = 'Add',font = ('Times 14',25),bg = 'blue',fg = '#A367B1',command = checked).place(y = 480 , x = 780)
        mo.mainloop()


    erfun = Tk()

    def yes_or_no():
        choice= messagebox.askquestion('exit', 'Do you want to exit?')
        if choice == 'yes':
            erfun.destroy()
        else:
            return

    erfun.geometry("1140x700+100+50")
    erfun.title("Khayam")
    erfun.resizable(False , False)
    erfun.config(bg = "black")
    menubar = Menu(erfun)
    la = Label(erfun,text = "wlcome to the khayam",font = ("Times 14", 22),bg = "black",fg = "yellow");la.pack()
    Search = Entry(erfun,font  = ("Times" , 22),bd = 5,bg = "#939393",fg = "#008800");Search.place(x = 790 , y = 50)
    lae = Button(erfun,text = "search",font = ("Times 14",20),fg = "#6C22A6",bg = "#030637");lae.place(x = 650 , y = 47)
    mosh = Button(erfun,text = "Add item",font = ("Times 14",20),bg = "#030637",cursor = "heart",fg = '#6C22A6',command = Mosh);mosh.place(x = 570 , y = 620)
    #def language

    def ENG():
        choice= messagebox.askquestion('Language', 'are you sure ?')
        if choice == 'yes':
            lae.config(text = "search")
            la.config(text = "wlcome to the khayam")
            Name.config(text = "Asthma:")
            Price.config(text = "Price:")
            Manuf.config(text = "Manufacturer:")
            Com.config(text = "Company:")
    def PER():
        choice= messagebox.askquestion('Language', 'are you sure ?')
        if choice == 'yes':
            lae.config(text = "سرچ")
            la.config(text = "خوش آمدید به خیام")
            Name.config(text = "نام کالا:")
            Price.config(text = "قیمت:")
            Manuf.config(text = "نام سازنده:")
            Com.config(text = "شرکت سازنده:")
    #
    #
    #def color
    def Red():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "red")
            la.config(bg = "red",fg = "yellow")
            lae.config(bg = "red",fg = "#2780FF")
            Name.config(bg = "red",fg = "#2780FF")
            Price.config(bg = "red",fg = "#2780FF")
            Manuf.config(bg = "red",fg = "#2780FF")
            Com.config(bg = "red",fg = "#2780FF")
            mosh.config(bg = "yellow")
    def Green():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "green")
            la.config(bg = "green",fg = "yellow")
            lae.config(bg = "green",fg = "#2780FF")
            Name.config(bg = "green",fg = "#2780FF")
            Price.config(bg = "green",fg = "#2780FF")
            Manuf.config(bg = "green",fg = "#2780FF")
            Com.config(bg = "green",fg = "#2780FF")
            mosh.config(bg = "red")
    def Yellow():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "yellow")
            la.config(bg = "yellow",fg = "black")
            lae.config(bg = "yellow",fg = "#2780FF")
            Name.config(bg = "yellow",fg = "#2780FF")
            Price.config(bg = "yellow",fg = "#2780FF")
            Manuf.config(bg = "yellow",fg = "#2780FF")
            Com.config(bg = "yellow",fg = "#2780FF")
            mosh.config(bg = "red")
    def Black():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "black")
            la.config(bg = "black",fg = "yellow")
            lae.config(bg = "black",fg = "#2780FF")
            Name.config(bg = "black",fg = "#2780FF")
            Price.config(bg = "black",fg = "#2780FF")
            Manuf.config(bg = "black",fg = "#2780FF")
            Com.config(bg = "black",fg = "#2780FF")
            mosh.config(bg = "red")
    def Pink():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "pink")
            la.config(bg = "pink",fg = "yellow")
            lae.config(bg = "pink",fg = "#2780FF")
            Name.config(bg = "pink",fg = "#2780FF")
            Price.config(bg = "pink",fg = "#2780FF")
            Manuf.config(bg = "pink",fg = "#2780FF")
            Com.config(bg = "pink",fg = "#2780FF")
            mosh.config(bg = "red")
    def Blue():
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            erfun.config(bg = "blue")
            la.config(bg = "blue",fg = "yellow")
            lae.config(bg = "blue",fg = "black")
            Name.config(bg = "blue",fg = "black")
            Price.config(bg = "blue",fg = "black")
            Manuf.config(bg = "blue",fg = "black")
            Com.config(bg = "blue",fg = "black")
            mosh.config(bg = "red")

    #end

    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "File" , menu = file)
    file.add_command(label = "mi")
    file.add_command(label = "Exit" , command = yes_or_no)
    #
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Edit" , menu = edit)
    edit.add_command(label = "black", command = Black)
    edit.add_command(label = "red", command = Red)
    edit.add_command(label = "green", command = Green)
    edit.add_command(label = "yellow", command = Yellow)
    edit.add_command(label = "pink", command = Pink)
    edit.add_command(label = "blue", command = Blue)
    erfun.config(menu = menubar)
    #
    lan = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Language" , menu = lan)
    lan.add_command(label = "English" , command = ENG)
    lan.add_command(label = "Persian" , command = PER)
    #


    li = Listbox(erfun,font = ("Times 14",22))
    for i in p12:
        li.insert(0,i)
    li.place(x = 790,y = 140,width = 290,height = 540)
    ###

    Name = Label(erfun,text = "Asthma:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Name.place(x = 50 , y = 100)
    Price = Label(erfun,text = "Price:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Price.place(x = 50 , y = 200)
    Manuf = Label(erfun,text = "Manufacturer:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Manuf.place(x = 50 , y = 300)
    Com = Label(erfun,text = "Company:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Com.place(x = 50 , y = 400)


    erfun.mainloop()
#


def Random(b):
    Str = ["a","b","c","d","e","f","g","h","i","j","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","$","?"]
    c = ""
    nm = random.randint(6,8)
    for i in range(nm):
        y = random.choice(Str)
        c = c+y
    b = c
    return b


def robat():
    ro = Tk()
    ro.title("I am Nat Robat Test")
    ro.config(bg = "black")
    ro.geometry("1140x700+100+50")
    ro.resizable(False , False)

    Label(ro,text = "I am not a robot" , fg = "white" ,bg = "black",font=('Times 14' , 55)).pack()
    Label(ro,text = "Please write the following text in the box" , fg = "red" ,bg = "black",font=('Times 14' , 30)).pack()
    tesr = ""
    tesr = Random(tesr)
    rala = Label(ro,text = tesr,fg = "yellow",bg = "black",font = ('Times',55)).place(x = 50,y = 250)
    raen = Entry(ro,font = ("Times 14",25),fg = "green",bd = 10);raen.place(x = 500 ,y = 270)

    def checkr():
        testr = raen.get()

        if testr != tesr:
            error("Error","The text is worong")
        elif testr == tesr:
            ro.destroy()
            Main()

    Button(ro,text = "check",font = ("Times 14",20),bg = "blue",fg = "pink",activebackground = "yellow",command = checkr).place(x = 600,y = 370)





    ro.mainloop()

#Register
def regi():

    root.destroy()
    window = Tk()
    window.title("register")
    window.config(bg = "red")
    window.geometry("1140x700+100+50")
    window.resizable(False , False)

    Label(window,text = "last name",font = ("Times 14",40),bg = "red").place(x = 300,y = 190)
    lname = Entry(window,font = ("Times 14",20));lname.place(x = 550 , y = 130)

    Label(window,text = "first name",font = ("Times 14",40),bg = "red").place(x = 290,y = 110)
    fname = Entry(window,font = ("Times 14",20));fname.place(x = 550 , y = 210)

    Label(window,text = "password",font = ("Times 14",40),bg = "red").place(x = 300,y = 270)
    passw = Entry(window,font = ("Times 14",20),show = "*");passw.place(x = 550 , y = 290)

    Label(window,text = "repeat the password",font = ("Times 14",40),bg = "red").place(x = 50,y = 350)
    passw2 = Entry(window,font = ("Times 14",20),show = "*");passw2.place(x = 550 , y = 365)

    def check():
        last_name = lname.get()
        farst_name = fname.get()
        passwo = passw.get()
        passwo2 = passw2.get()

        if len(last_name) == 0 or len(farst_name) == 0 or len(passwo) == 0 or len(passwo2) == 0:
            error("Error" , "Please complete all")
        elif len(passwo) < 8:
            error("Error" , "The password is simple")
        elif passwo != passwo2:
            error("Error" , "Ecribal error")
        else:
            window.destroy()
            robat()



    Button(window,text = "log in",font=('Times 14' , 20),bg = "black",fg = "white",activebackground = "yellow",command = check).place(x = 570,y = 470)


    window.mainloop()




def vorod():
    root.destroy()
    vor = Tk()
    vor.title("main")
    vor.geometry("1140x700+100+50")
    vor.resizable(False , False)
    vor.config(bg = "green")

    Label(vor,text = "last name",font = ("Times 14",40),bg = "green").place(x = 300,y = 190)
    Lname = Entry(vor,font = ("Times 14",20));Lname.place(x = 550 , y = 130)

    Label(vor,text = "first name",font = ("Times 14",40),bg = "green").place(x = 290,y = 110)
    Fname = Entry(vor,font = ("Times 14",20));Fname.place(x = 550 , y = 210)

    Label(vor,text = "password",font = ("Times 14",40),bg = "green").place(x = 300,y = 270)
    Passw = Entry(vor,font = ("Times 14",20),show = "*");Passw.place(x = 550 , y = 290)

    def chcked():
        clname = Lname.get()
        cfname = Fname.get()
        cpassw = Passw.get()
        if len(clname) == 0 or len(cfname) == 0 or len(cpassw) == 0:
            error("Error" , "Please complete all")
        elif len(cpassw) < 8:
            error("Error" , "The password is simple")
        else:
            #
            vor.destroy()
            robat()

            #


    Button(vor,text = "record",font=('Times 14' , 20),activebackground = "red",bg = "blue",command = chcked).place(y = 400,x = 465)

    vor.mainloop()






root.title("main")
root.geometry("1140x700+100+50")
root.resizable(False , False)
root.config(bg = "blue")



Label(root,text = "Welcom",font=('Times 14' , 55),fg = "yellow",bg = "blue").place(y = 100 , x = 450)
Button(root,text = "register",font=('Times 14' , 20),activebackground = "red",bg = "green",command = regi).place(y = 200,x = 590)
Button(root,text = " log in ",font=('Times 14' , 20),activebackground = "red",bg = "green",command = vorod).place(y = 200,x = 465)



root.mainloop()

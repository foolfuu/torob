from tkinter import *
from tkinter import messagebox
import random
p12 = []
pa1 = {}
pa2 = {}
pa3 = {}
#{a:b}
#{b:c}
#{c:d}
class khayam_algoritm:
    def error(x,y):
        messagebox.showinfo(x , y)
    
    def Searched(Search,li):
        pse = []
        sa = Search
        if len(sa) == 0:
            for i in range(li.size()):
                li.delete(0)
            for i in p12:
                li.insert(END,i)
        else:
            for i in p12:
                if sa in i:
                    pse.append(i)
            for i in range(li.size()):
                li.delete(0)
            if len(pse) == 0:
                pse.append('No product found')
            for i in pse:
                li.insert(END,i)
    
    def DELETE(li, ha, hp, hm, hc):
        itemnumber = li.curselection()
        if len(itemnumber)>0:
            itemname=li.get(itemnumber)
            if itemname != "No product found":
                choice= messagebox.askquestion('Delete', 'are you sure ?')
                if choice == 'yes':
                    if itemname in p12:
                        a = pa1[itemname]
                        b = pa2[a]
                        del pa1[itemname]
                        del pa2[a]
                        del pa3[b]
                        ha.config(text = '')
                        hp.config(text = '')
                        hm.config(text = '')
                        hc.config(text = '')
                        a = p12.index(itemname)
                        p12.pop(a)
                        for i in range(li.size()):
                            li.delete(0)
                        for i in p12:
                            li.insert(END,i)
    
    
    def Random(b):
        Str = ["a","b","c","d","e","f","g","h","i","j","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","2","3","4","5","6","7","8","9","!","@","$","?"]
        c = ""
        nm = random.randint(6,8)
        for i in range(nm):
            y = random.choice(Str)
            c = c+y
        b = c
        return b
    
    def yes_or_no(a):
        choice= messagebox.askquestion('exit', 'Do you want to exit?')
        if choice == 'yes':
            a.destroy()
        else:
            return

    # funktion for color

    # def red(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
    def Red(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            Er.config(bg = "red")
            La.config(bg = "red",fg = "yellow")
            Lae.config(bg = "#FA4659")
            De.config(bg = '#FA4659')
            Na.config(bg = "red",fg = "#2780FF")
            Pr.config(bg = "red",fg = "#2780FF")
            Ma.config(bg = "red",fg = "#2780FF")
            Co.config(bg = "red",fg = "#2780FF")
            Mo.config(bg = "#FA4659")
            Ha.config(bg = 'red',fg = 'black')
            Hp.config(bg = 'red',fg = 'black')
            Hm.config(bg = 'red',fg = 'black')
            Hc.config(bg = 'red',fg = 'black')
            Ac.config(bg = 'red',fg = 'yellow')
    
    def Green(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            Er.config(bg = "green")
            La.config(bg = "green",fg = "yellow")
            Lae.config(bg = "#0D9276")
            De.config(bg = '#0D9276')
            Na.config(bg = "green",fg = "#2780FF")
            Pr.config(bg = "green",fg = "#2780FF")
            Ma.config(bg = "green",fg = "#2780FF")
            Co.config(bg = "green",fg = "#2780FF")
            Mo.config(bg = "#0D9276")
            Ha.config(bg = 'green',fg = 'red')
            Hp.config(bg = 'green',fg = 'red')
            Hm.config(bg = 'green',fg = 'red')
            Hc.config(bg = 'green',fg = 'red')
            Ac.config(bg = 'green',fg = 'yellow')

    def Yellow(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
            choice= messagebox.askquestion('color', 'are you sure ?')
            if choice == 'yes':
                Er.config(bg = "yellow")
                La.config(bg = "yellow",fg = "black")
                Lae.config(bg = "#FFD124")
                De.config(bg = '#FFD124')
                Na.config(bg = "yellow",fg = "#2780FF")
                Pr.config(bg = "yellow",fg = "#2780FF")
                Ma.config(bg = "yellow",fg = "#2780FF")
                Co.config(bg = "yellow",fg = "#2780FF")
                Mo.config(bg = "#FFD124")
                Ha.config(bg = 'yellow',fg = 'red')
                Hp.config(bg = 'yellow',fg = 'red')
                Hm.config(bg = 'yellow',fg = 'red')
                Hc.config(bg = 'yellow',fg = 'red')
                Ac.config(bg = 'yellow',fg = 'black')
    
    def Black(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            Er.config(bg = "black")
            La.config(bg = "black",fg = "yellow")
            Lae.config(bg = "#030637")
            De.config(bg = '#030637')
            Na.config(bg = "black",fg = "#2780FF")
            Pr.config(bg = "black",fg = "#2780FF")
            Ma.config(bg = "black",fg = "#2780FF")
            Co.config(bg = "black",fg = "#2780FF")
            Mo.config(bg = "#030637")
            Ha.config(bg = 'black',fg = 'red')
            Hp.config(bg = 'black',fg = 'red')
            Hm.config(bg = 'black',fg = 'red')
            Hc.config(bg = 'black',fg = 'red')
            Ac.config(bg = 'black',fg = 'yellow')
    
    def Pink(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            Er.config(bg = "pink")
            La.config(bg = "pink",fg = "yellow")
            Lae.config(bg = "#E5A5FF")
            De.config(bg = '#E5A5FF')
            Na.config(bg = "pink",fg = "#2780FF")
            Pr.config(bg = "pink",fg = "#2780FF")
            Ma.config(bg = "pink",fg = "#2780FF")
            Co.config(bg = "pink",fg = "#2780FF")
            Mo.config(bg = "#E5A5FF")
            Ha.config(bg = 'pink',fg = 'red')
            Hp.config(bg = 'pink',fg = 'red')
            Hm.config(bg = 'pink',fg = 'red')
            Hc.config(bg = 'pink',fg = 'red')
            Ac.config(bg = 'pink',fg = 'yellow')

    def Blue(Er,La,Lae,De,Na,Pr,Ma,Co,Mo,Ha,Hp,Hm,Hc,Ac):
        choice= messagebox.askquestion('color', 'are you sure ?')
        if choice == 'yes':
            Er.config(bg = "blue")
            La.config(bg = "blue",fg = "yellow")
            Lae.config(bg = "#0766AD")
            De.config(bg = '#0766AD')
            Na.config(bg = "blue",fg = "black")
            Pr.config(bg = "blue",fg = "black")
            Ma.config(bg = "blue",fg = "black")
            Co.config(bg = "blue",fg = "black")
            Mo.config(bg = "#0766AD")
            Ha.config(bg = 'blue',fg = 'red')
            Hp.config(bg = 'blue',fg = 'red')
            Hm.config(bg = 'blue',fg = 'red')
            Hc.config(bg = 'blue',fg = 'red')
            Ac.config(bg = 'blue',fg = 'yellow')
    # funcktion for language
    # def per(lae, Dele, la, Name, Price, Manuf, Com, acli, mosh)
    def ENG(Lae, De, La, Na, Pr, Ma, Co, Ac, Mo):
        choice= messagebox.askquestion('Language', 'are you sure ?')
        if choice == 'yes':
            Lae.config(text = "search")
            De.config(text = 'Delete')
            La.config(text = "wlcome to the khayam")
            Na.config(text = "Item:")
            Pr.config(text = "Price:")
            Ma.config(text = "Manufacturer:")
            Co.config(text = "Company:")
            Ac.config(text = "Double click on the desired item")
            Mo.config(text = "Add item")
    
    def PER(Lae, De, La, Na, Pr, Ma, Co, Ac, Mo):
        choice= messagebox.askquestion('Language', 'are you sure ?')
        if choice == 'yes':
            Lae.config(text = "سرچ")
            De.config(text = 'حذف')
            La.config(text = "خوش آمدید به خیام")
            Na.config(text = "نام کالا:")
            Pr.config(text = "قیمت:")
            Ma.config(text = "نام سازنده:")
            Co.config(text = "شرکت سازنده:")
            Ac.config(text = "بر روی کالای مورد نظر دابل کلیک کنید")
            Mo.config(text = "اضافه کردن آیتم")
    # def checked(mo, pri, ast, man, comp)
    def checked(a, pr, Ast, ma, co):
        def back(a):
            a.destroy()
            khayam_page.Erfun()
        pr = pr.get()
        Ast = Ast.get()
        ma = ma.get()
        Comp = co.get()
        if len(pr) == 0 or len(Ast) == 0 or len(ma) == 0 or len(Comp) == 0 : khayam_algoritm.error("Error" , "Please complete all")
        else:
            pa1[pr] = Ast
            pa2[Ast] = ma
            pa3[ma] = Comp
            p12.append(pr)
            p12.sort()
            back(a)
    # def Show(event,li, hast, hpri, hman, hcom)
    '''
    def Show(event):
        if li.size() > 0:
            itemnumber = li.curselection()
            itemname = li.get(itemnumber)

            if itemname in p12:
                hast.config(text = itemname)
                a = pa1[itemname]
                hpri.config(text = a)
                b = pa2[a]
                hman.config(text = b)
                c = pa3[b]
                hcom.config(text = c)
    '''





class khayam_page:
    def vorod():
        root.destroy()
        vor = Tk()
        vor.title("main")
        vor.geometry("1140x700+100+50")
        vor.resizable(False , False)
        vor.config(bg = "green")

        Label(vor,text = "Last name",font = ("Times 14",40),bg = "green").place(x = 300,y = 190)
        Lname = Entry(vor,font = ("Times 14",20));Lname.place(x = 550 , y = 130)

        Label(vor,text = "First name",font = ("Times 14",40),bg = "green").place(x = 290,y = 110)
        Fname = Entry(vor,font = ("Times 14",20));Fname.place(x = 550 , y = 210)

        Label(vor,text = "Password",font = ("Times 14",40),bg = "green").place(x = 300,y = 270)
        Passw = Entry(vor,font = ("Times 14",20),show = "*");Passw.place(x = 550 , y = 290)

        def chcked():
            clname = Lname.get()
            cfname = Fname.get()
            cpassw = Passw.get()
            if len(clname) == 0 or len(cfname) == 0 or len(cpassw) == 0:
                khayam_algoritm.error("Error" , "Please complete all")
            elif len(cpassw) < 8:
                khayam_algoritm.error("Error" , "The password is simple")
            else:
                #
                vor.destroy()
                khayam_page.robat()

        Button(vor,text = "record",font=('Times 14' , 20),activebackground = "red",bg = "black",fg = 'white',command = chcked).place(y = 400,x = 465)
        vor.mainloop()
    
    def regi():
        root.destroy()
        window = Tk()
        window.title("register")
        window.config(bg = "red")
        window.geometry("1140x700+100+50")
        window.resizable(False , False)

        Label(window,text = "Last name",font = ("Times 14",40),bg = "red").place(x = 300,y = 190)
        lname = Entry(window,font = ("Times 14",20));lname.place(x = 550 , y = 130)

        Label(window,text = "First name",font = ("Times 14",40),bg = "red").place(x = 290,y = 110)
        fname = Entry(window,font = ("Times 14",20));fname.place(x = 550 , y = 210)

        Label(window,text = "Password",font = ("Times 14",40),bg = "red").place(x = 300,y = 270)
        passw = Entry(window,font = ("Times 14",20),show = "*");passw.place(x = 550 , y = 290)

        Label(window,text = "Repeat the password",font = ("Times 14",40),bg = "red").place(x = 50,y = 350)
        passw2 = Entry(window,font = ("Times 14",20),show = "*");passw2.place(x = 550 , y = 365)

        def check():
            last_name = lname.get()
            farst_name = fname.get()
            passwo = passw.get()
            passwo2 = passw2.get()

            if len(last_name) == 0 or len(farst_name) == 0 or len(passwo) == 0 or len(passwo2) == 0:
                khayam_algoritm.error("Error" , "Please complete all")
            elif len(passwo) < 8:
                khayam_algoritm.error("Error" , "The password is simple")
            elif passwo != passwo2:
                khayam_algoritm.error("Error" , "Ecribal error")
            else:
                window.destroy()
                khayam_page.robat()
    

        Button(window,text = "log in",font=('Times 14' , 20),bg = "black",fg = "white",activebackground = "yellow",command = check).place(x = 570,y = 470)


        window.mainloop()
    
    def robat():
        ro = Tk()
        ro.title("I am Nat Robat Test")
        ro.config(bg = "black")
        ro.geometry("1140x700+100+50")
        ro.resizable(False , False)

        Label(ro,text = "I am not a robot" , fg = "white" ,bg = "black",font=('Times 14' , 55)).pack()
        Label(ro,text = "Please write the following text in the box" , fg = "red" ,bg = "black",font=('Times 14' , 30)).pack()
        tesr = ""
        tesr = khayam_algoritm.Random(tesr)
        rala = Label(ro,text = tesr,fg = "yellow",bg = "black",font = ('Times',55)).place(x = 50,y = 250)
        raen = Entry(ro,font = ("Times 14",25),fg = "green",bd = 10);raen.place(x = 500 ,y = 270)

        def checkr():
            testr = raen.get()

            if testr != tesr:
                khayam_algoritm.error("Error","The text is worong")
            elif testr == tesr:
                ro.destroy()
                khayam_page.Erfun()

        Button(ro,text = "check",font = ("Times 14",20),bg = "blue",fg = "pink",activebackground = "yellow",command = checkr).place(x = 600,y = 370)

    def Erfun():
        def Mosh():
            def back():
                mo.destroy()
                khayam_page.Erfun()
            erfun.destroy()
            mo = Tk()
            mo.geometry("1140x700+100+50")
            mo.title("Khayam")
            mo.resizable(False , False)
            mo.config(bg = "black")
            a = Button(mo,text = "back",font = ('Times',25),bg = '#40A2D8',fg = 'red',bd = 5,command = back).place(x = 650 , y = 480)
            def checker(): khayam_algoritm.checked(mo, pri, ast, man, comp)
            Button(mo,text = 'Add',font = ('Times 14',25),bg = 'blue',fg = '#A367B1',command = checker).place(y = 480 , x = 780)
            
            Label(mo,text = "Price",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 400,y = 190)
            pri = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);pri.place(x = 550 , y = 130)

            Label(mo,text = "Item",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 420,y = 110)
            ast = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);ast.place(x = 550 , y = 210)

            Label(mo,text = "Manufacturer",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 215,y = 270)
            man = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);man.place(x = 550 , y = 290)

            Label(mo,text = "Company",font = ("Times 14",40),bg = "black",fg = '#2780FF').place(x = 290,y = 350)
            comp = Entry(mo,font = ("Times 14",20),bg = "#52D3D8",bd = 7);comp.place(x = 550 , y = 365)
        erfun = Tk()
        erfun.geometry("1140x700+100+50")
        erfun.title("Khayam")
        erfun.resizable(False , False)
        erfun.config(bg = "black")
        
        #
        la = Label(erfun,text = "wlcome to the khayam",font = ("Times 14", 22),bg = "black",fg = "yellow");la.pack()
        #

        # search and delete and add to list box
        #
        def searcher(): khayam_algoritm.Searched(Search.get(),li)
        def DELETED(): khayam_algoritm.DELETE(li, hast, hpri, hman, hcom)
        #
        lae = Button(erfun,text = "Search",font = ("Times 14",15),fg = "#6C22A6",bg = "#030637",bd = 7,command = searcher);lae.place(x = 650 , y = 47)
        mosh = Button(erfun,text = "Add item",font = ("Times 14",20),bg = "#030637",cursor = "heart",fg = '#6C22A6',bd = 7,command = Mosh);mosh.place(x = 570 , y = 620)
        Dele = Button(erfun,text = 'Delete',font = ("Times 14",20),bg = "#030637" ,fg = '#6C22A6',bd = 7,command = DELETED);Dele.place(y = 620 , x = 430)
        Search = Entry(erfun,font  = ("Times" , 22),bd = 5,bg = "#939393",fg = "#008800");Search.place(x = 790 , y = 50)
        #

        def Show(event):
            if li.size() > 0:
                itemnumber = li.curselection()
                itemname = li.get(itemnumber)

                if itemname in p12:
                    hast.config(text = itemname)
                    a = pa1[itemname]
                    hpri.config(text = a)
                    b = pa2[a]
                    hman.config(text = b)
                    c = pa3[b]
                    hcom.config(text = c)

        # list box
        # def show(): khayam_algoritm.Show(li, hast, hpri, hman, hcom)
        li = Listbox(erfun,font = ("Times 14",22))
        for i in p12:
            li.insert(END,i)
        li.bind('<Double-1>', Show)
        li.place(x = 790,y = 140,width = 290,height = 540)
        #

        # informatien item in shop
        acli = Label(erfun,text = 'Double click on the desired item',fg = 'yellow',bg = 'black',font = ('Times 14',15));acli.place(y = 105,x = 790)
        Name = Label(erfun,text = "Item:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Name.place(x = 50 , y = 100)
        Price = Label(erfun,text = "Price:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Price.place(x = 50 , y = 200)
        Manuf = Label(erfun,text = "Manufacturer:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Manuf.place(x = 50 , y = 300)
        Com = Label(erfun,text = "Company:",font = ("Times 14",20),fg = "#2780FF" , bg = "black");Com.place(x = 50 , y = 400)
        #
        hast = Label(erfun,font = ("Times",20),fg = 'red',bg = 'black');hast.place(y = 100 , x = 180)
        hpri = Label(erfun,font = ('Times',20),fg = 'red',bg = 'black');hpri.place(y = 200 , x = 150)
        hman = Label(erfun,font = ('Times',20),fg = 'red',bg = 'black');hman.place(y = 300 , x = 250)
        hcom = Label(erfun,font = ("Times",20),fg = 'red',bg = 'black');hcom.place(y = 400 , x = 200)
        ###

        # menu page
        menubar = Menu(erfun)
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File" , menu = file)
        #file.add_command(label = "mi")
        def Exit(): khayam_algoritm.yes_or_no(erfun)
        file.add_command(label = "Exit" , command = Exit)
        #
        edit = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit" , menu = edit)
        
        def color_black(): khayam_algoritm.Black(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "black",command = color_black)
        
        def color_red(): khayam_algoritm.Red(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "red",command = color_red)
        
        def color_green(): khayam_algoritm.Green(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "green",command = color_green)
        
        def color_yellow(): khayam_algoritm.Yellow(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "yellow",command = color_yellow)
        
        def color_pink(): khayam_algoritm.Pink(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "pink",command = color_pink)
        
        def color_blue(): khayam_algoritm.Blue(erfun, la, lae, Dele, Name, Price, Manuf, Com, mosh, hast, hpri, hman, hcom, acli)
        edit.add_command(label = "blue",command = color_blue)
        
        erfun.config(menu = menubar)
        #
        lan = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Language" , menu = lan)
        def language_english(): khayam_algoritm.ENG(lae, Dele, la, Name, Price, Manuf, Com, acli, mosh)
        lan.add_command(label = "English",command = language_english)
        
        def language_persian(): khayam_algoritm.PER(lae, Dele, la, Name, Price, Manuf, Com, acli, mosh)
        lan.add_command(label = "Persian", command = language_persian)
            ###
        erfun.mainloop()
    
    



# Initial page design
root = Tk()
root.title("khayam")
root.geometry("1140x700+100+50")
root.resizable(False , False)
root.config(bg = "blue")
Label(root,text = "Welcome",font=('Times 14' , 55),fg = "yellow",bg = "blue").place(y = 100 , x = 430)
Button(root,text = "register",font=('Times 14' , 20),activebackground = "red",bg = "green",command = khayam_page.regi).place(y = 200,x = 590)
Button(root,text = " log in ",font=('Times 14' , 20),activebackground = "red",bg = "green",command = khayam_page.vorod).place(y = 200,x = 465)
root.mainloop()
# end Initial page design
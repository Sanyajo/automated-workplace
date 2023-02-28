import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import psycopg2
from config import host, user, password, db_name
from functools import partial
import time
# import markdown
# import tempfile
# from docxtpl import DocxTemplate

list_WidyGSM = ['Код ГСМ','Название ГСМ','Вид ГСМ','Марка ГСМ']
list_PostawhikiGSM=['Код поставщика', 'Название производителя', 'Адрес производителя', 'Код ГСМ']
list_tab3=[]
list_tab4=[]

conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
        )
conn.autocommit = True

class loginSystem(tk.Frame):

    def __init__(self,logWin):
        super().__init__(logWin)
        self.loginSystem()
    #Окно логина
    def loginSystem(self):

        #методы возвращают размеры экрана, на котором запущено окно
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w=(w//2)-200
        h=(h//2)-200

        win.title('Авторизация')
        win.geometry('300x150+{}+{}'.format(w, h))
        win.resizable(False,False)

        self.frame = tk.Frame(win)
        self.frame.place(relwidth=1, relheight=1)

        self.lab_Login = tk.Label(self.frame, text = "Логин", font = 10)
        self.lab_Login.place(x=40,y=35)

        self.lab_Password = tk.Label(self.frame,text="Пароль",font = 15)
        self.lab_Password .place(x=40,y=80)

        self.inputLogin = ttk.Entry(self.frame, width=15)
        self.inputLogin.place(x=130,y=33)

        self.inputPassword = ttk.Entry(self.frame, width=15, show = "*")
        self.inputPassword.place(x=130,y=78)

        self.connButton = tk.Button(self.frame, text="Войти",fg="black",width=10, font=('',12),command=self.checkLogin)
        self.connButton.pack(side=tk.BOTTOM, pady = 10)

    def checkLogin(self):
        global Polzovatel
        Polzovatel=self.inputLogin.get()
        if Polzovatel == "admin" and self.inputPassword.get() == "admin":
            self.destroy()
            self.frame.destroy()
            mainProgramm(win)
        else:

            w = win.winfo_screenwidth()
            h = win.winfo_screenheight()
            w = (w // 2) - 200
            h = (h // 2) - 200
            errorWindow = tk.Toplevel(self)
            errorWindow.title("Ошибка входа")
            errorWindow.geometry('300x150+{}+{}'.format(w, h))
            errorWindow.resizable(False, False)

            self.errorWindowFrame= tk.Frame(errorWindow)
            self.errorWindowFrame.place(relwidth=1,relheight=1)

            self.errorLabel = tk.Label(self.errorWindowFrame, text="Неверный логин или пароль!\nПовторите попытку снова",font=('',14))
            self.errorLabel.pack(expand=1,pady=35)

            self.repeatButton=tk.Button(self.errorWindowFrame, text="Повторить",width=20,font=('',12),command=errorWindow.destroy)
            self.repeatButton.pack(side=tk.BOTTOM,pady=5)


class mainProgramm(tk.Frame):

    def __init__(self,win):
        super().__init__(win)
        self.startMain()

    def startMain(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2)-400
        h = (h // 2)-400

        win.title('АРМ заведующий предприятия')
        win.geometry('800x600+{}+{}'.format(w,h))
        win.resizable(False, False)

        self.frameMain = tk.Frame(win)
        self.frameMain.place(relwidth=1, relheight=1)

        self.l1 = tk.Frame(self.frameMain,bg="#107eaf",width=300,height=600)
        self.l1.pack(side=tk.RIGHT, fill=tk.Y)

        self.spiskiButton = tk.Button(self.frameMain,text = "Справочные документы",fg="black",width=18, font=('', 15),command=self.spiskiApp)
        self.spiskiButton.place(x=555, y = 100)

        self.docButton = tk.Button(self.frameMain,text="Оперативные документы", fg="black",width=18,font=('',15), command= self.docApp)
        self.docButton.place(x=555,y=200)

        self.othetButton = tk.Button(self.frameMain,text="Отчётные документы",fg="black",width=18,font=('',15),command = self.othWindowSp)
        self.othetButton.place(x=555,y=300)

        self.infoButton = tk.Button(self.frameMain,text="Инфо",fg = "black",width=18,font=('',15),command=self.infoApp)
        self.infoButton.place(x=555,y=475)

        self.closeApp = tk.Button(self.frameMain,text="Выход",fg="black",width=18,font=('',15),command=self.closeApp)
        self.closeApp.place(x=555,y=525)

        img = Image.open("photo.jpeg")
        self.tkimage = ImageTk.PhotoImage(img)
        self.l3=tk.Label(self.frameMain,image=self.tkimage)
        self.l3.place(x=50,y=75)
        ######
        self.infoUser = tk.Label(self.frameMain,text=f"Пользователь:\t{Polzovatel}",font=('',16))
        self.infoUser.place(x=50,y=400)

        self.post = tk.Label(self.frameMain,text="Должность:\tзаведущий заправкой ГСМ",font=('',16))
        self.post.place(x=50,y=425)

        named_tuple = time.localtime()
        time_string = time.strftime("%m/%d/%Y", named_tuple)
        self.LogTime=tk.Label(self.frameMain,text=f"Дата входа:\t{time_string}",font=('',16))
        self.LogTime.place(x=50,y=450)

    #Окно инфо
    def infoApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        infoAppWindow = tk.Toplevel(self)
        infoAppWindow.title('Инфо')
        infoAppWindow.geometry('800x600+{}+{}'.format(w, h))
        infoAppWindow.resizable(False, False)

        self.infoFrame = tk.Frame(infoAppWindow)
        self.infoFrame.place(relwidth=1, relheight=1)

        self.topLine = tk.Label(self.infoFrame, bg="#107eaf",height=5)
        self.topLine.pack(side=tk.TOP,fill = tk.X)

        self.topText = tk.Label(self.infoFrame,text="Информация о АРМ",bg="#107eaf", font = ('',18))
        self.topText.place(x=325,y=30)

        with open('infoProgramm.txt','r') as f:
            t = f.read()
        self.infApp = tk.Label(self.infoFrame,text =t,font = ('',18))
        self.infApp.pack(anchor="n",pady=45)

        self.botLine = tk.Label(self.infoFrame, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.infoFrame, text='Закрыть', width=5, font=('', 18), command=infoAppWindow.destroy)
        self.closeB.place(x=360, y=535)

        f.close()

    #Cправочные документы
    def spiskiApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        spiskiAppWindow = tk.Toplevel(self)
        spiskiAppWindow.title('Справочные документы')
        spiskiAppWindow.geometry('800x600+{}+{}'.format(w, h))
        spiskiAppWindow.resizable(False, False)

        self.spiskiFrame = tk.Frame(spiskiAppWindow)
        self.spiskiFrame.place(relwidth=1, relheight=1)

        self.topLine = tk.Label(self.spiskiFrame, bg="#107eaf", height=5)
        self.topLine.pack(side=tk.TOP, fill=tk.X)

        self.topText = tk.Label(self.spiskiFrame, text="Справочные документы", bg="#107eaf", font=('', 18))
        self.topText.place(x=305,y=30)

        self.spiskButton1 = tk.Button(self.spiskiFrame, text ="Виды ГСМ", bd=0, justify=CENTER, height=3,font=('',18),command=partial(self.viewDB, list_WidyGSM, "WidyGSM"))
        self.spiskButton1.pack(side = tk.TOP, fill = tk.X)

        self.spiskButton2 = tk.Button(self.spiskiFrame, text = "Поставщики ГСМ", bd=0, justify=CENTER, height=3, font=('',18),command=partial(self.viewDB, list_PostawhikiGSM, "PostawhikiGSM"))
        self.spiskButton2.pack(side=tk.TOP, fill = tk.X)

        self.spiskButton3 = tk.Button(self.spiskiFrame, text= "Водители предприятия", bd=0, justify=CENTER, height=3, font=('',18))
        self.spiskButton3.pack(side=tk.TOP, fill = tk.X)

        self.spiskButton4 = tk.Button(self.spiskiFrame,text = "Технические средства предприятия", bd=0, justify=CENTER, height=3, font=('',18))
        self.spiskButton4.pack(side=tk.TOP, fill= tk.X)

        self.botLine = tk.Label(self.spiskiFrame, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.spiskiFrame, text='Закрыть', width=5, font=('', 18), command=spiskiAppWindow.destroy)
        self.closeB.place(x=360, y=535)

    #Оперативные документы
    def docApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        docAppWindow = tk.Toplevel(self)
        docAppWindow.title('Оперативные документы')
        docAppWindow.geometry('800x600+{}+{}'.format(w, h))
        docAppWindow.resizable(False, False)

        self.docFrame = tk.Frame(docAppWindow)
        self.docFrame.place(relwidth=1, relheight=1)

        self.topLine = tk.Label(self.docFrame,bg="#107eaf",height=5)
        self.topLine.pack(side=tk.TOP, fill = tk.X)

        self.topLine = tk.Label(self.docFrame,text="Оперативные документы", bg="#107eaf", font = ('',18))
        self.topLine.place(x=300,y=30)

        self.docButton1 = tk.Button(self.docFrame, text = 'Договор на поставку',bd = 0, justify=CENTER, height=3, font=('',18))
        self.docButton1.pack(side = tk.TOP, fill = X)

        self.docButton2 = tk.Button(self.docFrame, text = 'Товарно-транспортная накладная', bd = 0, justify=CENTER, height=3, font=('',18))
        self.docButton2.pack(side = tk.TOP, fill = X)

        self.docButton3 = tk.Button(self.docFrame, text = 'Карточка складского учета', bd = 0, justify=CENTER, height=3,font=('',18))
        self.docButton3.pack(side=tk.TOP, fill = X)

        self.docButton4 = tk.Button(self.docFrame, text = 'Путевой лист',bd = 0, justify=CENTER,height=3,font=('',18))
        self.docButton4.pack(side=tk.TOP, fill = X)

        self.botLine = tk.Label(self.docFrame, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.docFrame, text='Закрыть', width=5, font=('', 18), command=docAppWindow.destroy)
        self.closeB.place(x=360, y=535)

    #Отчетные документы
    def othWindowSp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        othWind = tk.Toplevel(self)
        othWind.title("Отчётные документы")
        othWind.geometry("800x600+{}+{}".format(w,h))
        othWind.resizable(False,False)

        self.othWindow = tk.Frame(othWind)
        self.othWindow.place(relheight=1,relwidth=1)

        self.topLine = tk.Label(self.othWindow, bg="#107eaf", height=5)
        self.topLine.pack(side=tk.TOP, fill=tk.X)

        self.topText = tk.Label(self.othWindow, text="Отчётные документы", bg="#107eaf", font=('', 18))
        self.topText.place(x=315,y=30)

        self.otButton1 = tk.Button(self.othWindow,text = 'Отчёт по заключенным договорам на поставку ГСМ',bd=0,justify=CENTER,height=3,font=('',18))
        self.otButton1.pack(side=tk.TOP,fill=X)

        # self.otButton2 = tk.Button(self.othWindow,text='Отчёт о движении ГСМ на складе',bd=0,justify=CENTER, height=3, font=('', 18),command=partial(self.insertTable, list_tab2))
        # self.otButton2.pack(side=tk.TOP,fill=X)

        self.otButton3 = tk.Button(self.othWindow, text='Отчёт по водителям',bd=0, justify=CENTER, height=3,font=('',18), command=partial(self.insertTable, list_tab3))
        self.otButton3.pack(side=tk.TOP, fill=X)

        self.otButton4 = tk.Button(self.othWindow, text='Отчёт по путевым листам',bd=0, justify=CENTER, height=3,font=('', 18), command=partial(self.insertTable, list_tab4))
        self.otButton4.pack(side=tk.TOP, fill=X)

        self.botLine = tk.Label(self.othWindow, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.othWindow, text='Закрыть', width=5, font=('', 18), command=othWind.destroy)
        self.closeB.place(x=360,y=535)

    #Окно добавления в таблицу
    def insertTable(self,nameBD):

        dbWindow = tk.Toplevel(self)
        dbWindow.title("Добавление в db")
        dbWindow.geometry("300x300")
        dbWindow.resizable(False,False)

        self.dbMain = tk.Frame(dbWindow)
        self.dbMain.place(relwidth=1, relheight=1)

        ry = 35
        for i in nameBD:
            self.lab_Login = tk.Label(self.dbMain, text=i, font=10)
            self.lab_Login.place(x=45, y=ry)

            self.inputLogin = ttk.Entry(self.dbMain, width=15)
            self.inputLogin.place(x=80, y=ry)
            # a.append(b)
            ry+=20

        # try:
        #     pass
        #     with conn.cursor() as cursor:
        #         cursor.execute(
        #             f"""INSERT INTO tab1 (tab1_id, number, name) VALUES
        #             ('{a[0]}', '{self.inputLogin.get[1]}', '{self.inputLogin.get[2]}');"""
        #         )
        #         print("[INFO] Insert GOOOD!")
        # except Exception as _ex:
        #     pass

    #Окно закрытия приложения
    def closeApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        clWin = tk.Toplevel(self)
        clWin.title("Выход из АРМ")
        clWin.geometry('300x150+{}+{}'.format(w, h))
        clWin.resizable(False, False)

        self.closeWindow = tk.Frame(clWin)
        self.closeWindow.place(relwidth=1, relheight=1)

        self.textCloseWindow = tk.Label(self.closeWindow, text="Вы дейтвительно хотите выйти из АРМ?",font=('',14))
        self.textCloseWindow.place(x=15,y=40)

        self.yesButton = tk.Button(self.closeWindow, text="Да",width=12 ,font = ('',12),command=self.rebot)
        self.yesButton.place(x=15,y=100)

        self.noButton = tk.Button(self.closeWindow, text="Нет",fg='red', width=12, font=('', 12),command=clWin.destroy)
        self.noButton.place(x=150,y=100)

    #Простотр содержимого БД
    def viewDB(self,list,tablename):

        viewDB = tk.Toplevel(self)
        viewDB .title(f"{tablename}")
        viewDB .geometry('1280x1024')
        viewDB.rowconfigure(index=0,weight=1)
        viewDB.columnconfigure(index=0,weight=1)
        viewDB .resizable(True, True)

        self.viewDB  = tk.Frame(viewDB)
        self.viewDB.place(relwidth=1, relheight=1)
        data = ('',)
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "{tablename}" """)
                data = (row for row in cursor.fetchall())
        except Exception as _ex:
            print("HELP")

        self.tree = ttk.Treeview(self.viewDB,height=37,columns=list, show="headings")
        self.tree.pack(fill=X)

        for i in list:
            self.tree.heading(f"{i}",text=f"{i}",anchor=W)

        for row in data:
            self.tree.insert('',tk.END,values=tuple(row))

        for person in data:
            self.tree.insert("",END,values=tuple(person))

        self.blueLab = tk.Label(self.viewDB, bg="#107eaf", height=5)
        self.blueLab.pack(side = BOTTOM, fill = X)

        self.inputButton = tk.Button(self.viewDB, text="Добавить", bd=0, justify=CENTER, width=12, font=('', 18))
        self.inputButton.place(x=100,y=720)

        self.changeButton = tk.Button(self.viewDB, text = "Изменить", bd=0, justify=CENTER, width=12, font=('',18))
        self.changeButton.place(x=300,y=720)

        self.closeButton = tk.Button(self.viewDB, text = "Закрыть", bd=0, justify=CENTER, width=12, font=('',18),command=viewDB.destroy)
        self.closeButton.place(x=500,y=720)

    #Выход из системы
    def rebot(a, _event=None):
        a.destroy()
        loginSystem(win)


class mainBD(tk.Frame):
    pass

class Table(tk.Frame):
    def __int__(self,parent = None, headings = tuple(), rows = tuple()):
        super().__init__(parent)

        table=ttk.Treeview(self,show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head,text=head,anchor=tk.CENTER)
            table.column(head,anchor=tk.CENTER)

        for row in rows:
            table.insert('',tk.END, values=tuple(row))

        # scrolltable = tk.Scrollbar(self, command=table.yview)
        # table.configure(yscrollcommand=scrolltable.set)
        # scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        # table.pack(expand=tk.YES, fill=tk.BOTH)



if __name__ =="__main__":
    win = tk.Tk()
    start = loginSystem(win)
    start.pack()
    # start.destroy()
    # start=mainProgramm(win)
    # start.pack
    win.mainloop()
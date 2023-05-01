import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import psycopg2
from config import *
from functools import partial
import time
import datetime

import subprocess
import gzip
import os


# import markdown
# import tempfile
# from docxtpl import DocxTemplate

conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name,
        port = "5432"
        )
conn.autocommit = True

class progrload(tk.Frame):
    def __init__(self, win):
        super().__init__(win)
        self.progbar()

    def progbar(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        win.title('АРМ')
        win.geometry('500x400+{}+{}'.format(w, h))
        win.resizable(False, False)
        self.frame = tk.Frame(win, bg= "#4d4f4c")
        self.frame.place(relwidth=1, relheight=1)

        value_var = IntVar()
        value = 10

        img = Image.open("logo2.png")
        self.tkimage = ImageTk.PhotoImage(img)
        self.l3 = tk.Label(self.frame, image=self.tkimage, bg="#4d4f4c")
        self.l3.pack(expand=1)

        self.progressbar = ttk.Progressbar(orient="horizontal", variable=value_var, maximum=100)
        self.progressbar.pack(side = tk.BOTTOM, fill = tk.X)

        self.label = ttk.Label(self.frame, textvariable=value_var)
        self.progressbar.start()

        while True:
            self.frame.update()
            if value_var.get() == 11:
                self.progressbar.stop()
                loginSystem(win)
                break

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

        win.title('АРМ заведующий')
        win.geometry('800x600+{}+{}'.format(w,h))
        win.resizable(False, False)

        self.frameMain = tk.Frame(win)
        self.frameMain.place(relwidth=1, relheight=1)

        self.l1 = tk.Frame(self.frameMain,bg="#107eaf",width=300,height=600)
        self.l1.pack(side=tk.RIGHT, fill=tk.Y)
        self.l2 = tk.Label(self.frameMain,bg="#4d4f4c",width=500,height=600)
        self.l2.pack(side=tk.LEFT, fill=tk.Y)

        self.spiskiButton = tk.Button(self.frameMain,text = "Справочные документы",fg="black",width=18, font=('', 15),command=self.spiskiApp)
        self.spiskiButton.place(x=555, y = 100)

        self.docButton = tk.Button(self.frameMain,text="Оперативные документы", fg="black",width=18,font=('',15), command= self.docApp)
        self.docButton.place(x=555,y=200)

        self.othetButton = tk.Button(self.frameMain,text="Отчётные документы",fg="black",width=18,font=('',15),command = self.othWindowSp)
        self.othetButton.place(x=555,y=300)

        self.arhbd = tk.Button(self.frameMain,text="Восстановление БД", fg="black", width=18, font=('',15), command = self.arhbutton)
        self.arhbd.place(x=555, y =435)

        self.infoButton = tk.Button(self.frameMain,text="Инфо",fg = "black",width=18,font=('',15),command=self.infoApp)
        self.infoButton.place(x=555,y=475)

        self.closeApp = tk.Button(self.frameMain,text="Выход",fg="black",width=18,font=('',15),command=self.closeApp)
        self.closeApp.place(x=555,y=525)

        img = Image.open("logo2.png")
        self.tkimage = ImageTk.PhotoImage(img)
        self.l3=tk.Label(self.frameMain,image=self.tkimage,bg="#4d4f4c")
        self.l3.place(x=50,y=75)

        self.infoUser = tk.Label(self.frameMain,text=f"Пользователь:\t{Polzovatel}",font=('',16), bg="#4d4f4d")
        self.infoUser.place(x=50,y=400)

        self.post = tk.Label(self.frameMain,text="Должность:\tзаведущий заправкой ГСМ",font=('',16), bg="#4d4f4d")
        self.post.place(x=50,y=425)

        named_tuple = time.localtime()
        time_string = time.strftime("%m/%d/%Y", named_tuple)
        self.LogTime=tk.Label(self.frameMain,text=f"Дата входа:\t{time_string}",font=('',16), bg="#4d4f4d")
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

        self.spiskButton1 = tk.Button(self.spiskiFrame, text ="Виды ГСМ", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_typegsm, "typegsm", "Справочник вида ГСМ"))
        self.spiskButton1.pack(side = tk.TOP, fill = tk.X)

        self.spiskButton2 = tk.Button(self.spiskiFrame, text = "Поставщики ГСМ", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_vendorgsm, "vendorgsm", "Справочник поставщиков ГСМ"))
        self.spiskButton2.pack(side=tk.TOP, fill = tk.X)

        self.spiskButton3 = tk.Button(self.spiskiFrame, text= "Водители предприятия", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_companydrivers, "companydrivers", "Справочник водителей предприятия"))
        self.spiskButton3.pack(side=tk.TOP, fill = tk.X)

        self.spiskButton4 = tk.Button(self.spiskiFrame, text = "Технические средства предприятия", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_comptechnmeans, "comptechnmeans", "Справочник технических средств предприятия"))
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
        docAppWindow.geometry('800x700+{}+{}'.format(w, h))
        docAppWindow.resizable(False, False)

        self.docFrame = tk.Frame(docAppWindow)
        self.docFrame.place(relwidth=1, relheight=1)

        self.topLine = tk.Label(self.docFrame,bg="#107eaf",height=5)
        self.topLine.pack(side=tk.TOP, fill = tk.X)

        self.topLine = tk.Label(self.docFrame,text="Оперативные документы", bg="#107eaf", font = ('',18))
        self.topLine.place(x=300,y=30)

        self.docButton1 = tk.Button(self.docFrame, text = 'Договор на поставку', bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_deliverycontract, "deliverycontract", "Договор на поставку"))
        self.docButton1.pack(side = tk.TOP, fill = X)

        self.docButton2 = tk.Button(self.docFrame, text = 'Товарно-транспортная накладная', bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_ttn, "ttn", "ТТН"))
        self.docButton2.pack(side = tk.TOP, fill = X)

        self.docButton3 = tk.Button(self.docFrame, text = 'Карточка складского учета', bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_ksu, "ksu", "Карточная складского учета"))
        self.docButton3.pack(side=tk.TOP, fill = X)

        self.docButton4 = tk.Button(self.docFrame, text = 'Путевой лист', bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_pl, "pl", "ПЛ"))
        self.docButton4.pack(side=tk.TOP, fill = X)

        self.docButton5 = tk.Button(self.docFrame, text='Наряд', bd=0, justify=CENTER, height=3, font=('', 18), command=partial(self.viewDB, list_naryad, "naryad", "Наряд"))
        self.docButton5.pack(side=tk.TOP, fill=X)

        self.docButton6 = tk.Button(self.docFrame, text='Файл прихода', bd=0, justify=CENTER, height=3, font=('', 18),
                                    command=partial(self.viewDB, list_prihod, "prihfile", "Файл прихода"))
        self.docButton6.pack(side=tk.TOP, fill=X)

        self.docButton7 = tk.Button(self.docFrame, text='Файл расхода', bd=0, justify=CENTER, height=3, font=('', 18),
                                    command=partial(self.viewDB, list_rashod, "rashfile", "Файл расхода"))
        self.docButton7.pack(side=tk.TOP, fill=X)



        self.botLine = tk.Label(self.docFrame, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.docFrame, text='Закрыть', width=5, font=('', 18), command=docAppWindow.destroy)
        self.closeB.place(x=360, y=635)
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

        self.otButton2 = tk.Button(self.othWindow,text='Отчёт о движении ГСМ на складе',bd=0,justify=CENTER, height=3, font=('', 18))
        self.otButton2.pack(side=tk.TOP,fill=X)

        self.otButton3 = tk.Button(self.othWindow, text='Отчёт по водителям',bd=0, justify=CENTER, height=3,font=('',18))
        self.otButton3.pack(side=tk.TOP, fill=X)

        self.otButton4 = tk.Button(self.othWindow, text='Отчёт по путевым листам',bd=0, justify=CENTER, height=3,font=('', 18))
        self.otButton4.pack(side=tk.TOP, fill=X)

        self.botLine = tk.Label(self.othWindow, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.othWindow, text='Закрыть', width=5, font=('', 18), command=othWind.destroy)
        self.closeB.place(x=360,y=535)
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
    def viewDB(self, column_names, tablename, tablenamerus):
        self.viewTableDataBases = tk.Toplevel(self)
        self.viewTableDataBases.title(f"{tablenamerus}")
        screen_width = self.viewTableDataBases.winfo_screenwidth()
        self.viewTableDataBases.geometry(f'{screen_width}x800')
        self.viewTableDataBases.rowconfigure(index=0, weight=1)
        self.viewTableDataBases.columnconfigure(index=0, weight=1)
        self.viewTableDataBases.resizable(False, False)

        self.viewDB_frame = tk.Frame(self.viewTableDataBases)
        self.viewDB_frame.place(relwidth=1, relheight=1)

        data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "{tablename}" """)
                data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            print("ТАБЛИЦА НЕ ПОДТЯНУЛАСЬ")

        self.tree = ttk.Treeview(self.viewDB_frame, height=37, columns=column_names, show="headings")
        self.tree.pack(fill=X)

        total_width = 0
        for i in column_names:
            self.tree.heading(f"{i}", text=f"{i}")
            if i == '№':
                self.tree.column(f"{i}", stretch=False)
                self.tree.column(f"{i}", width=50)
                total_width += 50;
            else:
                column_width = screen_width // len(column_names)
                self.tree.column(f"{i}", width=column_width, stretch=True)
                total_width += column_width

        for row in data:
            self.tree.insert('', tk.END, values=tuple(row))
            for i, value in enumerate(row):
                max_width = max([len(str(val)) for j, val in enumerate(row)] + [len(column_names[i])])
                column_width = screen_width // len(column_names)
                self.tree.column(column_names[i], width=max_width + 20, anchor=CENTER)


        if tablename == "prihfile" or tablename == "rashfile" or tablename == "ksu":
            self.blueLab = tk.Label(self.viewDB_frame, bg="#107eaf", height=35)
            self.blueLab.pack(side=tk.BOTTOM, fill=tk.X)
            self.searchButton = tk.Button(self.viewDB_frame, text="Поиск", bd=0, justify=CENTER, width=12, font=('', 18), command =partial(self.serCH, tablename))
            self.searchButton.place(x=100, y=720)

            self.closeButton = tk.Button(self.viewDB_frame, text="Закрыть", bd=0, justify=CENTER, width=12, font=('', 18),
                                         command=self.reboot)
            self.closeButton.place(x=300, y=720)
        else:

            self.blueLab = tk.Label(self.viewDB_frame, bg="#107eaf", height=35)
            self.blueLab.pack(side=tk.BOTTOM, fill = tk.X)

            self.inputButton = tk.Button(self.viewDB_frame, text="Добавить", bd=0, justify=CENTER, width=12, font=('', 18),
                                         command=partial(self.inputTableWindows, column_names, tablename, tablenamerus))
            self.inputButton.place(x=100, y=720)

            self.changeButton = tk.Button(self.viewDB_frame, text="Изменить", bd=0, justify=CENTER, width=12, font=('', 18))
            self.changeButton.place(x=300, y=720)

            self.deleteButton = tk.Button(self.viewDB_frame, text="Удаление", bd=0, justify=CENTER, width=12, font=('', 18))
            self.deleteButton.place(x=500, y=720)

            self.searchButton = tk.Button(self.viewDB_frame, text="Поиск", bd=0, justify=CENTER, width=12, font=('', 18), command =partial(self.serCH, tablename))
            self.searchButton.place(x=700, y=720)

            self.closeButton = tk.Button(self.viewDB_frame, text="Закрыть", bd=0, justify=CENTER, width=12, font=('', 18),
                                         command=self.reboot)
            self.closeButton.place(x=900, y=720)

    #Выход из системы и архивация бд
    def rebot(a, _event=None):
        a.destroy()
        os.environ['PGPASSWORD'] = f'{password}'
        cmd = f'pg_dump -h {host} -p 5432 -U {user} -Fc {db_name} > {db_name}.dump'
        subprocess.call(cmd, shell=True)
        del os.environ['PGPASSWORD']
        loginSystem(win)

    def reboot(a, _event=None):
        a.destroy()
        mainProgramm(win)

    def inputTableWindows(self, column_names, tablename, tablenamerus):
        if tablename == "typegsm":
            buflist = list_typegsm
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в справочник ГСМ")
            inputTableWin.geometry('400x400')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1=tk.Label(self.inTable, text= f"{buflist[0]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable,width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text= f"{buflist[1]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e=ttk.Entry(self.inTable,width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=3, font=('',18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e=ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить",fg="black",width=18,font=('',15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=90,y=300)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black",width=18,font=('',15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=90, y=350)

        if tablename == "vendorgsm":
            buflist = list_vendorgsm
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в справочник поставщиков")
            inputTableWin.geometry('400x500')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=18, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=90, y=400)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=18, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=90, y=450)

        if tablename == "companydrivers":
            buflist = list_companydrivers
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в справочник водителей предприятия")
            inputTableWin.geometry('410x800')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"Табельный номер\n водителя", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"ФИО водителя", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"Государственный номер прикрепленного авто", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"Дата приема на работу", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"Дата выдачи водительсокого удостоверения", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"Дата действия водительсокого удостоверения", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)
            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"Номер водительского удостоверения", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)
            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"Категория водительского удостоверения", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)
            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=10, y=750)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=200, y=750)

        if tablename == "comptechnmeans":
            buflist = list_comptechnmeans
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в справочник технических средств")
            inputTableWin.geometry('410x800')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}", bd=0, justify=CENTER, height=2,font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)
            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)
            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)
            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.l9 = tk.Label(self.inTable, text=f"{buflist[8]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l9.pack(side=tk.TOP, fill=tk.X)
            self.l9e = ttk.Entry(self.inTable, width=15)
            self.l9e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=15, y=735)
            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=205, y=735)

        if tablename == "deliverycontract":
            buflist = list_deliverycontract
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в договора на поставку")
            inputTableWin.geometry('410x700')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l0 = tk.Label(self.inTable, text=f"{buflist[0]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l0.pack(side=tk.TOP, fill=tk.X)
            self.l0e = ttk.Entry(self.inTable, width=15)
            self.l0e.pack(fill=tk.X)

            self.l1 = tk.Label(self.inTable, text=f"{buflist[1]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[3]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[4]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[5]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[6]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)
            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[8]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)
            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)


            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=15, y=635)
            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=205, y=635)

        if tablename == "naryad":
            buflist = list_naryad
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в наряд")
            inputTableWin.geometry('400x600')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=18, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=90, y=500)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=18, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=90, y=550)

        if tablename == "pl":
            buflist = list_pl
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление ПЛ")
            inputTableWin.geometry('400x550')
            inputTableWin.resizable(False, False)
            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"Номер путевого листа", bd=0, justify=CENTER, height=3,
                               font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"Дата составления ПЛ", bd=0, justify=CENTER, height=3, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"Номер водительского удостоверения", bd=0, justify=CENTER,
                               height=3, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"Табельный номер водителя", bd=0, justify=CENTER, height=3,
                               font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"Государственный номер авто", bd=0, justify=CENTER,
                               height=3, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)


            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15), command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=15, y=500)
            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=205, y=500)

        if tablename == "ttn":
            buflist = list_ttn
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в ТТН")
            inputTableWin.geometry('400x800')
            inputTableWin.resizable(False, False)

            self.inTable = tk.Frame(inputTableWin)
            self.inTable.place(relwidth=1, relheight=1)

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)
            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)
            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)
            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)
            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)
            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)
            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)
            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)
            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.l9 = tk.Label(self.inTable, text=f"{buflist[8]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l9.pack(side=tk.TOP, fill=tk.X)
            self.l9e = ttk.Entry(self.inTable, width=15)
            self.l9e.pack(fill=tk.X)


            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15),command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.place(x=15, y=735)
            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=205, y=735)

    def inputTableSQL(self, column_names, tablename, tablenamerus):
        if tablename == "typegsm":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "code_gsm", "name_gsm", "unit") VALUES 
            	                            ('{value1}','{value2}', '{value3}') """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)

            except Exception as _ex:
                self.errorWindows()

        if tablename == "vendorgsm":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "code_post", "name_proizv", "addres_proizv", "code_gsm") VALUES 
            	                            ('{value1}','{value2}', '{value3}', '{value4}') """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "companydrivers":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            value6 = self.l6e.get()
            value7 = self.l7e.get()
            value8 = self.l8e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "tab_number", "drivers_name", "national_avto_num", "date_of_hire", "date_driverlicens", "validity_day_drlic", "num_drivlicens", "category_drivlicens") VALUES 
            	                            ('{value1}','{value2}', '{value3}', '{value4}', '{value5}', '{value6}', '{value7}', '{value8}') """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "deliverycontract":
            check = False
            value0 = self.l0e.get()
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = float(self.l5e.get())
            value6 = float(self.l6e.get())
            value7 =  value5 * value6
            value8 = float(self.l8e.get())
            value9 = float(value7*value8) /100.0
            value10= value9+value7
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "contract_number", "date_contract", "code_gsm", "code_post", "untill", "price", "amount", "stoim", "rate_nds", "price_nds", "price_of_nds") VALUES 
            	                            ('{value0}','{value1}', '{value2}', '{value3}', '{value4}', {value5}, {value6}, {value7}, {value8}, {value9}, {value10} )""")
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "naryad":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                               	                "nar_number", "tab_number", "drivers_name", "national_avto_num","num_drivlicens") VALUES 
                               	                ('{value1}','{value2}', '{value3}', '{value4}', '{value5}') """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "ttn":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            value6 = float(self.l6e.get())
            value7 = float(self.l7e.get())
            value8 = float(self.l8e.get())
            value9 = float(self.l9e.get())
            value10 = (value6 * value9) / 100.0
            value11 = value10 + value6
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "ttn_number", "date_zakl_ttn", "code_gsm", "code_post", "untill", "price", "amount", "stoim", "rate_nds", "price_nds", "price_of_nds") VALUES 
            	                            ('{value1}','{value2}', '{value3}', '{value4}', '{value5}', {value6}, {value7}, {value8}, {value9}, {value10}, {value11} )""")
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "pl":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                        	                            "pl_number", "date_pl", "tab_number","num_drivlicens","national_avto_num") VALUES 
                        	                            ('{value1}','{value2}', '{value3}', '{value4}', '{value5}') """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)

            except Exception as _ex:
                self.errorWindows()

        if tablename == "comptechnmeans":
            check = False
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = float(self.l5e.get())
            value6 = float(self.l6e.get())
            value7 = float(self.l7e.get())
            value8 = float(self.l8e.get())
            value9 = float(self.l9e.get())
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                        	                            "national_avto_num", "auto_mark", "body_number","untill","load_capacity","year_of_product","first_cost","kod_porc","last_cost") VALUES 
                        	                            ('{value1}','{value2}', '{value3}', '{value4}', {value5}, {value6}, {value7}, {value8}, {value9}) """)
                    check = True
                    if check:
                        self.refresh(column_names, tablename, tablenamerus)

            except Exception as _ex:
                self.errorWindows()



    def errorWindows(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200
        errorWindow = tk.Toplevel(self)
        errorWindow.title("Ошибка ввода")
        errorWindow.geometry('300x150+{}+{}'.format(w, h))
        errorWindow.resizable(False, False)

        self.errorWindowFrame = tk.Frame(errorWindow)
        self.errorWindowFrame.place(relwidth=1, relheight=1)

        self.errorLabel = tk.Label(self.errorWindowFrame, text="Некорректный данные !",
                                   font=('', 14))
        self.errorLabel.pack(expand=1, pady=35)

        self.repeatButton = tk.Button(self.errorWindowFrame, text="Повторить", width=20, font=('', 12),
                                      command=errorWindow.destroy)
        self.repeatButton.pack(side=tk.BOTTOM, pady=5)

    def serCH(self, tablename):

        val = searhComboboxList[tablename]
        serTable = tk.Toplevel(self)
        serTable.title("Поиск")
        serTable.geometry('300x100')
        serTable.resizable(False, False)

        self.sTable = tk.Frame(serTable)
        self.sTable.place(relheight=1, relwidth=1)

        self.combobox = ttk.Combobox(self.sTable, values=val)
        self.combobox.pack(anchor=NW, padx=6, pady=6)

        self.temp = ttk.Entry(self.sTable, width=15)
        self.temp.pack(fill=X)

        self.poisk = tk.Button(self.sTable, text="поиск", width=15, command=partial(self.serBD, tablename))
        self.poisk.pack(fill=X)
    def serBD(self, tablename):
        a1 = self.combobox.get()
        a2 = self.temp.get()

        table = tk.Toplevel(self)
        table.title("Искомые значения")
        table.geometry('1920x800')
        table.resizable(False, False)

        self.dtable = tk.Frame(table)
        self.dtable.place(relheight=1, relwidth=1)
        data = ()
        if a1 in searhListINT:
            a1 = searhSQLListINT[(tablename,a1)]
            a2 = float(a2)
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM {tablename} WHERE {a1} = {a2}
                                        """)
                    data = (row for row in cursor.fetchall())
            except Exception as _ex:
                self.errorWindows()
        else:
            a1 = searhSQLList[(tablename,a1)]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM {tablename} WHERE {a1} = '{a2}'
                                                    """)
                    data = (row for row in cursor.fetchall())
            except Exception as _ex:
                self.errorWindows()

        if tablename == "typegsm":
            val = list_typegsm
        if tablename == "vendorgsm":
            val = list_vendorgsm
        if tablename == "ttn":
            val = list_ttn
        if tablename == "rashfile":
            val = list_rashod
        if tablename == "prihfile":
            val = list_prihod
        if tablename == "pl":
            val = list_pl
        if tablename == "naryad":
            val = list_naryad
        if tablename == "ksu":
            val = list_ksu
        if tablename == "deliverycontract":
            val = list_deliverycontract
        if tablename == "comptechnmeans":
            val = list_comptechnmeans
        if tablename == "companydrivers":
            val = list_companydrivers

        self.TBL = ttk.Treeview(self.dtable, height=22, columns=val, show="headings")
        self.TBL.pack(fill=X)

        for i in val:
            self.TBL.heading(f"{i}", text=f"{i}")
            self.TBL.column(f"{i}", width=10, anchor=CENTER)

        for row in data:
            self.TBL.insert('', tk.END, values=tuple(row))

        self.blueLab = tk.Label(self.dtable, bg="#107eaf", height=35)
        self.blueLab.pack(side=tk.BOTTOM, fill=tk.X)
        self.closeButton = tk.Button(self.dtable, text="Закрыть", bd=0, justify=CENTER, width=12, font=('', 18),
                                     command=self.reboot)
        self.closeButton.place(x=900, y = 700)


    def arhbutton(self):
        win.title('Авторизация')
        win.geometry('300x150')
        win.resizable(False, False)

        self.frame = tk.Frame(win)
        self.frame.place(relwidth=1, relheight=1)

        self.lab_Login = tk.Label(self.frame, text="Логин", font=10)
        self.lab_Login.place(x=40, y=35)

        self.lab_Password = tk.Label(self.frame, text="Пароль", font=15)
        self.lab_Password.place(x=40, y=80)

        self.inputLogin = ttk.Entry(self.frame, width=15)
        self.inputLogin.place(x=130, y=33)

        self.inputPassword = ttk.Entry(self.frame, width=15, show="*")
        self.inputPassword.place(x=130, y=78)

        self.connButton = tk.Button(self.frame, text="Войти", fg="black", width=10, font=('', 12),
                                    command=self.checkarhbd)
        self.connButton.pack(side=tk.BOTTOM, pady=10)
    def checkarhbd(self):
        global sysAdmin
        sysAdmin = self.inputLogin.get()
        if sysAdmin == "sysadmin" and self.inputPassword.get() == "admin":
            self.destroy()
            self.frame.destroy()
            arhBD(win)
        else:
            w = win.winfo_screenwidth()
            h = win.winfo_screenheight()
            w = (w // 2) - 200
            h = (h // 2) - 200
            errorWindow = tk.Toplevel(self)
            errorWindow.title("Ошибка входа")
            errorWindow.geometry('300x150+{}+{}'.format(w, h))
            errorWindow.resizable(False, False)

            self.errorWindowFrame = tk.Frame(errorWindow)
            self.errorWindowFrame.place(relwidth=1, relheight=1)

            self.errorLabel = tk.Label(self.errorWindowFrame,
                                       text="Неверный логин или пароль!\nПовторите попытку снова", font=('', 14))
            self.errorLabel.pack(expand=1, pady=35)

            self.repeatButton = tk.Button(self.errorWindowFrame, text="Повторить", width=20, font=('', 12),
                                          command=errorWindow.destroy)
            self.repeatButton.pack(side=tk.BOTTOM, pady=5)

    def refresh(self, column_names, tablename, tablenamerus):
        self.viewTableDataBases.destroy()
        self.viewDB(column_names, tablename, tablenamerus)

class arhBD(tk.Frame):
    def __init__(self, win):
        super().__init__(win)
        self.startarhbd()

    def startarhbd(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        win.title('Восстановление БД')
        win.geometry('500x400+{}+{}'.format(w, h))
        win.resizable(False, False)
        self.frame = tk.Frame(win, bg="#4d4f4c")
        self.frame.place(relwidth=1, relheight=1)

        img = Image.open("logo2.png")
        self.tkimage = ImageTk.PhotoImage(img)
        self.l3 = tk.Label(self.frame, image=self.tkimage, bg="#4d4f4c")
        self.l3.pack(expand=1)

        value_var = IntVar()
        value = 10
        self.progressbar = ttk.Progressbar(orient="horizontal", variable=value_var, maximum=100)
        self.progressbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.label = ttk.Label(self.frame, textvariable=value_var)
        self.progressbar.start()

        dump_file_path = './kurs.dump'
        os.environ['PGPASSWORD'] = f'{password}'
        cmd = f'pg_restore -h {host} -p 5432 -U {user} -d kurs3 {dump_file_path}'
        p = subprocess.Popen(cmd, shell=True)
        del os.environ['PGPASSWORD']

        while True:
            self.frame.update()
            if value_var.get() == 99:
                self.progressbar.stop()
                loginSystem(win)
                break




if __name__ =="__main__":
    win = tk.Tk()
    start = progrload(win)
    start.pack()
    # start.destroy()
    # start=mainProgramm(win)
    # start.pack
    win.mainloop()
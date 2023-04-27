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

list_typegsm = ['Код ГСМ', 'Название ГСМ', 'Единица измерения']
list_vendorgsm=['Код поставщика', 'Название производителя', 'Адрес производителя', 'Код ГСМ']
list_companydrivers=['Табельный номер\n водителя', 'ФИО водителя', 'Государственный но\nмер прикрепленного авто', 'Дата приема\n на работу', '\tДата выдачи\n водительсокого удостоверения', '\tДата действия\n водительсокого удостоверения', 'Номер водительского\n удостоверения', 'Категория водительского\n удостоверения']
list_comptechnmeans=['Код гаражный', 'НомГосРегистр', 'Марка авто', 'Номер кузова', 'ЕдИмз', 'Грузоподъёмность', 'Год выпусмка', 'Первичная стоимость', 'Код %', 'Остаточная стоимость']
list_deliverycontract=['Номер договора','Дата заключения\n договора','Код ГСМ','Код поставщика','Единица\n измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']
list_naryad=['Номер наряда','Табельный номер\nводителя','ФИО водителя','Государственный номер\nавто','Номер водительского\n удостоверения']
list_pl=['Номер путевого\nлиста','Дата составления ПЛ','Номер водительского\nудостоверения','Табельный номер\nводителя','Государственный номер\nавто']
list_prihod=['Номер документа','Дата составленеия','Номер ТТН','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Количество','Цена','Ставка НДС']
list_rashod=['Номер документа','Номер ПЛ','Дата ПЛ','Код ГСМ','Единица измерения','Количество','Цена','Ставка НДС']
list_ksu=['Номер склада','Номер цистерны','Номер документа','Код ГСМ','Код поставщика','Дата оставления\nКСУ','Единица измерения','Стоимость единицы','Остаток на начало\nпериода','Количество прихода','Количество расхода','Остаток на конец\nпериода']
list_ttn=['Номер документа','Дата ТТН','Код ГСМ','Код поставщика','Единица измерения','Цена','Количество','Стоимость','Ставка НДС','Сумма НДС','Сумма с НДС']

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

        self.spiskButton1 = tk.Button(self.spiskiFrame, text ="Виды ГСМ", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_typegsm, "typegsm","Справочник вида ГСМ"))
        self.spiskButton1.pack(side = tk.TOP, fill = tk.X)

        self.spiskButton2 = tk.Button(self.spiskiFrame, text = "Поставщики ГСМ", bd=0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_vendorgsm, "vendorgsm","Справочник поставщиков ГСМ"))
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
        docAppWindow.geometry('800x600+{}+{}'.format(w, h))
        docAppWindow.resizable(False, False)

        self.docFrame = tk.Frame(docAppWindow)
        self.docFrame.place(relwidth=1, relheight=1)

        self.topLine = tk.Label(self.docFrame,bg="#107eaf",height=5)
        self.topLine.pack(side=tk.TOP, fill = tk.X)

        self.topLine = tk.Label(self.docFrame,text="Оперативные документы", bg="#107eaf", font = ('',18))
        self.topLine.place(x=300,y=30)

        self.docButton1 = tk.Button(self.docFrame, text = 'Договор на поставку',bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_deliverycontract, "deliverycontract", "Договор на поставку"))
        self.docButton1.pack(side = tk.TOP, fill = X)

        self.docButton2 = tk.Button(self.docFrame, text = 'Товарно-транспортная накладная', bd = 0, justify=CENTER, height=3, font=('',18), command=partial(self.viewDB, list_ttn, "ttn", "ТТН"))
        self.docButton2.pack(side = tk.TOP, fill = X)

        self.docButton3 = tk.Button(self.docFrame, text = 'Карточка складского учета', bd = 0, justify=CENTER, height=3,font=('',18), command=partial(self.viewDB, list_ksu, "ksu", "Карточная складского учета"))
        self.docButton3.pack(side=tk.TOP, fill = X)

        self.docButton4 = tk.Button(self.docFrame, text = 'Путевой лист',bd = 0, justify=CENTER,height=3,font=('',18), command=partial(self.viewDB, list_pl, "pl", "ПЛ"))
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

        # self.otButton3 = tk.Button(self.othWindow, text='Отчёт по водителям',bd=0, justify=CENTER, height=3,font=('',18), command=partial(self.insertTable, list_Woditely))
        # self.otButton3.pack(side=tk.TOP, fill=X)
        #
        # self.otButton4 = tk.Button(self.othWindow, text='Отчёт по путевым листам',bd=0, justify=CENTER, height=3,font=('', 18), command=partial(self.insertTable, list_tab4))
        # self.otButton4.pack(side=tk.TOP, fill=X)

        self.botLine = tk.Label(self.othWindow, bg="#107eaf", height=5)
        self.botLine.pack(side=tk.BOTTOM, fill=tk.X)

        self.closeB = tk.Button(self.othWindow, text='Закрыть', width=5, font=('', 18), command=othWind.destroy)
        self.closeB.place(x=360,y=535)

    #Окно добавления в таблицу
    def insertTable(self,tablename,list):

        # try:
        #     pass
        #     with conn.cursor() as cursor:
        #         cursor.execute(
        #             f"""INSERT INTO {tablename} {list_WidyGSM} VALUES
        #             ('{new_data[0]}', '{new_data[1]}', '{new_data[2]}');"""
        #         )
        #         print("[INFO] Insert GOOOD!")
        # except Exception as _ex:
            pass

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
        viewTableDataBases = tk.Toplevel(self)
        viewTableDataBases.title(f"{tablenamerus}")
        screen_width = viewTableDataBases.winfo_screenwidth()
        viewTableDataBases.geometry(f'{screen_width}x800')
        viewTableDataBases.rowconfigure(index=0, weight=1)
        viewTableDataBases.columnconfigure(index=0, weight=1)
        viewTableDataBases.resizable(False, False)

        self.viewDB = tk.Frame(viewTableDataBases)
        self.viewDB.place(relwidth=1, relheight=1)

        data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "{tablename}" """)
                data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            print("ТАБЛИЦА НЕ ПОДТЯНУЛАСЬ")

        self.tree = ttk.Treeview(self.viewDB, height=37, columns=column_names, show="headings")
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
        #
        # for person in data:
        #     self.tree.insert("", END, values=tuple(person))

        self.blueLab = tk.Label(self.viewDB, bg="#107eaf", height=35)
        self.blueLab.pack(side=tk.BOTTOM, fill = tk.X)

        self.inputButton = tk.Button(self.viewDB, text="Добавить", bd=0, justify=CENTER, width=12, font=('', 18),
                                     command=partial(self.inputTableWindows, tablename))
        self.inputButton.place(x=100, y=720)

        self.changeButton = tk.Button(self.viewDB, text="Изменить", bd=0, justify=CENTER, width=12, font=('', 18))
        self.changeButton.place(x=300, y=720)

        self.closeButton = tk.Button(self.viewDB, text="Закрыть", bd=0, justify=CENTER, width=12, font=('', 18),
                                     command=self.reboot)
        self.closeButton.place(x=500, y=720)


    def reboot(a, _event=None):
        a.destroy()
        mainProgramm(win)
    #Выход из системы
    def rebot(a, _event=None):
        a.destroy()
        loginSystem(win)


    def inputTableWindows(self, tablename):
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

            self.inputButton = tk.Button(self.inTable, text="Добавить",fg="black",width=18,font=('',15), command=partial(self.inputTableSQL, "typegsm"))
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

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=18, font=('', 15), command=partial(self.inputTableSQL, "vendorgsm"))
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

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15), command=partial(self.inputTableSQL, "companydrivers"))
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

            self.l10 = tk.Label(self.inTable, text=f"{buflist[9]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l10.pack(side=tk.TOP, fill=tk.X)
            self.l10e = ttk.Entry(self.inTable, width=15)
            self.l10e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
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

            # self.l10 = tk.Label(self.inTable, text=f"{buflist[9]}", bd=0, justify=CENTER, height=1, font=('', 18))
            # self.l10.pack(side=tk.TOP, fill=tk.X)
            # self.l10e = ttk.Entry(self.inTable, width=15)
            # self.l10e.pack(fill=tk.X)
            #
            # self.l11 = tk.Label(self.inTable, text=f"{buflist[10]}", bd=0, justify=CENTER, height=1, font=('', 18))
            # self.l11.pack(side=tk.TOP, fill=tk.X)
            # self.l11e = ttk.Entry(self.inTable, width=15)
            # self.l11e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
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

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=18, font=('', 15))
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
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
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

            self.l10 = tk.Label(self.inTable, text=f"{buflist[9]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l10.pack(side=tk.TOP, fill=tk.X)
            self.l10e = ttk.Entry(self.inTable, width=15)
            self.l10e.pack(fill=tk.X)

            self.l11 = tk.Label(self.inTable, text=f"{buflist[10]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l11.pack(side=tk.TOP, fill=tk.X)
            self.l11e = ttk.Entry(self.inTable, width=15)
            self.l11e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)
            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
            self.inputButton.place(x=15, y=735)
            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=205, y=735)

        if tablename == "prihfile":
            buflist = list_prihod
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в приход")
            inputTableWin.geometry('400x600')
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

            self.l10 = tk.Label(self.inTable, text=f"{buflist[9]}", bd=0, justify=CENTER, height=1, font=('', 18))
            self.l10.pack(side=tk.TOP, fill=tk.X)
            self.l10e = ttk.Entry(self.inTable, width=15)
            self.l10e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
            self.inputButton.place(x=10, y=550)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=210, y=550)

        if tablename == "rashfile":
            buflist = list_rashod
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в файл расхода")
            inputTableWin.geometry('400x500')
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

            self.l6 = tk.Label(self.inTable, text=f"{buflist[7]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)
            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
            self.inputButton.place(x=10, y=450)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=210, y=450)

        if tablename == "ksu":
            buflist = list_ksu
            inputTableWin = tk.Toplevel(self)
            inputTableWin.title("Добавление в КСУ")
            inputTableWin.geometry('400x650')
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

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)
            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}", bd=0, justify=CENTER, height=2, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)
            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.fram1 = tk.Frame(self.inTable, bg="#107eaf", width=300, height=600)
            self.fram1.pack(side=tk.BOTTOM, fill=tk.X)

            self.inputButton = tk.Button(self.inTable, text="Добавить", fg="black", width=15, font=('', 15))
            self.inputButton.place(x=10, y=600)

            self.closeB = tk.Button(self.inTable, text='Закрыть', fg="black", width=15, font=('', 15),
                                    command=inputTableWin.destroy)
            self.closeB.place(x=210, y=600)

    def inputTableSQL(self, tablename):
        if tablename == "typegsm":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "code_gsm", "name_gsm", "unit") VALUES 
            	                            ('{value1}','{value2}', '{value3}') """)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "vendorgsm":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
            	                            "code_post", "name_proizv", "addres_proizv", "code_gsm") VALUES 
            	                            ('{value1}','{value2}', '{value3}', '{value4}') """)
            except Exception as _ex:
                self.errorWindows()

        if tablename == "companydrivers":
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





if __name__ =="__main__":
    win = tk.Tk()
    start = loginSystem(win)
    start.pack()
    # start.destroy()
    # start=mainProgramm(win)
    # start.pack
    win.mainloop()
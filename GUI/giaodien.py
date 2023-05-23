from tkinter import *
from tkinter import simpledialog
import random
import os
from PIL import ImageTk, Image
import os
import tkinter.messagebox
from tkinter import ttk

gioithieu=[]
details = open("gt.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    gioithieu.append(line)

sanpham=[]
details = open("sp.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    sanpham.append(line)

ctkm=[]
details = open("ctkm.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    ctkm.append(line)

cuahang=[]
details = open("ch.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    cuahang.append(line)

tuyendung=[]
details = open("td.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    tuyendung.append(line)


nq=[]
details = open("nq.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    nq.append(line)

hoso=[]
details = open("hsns.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    hoso.append(line)

bangluong=[]
details = open("bl.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    bangluong.append(line)

A=[]
details = open("A.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    A.append(line)

B=[]
details = open("B.txt",encoding="utf8")
no_items  = int((details.readline()).rstrip("\n"))
for i in range(0,no_items):
    line = (details.readline().rstrip("\n"))
    B.append(line)


def phanloai(root):
        root['bg'] = 'White'
        root.title('THE SPACE COFFEE APP')
        root.geometry('830x750')

        title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                                 bd=10)
        title_Frame.grid(row=0, column=0, pady=50)

        title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                            fg='#453535')
        title_Label.grid(row=0, column=0, padx=150)

        # ========================================================FRAMES===================================================================
        Frame_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='#B29E84', relief='ridge',
                             bd=5)
        Frame_1.grid(row=2, column=0, padx=100, pady=5)
        Frame_2 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='#B29E84', relief='ridge',
                             bd=5)
        Frame_2.grid(row=3, column=0, padx=100, pady=5)


        # ========================================================LABELS===================================================================
        Labe = Label(text='BẠN LÀ ?', font=('arial', 25, 'bold'), fg='#453535',bg='white')
        Labe.grid(row=1, column=0, padx=50, pady=5)

        # ========================================================LABELS===================================================================
        Label_1 = Label(Frame_1, text='KHÁCH HÀNG', font=('arial', 25, 'bold'), bg='#B29E84', fg='#453535')
        Label_1.grid(row=2, column=0, padx=80, pady=5)
        Label_2 = Label(Frame_2, text='NHÂN VIÊN', font=('arial', 25, 'bold'), bg='#B29E84', fg='#453535')
        Label_2.grid(row=3, column=0, padx=100, pady=5)


        # ========================================================BUTTONS===================================================================
        Button_1 = Button(Frame_1, text='CHỌN', font=('arial', 16, 'bold'), width=8, fg='#453535', command=khachhang)
        Button_1.grid(row=2, column=3, padx=50)
        Button_2 = Button(Frame_2, text='CHỌN', font=('arial', 16, 'bold'), width=8, fg='#453535', command=dangnhap)
        Button_2.grid(row=3, column=3, padx=50)

        logo_import = (Image.open(r'logo.png'))
        resize = logo_import.resize((450, 367), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(resize)
        logos = Label(text='', bg='White', image=logo)
        logos.place(x=190, y=370)
        root.mainloop()


def khachhang():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('830x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    # ========================================================FRAMES===================================================================
    Frame_1 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10, bg='#B29E84', relief='ridge',
                         bd=5)
    Frame_1.grid(row=2, column=0, padx=75, pady=5)
    Frame_2 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10, bg='#B29E84', relief='ridge',
                         bd=5)
    Frame_2.grid(row=3, column=0, padx=75, pady=5)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10, bg='white',
                         bd=0)
    Frame_3.grid(row=5, column=0, padx=75, pady=5)
    # ========================================================LABELS===================================================================
    Button_1 = Button(Frame_1, text='Giới thiệu', font=('arial', 16, 'bold'), width=12, fg='#453535', command=Gioithieu)
    Button_1.grid(row=2, column=0)
    Button_2 = Button(Frame_1, text='Sản phẩm', font=('arial', 16, 'bold'), width=12, fg='#453535', command=Sanpham)
    Button_2.grid(row=2, column=1)
    Button_3 = Button(Frame_1, text='Chương trình khuyến mãi', font=('arial', 16, 'bold'), width=25, fg='#453535',
                      command=CTKM)
    Button_3.grid(row=2, column=2)
    Button_4 = Button(Frame_2, text='Chuỗi cửa hàng', font=('arial', 16, 'bold'), width=19, fg='#453535',
                      command=Cuahang)
    Button_4.grid(row=3, column=0)
    Button_5 = Button(Frame_2, text='Tuyển dụng', font=('arial', 16, 'bold'), width=12, fg='#453535', command=Tuyendung)
    Button_5.grid(row=3, column=1)
    Button_6 = Button(Frame_2, text='Nhượng quyền', font=('arial', 16, 'bold'), width=18, fg='#453535', command=NQ)
    Button_6.grid(row=3, column=2)

    win.mainloop()



def dangnhap():
    root = Tk()
    app = Window_1(root)
    root.mainloop()


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("THE SPACE COFFEE")
        self.master.geometry('850x750')
        self.Frame = Frame(self.master)
        self.Frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text='Đăng Nhập', font=('arial', 55, 'bold'), fg='#453535')
        self.Lbl_Title.grid(row=0, column=0, columnspan=4, pady=20)

        self.Login_Frame_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bd=5, bg='#B29E84',
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width=10, height=20, relief='ridge', bd=0,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=3, column=0)
        self.Login_Frame_3 = LabelFrame(self.Frame, width=30, height=30, bd=0)
        self.Login_Frame_3.grid(row=2, column=0)

        # ===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text='Tên đăng nhập', font=('arial', 20, 'bold'), bg='#B29E84',
                                    bd=10, fg='#453535')
        self.Label_Username.grid(row=1, column=0, padx=50)
        self.text_Username = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_Username.grid(row=1, column=1, padx=50)

        self.Label_Password = Label(self.Login_Frame_1, text='Mật khẩu', font=('arial', 20, 'bold'), bg='#B29E84',
                                    fg='#453535', bd=10)
        self.Label_Password.grid(row=2, column=0)
        self.text_Password = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.text_Password.grid(row=2, column=1)

        # =============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text='Đăng nhập', width=10, font=('airia', 15, 'bold'), fg='#453535',
                               command=self.Login)
        self.btnLogin.grid(row=5, column=0)

        self.btnReset = Button(self.Login_Frame_2, text='Xóa', width=10, font=('airia', 15, 'bold'), fg='#453535',
                               command=self.Reset)
        self.btnReset.grid(row=5, column=1)

        self.btnExit = Button(self.Login_Frame_2, text='Thoát', width=10, font=('airia', 15, 'bold'), fg='#453535',
                              command=self.Exit)
        self.btnExit.grid(row=5, column=2)

    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())
        print(u, '', p)
        if (u == str('') and p == str('')):
            self.new_window()
        else:
            tkinter.messagebox.askyesno("Đăng nhập", "Lỗi : Sai mật khẩu")
            self.Username.set("")
            self.Password.set("")

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.text_Username.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Đăng nhập hệ thống", "Bạn có chắc là muốn thoát")
        if self.Exit > 0:
            self.master.destroy()
            return

    def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)


class Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("THE SPACE COFFEE APP")
        self.master.geometry('850x750')
        self.master.config(bg="white")
        self.Frame = Frame(self.master, bg="white")
        self.Frame.pack()

        self.Lbl_Title = Label(self.Frame, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84',
                                 relief='raise',
                                 bd=10)
        self.Lbl_Title.grid(row=0, column=0, pady=50)

        self.title_Label = Label(self.Lbl_Title, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                            fg='#453535')
        self.title_Label.grid(row=0, column=0, padx=150)

        # ========================================================FRAMES===================================================================
        self.Frame_1 = LabelFrame(self.Frame, font=('arial', 17, 'bold'), width=10, height=10, bg='#B29E84', relief='ridge',
                             bd=5)
        self.Frame_1.grid(row=2, column=0, padx=25, pady=5)
        self.Frame_2 = LabelFrame(self.Frame, font=('arial', 17, 'bold'), width=10, height=10, bg='#B29E84', relief='ridge',
                             bd=5)
        self.Frame_2.grid(row=3, column=0, padx=25, pady=5)

        # ========================================================LABELS===================================================================
        self.Button_1 = Button(self.Frame_1, text='Hồ sơ nhân sự', font=('arial', 25, 'bold'), width=30, fg='#453535',
                          command=self.Hoso)
        self.Button_1.grid(row=2, column=0)
        self.Button_2 = Button(self.Frame_2, text='Bảng lương', font=('arial', 25, 'bold'), width=30, fg='#453535',
                          command=self.Bangluong)
        self.Button_2.grid(row=3, column=0)

    def Hoso(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_3(self.new_Window)

    def Bangluong(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_4(self.new_Window)

class Window_3:
    def __init__(self, master):
        self.master = master
        self.master.title("THE SPACE COFFEE APP")
        self.master.geometry('850x750')
        self.master.config(bg="white")
        self.Frame = Frame(self.master, bg="white")
        self.Frame.pack()

        self.Lbl_Title = Label(self.Frame, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84',
                                 relief='raise',
                                 bd=10)
        self.Lbl_Title.grid(row=0, column=0, pady=50)

        self.title_Label = Label(self.Lbl_Title, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                            fg='#453535')
        self.title_Label.grid(row=0, column=0, padx=150)

        # ========================================================FRAMES===================================================================
        self.Frame_1 = LabelFrame(self.Frame, font=('arial', 17, 'bold'), width=10, height=10,
                             bd=0)
        self.Frame_1.grid(row=2, column=0, padx=25, pady=5)
        for i in range(0, no_items):
            self.Label_1 = Label(self.Frame_1, text=hoso[i], font=('arial', 25, 'bold'), fg='#453535')
            self.Label_1.grid(row=2 + i, column=0, padx=100, pady=5)

class Window_4:
    def __init__(self, master):
        self.master = master
        self.master.title("THE SPACE COFFEE APP")
        self.master.geometry('850x750')
        self.master.config(bg="white")
        self.Frame = Frame(self.master, bg="white")
        self.Frame.pack()

        self.Lbl_Title = Label(self.Frame, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84',
                                 relief='raise',
                                 bd=10)
        self.Lbl_Title.grid(row=0, column=0, pady=50)

        self.title_Label = Label(self.Lbl_Title, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                            fg='#453535')
        self.title_Label.grid(row=0, column=0, padx=150)

        # ========================================================FRAMES===================================================================
        self.Frame_1 = LabelFrame(self.Frame, font=('arial', 17, 'bold'), width=10, height=10,
                             bd=0)
        self.Frame_1.grid(row=2, column=0, padx=25, pady=5)
        for i in range(0, no_items):
            self.Label_1 = Label(self.Frame_1, text=bangluong[i], font=('arial', 25, 'bold'), fg='#453535')
            self.Label_1.grid(row=2 + i, column=0, padx=100, pady=5)

def Gioithieu():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('1350x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=800, height=700, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('Times New Roman', 17, 'bold'), width=800, height=700,
                         bd=2)
    Frame_3.grid(row=2, column=0,  padx=100, pady=5)
    for i in range(0,no_items):
        Label_1 = Label(Frame_3, text=gioithieu[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2+i, column=0, padx=100, pady=5)
def Sanpham():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('830x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10,
                         bd=2)
    Frame_3.grid(row=5, column=0, padx=155, pady=5)
    for i in range(0, no_items):
        Label_1 = Label(Frame_3, text=sanpham[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2 + i, column=0, padx=155, pady=5)
def CTKM():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('830x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10,
                         bd=2)
    Frame_3.grid(row=5, column=0, padx=30, pady=5)
    for i in range(0, no_items):
        Label_1 = Label(Frame_3, text=ctkm[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2 + i, column=0, padx=30, pady=5)
def Cuahang():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('830x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10,
                         bd=2)
    Frame_3.grid(row=5, column=0, padx=45, pady=5)
    for i in range(0, no_items):
        Label_1 = Label(Frame_3, text=cuahang[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2 + i, column=0, padx=45, pady=5)
def Tuyendung():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('830x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10,
                         bd=2)
    Frame_3.grid(row=5, column=0, padx=31, pady=5)
    for i in range(0, no_items):
        Label_1 = Label(Frame_3, text=tuyendung[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2 + i, column=0, padx=31, pady=5)
def NQ():
    win = Tk()
    win['bg'] = 'White'
    win.title('THE SPACE COFFEE / Cung cấp thông tin khách hàng')
    win.geometry('1190x750')

    title_Frame = LabelFrame(win, font=('arial', 50, 'bold'), width=1000, height=100, bg='#B29E84', relief='raise',
                             bd=10)
    title_Frame.grid(row=0, column=0, pady=50)

    title_Label = Label(title_Frame, text='THE SPACE COFFEE', font=('arial', 30, 'bold'), bg='#B29E84',
                        fg='#453535')
    title_Label.grid(row=0, column=0, padx=150)

    Frame_3 = LabelFrame(win, font=('arial', 17, 'bold'), width=10, height=10,
                         bd=2)
    Frame_3.grid(row=5, column=0, padx=75, pady=5)
    for i in range(0,no_items):
        Label_1 = Label(Frame_3, text=nq[i], font=('arial', 25, 'bold'), fg='#453535')
        Label_1.grid(row=2+i, column=0, padx=100, pady=5)

root = Tk()
obj = phanloai(root)
root.mainloop()



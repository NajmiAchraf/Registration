from tkinter import messagebox
from tkinter import *
from DB import File
from Quick import List

btn_prm = {'padx': 16,
           'pady': 2,
           'bd': 1,
           'fg': '#000000',
           'width': 3,
           'height': 1,
           'relief': 'raised'}


class Registration:
    __author__ = 'Achraf Najmi'
    __version__ = '1.0.0.1 GM'
    __name__ = 'Registration'

    def __init__(self):
        self.root = Tk()
        self.root.title(f'{self.__name__} v{self.__version__}')
        self.root.resizable(False, False)

        self.File = File()
        self.FM = []
        for f in range(4):
            self.FM.append(Frame(self.root, relief=RIDGE))
            self.FM[f].grid(row=f, padx=20, pady=20)
            self.FM[f].rowconfigure(f, weight=1)
            self.FM[f].columnconfigure(f, weight=1)

        LB_TX = ['First Name :', 'Last Name :', 'Middle Name :', 'Address :', 'E.Mail :', 'Phone :']
        self.LB = []
        for l in range(6):
            self.LB.append(Label(self.FM[0], text=LB_TX[l]))
            self.LB[l].grid(row=l, column=0, sticky='snew', padx=5, pady=5)

        self.EN = []
        for e in range(6):
            self.EN.append(Entry(self.FM[0], width=30))
            self.EN[e].grid(row=e, column=1)
        self.c = self.EN[2].get()

        self.CBV = StringVar()
        cb2 = Checkbutton(self.FM[0], text='Disable')
        cb2.grid(row=2, column=2, sticky='snew', padx=5, pady=5)
        cb2.config(variable=self.CBV, command=lambda: self.cb())
        self.CBV.get()
        self.k1 = self.CBV.get()

        LLA_TX = ['Gender :', 'Month :']
        LLA = []
        for l in range(2):
            LLA.append(Label(self.FM[1], text=LLA_TX[l]))
            LLA[l].grid(row=l, column=0, sticky='snew', padx=5, pady=5)

        self.RBV = StringVar()
        RBF_TX = ['Mr.', 'Mme.', 'Mlle.']
        RBF = []
        for r in range(3):
            RBF.append(Radiobutton(self.FM[1], variable=self.RBV, value=RBF_TX[r], text=RBF_TX[r]))
            RBF[r].grid(row=0, column=int(r) + 1, sticky='snew', padx=5, pady=5)
        self.RBV.get()
        self.k2 = self.RBV.get()

        self.RBV1 = StringVar()
        RBF_TX = ['One Month', 'Three Month', 'Six Months']
        RBF = []
        for a in range(3):
            RBF.append(Radiobutton(self.FM[1], variable=self.RBV1, value=RBF_TX[a], text=RBF_TX[a]))
            RBF[a].grid(row=1, column=int(a) + 1, sticky='snew', padx=5, pady=5)
        self.RBV1.get()
        self.k3 = self.RBV1.get()

        # f2
        LBL = Label(self.FM[2], text='Comment :')
        LBL.grid(row=0, column=0, sticky='snew', padx=5, pady=5)
        self.CMT = Text(self.FM[2], width=20, height=5, font=('Arial', 16))
        self.CMT.grid(row=0, column=1, sticky='snew', padx=5, pady=5)

        BTN_TX = ['List', 'Submit', 'Cancel']
        self.BTN = []
        for b in range(3):
            self.BTN.append(Button(self.FM[3], text=BTN_TX[b], **btn_prm))
            self.BTN[b].grid(row=0, column=b, sticky=NSEW, padx=5, pady=5)

        self.BTN[0].config(command=lambda: List())
        self.BTN[1].config(command=lambda: self.GET())
        self.BTN[2].config(command=lambda: self.CAN())
        self.CAN()

        self.root.rowconfigure(0, weight=1, minsize=1)
        self.root.rowconfigure(1, weight=1, minsize=1)
        self.root.rowconfigure(2, weight=1, minsize=1)
        self.root.rowconfigure(3, weight=1, minsize=1)
        self.root.columnconfigure(0, weight=1, minsize=1)
        self.root.mainloop()

    def cb(self):
        self.k1 = self.CBV.get()
        if self.k1 == '1':
            self.EN[2].delete(0, END)
            self.EN[2].config(state=DISABLED)
            self.c = 'N/D'
        else:
            self.EN[2].config(state=NORMAL)
            self.c = self.EN[2].get().upper()

    def GET(self):
        file = open('../inscription.txt', 'a')
        file.write('\n------------------------------------------')

        a = self.EN[0].get().upper()
        file.write('\nFirst Name : {}'.format(a))
        print('First Name : {}'.format(a))

        b = self.EN[1].get().upper()
        file.write('\nLast Name : {}'.format(b))
        print('Last Name : {}'.format(b))

        self.cb()
        file.write('\nMiddle Name : {}'.format(self.c))
        print('Middle Name : {}'.format(self.c))

        d = self.EN[3].get().upper()
        file.write('\nAddress : {}'.format(d))
        print('Address : {}'.format(d))

        e = self.EN[4].get().lower()
        file.write('\nE.Mail : {}'.format(e))
        print('E.Mail : {}'.format(e))

        f = self.EN[5].get()
        file.write('\nPhone : {}'.format(f))
        print('Phone : {}'.format(f))

        self.k2 = self.RBV.get()
        self.k3 = self.RBV1.get()

        self.CMT.insert(1.0, '{}{} {} payed for {}, '.format(self.k2, a, b, self.k3))
        t = self.CMT.get(1.0, END)
        file.write('\nComment : {}'.format(t))
        print('Comment : {}'.format(t))

        file.write('\n')
        file.write('\n{}{} {} payed for {}.'.format(self.k2, a, b, self.k3))
        print('{}{} {} payed for {}.'.format(self.k2, a, b, self.k3))

        file.close()

        add = self.File.Add(a, b, self.c, d, e, f, self.k2, self.k3, t)
        messagebox.showinfo(title='Add Info', message=add)

        self.CAN()

    def CAN(self):
        self.EN[0].delete(0, END)
        self.EN[1].delete(0, END)
        self.EN[2].delete(0, END)
        self.EN[3].delete(0, END)
        self.EN[4].delete(0, END)
        self.EN[5].delete(0, END)
        self.RBV.set(0)
        self.RBV1.set(0)
        self.CBV.set(0)
        self.EN[2].config(state=NORMAL)
        self.CMT.delete(1.0, 'end')


if __name__ == '__main__':
    Registration()

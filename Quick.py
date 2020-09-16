from tkinter import *
from tkinter import ttk
from DB import *

btn_prm = {'padx': 16,
           'pady': 3,
           'bd': 1,
           'fg': '#000000',
           'width': 6,
           'height': 1,
           'relief': 'raised'}


class List(ttk.Treeview):
    def __init__(self):
        self.file = File()

        self.win = Tk()
        self.win.geometry("1000x500")
        self.win.minsize(width=300, height=300)
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        self.win.rowconfigure(0, weight=1)

        self.root = Canvas(self.win)
        self.root.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.hbar = Scrollbar(self.root, orient=HORIZONTAL)
        self.vbar = Scrollbar(self.root, orient=VERTICAL)

        ttk.Treeview.__init__(self, self.root)
        self.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.grid(row=0, column=0, sticky=NSEW)

        self.heading('#0', text='ID')
        self.configure(
            column=('#First', '#Last', '#Middle', '#Address', '#EMail', '#Phone', '#Gender', '#Month', '#Comment'))
        self.heading('#First', text='First Name')
        self.heading('#Last', text='Last Name')
        self.heading('#Middle', text='Middle Name')
        self.heading('#Address', text='Address')
        self.heading('#EMail', text='E.Mail')
        self.heading('#Phone', text='Phone')
        self.heading('#Gender', text='Gender')
        self.heading('#Month', text='Month')
        self.heading('#Comment', text='Comment')

        show = self.file.FastList()
        for row in show:
            self.insert('', END, '#{}'.format(row['ID']), text=row['ID'])
            self.set('#{}'.format(row['ID']), '#First', row['First'])
            self.set('#{}'.format(row['ID']), '#Last', row['Last'])
            self.set('#{}'.format(row['ID']), '#Middle', row['Middle'])
            self.set('#{}'.format(row['ID']), '#Address', row['Address'])
            self.set('#{}'.format(row['ID']), '#EMail', row['EMail'])
            self.set('#{}'.format(row['ID']), '#Phone', row['Phone'])
            self.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            self.set('#{}'.format(row['ID']), '#Month', row['Month'])
            self.set('#{}'.format(row['ID']), '#Comment', row['Comment'])

        self.vbar.grid(row=0, column=1, sticky=NS)
        self.vbar.configure(command=self.yview)
        self.hbar.grid(row=1, column=0, sticky=EW)
        self.hbar.configure(command=self.xview)

        BTN_TXT = ['Modify', 'Modify & Exit']
        BTN_FUN = [self.Open, self.Exit]
        self.BTN = []
        for b in range(2):
            self.BTN.append(Button(self.win, text=BTN_TXT[b], **btn_prm))
            self.BTN[b].grid(row=1, column=b, pady=7)
            self.BTN[b].configure(command=BTN_FUN[b])

        self.win.mainloop()

    def Open(self):
        open('Registration.db3')

    def Exit(self):
        self.win.destroy()
        exe = Cache("Registration.db3")
        return exe.display()


if __name__ == '__main__':
    List()

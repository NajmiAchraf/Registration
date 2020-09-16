from sqlite3 import *


class File:
    def __init__(self):
        self.db_file = connect("Registration.db3")
        self.db_file.row_factory = Row
        self.db_file.execute(
            "create table if not exists Ticket(ID integer primary key autoincrement, First text, Last text, Middle text"
            ", Address text, EMail text, Phone text, Gender text, Month text, Comment text)")
        self.db_file.commit()

    def Add(self, First, Last, Middle, Address, EMail, Phone, Gender, Month, Comment):
        self.db_file.execute(
            "insert into Ticket(First,Last,Middle,Address,EMail,Phone,Gender,Month,Comment) values(?,?,?,?,?,?,?,?,?)",
            (First, Last, Middle, Address, EMail, Phone, Gender, Month, Comment))
        self.db_file.commit()
        return "Registration is submitted"

    def FastList(self):
        show = self.db_file.execute('select * from Ticket')
        return show

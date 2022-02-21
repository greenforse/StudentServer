
from Edit_context import Edit_context
from Singleton import Singleton




class RepositoryStudent(metaclass=Singleton):
    
    def __init__(self):
        import main as m
        self.cur = m.conn.cursor()
        self.conn = m.conn
        
    def createList(self):
        self.cur.execute("SELECT* FROM student")
        list = self.cur.fetchall()
        for i in list:
            print(i)

    #def printList(self):
    #    #self.createList()
    #    for i in self.listStud:
    #        print(i)

    #def connect(self):
    #    self.cur = m.conn.cursor()
        
    def delete(self):
        self.createList()
        id = int(input("Введите ид студента для удаления: "))
        sql = ("DELETE FROM student WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()

    def editMName(self):
        newMName = input("Введите новое отчество: ")
        id = Edit_context().save[0][0]
        sql = ("UPDATE student SET m_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newMName, id])
        self.conn.commit()
        self.refreshBeforeEdit()

    def editLName(self):
        newLName = input("Введите новую фамилию: ")
        id = Edit_context().save[0][0]
        sql = ("UPDATE student SET s_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newLName, id])
        self.conn.commit()
        self.refreshBeforeEdit()

    def SelectCommand(self):
        self.createList()
        select = False
        while select == False:
            selectNumber = int(input("Введите номер пользователя"))
            try:
                sql = ("Select* FROM student WHERE id = %s ;")
                self.cur.execute(sql, [selectNumber])
                data = self.cur.fetchall()
                Edit_context().save = data
                select = True
            except:
                print("Такого пользователя нет")

    def ShowCommand(self):
        print(Edit_context().save)

    def DeselectCommand(self):
        Edit_context().save = None

    def editFName(self):
        newFName = input("Введите Новое Имя")
        id = Edit_context().save[0][0]
        sql = ("UPDATE student SET f_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newFName, id])
        self.conn.commit()
        self.refreshBeforeEdit()

    def refreshBeforeEdit(self):
        sql = ("SELECT* FROM student WHERE id =%s")
        self.cur.execute(sql, [Edit_context().save[0][0]])
        Edit_context().save = self.cur.fetchall()

    def add(self):
        id = int(input("id: "))
        firstName = str(input("Введите Name: "))
        secondName = input("Введите фамилию: ")
        lastName = input("Введите отчество: ")
        groupId = input("Введите группу студента: ")
        sql = ("INSERT INTO student (id,f_name, s_name, m_name,group_id) VALUES (%s, %s, %s, %s,%s);")
        self.cur.execute(sql, [id, firstName, secondName, lastName,groupId])
        self.conn.commit()

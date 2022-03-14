
from Edit_context import Edit_context
from Singleton import Singleton




class RepositoryStudent(metaclass=Singleton):
    
    def __init__(self):
        import main as m
        self.cur = m.conn.cursor()
        self.conn = m.conn
        
    def createList(self):
        self.cur.execute("SELECT* FROM student") 
        return self.cur.fetchall()

    #def printList(self):
    #    #self.createList()
    #    for i in self.listStud:
    #        print(i)

    #def connect(self):
    #    self.cur = m.conn.cursor()
        
    def delete(self, id):
        sql = ("DELETE FROM student WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()

    def editMName(self, newMName, id):
        sql = ("UPDATE student SET m_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newMName, id])
        self.conn.commit()
        #self.refreshBeforeEdit()

    def editLName(self, newLName, id):
        sql = ("UPDATE student SET s_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newLName, id])
        self.conn.commit()

    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM student WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        otvet = self.cur.fetchall()
        return otvet

    #def ShowCommand(self):
    #    print(Edit_context().save)

    #def DeselectCommand(self):
    #    Edit_context().save = None

    def editFName(self, newFName, id):
        sql = ("UPDATE student SET f_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newFName, id])
        self.conn.commit()

    def refreshBeforeEdit(self, id):
        sql = ("SELECT* FROM student WHERE id =%s")
        self.cur.execute(sql, id)
        return self.cur.fetchall()


    def add(self, id, firstName, secondName, lastName, groupId):
        sql = ("INSERT INTO student (id,f_name, s_name, m_name,group_id) VALUES (%s, %s, %s, %s,%s);")
        self.cur.execute(sql, [id, firstName, secondName, lastName,groupId])
        self.conn.commit()

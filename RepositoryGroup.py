from Edit_context import Edit_Context
from Singleton import Singleton


class RepositoryGroup(metaclass=Singleton):
    def __init__(self):
        import main as m
        self.conn = m.conn
        self.cur = self.conn.cursor()

    def createList(self):
        self.cur.execute("SELECT* FROM groups")
        list = self.cur.fetchall()
        for i in list:
            print(i)
            
    def editId(self):
        sql = ("UPDATE groups SET id = %s WHERE id=%s;")
        newId = input("Введите новое ID: ")
        self.cur.execute(sql, [newId, Edit_Context().save[0][0]])
        self.conn.commit()

    def SelectCommand(self):
        self.createList()
        select = False
        while select == False:
            selectNumber = int(input("Введите название группы"))
            try:
                sql = ("Select* FROM groups WHERE id = %s ;")
                self.cur.execute(sql, [selectNumber])
                data = self.cur.fetchall()
                Edit_context().save = data
                select = True
            except:
                print("Такой группы нет")

    def viewStudent(self):
        sql = ("SELECT* FROM student WHERE id=%s")
        self.cur.execute(sql, [Edit_Context().save[0][0]])
        list = self.cur.fetchall()
        for i in list:
            print(i)

    def delete(self):
        self.createList()
        id = int(input("Введите ид группы для удаления: "))
        sql = ("DELETE FROM grops WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()

    def add(self):
        id = input("id: ")
        course = input("Введите курс: ")
        specialization = input("Введите специализацию: ")
        sql = ("INSERT INTO student (id, course, specialization_id ) VALUES (%s, %s, %s, %s);")
        self.cur.execute(sql, [id, course, specialization, null])
        self.conn.commit()
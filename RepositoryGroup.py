
class RepositoryGroup:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()


    def createList(self):
        self.cur.execute("SELECT* FROM groups")
        return self.cur.fetchall()

    def editCourse(self,nextCourse,id):
        sql = ("UPDATE groups SET course = %s WHERE id=%s;")
        self.cur.execute(sql, [nextCourse, id])
        self.conn.commit()

    def editId(self,newId,id):
        sql = ("UPDATE groups SET id = %s WHERE id=%s;")
        self.cur.execute(sql, [newId, id])
        self.conn.commit()


    def editHeadOf(self, group, studentId):
        sql=("UPDATE groups SET head_of = %s WHERE id=%s")
        self.cur.execute(sql, [studentId, group])
        self.conn.commit()



    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM groups WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        return self.cur.fetchall()

    def viewStudent(self):
        sql = ("SELECT* FROM student WHERE id=%s")
        self.cur.execute(sql, [Edit_Context().save[0][0]])
        list = self.cur.fetchall()
        for i in list:
            print(i)

    def delete(self,id):
        sql = ("DELETE FROM groups WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()

    def add(self, id, spec, course):
        sql = ("INSERT INTO groups (id, course, specialization_id ) VALUES (%s, %s, %s);")
        self.cur.execute(sql, [id, course, spec])
        self.conn.commit()

    def refreshBeforeEdit(self, id):
        sql = ("SELECT* FROM groups WHERE id =%s")
        self.cur.execute(sql, id)
        return self.cur.fetchall()

    def addToSpec(self,specId,id):
        sql = ("UPDATE groups SET specialization_id = %s WHERE id=%s;")
        self.cur.execute(sql, [specId, id])
        self.conn.commit()

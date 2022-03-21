class TeacherRepository:
    def __init__(self, conn):
        self.cur = conn.cursor()
        self.conn = conn

    def createList(self):
        sql = ("SELECT* FROM teacher")
        self.cur.execute(sql)
        return self.cur.fetchall()

    def delete(self, id):
        sql = ("DELETE FROM teacher WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()

    def editMName(self, newMName, id):
        sql = ("UPDATE teacher SET m_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newMName, id])
        self.conn.commit()
        # self.refreshBeforeEdit()

    def editLName(self, newLName, id):
        sql = ("UPDATE teacher SET s_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newLName, id])
        self.conn.commit()

    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM teacher WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        return self.cur.fetchall()

    def editFName(self, newFName, id):
        sql = ("UPDATE teacher SET f_name = %s WHERE id=%s;")
        self.cur.execute(sql, [newFName, id])
        self.conn.commit()

    def refreshBeforeEdit(self, id):
        sql = ("SELECT* FROM teacher WHERE id =%s")
        self.cur.execute(sql, id)
        return self.cur.fetchall()

    def add(self, id, firstName, secondName, lastName, kafedra_id, academic_degree, ):
        sql = (
            "INSERT INTO teacher (id,f_name, s_name, m_name,kafedra_id,academic_degree) VALUES (%s, %s, %s, %s,%s,%s);")
        self.cur.execute(sql, [id, firstName, secondName, lastName, kafedra_id, academic_degree])
        self.conn.commit()

    def editKafedra(self, id, kafedra):
        sql = ("UPDATE teacher SET kafedra_id = %s WHERE id=%s;")
        self.cur.execute(sql, [kafedra, id])
        self.conn.commit()

    def editAcademicDegree(self, id, academicDegree):
        sql = ("UPDATE teacher SET kafedra_id = %s WHERE id=%s;")
        self.cur.execute(sql, [academicDegree, id])
        self.conn.commit()

class MarkRepository:

    def __init__(self, conn):
        self.cur = conn.cursor()
        self.conn = conn

    def createListFromStudentMark (self,studentId):
        sql = ("SELECT p.name, m.value FROM marks m INNER JOIN predmet p ON p.id = m.predmet_id WHERE m.student_id = %s and m.value IS NOT NULL")
        self.cur.execute(sql, [studentId])
        return self.cur.fetchall()

    def createListFromPredmetMark (self,predmetId):
        sql = ("Select s.f_name, s.s_name, m.value FROM marks m INNER JOIN student s ON s.id = m.student_id	INNER JOIN predmet p ON p.id = m.predmet_id WHERE p.id = 1")
        self.cur.execute(sql, [predmetId])
        return self.cur.fetchall()

    def createListFromStudentZachet(self,studentId):
        sql = ("SELECT p.name, m.zachet FROM marks m INNER JOIN predmet p ON p.id = m.predmet_id WHERE m.student_id = %s and m.value IS NULL")
        self.cur.execute(sql, [studentId])
        return self.cur.fetchall()

    def editPredmetMarks(self, marksId, value):
        sql("UPDATE marks SET value = %s WHERE id = %s")
        self.cur.execute(sql, [value, marksId])

    def delete(self, id):
        sql = ("DELETE FROM mark WHERE id = %s")
        self.cur.execute(sql, [id])
        self.conn.commit()
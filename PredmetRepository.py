class PredmetRepository:

    def __init__(self, conn):
        self.cur = conn.cursor()
        self.conn = conn

    def createList(self):
        self.cur.execute("SELECT* FROM predmet")
        return self.cur.fetchall()

    def createListByGroup(self, group):
        sql = ("SELECT* FROM predmet WHERE group_id= %s")
        self.cur.execute(sql, [group])
        return self.cur.fetchall()

    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM predmet WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        return self.cur.fetchall()

    def refreshBeforeEdit(self, id):
        sql = ("SELECT* FROM predmet WHERE id =%s")
        self.cur.execute(sql, id)
        return self.cur.fetchall()

    def add(self, id, name, zachet):
        sql = ("INSERT INTO predmet (id,name,zachet,specialization_id) VALUES (%s, %s,%s,null);")
        self.cur.execute(sql, [id, name, zachet])
        self.conn.commit()

    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM predmet WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        return self.cur.fetchall()

    def addPredmetInSpecializacion(self, predmetId, specialization, course):
        sql = ("INSERT INTO predmet_specialization (predmet_id,specialization_id,course) VALUES(%s,%s,%s);")
        self.cur.execute(sql, [predmetId, specialization, course])
        self.conn.commit()

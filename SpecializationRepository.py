class SpecializationRepository:

    def __init__(self, conn):
        self.cur = conn.cursor()
        self.conn = conn

    def viewList(self):
        self.cur.execute("SELECT* FROM specialization")
        return self.cur.fetchall()

    def SelectCommand(self, selectNumber):
        sql = ("Select* FROM specialization WHERE id=%s ;")
        self.cur.execute(sql, [selectNumber])
        return self.cur.fetchall()

import psycopg2
from StudentController import StudentController
from GroupController import GroupController
from TeacherController import TeacherController
from RepositoryStudent import RepositoryStudent
from RepositoryGroup import RepositoryGroup
from TeacherRepository import TeacherRepository
from Menu import Menu

class Controller:

    def __init__(self):
        self.connect()
        self.buildController()
        self.buildMainMenu()


    def buildController(self):
        self.studController = StudentController(RepositoryStudent(self.conn), "student", "students")
        self.groupController = GroupController(RepositoryGroup(self.conn), self.studController)
        self.teachController = TeacherController(TeacherRepository(self.conn))

    def buildMainMenu(self):
        self.mainMenu = Menu("Главное меню", 0)
        self.mainMenu.addControllerSubMenu(self.studController.createMenu())
        self.mainMenu.addControllerSubMenu(self.groupController.createMenu())
        self.mainMenu.addControllerSubMenu(self.teachController.createMenu())


    def connect(self):
        self.conn = psycopg2.connect(
            host="192.168.56.101",
            port=5432,
            database="Students",
            user='student',
            password='student')


    def menuExecute(self):
        self.mainMenu.execute()
        self.conn.close()

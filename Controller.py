import psycopg2
from StudentController import StudentController
from GroupController import GroupController
from TeacherController import TeacherController
from MarkController import MarkController
from PredmetController import PredmetController
from SpecializacionController import SpecializationController

from RepositoryStudent import RepositoryStudent
from RepositoryGroup import RepositoryGroup
from TeacherRepository import TeacherRepository
from MarkRepository import MarkRepository
from PredmetRepository import PredmetRepository
from SpecializationRepository import SpecializationRepository
from Menu import Menu


class Controller:

    def __init__(self):
        self.connect()
        self.buildController()
        self.buildMainMenu()


    def buildController(self):
        self.specializationController = SpecializationController(SpecializationRepository(self.conn))
        self.studController = StudentController(RepositoryStudent(self.conn), "student", "students")
        self.groupController = GroupController(RepositoryGroup(self.conn), self.studController)
        self.teachController = TeacherController(TeacherRepository(self.conn))
        self.predmetController = PredmetController(PredmetRepository(self.conn), self.specializationController)
        self.markController = MarkController(MarkRepository(self.conn), self.studController, self.predmetController)


    def buildMainMenu(self):
        self.mainMenu = Menu("Главное меню", 0)
        self.mainMenu.addControllerSubMenu(self.studController.createMenu())
        self.mainMenu.addControllerSubMenu(self.groupController.createMenu())
        self.mainMenu.addControllerSubMenu(self.teachController.createMenu())
        self.mainMenu.addControllerSubMenu(self.markController.createMenu())
        self.mainMenu.addControllerSubMenu(self.predmetController.createMenu())


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

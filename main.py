import psycopg2
from Menu import Menu
from StudentController import StudentController
import RepositoryStudent as rs
conn = psycopg2.connect(
    host="192.168.56.101",
    port=5432,
    database="Students",
    user='student',
    password='student')

controllerStudent = StudentController(rs.RepositoryStudent, "student", "students")

glavnoeMenu = Menu("Главное меню", 0)
#studentMenu = controllerStudent.createMenu()
glavnoeMenu.addControllerSubMenu(controllerStudent.createMenu())
#glavnoeMenu.additem(1, "Список студентов", StudentController.printList)
#AddStud = glavnoeMenu.additem(2, "Добавить студента", RepositoryStudent().add)
#glavnoeMenu.additem(3, "Удалить пользователя", RepositoryStudent().delete)
#####
#editStudents = glavnoeMenu.addSubMenu("Редактировать пользователя", 4)
#editStudents.set_startup_command(RepositoryStudent().SelectCommand)
#editStudents.set_before_select_command(RepositoryStudent().ShowCommand)
#editStudents.set_tear_down_command(RepositoryStudent().DeselectCommand)
#editStudents.additem(1, "Изменить имя", RepositoryStudent().editFName)
#editStudents.additem(2, "Изменить фамилию", RepositoryStudent().editLName)
#editStudents.additem(2, "Изменить Отчество", RepositoryStudent().editMName)
glavnoeMenu.execute()

conn.close()

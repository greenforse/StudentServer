from Edit_context import Edit_context
from Menu import Menu
from MenuService import MenuService
import Views

class MarkController:
    def __init__(self, repository, controllerStudent,controllerPredmet):
        self.repository = repository
        self.menuService = MenuService()
        self.controllerStudent = controllerStudent
        self.controllerPredmet = controllerPredmet

    def viewAllMarkStudent(self):
        #self.controllerStudent.SelectCommand()
        print(self.repository.createListFromStudentMark(Edit_context().save[0][0]))

    def viewAllMarksPredmet(self):
        print(self.repository.createListFromPredmetMark(Edit_context().save[0][0]))


    def editMark(self):
        markId = input("Введите id оценки: ")
        value = input("Введите значение: ")
        while value > 5 or value < 2:
            value = input("не подходящее значение, введите оценку еще раз: ")
        self.repository.editPredmetMarks(markId, value)


    def createMenu(self):
        markMenu = Menu("Оценки", 1, True)
        viewMarkStud = markMenu.addSubMenu("Смотреть оценки студентов", 1)
        viewMarkStud.set_startup_command(self.controllerStudent.SelectCommand)
        viewMarkStud.set_before_select_command(self.controllerStudent.ShowCommand)
        viewMarkStud.set_tear_down_command(self.controllerStudent.DeselectCommand)
        viewMarkStud.additem(1, "Посмотреть оценки", self.viewAllMarkStudent)
        viewMarkStud.additem(2, "Изменить Оценку", self.editMark)

        viewMarkPredmet = markMenu.addSubMenu("Смотреть оценки по предметам", 1)
        viewMarkPredmet.set_startup_command(self.controllerPredmet.SelectCommand)
        viewMarkPredmet.set_before_select_command(self.controllerPredmet.ShowCommand)
        viewMarkPredmet.set_tear_down_command(self.controllerPredmet.DeselectCommand)
        viewMarkPredmet.additem(1, "Посмотреть оценки", self.viewAllMarksPredmet)
        viewMarkPredmet.additem(2, "Изменить Оценку", self.editMark)
        return markMenu







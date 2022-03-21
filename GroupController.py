from Menu import Menu
from Edit_context import Edit_context


class GroupController:
    def __init__(self, repository, studentController):
        self.repository = repository
        self.studentController = studentController

    def listGroups(self):
        list = self.repository.createList()
        for l in list:
            print(l)

    def add(self):
        self.listGroups()
        id=input("Введите ид группы: ")
        spec = input("Введите Спецификацию: ")
        course = input("Введите курс: ")
        self.repository.add(id, spec, course)

    def delete(self):
        self.listGroups()
        id = input("Введите ид группы: ")
        self.repository.delete(id)

    def editCourse(self):
        nextCourse=int(input("Введите курс"))
        self.repository.editCourse(nextCourse, Edit_context().save[0][0])
        self.refreshBeforeEdit()

    def editHeadOf(self):
        print(Edit_context().save)
        self.studentController.printListByGroup(Edit_context().save[0][0])
        try:
            studentId = int(input("Введите Id studentika: "))
            self.repository.editHeadOf(Edit_context().save[0][0], studentId)
        except:
            print("Всё не то Миша, давай поНовой!")
        self.refreshBeforeEdit()

    def ShowCommandStudent(self):
        self.studentController.printListByGroup(Edit_context().save[0][0])

    def createMenu(self):
        studMenu = Menu("Group", 2, True)
        studMenu.additem(1, "Список групп", self.listGroups)
        studMenu.additem(2, "Добавить группу", self.add)
        studMenu.additem(3, "Удалить группу", self.delete)
        editStudents = studMenu.addSubMenu("Редактировать group", 4)
        editStudents.set_startup_command(self.SelectCommand)
        editStudents.set_before_select_command(self.ShowCommand)
        editStudents.set_tear_down_command(self.DeselectCommand)
        editStudents.additem(1, "Изменить StaroStar", self.editHeadOf)
        editStudents.additem(2, "Изменить Course", self.editCourse)
        viewStudentByGroup = studMenu.addSubMenu("Показать студентов в группе", 5)
        viewStudentByGroup.set_startup_command(self.SelectCommand)
        viewStudentByGroup.set_before_select_command(self.ShowCommandStudent)
        viewStudentByGroup.set_tear_down_command(self.DeselectCommand)
        return studMenu

    def DeselectCommand(self):
        Edit_context().save = None

    def SelectCommand(self):
        self.listGroups()
        select = False
        while select == False:
            selectNumber = input("Введите номер Группы ")
            try:
                Edit_context().save = self.repository.SelectCommand(selectNumber)
                select = True
            except:
                print("Всё не то Миша, давай по Новой!")

    def ShowCommand(self):
        print(Edit_context().save)

    def refreshBeforeEdit(self):
        Edit_context().save = self.repository. refreshBeforeEdit([Edit_context().save[0][0]])
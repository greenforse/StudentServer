from Edit_context import Edit_context
from Menu import Menu


class TeacherController:

    def __init__(self, repository):
        # self.tableName = tableName
        self.oneName = "teacher"
        self.moreName = "teachers"
        self.repository = repository

    def printList(self):
        list = self.repository.createList()
        for i in list:
            print(i)

    def delete(self):
        id = int(input(f"Inter  delete {self.oneName}Id: "))
        self.repository.delete(id)

    def editMName(self):
        newMName = input("Введите новое отчество: ")
        id = Edit_context().save[0][0]
        self.repository.editMName(newMName, id)
        self.refreshBeforeEdit()

    def editLName(self):
        newLName = input("Введите новую фамилию: ")
        id = Edit_context().save[0][0]
        self.repository.editLName(newLName, id)
        self.refreshBeforeEdit()

    def editFName(self):
        newFName = input("Введите Новое Имя")
        id = Edit_context().save[0][0]
        self.repository.editLName(newFName, id)
        self.refreshBeforeEdit()

    def add(self):
        id = int(input("id: "))
        firstName = str(input("Введите Name: "))
        secondName = input("Введите фамилию: ")
        lastName = input("Введите отчество: ")
        kafedraID = input("Введите кафедру: ")
        academicDegree = input("Введите ученую сткпень: ")
        self.repository.add(id, firstName, secondName, lastName, kafedraID, academicDegree)

    def SelectCommand(self):
        self.printList()
        select = False
        while select == False:
            selectNumber = int(input("Введите номер пользователя"))
            try:
                Edit_context().save = self.repository.SelectCommand(selectNumber)
                select = True
            except:
                print("Такого пользователя нет")

    def ShowCommand(self):
        print(Edit_context().save)

    def createMenu(self):
        studMenu = Menu("Учителя", 1, True)
        studMenu.additem(1, "Список Учителей", self.printList)
        AddStud = studMenu.additem(2, "Добавить учителя", self.add)
        studMenu.additem(3, "Удалить учителя", self.delete)
        ####
        editStudents = studMenu.addSubMenu("Редактировать учителя", 4)
        editStudents.set_startup_command(self.SelectCommand)
        editStudents.set_before_select_command(self.ShowCommand)
        editStudents.set_tear_down_command(self.DeselectCommand)
        editStudents.additem(1, "Изменить фамилию", self.editFName)
        editStudents.additem(2, "Изменить имя", self.editLName)
        editStudents.additem(3, "Изменить Отчество", self.editMName)
        editStudents.additem(3, "Изменить kafedry", self.editKafedra)
        editStudents.additem(3, "Изменить Ученую степень", self.editAcademicDegree)
        return studMenu

    def refreshBeforeEdit(self):
        Edit_context().save = self.repository.refreshBeforeEdit([Edit_context().save[0][0]])

    def DeselectCommand(self):
        Edit_context().save = None

    def editKafedra(self):
        kaf = input("Введите новую кафедру: ")
        self.repository.editKafedra(Edit_context().save[0][0], kaf)

    def editAcademicDegree(self):
        acad = input("Ввудите новую Ученую степень: ")
        self.repository.editAcademicDegree(Edit_context().save[0][0], acad)

from RepositoryStudent import RepositoryStudent
from Edit_context import Edit_context
from Menu import Menu

class StudentController:
    def __init__(self, repository, oneName, moreName):
        #self.tableName = tableName
        self.oneName = oneName
        self.moreName = moreName
        self.repository = repository

    def printList(self):
        list = RepositoryStudent().createList()
        for i in list:
            print(i)

    def delete(self):
        id = int(input(f"Inter  delete {self.oneName}Id: "))
        RepositoryStudent().delete(id)

    def editMName (self):
        newMName = input("Введите новое отчество: ")
        id = Edit_context().save[0][0]
        self.repository().editMName(newMName, id)
        self.refreshBeforeEdit()

    def editLName(self):
        newLName = input("Введите новую фамилию: ")
        id = Edit_context().save[0][0]
        self.repository().editLName(newLName, id)
        self.refreshBeforeEdit()

    def editFName(self):
        newFName = input("Введите Новое Имя")
        id = Edit_context().save[0][0]
        self.repository().editLName(newFName, id)
        self.refreshBeforeEdit()

    def add(self):
        id = int(input("id: "))
        firstName = str(input("Введите Name: "))
        secondName = input("Введите фамилию: ")
        lastName = input("Введите отчество: ")
        groupId = input("Введите группу студента: ")
        self.repository().add(id, firstName, secondName, lastName, groupId)

    def SelectCommand(self):
        self.printList()
        select = False
        while select == False:
            selectNumber = int(input("Введите номер пользователя"))
            try:
                Edit_context().save = self.repository().SelectCommand(selectNumber)
                select = True
            except:
                print("Такого пользователя нет")

    def ShowCommand(self):
        print(Edit_context().save)

    def createMenu(self):
        studMenu = Menu("Студенты", 1, True)
        studMenu.additem(1, "Список студентов", self.printList)
        AddStud = studMenu.additem(2, "Добавить студента", self.add)
        studMenu.additem(3, "Удалить пользователя", self.delete)
        ####
        editStudents = studMenu.addSubMenu("Редактировать пользователя", 4)
        editStudents.set_startup_command(self.SelectCommand)
        editStudents.set_before_select_command(self.ShowCommand)
        editStudents.set_tear_down_command(self.DeselectCommand)
        editStudents.additem(1, "Изменить фамилию", self.editFName)
        editStudents.additem(2, "Изменить имя", self.editLName)
        editStudents.additem(2, "Изменить Отчество", self.editMName)
        return studMenu

    def refreshBeforeEdit(self):
        Edit_context().save = self.repository(). refreshBeforeEdit([Edit_context().save[0][0]])

    def DeselectCommand(self):
        Edit_context().save = None

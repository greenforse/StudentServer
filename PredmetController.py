from Edit_context import Edit_context
from Menu import Menu
from MenuService import MenuService
import Views

class PredmetController:
    def __init__(self, repository,specializationController):
        self.repository = repository
        self.menuService = MenuService()
        # self.controllerStudent = controllerStudent
        # self.controllerPredmet = controllerPredmet
        self.specializationController = specializationController
    def viewList(self):
        predmet = self.repository.createList()
        self.menuService.printList(predmet, Views.single_predmet_print)

    def SelectCommand(self):
        self.viewList()
        select = False
        while select == False:
            selectNumber = int(input("Введите номер предмета"))
            try:
                Edit_context().save = self.repository.SelectCommand(selectNumber)
                select = True
            except:
                print("Такого предмета нет")

    def ShowCommand(self):
        self.menuService.printList(Edit_context().save, Views.single_predmet_print)

    def DeselectCommand(self):
        Edit_context().save = None

    def add(self):
        id = input("Введите id")
        name = input("Введите название предмета: ")
        form = int(input("Засчет ? 1-да 2- нет: "))
        #while form != 1 or form != 2:
        #    form = int(input("Засчет ? 1-да 2- нет: "))
        if form == 1:
            zachet = True
        else:
            zachet = False
        self.repository.add(id, name, zachet)

    def addPredmeInSpecialization(self):
        predmetId = Edit_context().save[0][0]
        self.specializationController.SelectCommand()
        specializationId = Edit_context().save[0][0]
        course = input("Введите курс: ")
        self.repository.addPredmetInSpecializacion(predmetId, specializationId,course)
        self.DeselectCommand()

    def createMenu(self):
        markMenu = Menu("Предметы", 1, True)
        markMenu.additem(1,"Показать все предметы", self.viewList)
        markMenu.additem(1, "Добавить предмет", self.add)
        markMenu.additem(2, "Удалить предмет", self.delete)
        viewMarkStud = markMenu.addSubMenu("Редактировать предметы ", 2)
        viewMarkStud.set_startup_command(self.SelectCommand)
        viewMarkStud.set_before_select_command(self.ShowCommand)
        viewMarkStud.set_tear_down_command(self.DeselectCommand)
        viewMarkStud.additem(3,"Добавить предмет в специализацию", self.addPredmeInSpecialization)

        return markMenu

    def delete(self):
        pass
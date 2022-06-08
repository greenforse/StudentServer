from Edit_context import Edit_context
from Menu import Menu
from MenuService import MenuService
import Views

class SpecializationController:
    def __init__(self, repository):
        self.repository = repository
        self.menuService = MenuService()

    def viewList(self):
        self.menuService.printNotIntID(self.repository.viewList(), Views.print_spec)

    def SelectCommand(self):
        self.viewList()
        select = False
        while select == False:
            Edit_context().save = self.repository.viewList()
            selectNumber = int(input("Введите номер специализации"))
            try:
                select = Edit_context().save[selectNumber-1]
                Edit_context().save = select
                select = True
            except:
                print("Такой специализации нет")
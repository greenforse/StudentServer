class MenuService:
    def printList(self, lst, view):
        for elem in lst:
            view.single_print(elem)

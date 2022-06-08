class MenuService:
    def printList(self, lst, view):
        for elem in lst:
            view(elem)

    def printNotIntID(self, lst ,view):
        for i in range (len(lst)):
            view(lst[i], i+1 )
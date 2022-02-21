from Singleton import Singleton


class Edit_context(metaclass=Singleton):
    def __init__ (self):
        self.save = None
    #def get_instanse(self):

from tinydb import TinyDB, Query


class MainModel:
    """
    ==> Gestion des données (CRUD) pour : player, tournament et report.
    """
    # db = TinyDB("./ddb/db.json")
    #
    # def save_data(self):
    #     table = MainModel.db.table(self.__class__.__name__)
    #     table.insert(self.__dict__)
    #
    # def update_data(self, kye, value):
    #     table = MainModel.db.table(self.__class__.__name__)
    #     query = Query()
    #     table.update({kye: value}, query.id == self.id)
    #
    # def delate_data(self):
    #     table = MainModel.db.table(self.__class__.__name__)
    #     query = Query()
    #     table.remove(query.id == self.id)

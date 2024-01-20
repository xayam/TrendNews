from mykivy import MyKivy


class View(MyKivy):

    def __init__(self, model):
        self.model = model
        self.controller = self.model.controller

        super().__init__(model=self.model)

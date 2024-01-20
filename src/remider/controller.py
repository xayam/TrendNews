from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model(controller=self)
        self.view = View(model=self.model)

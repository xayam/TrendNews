from log import Log
from conf import Conf


class Model:

    def __init__(self, controller=None):
        self.controller = controller

        self.opt = None
        self.log = Log()
        self.reset_opt()
        self.conf = Conf(model=self)

    def reset_opt(self):
        self.opt = {

        }

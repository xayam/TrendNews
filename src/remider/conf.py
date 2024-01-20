import json
import os


class Conf:
    NAME = "Remider TrendNews"

    OPTIONS = "options.json"

    LICENSE = "LICENSE"
    ICON_ICO = "img/icon.ico"
    ICON_PNG = "img/icon.png"
    GITHUB_SYNCBOOKER = "https://github.com/xayam/syncbooker"
    EMAIL = "xayam@yandex.ru"

    # Icon paths
    ICON_CATALOG = "img/catalog.png"
    ICON_CATALOG_PRESSED = "img/catalog_pressed.png"
    ICON_OPTIONS = "img/options.png"
    ICON_OPTIONS_PRESSED = "img/options_pressed.png"

    def __init__(self, model):
        self.model = model
        self.controller = self.model.controller

        self.load_options()

    def load_options(self):
        if os.path.exists(self.OPTIONS):
            with open(self.OPTIONS, mode="r") as opt:
                self.model.opt = json.load(opt)
        else:
            self.save_options()

    def save_options(self):
        if self.controller is None:
            return
        json_string = json.dumps(self.model.opt)
        with open(self.OPTIONS, mode="w") as opt:
            opt.write(json_string)

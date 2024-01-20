from functools import partial

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App as KivyApp
from kivy.uix.tabbedpanel import TabbedPanel

from catalog import Catalog
from options import Options


class MyKivy(KivyApp):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.controller = self.model.controller

        Config.set('kivy', 'window_icon', self.model.conf.ICON_PNG)
        self.controller.container = TabbedPanel()
        self.controller.container.size_hint = (1, 1)
        self.controller.container.do_default_tab = False
        self.controller.catalog = Catalog(model=self.model)
        self.controller.container.add_widget(self.controller.catalog)
        self.controller.container.clear_tabs()
        self.controller.container.tab_height = 0

    def build(self):
        self.icon = self.model.conf.ICON_ICO
        self.title = "Remider TrendNews"
        Clock.schedule_once(partial(self.switch,
                                    self.controller.catalog), 0)
        return self.controller.container

    def switch(self, tab, *args):
        self.controller.container.switch_to(tab)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class Catalog(TabbedPanelItem):
    def __init__(self, model):
        self.model = model
        self.controller = self.model.controller

        TabbedPanelItem.__init__(self,
                                 background_normal=self.model.conf.ICON_CATALOG,
                                 background_down=self.model.conf.ICON_CATALOG_PRESSED)

        self.catalog_buttons = GridLayout(cols=1,
                                          size_hint=(1, None),
                                          padding=[20, 20],
                                          spacing=[20])
        self.navigator = BoxLayout(size_hint=(1, None),
                                   pos_hint={"y": 1},
                                   padding=(0, 0),
                                   height=48,
                                   )
        self.add_button = Button(text="Добавить новость-запрос",
                                 on_release=self.add_click)
        self.navigator.add_widget(self.add_button)
        self.catalog_scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)

        for _ in range(10):
            box_layout = BoxLayout(size_hint=(1, None),
                                   padding=(0, 0),
                                   height=200,
                                   orientation="vertical")
            header_layout = BoxLayout(size_hint=(1, None),
                                      pos_hint={"y": 1},
                                      padding=(0, 0),
                                      height=32,
                                      orientation="horizontal")
            text_input = TextInput(text='',
                                   multiline=False,
                                   hint_text="Название")
            delete_button = Button(text="Удалить")
            active_box = CheckBox(active=True, on_release=self.on_active_click)
            header_layout.add_widget(text_input)
            header_layout.add_widget(active_box)
            header_layout.add_widget(delete_button)
            text_info = TextInput(text='',
                                  multiline=True,
                                  hint_text="Запрос")
            box_layout.add_widget(header_layout)
            box_layout.add_widget(text_info)
            self.catalog_buttons.add_widget(box_layout)
            self.catalog_buttons.height += box_layout.height + 20
        self.catalog_scrollview.add_widget(self.catalog_buttons)
        self.all = BoxLayout(size_hint=(1, 1), orientation="vertical")
        self.all.add_widget(self.navigator)
        self.all.add_widget(self.catalog_scrollview)
        self.add_widget(self.all)

    def add_click(self, event=None):
        pass

    def on_active_click(self, event=None):
        print(event)


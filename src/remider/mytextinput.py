from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from utils import *


class MyTextInput(TextInput):

    def __init__(self, model, **kwargs):
        self.model = model
        self.controller = self.model.controller
        super().__init__(
            size_hint=(1, None),
            padding=(10, 10),
            focus=False,
            use_bubble=False,
            use_handles=False,
            scroll_from_swipe=False,
            selection_color=self.model.opt[SEL],
            background_color=self.model.opt[BG],
            foreground_color=self.model.opt[FG],
            **kwargs
        )
        self.is_focusable = False

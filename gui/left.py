from tkinter import Frame
from .widget import Widget
from .sheet import Sheet


class LeftPanel(Widget):
    def __init__(self, root):
        super().__init__(Frame, root)

        self.grid(0, 1, stick='news')
        self['bg'] = '#444'

        self.sheet = Sheet(self)

from tkinter import Frame
from .widget import Widget


class TopBar(Widget):
    def __init__(self, root):
        super().__init__(Frame, root, height=20)
        self.grid(0, 0, w=3, sticky='news')
        self['bg'] = '#ccc'

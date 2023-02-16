from tkinter import Tk, Frame
from .widget import Widget
from .top import TopBar
from .left import LeftPanel


class BottomBar(Widget):
    def __init__(self, root):
        super().__init__(Frame, root, height=20)
        self.grid(0, 2, w=3, stick='news')
        self['bg'] = '#ccc'


class MainPanel(Widget):
    def __init__(self, root):
        super().__init__(Frame, root)
        self.grid(1, 1, stick='news')
        self['bg'] = '#888'


class App(Widget):
    def __init__(self):
        super().__init__(Tk, None)

        self.tk.state('zoomed')

        self.tk.rowconfigure(0, weight=0)
        self.tk.rowconfigure(1, weight=1)
        self.tk.rowconfigure(2, weight=0)

        self.tk.columnconfigure(0, weight=0)
        self.tk.columnconfigure(1, weight=1)
        self.tk.columnconfigure(2, weight=0)

        self.top = TopBar(self)
        self.bot = BottomBar(self)
        self.main = MainPanel(self)
        self.left = LeftPanel(self)

    def run(self):
        self.tk.mainloop()

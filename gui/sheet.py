from state import sprite
from tkinter import Frame, Canvas
from .widget import Widget


class Cell(Widget):
    def __init__(self, root, i):
        super().__init__(Canvas, root, width=16, height=32)

        x, y = divmod(i, 16)
        self.grid(x, y)

        self['bg'] = '#000'
        self['highlightthickness'] = 1
        self['highlightbackground'] = root['bg']

    def on_enter(self, event):
        self['highlightbackground'] = '#fff'

    def on_leave(self, event):
        self['highlightbackground'] = self.root['bg']

    def update(self, sprt):
        self.tk.delete('all')
        self.tk.create_image(1, 1, image=sprt.image, anchor='nw')


class Sheet(Widget):
    def __init__(self, root):
        super().__init__(Frame, root)
        self.tk.grid(column=0, row=0, padx=4, pady=4)
        self['bg'] = root['bg']

        for i in range(0, 16):
            self.tk.rowconfigure(i, weight=1, pad=2)
            self.tk.columnconfigure(i, weight=1, pad=2)

        self.cell = [Cell(self, i) for i in range(0, 256)]

    def update(self, i=0):
        sprt = sprite.sheet[i]
        sprt[0, 0] = '#1ff'

        sprt[1, 1] = '#fff'
        sprt[15, 31] = '#fff'

        self.cell[i].update(sprt)

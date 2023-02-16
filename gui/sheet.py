from state import sprite
from tkinter import Frame, Canvas
from .widget import Widget

CELL_W = 16
CELL_H = 32
PAD = 2


def _cell2coor(x, y):
    return x*CELL_W + (x+1)*PAD, y*CELL_H + (y+1)*PAD


def _coor2cell(x, y):
    x, dx = divmod(x-PAD, CELL_W+PAD)
    y, dy = divmod(y-PAD, CELL_H+PAD)
    if dx < CELL_W and dy < CELL_H:
        return x, y
    else:
        return None


class Sheet(Widget):
    def __init__(self, root):
        super().__init__(Canvas, root, width=100)
        self.grid(0, 0)
        self['bg'] = '#222'
        self['highlightthickness'] = 0

        self['width'], self['height'] = _cell2coor(16, 16)

        self.cell = [self._create_cell(i) for i in range(0, 256)]
        self.cell_hover = self._create_rect('#400', 'hidden')
        self.cell_select = self._create_rect('#f44')
        self._highlight(self.cell_select, 0, 0)

    def update(self, i=0):
        sprt = sprite.sheet[i]
        item = self.cell[i]

        for i in range(0, 16):
            sprt[i, 0] = '#fff'
            sprt[i, 31] = '#fff'
            sprt[0, i] = '#fff'
            sprt[15, i] = '#fff'

        self.tk.itemconfig(item, image=sprt.image)

    def _create_cell(self, i):
        y, x = divmod(i, 16)
        x, y = _cell2coor(x, y)

        sprt = sprite.sheet[i].image
        return self.tk.create_image((x, y), image=sprt, anchor='nw')

    def _create_rect(self, outline, state='normal'):
        return self.tk.create_rectangle(0, 0, CELL_W+1, CELL_H+1, outline=outline, state=state)

    def _highlight(self, rect, x, y):
        x, y = _cell2coor(x, y)
        self.tk.moveto(rect, x-2, y-2)

    def _set_state(self, item, state):
        self.tk.itemconfig(item, state=state)

    def on_move(self, event):
        cell = _coor2cell(event.x, event.y)

        if cell is not None:
            x, y = cell
            self._set_state(self.cell_hover, 'normal')
            self._highlight(self.cell_hover, x, y)

    def on_leave(self, event):
        self._set_state(self.cell_hover, 'hidden')

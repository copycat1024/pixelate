from tkinter import Tk, Widget as TkWidget


class Widget:
    def __init__(self, tk_class, root, *arg, **kwargs):
        if tk_class is not Tk:
            if isinstance(root, Widget):
                self.root = root.tk
            elif isinstance(root, TkWidget):
                self.root = root

            self.tk = tk_class(self.root, *arg, **kwargs)

            self.tk.bind('<Enter>', self.on_enter)
            self.tk.bind('<Leave>', self.on_leave)
        else:
            self.tk = tk_class()

    def __setitem__(self, i, value):
        self.tk[i] = value

    def __getitem__(self, i):
        return self.tk[i]

    def grid(self, x, y, w=1, h=1, pad=0, **kwargs):
        self.tk.grid(
            column=x,
            row=y,
            columnspan=w,
            rowspan=h,
            padx=pad,
            pady=pad,
            **kwargs,
        )

    def on_enter(self, event):
        pass

    def on_leave(self, event):
        pass

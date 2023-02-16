from tkinter import PhotoImage


def rgb332_to_hash(rgb):
    if rgb > 255 or rgb < 0:
        raise ValueError('rgb332 must be in [0, 255]')
    r, rgb = divmod(rgb, 32)
    g, b = divmod(rgb, 4)

    r = round((r * 15) / 7)
    g = round((g * 15) / 7)
    b = round((b * 15) / 3)
    return f'#{r:x}{g:x}{b:x}'


class Sprite:
    def __init__(self, w=16, h=32):
        self.image = PhotoImage(width=w, height=h)

        for x in range(0, 16):
            for y in range(0, 32):
                self[x, y] = '#000'

    def __setitem__(self, i, value):
        self.image.put(value, i)

    def __getitem__(self, i):
        return self.image.get(*i)


class SpriteSheet:
    def __init__(self, count=256):
        self.data = [None] * count

    def __getitem__(self, i):
        if self.data[i] is None:
            self.data[i] = Sprite()

        return self.data[i]


sheet = SpriteSheet()

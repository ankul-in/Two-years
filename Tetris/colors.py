#colors.py
class Colors:
    a = "#FFBBE1"
    b = "#DD7BDF"
    c = "#B3BFFF"
    d = "#FF8F8F"
    e = "#FCB53B"
    f = "#B77466"
    g = "#8C00FF"
    h = "#E4004B"
    white=(255,255,255)
    black=(0,0,0)

    @classmethod
    def get_cell_colors(cls):
        return [
            cls.a, cls.b, cls.c, cls.d,
            cls.e, cls.f, cls.g, cls.h
        ]
    



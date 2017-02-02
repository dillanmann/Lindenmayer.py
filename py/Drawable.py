

class Drawable(object):

    def __init__(self, x=0, y=0, other=None):
        self.type = None
        self.size = Vector2f(100.0, 100.0)
        self.position = Vector2f(x, y) if other is not None else other.position

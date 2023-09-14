class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r, self.g, self.b = r, g, b

    def __call__(self) -> tuple[int, int, int]:
        return self.r, self.b, self.g

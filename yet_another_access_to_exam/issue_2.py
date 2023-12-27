END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class Color:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, another_color) -> bool:
        if isinstance(another_color, Color):
            return ((self.red == another_color.red) &
                    (self.green == another_color.green) &
                    (self.blue == another_color.blue))
        raise ValueError('Only for Color class!')


if __name__ == "__main__":
    color1 = Color(255, 0, 0)
    color2 = Color(255, 0, 0)
    color3 = Color(0, 255, 0)
    print(color1 == color2)
    print(color2 == color3)

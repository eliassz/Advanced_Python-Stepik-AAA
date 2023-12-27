END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class Color:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, another_color):

        if not isinstance(another_color, Color):
            raise NotImplementedError

        new_red = min(self.red + another_color.red, 255)
        new_green = min(self.green + another_color.green, 255)
        new_blue = min(self.blue + another_color.blue, 255)

        return Color(new_red, new_green, new_blue)

    def __repr__(self) -> str:
        return f'{START};{self.red};{self.green};{self.blue}{MOD}*{END}{MOD}'


if __name__ == "__main__":
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)

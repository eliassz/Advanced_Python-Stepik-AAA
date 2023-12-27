END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class Color:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self) -> str:
        return f'{START};{self.red};{self.green};{self.blue}{MOD}*{END}{MOD}'


if __name__ == "__main__":
    red = Color(255, 0, 0)
    print(red)

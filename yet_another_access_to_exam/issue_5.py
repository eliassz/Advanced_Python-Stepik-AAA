END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class Color:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __mul__(self, c: float):
        if not isinstance(c, float):
            raise NotImplementedError
        contrast = -256 * (1 - c)
        factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
        return Color(*map(
            lambda x: int(
                factor * (x - 128) + 128), [self.red, self.green, self.blue]
            )
        )

    def __rmul__(self, c: float):

        return self.__mul__(c)

    def __repr__(self) -> str:
        return f'{START};{self.red};{self.green};{self.blue}{MOD}*{END}{MOD}'


if __name__ == "__main__":
    red = Color(255, 0, 0)
    new_color = 0.5 * red
    print(new_color)

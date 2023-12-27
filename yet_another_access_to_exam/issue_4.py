END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class Color:
    def __init__(self, red, green, blue) -> None:
        self.rgb = (red, green, blue)

    def __repr__(self) -> str:
        return (f'{START};{self.rgb[0]};{self.rgb[1]};'
                f'{self.rgb[2]}{MOD}*{END}{MOD}')

    def __hash__(self) -> int:
        return hash(self.rgb)

    def __eq__(self, another_color) -> bool:
        if isinstance(another_color, Color):
            return ((self.rgb[0] == another_color.rgb[0]) &
                    (self.rgb[1] == another_color.rgb[1]) &
                    (self.rgb[2] == another_color.rgb[2]))
        raise NotImplementedError


if __name__ == "__main__":
    color1 = Color(255, 0, 0)
    color2 = Color(255, 0, 0)
    color3 = Color(0, 255, 0)
    color_list = [color1, color2, color3]
    print(set(color_list))

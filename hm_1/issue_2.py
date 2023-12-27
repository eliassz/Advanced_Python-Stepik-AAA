import keyword


class BaseAdvert:
    def __init__(self, input_dict):
        if 'title' not in input_dict:
            raise ValueError("missing 'title' field")

        self._price = 0
        for key, value in input_dict.items():
            if isinstance(value, dict):
                value = BaseAdvert(value)

            if keyword.iskeyword(key):
                key += '_'

            setattr(self, key, value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("must be >= 0")
        self._price = value


class ColorizeMixin:
    def __init__(self, *args, repr_color_code=32, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.repr_color_code = repr_color_code

    def __repr__(self):
        return (
            f"\033[1;{self.repr_color_code};40m"
            f"{self.title} | {self.price} ₽"
            "\033[0m"
        )


class Advert(ColorizeMixin, BaseAdvert):
    pass


if __name__ == '__main__':
    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    print(iphone_ad)

    dog_dict = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }
    dog_ad = Advert(dog_dict, repr_color_code=33)
    print(dog_ad)

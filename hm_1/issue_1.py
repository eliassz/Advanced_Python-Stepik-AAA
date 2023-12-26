import keyword


class Advert:
    def __init__(self, input_dict):
        self._price = 0
        for key, value in input_dict.items():
            if isinstance(value, dict):
                value = Advert(value)

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


if __name__ == '__main__':
    import json

    lesson_str = """{
    "title": "python",
    "price": 100,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    lesson_ad.location.address
    location = 'город Москва, Лесная, 7'
    assert lesson_ad.location.address == location, 'failed case #1'
    print('case 1 is correct!')

    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    assert dog_ad.class_ == 'dogs', 'failed case #2'
    print('case 2 is correct!')

    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
    except ValueError:
        print('case 3 is correct!')

    lesson_str = '{"title": "python", "price": 1}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    try:
        lesson_ad.price = -3
    except ValueError:
        print('case 4 is correct!')

    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0
    print('case 5 is correct!')

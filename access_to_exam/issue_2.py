class EmojiMixin:
    emojies = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '💧',
        'electric': '⚡️',
    }

    def __str__(self):
        return f'{self.name}/{EmojiMixin.emojies[self.poketype]}'


class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self) -> str:
        return f'{self.name}/{self.poketype}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)

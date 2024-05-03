from abc import ABC, abstractclassmethod


class BasePokemon:
    def __init__(self, name: str, poketype: str, experience: int = 100):
        self.name = name
        self.poketype = poketype
        self.experience = experience

    def __str__(self) -> str:
        return f'{self.name}/{self.poketype}'


class PokemonTrainInterface(ABC):
    @property
    @abstractclassmethod
    def experience(self):
        pass

    @abstractclassmethod
    def increase_experience(self, value):
        pass


class Pokemon(PokemonTrainInterface, BasePokemon):
    def experience(self):
        return self.experience

    def increase_experience(self, value):
        self.experience += value


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    bulbasaur.increase_experience(100)
    assert bulbasaur.experience == 200, "Try hard, Neeman!"
    print("It's alright!")

from src.item import Item

class MixinLanguage:
    def __init__(self, *args, language='EN', **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang not in ('EN', 'RU'):
            print("AttributeError: property 'language' of 'Keyboard' object has no setter")
        else:
            self.__language = lang

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):

    def __init__(self,  name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return super().__str__()

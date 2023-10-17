def test__str__(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'

def test_def_language(keyboard):
    assert keyboard.language == 'EN'

def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'

import main as m
import animaux as ac

def test_original_parler():
    assert m.parler(ac.Animal("chien")) == "Woof!"
    assert m.parler(ac.Animal("chat")) == "Meow!"
    assert m.parler(ac.Animal("oiseau")) == "Cui-cui!"

def test_refactored_parler():
    assert ac.Chien().parler() == "Woof!"
    assert ac.Chat().parler() == "Meow!"
    assert ac.Oiseau().parler() == "Cui-cui!"
def parler(animal):
    if animal.type == "chien":
        return "Woof!"
    elif animal.type == "chat":
        return "Meow!"
    elif animal.type == "oiseau":
        return "Cui-cui!"
    else:
        return None

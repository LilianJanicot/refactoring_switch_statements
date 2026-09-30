class Animal:
    def __init__(self, type):
        self.type = type

class Chien:
    def __init__(self):
        self.type = "chien"

    def parler(self):
        return "Woof!"

class Chat:
    def __init__(self):

        self.type = "chat"
        
    def parler(self):
        return "Meow!"

class Oiseau:
    def __init__(self):
        self.type = "oiseau"

    def parler(self):
        return "Cui-cui!"
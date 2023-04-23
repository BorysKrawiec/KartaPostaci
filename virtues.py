class Virtues:

    def __init__(self, conscience, self_control, courage):
        self.conscience = conscience
        self.self_control = self_control
        self.courage = courage

    def get_humanity(self):
        return self.conscience + self.self_control

    def get_willpower(self):
        return self.courage

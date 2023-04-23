class Abilities:

    abilities_names = ["Alertness", "Athletics", "Brawl", "Dodge", "Empathy", "Expression", "Intimidation",
                       "Leadership", "Streetwise", "Subterfuge", "Animal Ken", "Crafts", "Drive", "Etiquette",
                       "Firearms", "Melee", "Performance", "Security", "Stealth", "Survival", "Academics",
                       "Computer", "Finance", "Investigation", "Law", "Linguistics", "Medicine", "Occult",
                       "Politics", "Science"]

    def __init__(self, name, specialization, value):
        self.name = name
        self.specialization = specialization
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, kropki):
        if type(kropki) == int and 0 < kropki < 6:
            self._value = kropki
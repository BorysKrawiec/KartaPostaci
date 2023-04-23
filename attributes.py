class Attributes:

    attributes_names = ["Strength", "Dexterity", "Stamina", "Charisma", "Manipulation", "Appearance", "Perception", "Intelligence", "Wits"]

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
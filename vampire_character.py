from attributes import Attributes
from abilities import Abilities
from character import Character
from virtues import Virtues


class Vampire(Character):
    clans = ["Tremere", "Ventrue", "Malkavian"]

    def __init__(self, name, player, chronicle, nature, demanor, concept, genertation, sire, haven):
        super().__init__()
        self.name = name
        self.player = player
        self.chronicle = chronicle
        self.nature = nature
        self.demanor = demanor
        self.concept = concept
        self.genertation = genertation
        self.sire = sire
        self.haven = haven
        self.attributes = {}
        for attribute in Attributes.attributes_names:
            self.attributes[attribute] = Attributes(attribute, None, 1)
        self.abilities = {}
        for ability in Abilities.abilities_names:
            self.abilities[ability] = Abilities(ability, None, 0)
        self.virtues = Virtues(2, 2, 2)
        self.humanity = self.virtues.get_humanity()
        self.willpower = self.virtues.get_willpower()














    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, name):
    #     self.__name = name

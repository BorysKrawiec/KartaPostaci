import random
from abc import ABC

class Character(ABC):
    def __init__(self):
        pass

    @staticmethod
    def roll(attribute, ability, difficulty):
        total_dice = attribute.value + ability.value
        results = []
        succes = 0
        while total_dice > 0:
            die_result = random.randint(1, 10)
            results.append(die_result)
            if die_result >= difficulty:
                succes += 1
                if die_result == 10:
                    total_dice += 1
            elif die_result == 1:
                succes -= 1
            total_dice -= 1
        return results, succes
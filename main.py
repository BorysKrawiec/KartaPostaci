from vampire_character import Vampire

vampire1 = Vampire("Kalksztein", "Razi", "Empire City", "Beneficjent", "Survivalista", "Cwaniak", "8", "Nieznany", "Kanały")
print(dir(Vampire))

vampire1.attributes["Strength"].value = 5
vampire1.abilities["Brawl"].value = 3

for key, attribute in vampire1.attributes.items():
    print(attribute.name, attribute.value)
for key, ability in vampire1.abilities.items():
    print(ability.name, ability.value)



rolls, succes = vampire1.roll(vampire1.attributes["Strength"], vampire1.abilities["Brawl"], 5)
print(rolls)
print(succes)

#print(vampire1.clans)

# vampire1.name = "Bernard"
# print(vampire1.name)
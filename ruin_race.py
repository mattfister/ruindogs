import random

__author__ = 'Matt Fister'


class RuinRace():
    def __init__(self, name, plural_name, classes):
        self.name = name
        self.plural_name = plural_name
        self.classes = classes

ruin_races = [RuinRace("Aboleth", "Aboleths", ["Lasher", "Slime Mage", "Overseer", "Servitor"]),
              RuinRace("Abomination", "Abominations", ["Astral Stalker", "Atropal"]),
              RuinRace("Choker", "Chokers", ["Warrior"]),
              RuinRace("Banshrae", "Banshraes", ["Dartswarmer", "Warrior"]),
              RuinRace("Bodak", "Bodaks", ["Skulk", "Reaver"]),
              RuinRace("Demon", "Demons", ["Wizard", "Warrior", "Priest", "General"]),
              RuinRace("Cyclops", "Cyclopses", ["Guard", "Warrior", "Impaler", "Rambler", "Hewer", "Battleweaver"]),
              RuinRace("Dark One", "Dark Ones", ["Creeper", "Stalker"]),
              RuinRace("Doppelganger", "Doppelgangers", ["Sneak", "Assassin"]),
              RuinRace("Dragonborn", "Dragonborn", ["Gladiator", "Raider", "Champion"]),
              RuinRace("Drow", "Drow", ["Warrior", "Arachnomancer", "Blademaster", "Priest"]),
              RuinRace("Dwarf", "Dwarves", ["Bolter", "Hammerer", "Warrior", "Paladin", "Priest"]),
              RuinRace("Eladrin", "Eladrin", ["Fey Knight", "Twilight Enchanter", "Twilight Incanter", "Bralani", "Ghaele"]),
              RuinRace("Elf", "Elves", ["Archer", "Scout", "Warrior", "Berserker", "Wizard", "Cleric"]),
              RuinRace("Human", "Humans", ["Warrior", "Fighter", "Peasant", "Adventurer", "Wizard", "Cleric", "Ranger"])]


def get_ruin_race():
    return random.choice(ruin_races)

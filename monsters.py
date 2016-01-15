import random
from freezeword import a_or_an


class Monster(object):
    def __init__(self, name, name_plural, challenge_rating, sentient=False, race=None):
        self.name = name
        self.name_plural = name_plural
        self.sentient = sentient
        self.race = race
        self.challenge_rating = challenge_rating

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name


monsters = [
    Monster("Awakened Shrub", "Awakened Shrubs",0),
    Monster("Baboon", "Baboons", 0),
    Monster("Badger", "Badgers", 0),
    Monster("Cat", "Cats", 0),
    Monster("Bat", "Bats", 0),
    Monster("Commoner", "Commoners", 0, True, "Humans"),
    Monster("Crab", "Crabs", 0),
    Monster("Crawling Claw", "Crawling Claws", 0),
    Monster("Deer", "Deer", 0),
    Monster("Eagle", "Eagles", 0),
    Monster("Frog", "Frogs", 0),
    Monster("Giant fire beetle", "Giant fire beetles", 0),
    Monster("Goat", "Goats", 0),
    Monster("Hawk", "Hawks", 0),
    Monster("Homunculus", "Homunculi", 0),
    Monster("Hyena", "Hyenas", 0),
    Monster("Jackal", "Jackals", 0),
    Monster("Lemure", "Lemures", 0),
    Monster("Myconid Sprout", "Myconid Sprouts", True, "Myconids"),
    Monster("Octopus", "Octopi", 0),
    Monster("Owl", "Owls", 0),
    Monster("Quipper", "Quippers", 0),
    Monster("Rat", "Rats", 0),
    Monster("Raven", "Ravens", 0),
    Monster("Scorpion", "Scorpions", 0),
    Monster("Sea Horse", "Sea Horses", 0),
    Monster("Shrieker", "Shriekers", 0),
    Monster("Spider", "Spiders", 0),
    Monster("Vulture", "Vultures", 0),
    Monster("Bandit", "Bandits", True, "Humans"),
    Monster("Blood Hawk", "Blood Hawks", 1/8),
    Monster("Camel", "Camels", 1/8),
    Monster("Cultist", "Cultists", 1/8, True, "Humans"),
    Monster("Flumph", "Flumphs", 1/8),
    Monster("Flying Snake", "Flying Snakes", 1/8),
    Monster("Giant Crab", "Giant Crabs", 1/8),
    Monster("Giant Rat", "Giant Rats", 1/8),
    Monster("Giant Weasel", "Giant Weasels", 1/8),
    Monster("Guard", "Guards", 1/8, True, "Humans"),
    Monster("Kobold", "Kobolds", 1/8, True, "Kobolds"),
    Monster("Manes", "Manes", 1/8),
    Monster("Mastiff", "Mastiffs", 1/8),
    Monster("Merfolk", "Merfolk", 1/8),
    Monster("Monodrone", "Monodrones", 1/8),
    Monster("Mule", "Mules", 1/8),
    Monster("Noble", "Nobles", 1/8),
    Monster("Poisonous Snake", "Poisonous Snakes", 1/8),
    Monster("Pony", "Ponies", 1/8),
    Monster("Slaad Tadpole", "Slaad Tadpoles", 1/8),
    Monster("Stirge", "Stirges", 1/8),
    Monster("Tribal Warrior", "Tribal Warriors", 1/8, True, "Humans"),
    Monster("Twig Blight", "Twig Blights", 1/8),
    Monster("Acolyte", "Acolytes", 1/4, True, "Humans"),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Axe Beak", "Axe Beaks", 1/4),
    Monster("Blink Dog", "Blink Dogs", 1/4),
    Monster("Boar", "Boars", 1/4),
    Monster("Constrictor Snake", "Constrictor Snakes", 1/4),
    Monster("Draft Horse", "Draft Horses", 1/4),
    Monster("Dretch", "Dretches", 1/4),
    Monster("Drow", "Drows", 1/4, True, "Drows"),
    Monster("Duodrone", "Duodrones", 1/4),
    Monster("Elk", "Elks", 1/4),
    Monster("Flying Sword", "Flying Swords", 1/4),
    Monster("Giant Badger", "Giant Badgers", 1/4),
    Monster("Giant Bat", "Giant Bats", 1/4),
    Monster("Giant Centipede", "Giant Centipedes", 1/4),
    Monster("Giant Frog", "Giant Frogs", 1/4),
    Monster("Giant Lizard", "Giant Lizards", 1/4),
    Monster("Giant Owl", "Giant Owls", 1/4),
    Monster("Giant Poisonous Snake", "Giant Poisonous Snakes", 1/4),
    Monster("Giant Wolf Spider", "Giant Wolf Spiders", 1/4),
    Monster("Goblin", "Goblins", 1/4, True, "Goblins"),
    Monster("Kenku", "Kenkus", 1/4, True, "Kenku"),
    Monster("Kuo-Toa", "Kuo-Toa", 1/4, True, "Kuo-Toa"),
    Monster("Mud Mephit", "Mud Mephits", 1/4),
    Monster("Needle Blight", "Needle Blights", 1/4),
    Monster("Panther", "Panthers", 1/4),
    Monster("Pixie", "Pixies", 1/4, True, "Pixies"),
    Monster("Pseudodragon", "Pseudodragons", 1/4),
    Monster("Pteranodon", "Pteranodons", 1/4),
    Monster("Riding Horse", "Riding Horses", 1/4),
    Monster("Smoke Mephit", "Smoke Mephits", 1/4),
    Monster("Sprite", "Sprites", 1/4, True, "Sprites"),
    Monster("Steam Mephit", "Steam Mephits", 1/4),
    Monster("Swarm of Bats", "Swarms of Bats", 1/4),
    Monster("Swarm of Rats", "Swarms of Rats", 1/4),
    Monster("Swarm of Ravens", "Swarms of Rravens", 1/4),
    Monster("Troglodyte", "Troglodytes", 1/4, True, "Troglodytes"),
    Monster("Violet Fungus", "Violet Fungi", 1/4),
    Monster("Winged Kobold", "Winged Kobolds", 1/4, True, "Kobolds"),
    Monster("Wolf", "Wolves", 1/4),
    Monster("Zombie", "Zombies", 1/4),
    Monster("Ape", "Apes", 1/2),
    Monster("Black Bear", "Black Bears", 1/2),
    Monster("Cockatrice", "Cockatrice", 1/2),
    Monster("Crocodile", "Crocodiles", 1/2),
    Monster("Darkmantle", "Darkmantles", 1/2),
    Monster("Deep Gnome", "Deep Gnomes", 1/2, True, "Deep Gnomes"),
    Monster("Dust Mephit", "Dust Mephits", 1/2),
    Monster("Gas Spore", "Gas Spores", 1/2),
    Monster("Giant Goat", "Giant Goats", 1/2),
    Monster("Giant Sea Horse", "Giant Sea Horses", 1/2),
    Monster("Giant Wasp", "Giant Wasps", 1/2),
    Monster("Gnoll", "Gnolls", 1/2, True, "Gnolls"),
    Monster("Gray Ooze", "Gray Oozes", 1/2),
    Monster("Hobgoblin", "Hobgoblins", 1/2, True, "Goblins"),
    Monster("Ice Mephit", "Ice Mephits", 1/2),
    Monster("Jackalwere", "Jackalweres", 1/2),
    Monster("Lizardfolk", "Lizardfolk", 1/2, True, "Lizardfolk"),
    Monster("Magma Mephit", "Magma Mephits", 1/2),
    Monster("Magmin", "Magmins", 1/2),
    Monster("Myconid Adult", "Myconid Adults", 1/2, True, "Myconids"),
    Monster("Orc", "Orcs", 1/2, "Orc"),
    Monster("Piercer", "Piercers", 1/2),
    Monster("Reef Shark", "Reef Sharks", 1/2),
    Monster("Rust Monster", "Rust Monsters", 1/2),
    Monster("Sahuagin", "Sahuagin", 1/2, True, "Sahuagin"),
    Monster("Satyr", "Satyrs", 1/2, True, "Satyrs"),
    Monster("Scout", "Scouts", 1/2, True, "Humans"),
    Monster("Shadow", "Shadows", 1/2),
    Monster("Swarm of Insects", "Swarms of Insects", 1/2),
    Monster("Thug", "Thugs", 1/2, True, "Humans"),
    Monster("Tridrone", "Tridrones", 1/2),
    Monster("Vine Blight", "Vine Blights", 1/2),
    Monster("Warhorse", "Warhorses", 1/2),
    Monster("Warhorse Skeleton", "Warhorse Skeletons", 1/2),
    Monster("Worg", "Worgs", 1/2),
    Monster("Animated Armor", "Animated Armors", 1),
    Monster("Brass Dragon Wyrmling", "Brass Dragon Wyrmlings", 1),
    Monster("Brown Bear", "Brown Bears", 1),
    Monster("Bugbear", "Bugbears", 1),
    Monster("Copper Dragon Wyrmling", "Copper Dragon Wyrmlings", 1),
    Monster("Death Dog", "Death Dogs", 1),
    Monster("Dire Wolf", "Dire Wolves", 1),
    Monster("Dryad", "Dryads", 1, True, "Dryads"),
    Monster("Duergar", "Duergars", 1, True, "Duergars"),
    Monster("Young Faerie Dragon", "Young Faerie Dragons", 1),
    Monster("Fire Snake", "Fire Snakes", 1),
    Monster("Ghoul", "Ghouls", 1),
    Monster("Giant Eagle", "Giant Eagles", 1),
    Monster("Giant Hyena", "Giant Hyenas", 1),
    Monster("Giant Octopus", "Giant Octopi", 1),
    Monster("Giant Spider", "Giant Spider", 1),
    Monster("Giant Toad", "Giant Toads", 1),
    Monster("Giant Vulture", "Giant Vultures", 1),
    Monster("Goblin Boss", "Goblin Bosses", 1),
    Monster("Half-Ogre", "Half-Ogres", 1, True, "Ogres"),
    Monster("Harpy", "Harpies", 1, True, "Harpies"),
    Monster("Hippogriff", "Hippogriffs", 1),
    Monster("Imp", "Imp", 1, True, "Demons"),
    Monster("Kuo-Toa Whip", "Kuo-Toa Whips", 1, True, "Kuo-Toa"),
    Monster("Lion", "Lions", 1),
    Monster("Quadrone", "Quadrones", 1),
    Monster("Quaggoth Spore Servant", "Quaggoth Spore Servants", 1),
    Monster("Quasit", "Quasits", 1),
    Monster("Scarecrow", "Scarecrows", 1),
    Monster("Specter", "Specters", 1),
    Monster("Swarm of Quippers", "Swarms of Quippers", 1),
    Monster("Worg", "Worgs", 1),
    Monster("Thri-Kreen", "Thri-Kreens", 1, True, "Thri-Kreens"),
    Monster("Tiger", "Tigers", 1),
    Monster("Yuan-Ti Pureblood", "Yuan-Ti Purebloods", 1, True, "Yuan-Ti"),
    Monster("Allosaurus", "Allosauruses", 2),
    Monster("Ankheg", "Ankhegs", 2),
    Monster("Awakened Tree", "Awakened Trees", 2),
    Monster("Azer", "Azers", 2),
    Monster("Bandit Captain", "Bandit Captains", 2, True, "Humans"),
    Monster("Berserker", "Berserkers", 2, True, "Humans"),
    Monster("Black Dragon Wyrmling", "Black Dragon Wyrmlings", 2),
    Monster("Bronze Dragon Wyrmling", "Bronze Dragon Wyrmlings", 2),
    Monster("Carrion Crawler", "Carrion Crawlers", 2),
    Monster("Centaur", "Centaurs", 2, True, "Centaurs"),
    Monster("Cult Fanatic", "Cult Fanatics", 2, True, "Humans"),
    Monster("Druid", "Druids", 2, True, "Humans"),
    Monster("Ettercap", "Ettercaps", 2),
    Monster("Old Faerie Dragon", "Old Faerie Dragons", 2),
    Monster("Gargoyle", "Gargoyles", 2),
    Monster("Gelatinous Cube", "Gelatinous Cubes", 2),
    Monster("Ghast", "Ghasts", 2),
    Monster("Giant Boar", "Giant Boars", 2),
    Monster("Giant Constrictor Snake", "Giant Constrictor Snakes", 2),
    Monster("Giant Elk", "Giant Elks", 2),
    Monster("Gibbering Mouther", "Gibbering Mouthers", 2),
    Monster("Githzerai Monk", "Githzerai Monks", 2, True, "Githzerai"),
    Monster("Gnoll Pack Lord", "Gnoll Pack Lords", 2, True, "Gnolls"),
    Monster("Green Dragon Wyrmling", "Green Dragon Wyrmling", 2),
    Monster("Grick", "Gricks", 2),
    Monster("Griffon", "Griffons", 2),
    Monster("Hunter Shark", "Hunter Sharks", 2),
    Monster("Intellect Devourer", "Intellect Devourers", 2),
    Monster("Lizardfolk Shaman", "Lizardfolk Shamans", 2, True, "Lizardfolk"),
    Monster("Merrow", "Merrows", 2),
    Monster("Mimic", "Mimics", 2),
    Monster("Minotaur Skeleton", "Minotaur Skeletons", 2),
    Monster("Myconid Sovereign", "Myconid Sovereigns", 2, True, "Myconids"),
    Monster("Nothic", "Nothics", 2),
    Monster("Ochre Jelly", "Ochre Jellies", 2),
    Monster("Ogre", "Ogres", 2, True, "Ogres"),
    Monster("Ogre Zombie", "Ogre Zombies", 2),
    Monster("Orc Eye of Gruumsh", "Orc Eyes of Gruumsh", 2, True, "Orcs"),
    Monster("Orog", "Orogs", 2),
    Monster("Pegasus", "Pegasi", 2),
    Monster("Pentadrone", "Pentadrones", 2),
    Monster("Peryton", "Perytons", 2),
    Monster("Plesiosaurus", "Plesiosauruses", 2),
    Monster("Polar Bear", "Polar Bears", 2),
    Monster("Poltergeist", "Poltergeists", 2),
    Monster("Priest", "Priests", 2, True, "Humans"),
    Monster("Rhinoceros", "Rhinoceroses", 2),
    Monster("Rug of Smothering", "Rugs of Smothering", 2),
    Monster("Saber-Toothed Tiger", "Saber-Toothed Tigers", 2),
    Monster("Sahuagin Priestess", "Sahuagin Priestesses", 2, True, "Sahuagins"),
    Monster("Sea Hag", "Sea Hags", 2),
    Monster("Silver Dragon Wyrmling", "Silver Dragon Wyrmlings", 2),
    Monster("Spined Devil", "Spined Devils", 2, True, "Demons"),
    Monster("Swarm of Poisonous Snakes", "Swarms of Poisonous Snakes", 2),
    Monster("Wererat", "Wererat", 2),
    Monster("White Dragon Wyrmling", "White Dragon Wyrmlings", 2),
    Monster("Will-O’-Wisp", "Will-O’-Wisps", 2),
    Monster("Quaggoth", "Quaggoths", 3, True, "Quaggoths"),
    Monster("Ankylosaurus", "Ankylosauruses", 3),
    Monster("Basilisk", "Basilisks", 3),
    Monster("Bearded Devil", "Bearded Devils", 3, True, "Demons"),
    Monster("Blue Dragon Wyrmling", "Blue Dragon Wyrmlings", 3),
    Monster("Bugbear Chief", "Bugbear Chiefs", 3),
    Monster("Displacer Beast", "Displacer Beasts", 3),
    Monster("Doppelganger", "Doppelgangers", 3),
    Monster("Giant Scorpion", "Giant Scorpions", 3),
    Monster("Githyanki Warrior", "Githyanki Warriors", 3, True, "Githyanki"),
    Monster("Gold Dragon Wyrmling", "Gold Dragon Wyrmlings", 3),
    Monster("Green Hag", "Green Hags", 3),
    Monster("Grell", "Grells", 3),
    Monster("Hell Hound", "Hell Hounds", 3),
    Monster("Hobgoblin Captain", "Hobgoblin Captains", 3, True, "Goblins"),
    Monster("Hook Horror", "Hook Horrors", 3),
    Monster("Killer Whale", "Killer Whales", 3),
    Monster("Knight", "Knights", 3, True, "Humans"),
    Monster("Kuo-Toa Monitor", "Kuo-Toa Monitors", 3, True, "Kuo-Toa"),
    Monster("Manticore", "Manticores", 3),
    Monster("Minotaur", "Minotaurs", 3),
    Monster("Mummy", "Mummies", 3),
    Monster("Nightmare", "Nightmares", 3),
    Monster("Owlbear", "Owlbears", 3),
    Monster("Phase Spider", "Phase Spiders", 3),
    Monster("Quaggoth Thonot", "Quaggoth Thonots", 3, True, "Quaggoths"),
    Monster("Spectator", "Spectators", 3),
    Monster("Veteran", "Veterans", 3, True, "Humans"),
    Monster("Water Weird", "Water Weirds", 3),
    Monster("Werewolf", "Werewolves", 3),
    Monster("Wight", "Wights", 3),
    Monster("Winter Wolf", "Winter Wolves", 3),
    Monster("Yeti", "Yetis", 3),
    Monster("Yuan-Ti Malison", "Yuan-Ti Malisons", 3, True, "Yuan-Ti"),
    Monster("Banshee", "Banshees", 4),
    Monster("Black Pudding", "Black Puddings", 4),
    Monster("Bone Naga", "Bone Nagas", 4),
    Monster("Chuul", "Chuuls", 4),
    Monster("Couatl", "Couatls", 4),
    Monster("Elephant", "Elephants", 4),
    Monster("Ettin", "Ettins", 4),
    Monster("Flameskull", "Flameskulls", 4),
    Monster("Ghost", "Ghosts", 4),
    Monster("Gnoll Fang of Yeenoghu", "Gnoll Fangs of Yeenoghu", 4, True, "Gnolls"),
    Monster("Helmed Horror", "Helmed Horrors", 4),
    Monster("Incubus", "Incubi", 4, True, "Demons"),
    Monster("Lamia", "Lamias", 4),
    Monster("Lizard King", "Lizard Kings", 4),
    Monster("Orc War Chief", "Orc War Chiefs", 4, True, "Orcs"),
    Monster("Red Dragon Wyrmling", "Red Dragon Wyrmlings", 4),
    Monster("Shadow Demon", "Shadow Demons", 4),
    Monster("Succubus", "Succubi", 4, True, "Demons"),
    Monster("Wereboar", "Wereboars", 4),
    Monster("Weretiger", "Weretigers", 4),
    Monster("Air Elemental", "Air Elementals", 5),
    Monster("Barbed Devil", "Barbed Devils", 5, True, "Demons"),
    Monster("Barlgura", "Barlguras", 5),
    Monster("Beholder Zombie", "Beholder Zombies", 5),
    Monster("Bulette", "Bulettes", 5, True, "Demons"),
    Monster("Cambion", "Cambions", 5, True, "Demons"),
    Monster("Drow Elite Warrior", "Drow Elite Warriors", 5, True, "Drow"),
    Monster("Earth Elemental", "Earth Elementals", 5),
    Monster("Fire Elemental", "Fire Elementals", 5),
    Monster("Flesh Golem", "Flesh Golems", 5),
    Monster("Giant Crocodile", "Giant Crocodiles", 5),
    Monster("Giant Shark", "Giant Sharks", 5),
    Monster("Gladiator", "Gladiators", 5, True, "Humans"),
    Monster("Gorgon", "Gorgons", 5),
    Monster("Half-Red Dragon Veteran", "Half-Red Dragon Veterans", 5),
    Monster("Hill Giant", "Hill Giants", 5, True, "Giants"),
    Monster("Mezzoloth", "Mezzoloths", 5),
    Monster("Night Hag", "Night Hags", 5),
    Monster("Otyugh", "Otyughs", 5),
    Monster("Red Slaad", "Red Slaads", 5),
    Monster("Revenant", "Revenants", 5),
    Monster("Roper", "Ropers", 5),
    Monster("Sahuagin Baron", "Sahuagin Barons", 5, True, "Sahuagin"),
    Monster("Salamander", "Salamanders", 5),
    Monster("Shambling Mound", "Shambling Mounds", 5),
    Monster("Triceratops", "Triceratops", 5),
    Monster("Troll", "Trolls", 5),
    Monster("Umber Hulk", "Umber Hulks", 5),
    Monster("Unicorn", "Unicorns", 5),
    Monster("Vampire Spawn", "Vampire Spawns", 5, True, "Vampires"),
    Monster("Water Elemental", "Water Elementals", 5),
    Monster("Werebear", "Werebears", 5),
    Monster("Wraith", "Wraiths", 5),
    Monster("Xorn", "Xornx", 5),
    Monster("Young Remorhaz", "Young Remorhazes", 5),
    Monster("Chasme", "Chasmes", 6),
    Monster("Chimera", "Chimeras", 6),
    Monster("Cyclops", "Cyclopses", 6, True, "Cyclopses"),
    Monster("Drider", "Driders", 6),
    Monster("Galeb Duhr", "Galeb Duhrs", 6),
    Monster("Githzerai Zerth", "Githzerai Zerths", 6),
    Monster("Hobgoblin Warlord", "Hobgoblin Warlords", 6, True, "Goblins"),
    Monster("Invisible Stalker", "Invisible Stalkers", 6),
    Monster("Kuo-Toa Archpriest", "Kuo-Toa Archpriests", 6, True, "Kuo-Toa"),
    Monster("Mage", "Mages", 6, True, "Humans"),
    Monster("Mammoth", "Mammoths", 6),
    Monster("Medusa", "Medusas", 6),
    Monster("Vrock", "Vrocks", 6),
    Monster("Wyvern", "Wyverns", 6),
    Monster("Young Brass Dragon", "Young Brass Dragons", 6),
    Monster("Young White Dragon", "Young White Dragons", 6),
    Monster("Blue Slaad", "Blue Slaads", 7),
    Monster("Drow Mage", "Drow Mages", 7, True, "Drow"),
    Monster("Giant Ape", "Giant Apes", 7),
    Monster("Grick Alpha", "Grick Alphas", 7),
    Monster("Mind Flayer", "Mind Flayers", 7, True, "Mind Flayers"),
    Monster("Oni", "Onis", 7),
    Monster("Shield Guardian", "Shield Guardians", 7),
    Monster("Stone Giant", "Stone Giants", 7, True, "Giants"),
    Monster("Young Black Dragon", "Young Black Dragons", 7),
    Monster("Young Copper Dragon", "Young Copper Dragons", 7),
    Monster("Yuan-Ti Abomination", "Yuan-Ti Abominations", 7, True, "Yuan-Ti"),
    Monster("Assassin", "Assassins", 8, True, "Humans"),
    Monster("Chain Devil", "Chain Devils", 8),
    Monster("Cloaker", "Cloakers", 8),
    Monster("Drow Priestess of Lolth", "Drow Priestesses of Lolth", 8, True, "Drow"),
    Monster("Fomorian", "Fomorians", 8),
    Monster("Frost Giant", "Frost Giants", 8, True, "Giants"),
    Monster("Githyanki Knight", "Githyanki Knights", 8),
    Monster("Green Slaad", "Green Slaads", 8),
    Monster("Hezrou", "Hezrous", 8),
    Monster("Hydra", "Hydras", 8),
    Monster("Mind Flayer Arcanist", "Mind Flayer Arcanists", 8, True, "Mind Flayers"),
    Monster("Spirit Naga", "Spirit Nagas", 8),
    Monster("Tyrannosaurus Rex", "Tyrannosaurus Rexes", 8),
    Monster("Young Bronze Dragon", "Young Bronze Dragons", 8),
    Monster("Young Green Dragon", "Young Green Dragons", 8),
    Monster("Abominable Yeti", "Abominable Yetis", 9),
    Monster("Bone Devil", "Bone Devils", 9),
    Monster("Clay Golem", "Clay Golems", 9),
    Monster("Cloud Giant", "Cloud Giants", 9, True, "Giants"),
    Monster("Fire Giant", "Fire Giants", 9, True, "Giants"),
    Monster("Glabrezu", "Glabrezus", 9),
    Monster("Gray Slaad", "Gray Slaads", 9),
    Monster("Nycaloth", "Nycaloths", 9),
    Monster("Treant", "Treants", 9),
    Monster("Young Blue Dragon", "Young Blue Dragons", 9),
    Monster("Young Silver Dragon", "Young Silver Dragons", 9),
    Monster("Aboleth", "Aboleths", 10),
    Monster("Death Slaad", "Death Slaads", 10),
    Monster("Deva", "Devas", 10),
    Monster("Guardian Naga", "Guardian Nagas", 10),
    Monster("Stone Golem", "Stone Golems", 10),
    Monster("Yochlol", "Yochlols", 10),
    Monster("Young Gold Dragon", "Young Gold Dragons", 10),
    Monster("Young Red Dragon", "Young Red Dragons", 10),
    Monster("Behir", "Behirs", 12),
    Monster("Dao", "Daos", 12),
    Monster("Djinni", "Djinni", 12),
    Monster("Efreeti", "Efreeti", 12),
    Monster("Gynosphinx", "Gynosphinxes", 12),
    Monster("Horned Devil", "Horned Devils", 12),
    Monster("Marid", "Marids", 12),
    Monster("Remorhaz", "Remorhazes", 12),
    Monster("Roc", "Rocs", 12),
    Monster("Arcanaloth", "Arcanaloths", 12),
    Monster("Archmage", "Archmages", 12, True, "Humans"),
    Monster("Adult Brass Dragon", "Adult Brass Dragons", 12),
    Monster("Adult White Dragon", "Adult White Dragons", 13),
    Monster("Beholder", "Beholders", 13),
    Monster("Nalfeshnee", "Nalfeshnees", 13),
    Monster("Rakshasa", "Rakshasas", 13),
    Monster("Storm giant", "Storm giants", 13),
    Monster("Ultroloth", "Ultroloths", 13),
    Monster("Vampire", "Vampires", 13),
    Monster("Young Red Shadow Dragon", "Young Red Shadow Dragons", 13),
    Monster("Adult Black Dragon", "Adult Black Dragons", 14),
    Monster("Adult Copper Dragon", "Adult Copper Dragons", 14),
    Monster("Death Tyrant", "Death Tyrants", 14),
    Monster("Ice Devil", "Ice Devils", 14),
    Monster("Adult Bronze Dragon", "Adult Bronze Dragons", 15),
    Monster("Adult Green Dragon", "Adult Green Dragons", 15),
    Monster("Mummy Lord", "Mummy Lords", 15),
    Monster("Purple Worm", "Purple Worms", 15),
    Monster("Vampire Spellcaster", "Vampire Spellcasters", 15),
    Monster("Vampire Warrior", "Vampire Warriors", 15),
]


def get_monster(challenge_rating, offset=0, sentient=False):
    choices = []
    for monster in monsters:
        if monster.challenge_rating >= challenge_rating-offset and monster.challenge_rating <= challenge_rating+offset:
            if sentient:
                if monster.sentient:
                    choices.append(monster)
            else:
                choices.append(monster)
    return random.choice(choices)


def get_race(challenge_rating):
    candidate_monsters = []
    for monster in monsters:
        if monster.race is not None:
            candidate_monsters.append(monster)

    lowest_level_monsters_by_race = {}
    candidate_races = []
    for monster in candidate_monsters:
        if not monster.race in lowest_level_monsters_by_race.keys() and monster.challenge_rating < challenge_rating:
            lowest_level_monsters_by_race[monster.race] = monster
            candidate_races.append(monster.race)
        #else:
        #    if monster.challenge_rating < lowest_level_monsters_by_race[monster.race].challenge_rating:
        #        candidate_monsters[monster.race] = monster

    return random.choice(candidate_races)


def get_monster_under_cr(challenge_rating, race=None):
    candidates = []
    for monster in monsters:
        if race is None:
            if monster.challenge_rating <= challenge_rating:
                candidates.append(monster)
        else:
            if monster.challenge_rating <= challenge_rating and race == monster.race:
                candidates.append(monster)
    if len(candidates) == 0:
        return None
    return random.choice(candidates)

def build_encounter(challenge_rating, race=None):
    cr = challenge_rating
    encounter = []
    while cr > 0:
        monster = get_monster_under_cr(challenge_rating, race)
        if monster == None:
            break
        encounter.append(monster)
        cr -= monster.challenge_rating
    return encounter


#
# 16
# Adult blue dragon
# Adult silver dragon
# Iron golem
# Marilith
# Mummy lord (in lair)
# Planetar
# 17
# Adult blue dracolich
# Adult gold dragon
# Adult red dragon
# Androsphinx
# Death knight
# Dragon turtle
# Goristro
# 18
# Demilich
# 19
# Balor
# 20
# Ancient brass dragon
# Ancient white dragon
# Demilich (in lair)
# Pit fiend
# 21
# Ancient black dragon
# Ancient copper dragon
# Lich (not in lair)
# Solar
# 22
# Ancient bronze dragon
# Ancient green dragon
# Lich (in lair)
# 23
# Ancient blue dragon
# Ancient silver dragon
# Empyrean
# Kraken
# 24
# Ancient gold dragon
# Ancient red dragon
# 30
# Tarrasque

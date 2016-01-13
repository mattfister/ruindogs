class Monster(object):
    def __init__(self, name, name_plural, challenge_rating, sentient=False, race=None):
        self.name = name
        self.name_plural = name_plural
        self.sentient = sentient
        self.race = race
        self.challenge_rating = challenge_rating


monsters = [
    Monster("Awakened Shrub", "Awakened Shrubs",0),
    Monster("Baboon", "Baboons", 0),
    Monster("Badger", "Badgers", 0),
    Monster("Cat", "Cats", 0),
    Monster("Bat", "Bats", 0),
    Monster("Commoner", "Commoners", 0, True, "humans"),
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
    Monster("Myconid Sprout", "Myconid Sprouts", 0),
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
    Monster("Bandit", "Bandits", 0),
    Monster("Blood Hawk", "Blood Hawks", 1/8),
    Monster("Camel", "Camels", 1/8),
    Monster("Cultist", "Cultists", 1/8),
    Monster("Flumph", "Flumphs", 1/8),
    Monster("Flying Snake", "Flying Snakes", 1/8),
    Monster("Giant Crab", "Giant Crabs", 1/8),
    Monster("Giant Rat", "Giant Rats", 1/8),
    Monster("Giant Weasel", "Giant Weasels", 1/8),
    Monster("Guard", "Guards", 1/8),
    Monster("Kobold", "Kobolds", 1/8),
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
    Monster("Tribal Warrior", "Tribal Warriors", 1/8),
    Monster("Twig Blight", "Twig Blights", 1/8),
    Monster("Acolyte", "Acolytes", 1/4),
    Monster("Axe beak", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),
    Monster("Aarakocra", "Aarakocras", 1/4),

]



# Blink dog
# Boar
# Bullywug
# Constrictor snake
# Draft horse
# Dretch
# Drow
# Duodrone
# Elk
# Flying sword
# Giant badger
# Giant bat
# Giant centipede
# Giant frog
# Giant lizard
# Giant owl
# Giant poisonous snake
# Giant wolf spider
# Goblin
# Grimlock
# Kenku
# Kuo-toa
# Mud mephit
# Needle blight
# Panther
# Pixie
# Pseudodragon
# Pteranodon
# Riding horse
# Skeleton
# Smoke mephit
# Sprite
# Steam mephit
# Swarm of bats
# Swarm of rats
# Swarm of ravens
# Troglodyte
# Violet fungus
# Winged kobold
# Wolf
# Zombie
# 1/2
# Ape
# Black bear
# Cockatrice
# Crocodile
# Darkmantle
# Deep gnome
# Dust mephit
# Gas spore
# Giant goat
# Giant sea horse
# Giant wasp
# Gnoll
# Gray ooze
# Hobgoblin
# Ice mephit
# Jackalwere
# Lizardfolk
# Magma mephit
# Magmin
# Myconid adult
# Orc
# Piercer
# Reef shark
# Rust monster
# Sahuagin
# Satyr
# Scout
# Shadow
# Swarm of insects
# Thug
# Tridrone
# Vine blight
# Warhorse
# Warhorse skeleton
# Worg
# 1
# Animated armor
# Brass dragon wyrmling
# Brown bear
# Bugbear
# Copper dragon wyrmling
# Death dog
# Dire wolf
# Dryad
# Duergar
# Faerie dragon (young)
# Fire snake
# Ghoul
# Giant eagle
# Giant hyena
# Giant octopus
# Giant spider
# Giant toad
# Giant vulture
# Goblin boss
# Half-ogre
# Harpy
# Hippogriff
# Imp
# Kuo-toa whip
# Lion
# Quadrone
# Quaggoth spore servant
# Quasit
# Scarecrow
# Specter
# Spy
# Swarm of quippers
# Thri-kreen
# Tiger
# Yuan-ti pureblood
# 2
# Allosaurus
# Ankheg
# Awakened tree
# Azer
# Bandit captain
# Berserker
# Black dragon wyrmling
# Bronze dragon wyrmling
# Carrion crawler
# Centaur
# Cult fanatic
# Druid
# Ettercap
# Faerie dragon (old)
# Gargoyle
# Gelatinous cube
# Ghast
# Giant boar
# Giant constrictor snake
# Giant elk
# Gibbering mouther
# Githzerai monk
# Gnoll pack lord
# Green dragon wyrmling
# Grick
# Griffon
# Hunter shark
# Intellect devourer
# Lizardfolk shaman
# Merrow
# Mimic
# Minotaur skeleton
# Myconid sovereign
# Nothic
# Ochre jelly
# Ogre
# Ogre zombie
# Monsters by Challenge Rating
# 2
# Monsters by Challenge Rating
# Orc Eye of Gruumsh
# Orog
# Pegasus
# Pentadrone
# Peryton
# Plesiosaurus
# Polar bear
# Poltergeist (specter)
# Priest
# Quaggoth
# Rhinoceros
# Rug of smothering
# Saber-toothed tiger
# Sahuagin priestess
# Sea hag
# Silver dragon wyrmling
# Spined devil
# Swarm of poisonous snakes
# Wererat
# White dragon wyrmling
# Will-o’-wisp
# 3
# Ankylosaurus
# Basilisk
# Bearded devil
# Blue dragon wyrmling
# Bugbear chief
# Displacer beast
# Doppelganger
# Giant scorpion
# Githyanki warrior
# Gold dragon wyrmling
# Green hag
# Grell
# Hell hound
# Hobgoblin captain
# Hook horror
# Killer whale
# Knight
# Kuo-toa monitor
# Manticore
# Minotaur
# Mummy
# Nightmare
# Owlbear
# Phase spider
# Quaggoth thonot
# Spectator
# Veteran
# Water weird
# Werewolf
# Wight
# Winter wolf
# Yeti
# Yuan-ti malison
# 4
# Banshee
# Black pudding
# Bone naga
# Chuul
# Couatl
# Elephant
# Ettin
# Flameskull
# Ghost
# Gnoll fang of Yeenoghu
# Helmed horror
# Incubus
# Lamia
# Lizard king/queen
# Orc war chief
# Red dragon wyrmling
# Sea hag (in coven)
# Shadow demon
# Succubus
# Wereboar
# Weretiger
# 5
# Air elemental
# Barbed devil
# Barlgura
# Beholder zombie
# Bulette
# Cambion
# Drow elite warrior
# Earth elemental
# Fire elemental
# Flesh golem
# Giant crocodile
# Giant shark
# Gladiator
# Gorgon
# Green hag (in coven)
# Half-red dragon veteran
# Hill giant
# Mezzoloth
# Night hag
# Otyugh
# Red slaad
# Revenant
# Roper
# Sahuagin baron
# Salamander
# Shambling mound
# Triceratops
# Troll
# Umber hulk
# Unicorn
# Vampire spawn
# Water elemental
# Werebear
# Wraith
# Xorn
# Young remorhaz
# 6
# Chasme
# Chimera
# Cyclops
# Drider
# Galeb duhr
# Githzerai zerth
# Hobgoblin warlord
# Invisible stalker
# Kuo-toa archpriest
# Mage
# Mammoth
# Medusa
# Vrock
# Wyvern
# Young brass dragon
# Young white dragon
# 7
# Blue slaad
# Drow mage
# Giant ape
# Grick alpha
# Mind flayer
# Night hag (in coven)
# Oni
# Shield guardian
# Stone giant
# Young black dragon
# Young copper dragon
# Yuan-ti abomination
# 8
# Assassin
# Chain devil
# Cloaker
# Drow priestess of Lolth
# Fomorian
# Frost giant
# Githyanki knight
# Green slaad
# Hezrou
# Hydra
# Mind flayer arcanist
# Spirit naga
# Tyrannosaurus rex
# Young bronze dragon
# Young green dragon
# 9
# Abominable yeti
# Bone devil
# Clay golem
# Cloud giant
# Fire giant
# Glabrezu
# Gray slaad
# Nycaloth
# Treant
# Young blue dragon
# Young silver dragon
# 10
# Aboleth
# Death slaad
# Deva
# Guardian naga
# Stone golem
# Yochlol
# Young gold dragon
# Young red dragon
# 11
# Behir
# Dao
# Djinni
# Efreeti
# Gynosphinx
# Horned devil
# Marid
# Remorhaz
# Roc
# 12
# Arcanaloth
# Archmage
# Erinyes
# 13
# Adult brass dragon
# Adult white dragon
# Beholder (not in lair)
# Nalfeshnee
# Rakshasa
# Storm giant
# Ultroloth
# Vampire
# Young red shadow dragon
# 14
# Adult black dragon
# Adult copper dragon
# Beholder (in lair)
# Death tyrant (not in lair)
# Ice devil
# 15
# Adult bronze dragon
# Adult green dragon
# Death tyrant (in lair)
# Mummy lord (not in lair)
# Purple worm
# Vampire (spellcaster)
# Vampire (warrior)
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

import random

class DnDCharacter:
    races = ["Human", "Dragonborn", "Gnome", "Plasmiod", "Half-Elf", "Half-Orc", "Tiefling", "Elf", "Dwarf", "Halfling"]
    classes = ["Fighter", "Artificer", "Barbarian", "Bard", "Blood Hunter", "Cleric", "Druid", "Monk", "Palidin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard"]

    def __init__(self):
        self.name = self.generate_name()
        self.race = random.choice(self.races)
        self.char_class = random.choice(self.classes)
        self.level = random.randint(1, 20)
        self.stats = self.generate_stats()

    def generate_name(self):
        prefixes = ["Ald", "Bal", "Cal", "Dorn", "Eld", "Fal"]
        suffixes = ["dor", "gar", "len", "mir", "nor", "rath"]
        return random.choice(prefixes) + random.choice(suffixes)

    def generate_stats(self):
        stats = {}
        stats["Strength"] = random.randint(10, 16)
        stats["Dexterity"] = random.randint(10, 16)
        stats["Constitution"] = random.randint(10, 16)
        stats["Intelligence"] = random.randint(10, 16)
        stats["Wisdom"] = random.randint(10, 16)
        stats["Charisma"] = random.randint(10, 16)
        return stats

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nClass: {self.char_class}\nLevel: {self.level}\nStats: {self.stats}"

# Example usage
# player1 = DnDCharacter()
# print(player1)

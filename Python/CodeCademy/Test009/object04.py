class MainStorage:
    storage = {}


class Orc(MainStorage):
    orcs = MainStorage.storage["orcs"] = {}

    def __init__(self, name, lvl=1):
        self.name = name
        self.lvl = lvl
        if lvl in self.orcs:
            self.orcs[lvl].append(name)
        else:
            self.orcs[lvl] = [name]
        self.init()

    def init(self):
        if self.lvl == 1:
            self.hp = 50
        elif self.lvl == 2:
            self.hp = 100


class Elf(MainStorage):
    elves = MainStorage.storage["elves"] = {}

    def __init__(self, name, lvl=1):
        self.name = name
        self.lvl = lvl
        if lvl in self.elves:
            self.elves[lvl].append(name)
        else:
            self.elves[lvl] = [name]
        self.init()

    def init(self):
        if self.lvl == 1:
            self.hp = 50
        elif self.lvl == 2:
            self.hp = 100

orc = Orc("Papai")
orc1 = Orc("Grunt")
orc2 = Orc("Babel", 2)
elf = Elf("Eljacua")

print(MainStorage.storage)

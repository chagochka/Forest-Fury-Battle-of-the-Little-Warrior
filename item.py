import random


class Item:
    """
    Класс предмет
    """
    rarities = ['common', 'uncommon', 'rare', 'mythical', 'legendary']

    def __init__(self, image, rarity, item_type, ench=False):
        self.ench = ench
        self.image = image
        self.rarity = rarity
        self.type = item_type
        self.stat = 0

    def blit_image(self, window, pos):
        window.blit(self.image, pos)


class Weapon(Item):
    stats = ((100, 120), (120, 150), (150, 170), (170, 200), (200, 250))

    def __init__(self, image, rarity, item_type):
        super().__init__(image, rarity, item_type)
        self.ench = False
        self.image = image
        self.rarity = rarity
        self.type = item_type
        stats_index = self.rarities.index(self.rarity)
        if self.ench:
            coof = 50
        else:
            coof = 0
        self.stat = random.randint(self.stats[self.type][stats_index][0], self.stats[self.type][stats_index][1]) + coof


class Armor(Item):
    stats = {
        'boots': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'trousers': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'breastplate': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'helmet': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
    }

    def __init__(self, image, rarity, item_type, ench=False):
        super().__init__(image, rarity, item_type, ench)
        self.ench = ench
        self.image = image
        self.rarity = rarity
        self.type = item_type
        stats_index = self.rarities.index(self.rarity)
        if self.ench:
            coof = 50
        else:
            coof = 0
        self.stat = random.randint(self.stats[self.type][stats_index][0], self.stats[self.type][stats_index][1]) + coof


class HealingBottle(Item):
    """Класс зелья здоровья"""

    rarities = ['uncommon', 'mythical', 'legendary']
    stats = {
        'uncommon': 25,
        'mythical': 50,
        'legendary': 100
    }

    def __init__(self, image, rarity, item_type):
        super().__init__(image, rarity, item_type)
        self.stat = self.stats[rarity]
        self.rarity = rarity

    def heal(self, player):
        if player.health + self.stat < 1000:
            if player.health + self.stat > player.max_health:
                player.max_health += player.health + self.stat - player.max_health
            player.health += self.stat

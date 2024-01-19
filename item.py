import random


class Item:
    """
    Класс предмет
    """
    rarities = ['common', 'uncommon', 'rare', 'mythical', 'legendary']

    def __init__(self, image, rarity, item_type):

        self.image = image
        self.rarity = rarity
        self.type = item_type

    def blit_image(self, window, pos):
        window.blit(self.image, pos)


class Weapon(Item):
    stats = ((100, 120), (120, 150), (150, 170), (170, 200), (200, 250))

    def __init__(self, image, rarity, item_type):
        super().__init__(image, rarity, item_type)
        self.image = image
        self.rarity = rarity
        self.type = item_type
        stats_index = self.rarities.index(self.rarity)
        self.stat = random.randint(self.stats[stats_index][0], self.stats[stats_index][1])


class Armor(Item):
    stats = {
        'boots': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'trousers': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'breastplate': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        'helmet': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
    }

    def __init__(self, image, rarity, item_type):
        super().__init__(image, rarity, item_type)
        self.image = image
        self.rarity = rarity
        self.type = item_type
        stats_index = self.rarities.index(self.rarity)
        self.stat = random.randint(self.stats[self.type][stats_index][0], self.stats[self.type][stats_index][1])


class HealingBottle(Item):
    """Класс зелья здоровья"""

    def __init__(self, image, rarity, item_type):
        super().__init__(image, rarity, item_type)
        self.timer = 0
        self.created = False
        self.stat = 100

    def is_created(self):
        """
        Возвращает True/False в зависимости от того выпало ли зелье
        :return: bool
        """
        return self.created

    def drop(self, x, y):
        """
        Устанавливает координаты и рандомно выбирает количество лечения
        :param x: int
        :param y: int
        :return: None
        """
        self.created = True
        self.cords = (x, y)
        self.heal = random.choices([50, 75, 100], weights=[5, 3, 1], k=1)[0]

    def use_heal(self):
        """
        Устанавливает таймер на использование
        :return: None
        """
        self.timer = 300

    def can_use(self):
        """
        Возвращает True/False в зависимости от того можно ли использовать зелье
        :return:
        """
        return self.timer <= 0
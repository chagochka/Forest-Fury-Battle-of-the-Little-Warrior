class Item():
	"""
	Класс предмет
	"""

	def __init__(self, image, rarity, type):
		self.image = image
		self.rarity = rarity
		self.type = type

	def drop(self, window, pos):
		window.blit(self.image, pos)


class Weapon(Item):
	stats = {
		'common': 100,
		'uncommon': 150,
		'mythical': 200,
		'legendary': 300,
	}

	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)
		self.image = image
		self.rarity = rarity
		self.type = type
		self.stat = self.damage = self.stats[self.rarity]


class Armor(Item):
	stats = {
		'common': 100,
		'uncommon': 150,
		'mythical': 200,
		'legendary': 300,
	}

	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)
		self.image = image
		self.rarity = rarity
		self.type = type
		self.stat = self.defense = self.stats[self.rarity]

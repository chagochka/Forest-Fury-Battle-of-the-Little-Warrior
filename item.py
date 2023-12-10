class Item():
	"""
	Класс предмет
	"""

	def __init__(self, image, rarity, type):
		self.image = image
		self.rarity = rarity
		self.type = type

	def drop(self, window, pos):
		"""
		Функция проверяет сложность побежденного монстра и если сложность босс - то дает в инвентарь игроку случайный
		легендарный дроп иначе - с 30% шансом вызывает функцию для получения любого дропа (даже хуже имеющегося)
		:param window:
		:param pos:
		:param diff: Str - сложность убитого монстра
		:return: None
		"""
		window.blit(self.image, pos)


class Weapon(Item):
	damages = {
		'common': 100,
		'uncommon': 150,
		'mythical': 250,
		'legendary': 400,
	}

	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)
		self.image = image
		self.rarity = rarity
		self.type = type
		self.damage = self.damages[self.rarity]


class Armor(Item):
	defenses = {
		'common': 100,
		'uncommon': 150,
		'mythical': 250,
		'legendary': 400,
	}

	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)

		self.image = image
		self.rarity = rarity
		self.type = type
		self.defense = self.defenses[self.rarity]

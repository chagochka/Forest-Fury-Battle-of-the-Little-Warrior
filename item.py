import pygame as pg


class Item():
	"""
	Класс предмет
	"""

	def __init__(self, image, rarity, type):
		self.image = image
		self.rarity = rarity
		self.type = type

	def drop_weapon(self, diff, pos):
		"""
		Функция проверяет сложность побежденного монстра и если сложность босс - то дает в инвентарь игроку случайный
		легендарный дроп иначе - с 30% шансом вызывает функцию для получения любого дропа (даже хуже имеющегося)
		:param diff: Str - сложность убитого монстра
		:return: None
		"""
		pass


class Weapon(Item):
	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)
		damages = {
			'common': 100,
			'rare': 150,
			'epic': 250,
			'legendary': 400,
		}
		self.image = image
		self.rarity = rarity
		self.type = type
		self.damage = damages[self.rarity]


class Armor(Item):
	def __init__(self, image, rarity, type):
		super().__init__(image, rarity, type)
		defenses = {
			'common': 100,
			'rare': 150,
			'epic': 250,
			'legendary': 400,
		}
		self.image = image
		self.rarity = rarity
		self.type = type
		self.defense = defenses[self.rarity]

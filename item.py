import pygame as pg


class Item():
	"""
	Класс предмет
	"""
	def __init__(self, image, rarity, item_class):
		self.image = image
		self.rarity = rarity
		self.item_class = item_class

	def drop_weapon(self, diff, pos):
		"""
		Функция проверяет сложность побежденного монстра и если сложность босс - то дает в инвентарь игроку случайный
		легендарный дроп иначе - с 30% шансом вызывает функцию для получения любого дропа (даже хуже имеющегося)
		:param diff: Str - сложность убитого монстра
		:return: None
		"""
		pass


class Weapon(Item):
	def __init__(self, image, rarity, item_class, damage):
		super().__init__(image, rarity, item_class)
		self.image = image
		self.rarity = rarity
		self.item_class = item_class
		self.damage = damage


class Armor(Item):
	def __init__(self, image, rarity, item_class, defense):
		super().__init__(image, rarity, item_class)
		self.image = image
		self.rarity = rarity
		self.item_class = item_class
		self.defense = defense

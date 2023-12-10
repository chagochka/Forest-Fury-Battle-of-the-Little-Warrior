import pygame as pg


class Item(pg.sprite.Sprite):
	"""
	Класс предмет
	"""

	def __init__(self, group_sprites, pos, image, rarity, item_class):
		super().__init__(group_sprites)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = pos
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
	def __init__(self, group_sprites, pos, image, rarity, item_class, damage):
		super().__init__(group_sprites, pos, image, rarity, item_class)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = pos
		self.rarity = rarity
		self.item_class = item_class
		self.damage = damage


class Armor(Item):
	def __init__(self, group_sprites, pos, image, rarity, item_class, defense):
		super().__init__(group_sprites, pos, image, rarity, item_class)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = pos
		self.rarity = rarity
		self.item_class = item_class
		self.defense = defense

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

	# self.inventory_rarities = {
	#     'sword': '',
	#     'boots': '',
	#     'trousers': '',
	#     'breastplate': '',
	#     'helmet': ''
	# }
	# self.rarities = ['common', 'uncommon', 'rare', 'mythical', 'legendary']  # редкости снаряжения
	# self.weapon = ['sword', 'boots', 'trousers', 'breastplate', 'helmet']  # типы снаряжения (accessory deleted)
	# self.weapons = {
	#     'sword': [(100, 120), (120, 150), (150, 170), (170, 200), (200, 250)],  # статистика снаряжения по редкости
	#     'boots': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
	#     'trousers': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
	#     'breastplate': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
	#     'helmet': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
	#     # 'accessory': [(100, 150), (150, 200), (200, 250), (250, 300), (300, 350)]
	# }
	# self.stats = {
	#     'sword': 0,
	#     'boots': 0,
	#     'trousers': 0,
	#     'breastplate': 0,
	#     'helmet': 0
	# }

	def weapon_stats(self):
		"""
		Функция рандомно выбирает тип редкость и статистику предмета
		:return: None
		"""
		rarity = random.choices(self.rarities, weights=[5, 4, 3, 2, 1], k=1)[0]  # редкость дропа
		weapon = random.choices(self.weapon, weights=[8, 9, 9, 10, 9], k=1)[0]  # тип оружия/брони
		# (шанс на аксессуар удален)
		statistic = random.randint(self.weapons[weapon][self.rarities.index(rarity)][0],
		                           self.weapons[weapon][self.rarities.index(rarity)][1])  # статистика урон защита и тд
		if self.stats[weapon] < statistic:
			self.stats[weapon] = statistic
			self.inventory_rarities[weapon] = rarity

	def armor_protection(self):  # определяет общий процент защиты от брони
		"""
		Возвращает текущий процент защиты от брони
		:return: int
		"""
		p1 = self.stats['boots']
		p2 = self.stats['trousers']
		p3 = self.stats['breastplate']
		p4 = self.stats['helmet']
		return sum([p1, p2, p3, p4])

	def sword_damage(self):
		"""
		Возвращает текущий урон от меча
		:return: int
		"""
		return self.stats['sword']

	def drop_weapon(self, diff):
		"""
		Функция проверяет сложность побежденного монстра и если сложность босс - то дает в инвентарь игроку случайный
		легендарный дроп иначе - с 30% шансом вызывает функцию для получения любого дропа (даже хуже имеющегося)
		:param diff: Str - сложность убитого монстра
		:return: None
		"""
		if diff == 'boss':  # если игрок убивает босса тоь дропается лег шмотка
			rarity = 'legendary'
			weapon = random.choices(self.weapon, weights=[8, 9, 9, 10, 9], k=1)[0]
			statistic = random.randint(self.weapons[weapon][self.rarities.index(rarity)][0],
			                           self.weapons[weapon][self.rarities.index(rarity)][1])
			if self.stats[weapon] < statistic:
				self.stats[weapon] = statistic
				self.inventory_rarities[weapon] = rarity
			if random.choices([True, False], weights=[1, 2], k=1)[0] and player.score < 5000:
				player.healing += 30
		else:
			a = random.choices([True, False], weights=[2, 1], k=1)[0]  # определяется выпадет ли дроп
			if a:
				item.weapon_stats()  # выбор характеристик дропа

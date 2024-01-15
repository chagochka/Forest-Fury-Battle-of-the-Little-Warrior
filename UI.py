import pygame

class UI:
	def __init__(self, window, font, player):
		self.window = window
		self.font = font
		self.player = player

	def items_draw(self):
		y = 64  # вывод снаряжения
		for item in self.player.inventory.values():
			if item:
				self.window.blit(item.image, (self.window.get_width() - 64, y - 64))
				self.window.blit(self.font.render(str(item.stat), True, 'white'), (1280 - 80, y - 24))
			y += 64

	def write_stats(self, monsters):
		"""
		Выводит на экран игры все надписи (хп героя, хп монстра, кд, хил, результат)
		:return: None
		"""

		# Отрисовка полоски здоровья игрока
		pygame.draw.rect(self.window, '#222222', (10, 10, 250, 20))
		pygame.draw.rect(self.window, 'red', (10, 10, self.player.health / 2, 20))
		pygame.draw.rect(self.window, '#111111', (10, 10, 250, 20), 3)

		# Отрисовка опыта
		text_surf = self.font.render(str(self.player.score), False, '#EEEEEE')
		text_rect = text_surf.get_rect(bottomright=(1260, 700))
		pygame.draw.rect(self.window, '#222222', text_rect.inflate(20, 20))
		pygame.draw.rect(self.window, '#222222', text_rect.inflate(20, 20), 3)
		self.window.blit(text_surf, text_rect)

		# Отрисовка общей защиты
		defens = self.font.render(str(sum([i.stat if i else 0 for i in list(self.player.inventory.values())[1:]])), False, '#EEEEEE')
		icon = pygame.image.load('images/armor.gif')
		self.window.blit(icon, (10, 40))
		self.window.blit(defens, (50, 45))

		# Отрисовка полоски здоровья моба
		pygame.draw.rect(self.window, '#222222', (10, 690, monsters.max_hp, 20))
		pygame.draw.rect(self.window, (0, 150, 100), (10, 690, monsters.hp, 20))
		pygame.draw.rect(self.window, '#111111', (10, 690, monsters.max_hp, 20), 3)

	def inventory_draw(self):
		"""
		Рисует ячейки инвентаря и их содержимое
		:return: None
		"""
		inventory_cell = pygame.image.load('images/inventory.gif')
		potion_inventory = pygame.image.load('images/potion_in_inventory.gif')

		self.window.blit(inventory_cell, (self.window.get_width() // 2 - 96, self.window.get_height() - 64))
		self.window.blit(inventory_cell, (self.window.get_width() // 2 - 32, self.window.get_height() - 64))
		self.window.blit(inventory_cell, (self.window.get_width() // 2 + 32, self.window.get_height() - 64))
		if self.player.items_inventory[0]:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 - 96, self.window.get_height() - 64))
			self.window.blit(self.font.render(str(self.player.items_inventory[0]), True, (200, 200, 200)),
			            (self.window.get_width() // 2 - 96 + 48, self.window.get_height() - 64 + 32))
		if self.player.items_inventory[1]:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 - 32, self.window.get_height() - 64))
			self.window.blit(self.font.render(str(self.player.items_inventory[1]), True, (200, 200, 200)),
			            (self.window.get_width() // 2 - 32 + 48, self.window.get_height() - 64 + 32))
		if self.player.items_inventory[2]:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 + 32, self.window.get_height() - 64))
			self.window.blit(self.font.render(str(self.player.items_inventory[2]), True, (200, 200, 200)),
			            (self.window.get_width() // 2 + 32 + 48, self.window.get_height() - 64 + 32))

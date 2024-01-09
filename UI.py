import pygame

class UI:
	def __init__(self, window, font, player, monster):
		self.window = window
		self.font = font
		self.player = player
		self.monster = monster

	def items_draw(self, values):
		y = 64  # вывод снаряжения
		for item in self.player.inventory.values():
			if item:
				self.window.blit(item.image, (self.window.get_width() - 64, y - 64))
				self.window.blit(self.font.render(str(item.stat), True, 'white'), (1280 - 80, y - 24))
			y += 64

	def write_stats(self, player, monster):
		"""
		Выводит на экран игры все надписи (хп героя, хп монстра, кд, хил, результат)
		:return: None
		"""
		health = self.font.render('Player: ' + (str(self.player.health).split('.')[0] + 'hp' if self.player.health > 0 else 'Dead'),
		                          False, (0, 0, 0), (0, 150, 50))
		self.window.blit(health, (0, 0))

		heat = self.font.render('Ready to heat: ' + str(self.player.timer <= 0), False, (0, 0, 0), (200, 100, 100))
		self.window.blit(heat, (0, 33))

		score = self.font.render('Score: ' + str(self.player.score), False, (0, 0, 0), (200, 200, 0))
		self.window.blit(score, (580, 0))

		monster_hp = self.font.render('Monster: ' + (str(self.monsters.hp) + 'hp' if self.monsters.hp > 0 else 'Dead'),
		                              False, (0, 0, 0), (0, 150, 100))
		self.window.blit(monster_hp, (0, 685))

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
		if player.items_inventory[1]:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 - 32, self.window.get_height() - 64))
			self.window.blit(self.font.render(str(self.player.items_inventory[1]), True, (200, 200, 200)),
			            (self.window.get_width() // 2 - 32 + 48, self.window.get_height() - 64 + 32))
		if player.items_inventory[2]:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 + 32, self.window.get_height() - 64))
			self.window.blit(self.font.render(str(self.player.items_inventory[2]), True, (200, 200, 200)),
			            (self.window.get_width() // 2 + 32 + 48, self.window.get_height() - 64 + 32))


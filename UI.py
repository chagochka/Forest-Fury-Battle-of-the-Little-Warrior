import pygame


class UI:
	def __init__(self, window, font, player):
		self.window = window
		self.font = font
		self.player = player

	def items_draw(self):
		y = 64  # вывод снаряжения
		for item in list(self.player.inventory.values())[:-1]:
			if item.image:
				self.window.blit(item.image, (self.window.get_width() - 64, y - 64))
				self.window.blit(self.font.render(str(item.stat), True, 'white'), (1280 - 80, y - 24))
			y += 64

	def write_stats(self, monsters):
		"""
		Выводит на экран игры все надписи (хп героя, хп монстра, кд, хил, результат)
		:return: None
		"""

		# Отрисовка полоски здоровья игрока
		pygame.draw.rect(self.window, '#222222', (10, 10, self.player.max_health / 2, 20))
		pygame.draw.rect(self.window, 'red', (10, 10, self.player.health / 2, 20))
		pygame.draw.rect(self.window, '#111111', (10, 10, self.player.max_health / 2, 20), 3)

		# Отрисовка опыта
		text_surf = self.font.render(str(self.player.score), False, '#EEEEEE')
		text_rect = text_surf.get_rect(bottomright=(1260, 700))
		pygame.draw.rect(self.window, '#222222', text_rect.inflate(20, 20))
		pygame.draw.rect(self.window, '#222222', text_rect.inflate(20, 20), 3)
		self.window.blit(text_surf, text_rect)

		# Отрисовка общей защиты
		defens = self.font.render(str(sum([i.stat if i else 0 for i in list(self.player.inventory.values())[1:-1]])),
		                          False, '#EEEEEE')
		icon = pygame.image.load('images/armor.gif')
		self.window.blit(icon, (10, 40))
		self.window.blit(defens, (50, 45))

		boss_names = {  # имена боссов
			'boss': 'DEMON',
			'boss_eye': 'Ghost Eye'
		}

		# Отрисовка полоски здоровья моба

		font = pygame.font.Font('font/joystix.ttf', 30)
		if monsters.diff == 'boss':
			pygame.draw.rect(self.window, '#222222', (
				(self.window.get_width() / 2) - monsters.max_hp / 2, 10, monsters.max_hp, 20))
			pygame.draw.rect(self.window, (0, 150, 100), (
				(self.window.get_width() / 2) - monsters.hp / 2, 10, monsters.hp, 20))
			pygame.draw.rect(self.window, '#111111', (
				(self.window.get_width() / 2) - monsters.max_hp / 2, 10, monsters.max_hp, 20), 3)
			boss_text = font.render(boss_names[monsters.diff], False, 'red')
			self.window.blit(boss_text, (self.window.get_width() / 2 - boss_text.get_rect()[2] / 2, 40))

		elif monsters.diff == 'boss_eye':
			for i in range(monsters.max_hp // 500):
				pygame.draw.rect(self.window, '#222222', (  # серый
					(self.window.get_width() / 2) - monsters.max_hp / 2 // (monsters.max_hp // 500), 10 + i * 25,
					monsters.max_hp // (monsters.max_hp // 500), 20))

				pygame.draw.rect(self.window, (0, 150, 100), (  # зеленый
					(self.window.get_width() / 2) - monsters.hp / 2 // (monsters.max_hp // 500), 10 + i * 25,
					monsters.hp // (monsters.max_hp // 500), 20))

				pygame.draw.rect(self.window, '#111111', (  # черный
					(self.window.get_width() / 2) - monsters.max_hp / 2 // (monsters.max_hp // 500), 10 + i * 25,
					monsters.max_hp // (monsters.max_hp // 500), 20), 3)

			boss_text = font.render(boss_names[monsters.diff], False, 'red')
			self.window.blit(boss_text, (self.window.get_width() / 2 - boss_text.get_rect()[2] / 2, 40))

		else:
			pygame.draw.rect(self.window, '#222222', (
				(monsters.x + 64) - monsters.max_hp / 2 - 64, monsters.y - 30 - 64,
				monsters.max_hp,
				15))
			pygame.draw.rect(self.window, (0, 150, 100), (
				(monsters.x + 64) - monsters.hp / 2 - 64, monsters.y - 30 - 64, monsters.hp,
				15))
			pygame.draw.rect(self.window, '#111111', (
				(monsters.x + 64) - monsters.max_hp / 2 - 64, monsters.y - 30 - 64,
				monsters.max_hp,
				15), 3)

	def inventory_draw(self):
		"""
		Рисует ячейки инвентаря и их содержимое
		:return: None
		"""
		inventory_cell = pygame.image.load('images/inventory.gif')
		potion_inventory = pygame.image.load('images/potion_in_inventory.gif')
		rarity_colors = {
			'uncommon': 'gray',
			'mythical': 'purple',
			'legendary': 'yellow'
		}

		x1 = -128
		for i in range(3):
			if len(self.player.inventory['potion']) >= i + 1 and self.player.inventory['potion'][i]:
				pygame.draw.rect(
					self.window, rarity_colors[self.player.inventory['potion'][i].rarity],
					(self.window.get_width() // 2 + x1, self.window.get_height() - 64, 64, 64))
			self.window.blit(inventory_cell, (self.window.get_width() // 2 + x1, self.window.get_height() - 64))
			x1 += 64

		x2 = -128
		for bot in self.player.inventory['potion']:
			self.window.blit(potion_inventory, (self.window.get_width() // 2 + x2, self.window.get_height() - 64))
			stat = self.font.render(str(bot.stat), True, (200, 200, 200))
			self.window.blit(stat, (
				self.window.get_width() // 2 + x2 + (32 - stat.get_width() / 2), self.window.get_height() - 64 + 32))
			x2 += 64

	def set_cursor(self):
		self.window.blit(pygame.image.load('images/dwarven_gauntlet.gif'), pygame.mouse.get_pos())
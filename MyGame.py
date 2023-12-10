import random

import pygame
from pygame import transform

from item import Weapon


class Monster:
	"""
	Класс монстра
	"""

	def __init__(self):
		self.difficulty = ['low', 'medium', 'high', 'boss']
		self.monster_statistics = {
			'low': [20, (100, 150), 0.7],  # атака, хп монстра
			'medium': [50, (150, 200), 0.5],
			'high': [75, (200, 250), 0.3],
			'boss': [100, (250, 500), 0.3]
		}
		self.timer = 0
		self.scores = {
			'low': 50,
			'medium': 100,
			'high': 150,
			'boss': 200
		}

		while True:
			self.x = random.randint(0, 1160)
			self.y = random.randint(0, 610)
			if (self.x, self.y) != (5, 5):
				break

		if player.score <= 2000:
			self.diff = random.choices(self.difficulty, weights=[4, 3, 2, 1], k=1)[0]
		else:
			self.diff = 'boss'
		self.atk = self.monster_statistics[self.diff][0]
		self.hp = random.randint(self.monster_statistics[self.diff][1][0], self.monster_statistics[self.diff][1][-1])
		self.speed = self.monster_statistics[self.diff][-1]
		self.right = True

	def is_life(self):
		"""
		Проверка живой ли монстр, если нет то выпадает дроп
		:return: bool
		"""
		if self.hp <= 0:
			rar = random.choices(list(Weapon.damages.keys()), weights=[0.4, 0.3, 0.2, 0.1] if self.diff != 'boss' else [0, 0, 0, 1])
			items.append((Weapon(pygame.image.load(f'images/{rar[0]}_sword.gif'), rar[0], 'sword'),
			              (self.x, self.y), cycle))
			if player.score <= 2000:
				player.health += 50
			player.score += self.scores[self.diff]
			return False
		return True

	def monster_move(self):
		"""
		Движение монстра по карте (автоматически)
		:return: None
		"""
		if self.hp > 0:
			if player.x != int(self.x):
				if player.x > self.x:
					self.x += self.speed
					self.right = True
				else:
					self.x -= self.speed
					self.right = False
			if player.y != int(self.y):
				if player.y > self.y:
					self.y += self.speed
				else:
					self.y -= self.speed

	def attack(self):
		"""
		 Атака по игроку (автоматически) + кд
		 :return None
		"""
		if player.attack_range() and self.hp > 0 >= self.timer:
			player.damage_taken(self.atk)
			self.timer = 500


class Player:
	"""
	Класс игрока
	"""

	def __init__(self):
		self.health = 500
		self.attack = 200
		self.x = 580
		self.y = 305
		self.timer = 0
		self.score = 0
		self.healing = 500
		self.right = True
		self.inventory = {
			'sword': '',
			'boots': '',
			'trousers': '',
			'breastplate': '',
			'helmet': ''
		}

	def damage_taken(self, damage):
		"""
		Функция отнимает здоровье персонажа (броня блокирует процент урона максимум блокировки урона - 60%)
		:param damage: int
		:return: None
		"""
		self.health -= damage / 100 * (100)  # получение урона

	def damage_given(self):  # Нанесение урона мобу
		"""
		Отнимает здоровье у монстра (начальный урон + дополнительный урон от меча)
		:return: None
		"""
		if self.attack_range():
			if monsters.hp > 0 >= player.timer and self.health >= 0:
				monsters.hp -= self.attack
				monsters.is_life()
				player.timer = 300

	def attack_range(self):  # радиус атаки
		"""
		Возвращает True/False в зависимости от того насколько близко монстр находится к игроку (до 128 пикселей - True)
		:return: bool
		"""
		return -128 <= self.x - monsters.x <= 128 and -128 <= self.y - monsters.y <= 128

	def move_left(self):  # Движение игрока по карте
		"""
		Перемещает персонажа по оси Х влево
		:return: None
		"""
		if self.x - 1 >= 0 and self.health > 0:
			self.x -= 1
			self.right = False

	def move_right(self):  # Движение игрока по карте
		"""
		Перемещает персонажа по оси Х вправо
		:return: None
		"""
		if self.x + 1 <= 1160 and self.health > 0:
			self.x += 1
			self.right = True

	def move_down(self):  # Движение игрока по карте
		"""
		Перемещает персонажа по оси У вниз
		:return: None
		"""
		if self.y + 1 <= 610 and self.health > 0:
			self.y += 1

	def move_up(self):  # Движение игрока по карте
		"""
		Перемещает персонажа по оси У вверх
		:return: None
		"""
		if self.health > 0:
			if self.y - 1 >= 0:
				self.y -= 1


# item = Items()
player = Player()
monsters = Monster()

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('fight!')

player_model_right = pygame.image.load('images/ninja.gif')
player_model_left = transform.flip(player_model_right, True, False)  # герой смотрящий влево

monster_textures = {
	'low': pygame.image.load('images/slither.gif'),
	'medium': pygame.image.load('images/spider.gif'),
	'high': pygame.image.load('images/knight.gif'),
	'boss': pygame.image.load('images/boss.gif')
}

monster_model_right = monster_textures[monsters.diff]
monster_model_left = transform.flip(monster_model_right, True, False)  # монстр смотрящий влево
background = pygame.image.load('images/background.jpg')
menu = pygame.image.load('images/game_menu.jpg')

boots = {'common': 'images/common_boots.gif', 'uncommon': 'images/uncommon_boots.gif',
         'rare': 'images/rare_boots.gif', 'mythical': 'images/mythical_boots.gif',
         'legendary': 'images/legendary_boots.gif'}
trousers = {'common': 'images/common_trousers.gif', 'uncommon': 'images/uncommon_trousers.gif',
            'rare': 'images/rare_trousers.gif', 'mythical': 'images/mythical_trousers.gif', 'legendary':
	            'images/legendary_trousers.gif'}
breastplate = {'common': 'images/common_breastplate.gif', 'uncommon': 'images/uncommon_breastplate.gif',
               'rare': 'images/rare_breastplate.gif', 'mythical': 'images/mythical_breastplate.gif',
               'legendary': 'images/legendary_breastplate.gif'}
helmet = {'common': 'images/common_helmet.gif', 'uncommon': 'images/uncommon_helmet.gif',
          'rare': 'images/rare_helmet.gif', 'mythical': 'images/mythical_helmet.gif',
          'legendary': 'images/legendary_helmet.gif'}
swords = {'common': 'images/common_sword.gif', 'uncommon': 'images/uncommon_sword.gif',
          'rare': 'images/rare_sword.gif', 'mythical': 'images/mythical_sword.gif',
          'legendary': 'images/legendary_sword.gif'}

inGame = False
items = []
run = True
cycle = 0
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()

	if inGame:

		if key[pygame.K_d] and player.x < 1160:  # движение героя
			player.move_right()
		if key[pygame.K_s] and player.y < 610:
			player.move_down()
		if key[pygame.K_a] and player.x >= 0:
			player.move_left()
		if key[pygame.K_w] and player.y >= 0:
			player.move_up()
		if key[pygame.K_e]:
			player.damage_given()
		if key[pygame.K_t]:
			print(monsters.timer)

		monsters.monster_move()
		monsters.attack()
		monsters.timer -= 1
		player.timer -= 1

		if monsters.hp <= 0 and monsters.timer <= 0:
			del monsters
			monsters = Monster()
			monster = monster_textures[monsters.diff]

		if key[pygame.K_m]:
			print('Cords= ' + str((player.x, player.y)), str((monsters.x, monsters.y)))
			print('Hp= ' + str(player.health), str(monsters.hp))
			print('monster info:', monsters.diff)

		# if key[pygame.K_i] and player.timer <= 0:
		# 	print(item.inventory_rarities, item.stats)

		if key[pygame.K_ESCAPE]:
			inGame = False

		if key[pygame.K_h]:
			if player.healing > 0 and player.health > 0:
				player.health += 1
				player.healing -= 1

		window.blit(background, (0, 0))  # фон, монстр, игрок
		window.blit(monster_model_right if monsters.right else monster_model_left, (monsters.x, monsters.y))
		window.blit(player_model_right if player.right else player_model_left, (player.x, player.y))
		# загружаем модельку игрока и монстра смотрящую в ту сторону куда направлено движение (право лево)

		y = 0
		for item in player.inventory.values():
			if item:
				window.blit(item.image, (1192, y))
			y += 64

		Font = pygame.font.SysFont('timesnewroman', 30)  # отображает на экране хп и тд
		health = Font.render('Player: ' + (str(player.health).split('.')[0] + 'hp' if player.health > 0 else 'Dead'),
		                     False, (0, 0, 0), (0, 150, 50))
		window.blit(health, (0, 0))

		heat = Font.render('Ready to heat: ' + str(player.timer <= 0), False, (0, 0, 0), (200, 100, 100))
		window.blit(heat, (0, 33))

		heal_point = Font.render('Heal: ' + str(player.healing), False, (0, 0, 0), (0, 150, 100))
		window.blit(heal_point, (0, 66))

		score = Font.render('Score: ' + str(player.score), False, (0, 0, 0), (200, 200, 0))
		window.blit(score, (580, 0))

		monster_hp = Font.render('Monster: ' + (str(monsters.hp) + 'hp' if monsters.hp > 0 else 'Dead'),
		                         False, (0, 0, 0), (0, 150, 100))
		window.blit(monster_hp, (0, 685))

		for dropped_item, pos, drop_cycle in items:
			dropped_item.drop(window, pos)
			if cycle - drop_cycle == 1000:
				items.pop(items.index((dropped_item, pos, drop_cycle)))
			if (player.x - pos[0] <= 50 or pos[0] - player.x <= 50) and (player.y - pos[1] <= 50 or pos[
				1] - player.y <= 50) and (not player.inventory[
				dropped_item.type] or dropped_item.damage > player.inventory[dropped_item.type].damage):
				player.inventory[dropped_item.type] = dropped_item
				items.pop(items.index((dropped_item, pos, drop_cycle)))

	else:
		window.blit(menu, (0, 0))  # меню игры, кнопки и тд

		if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
			300 >= pygame.mouse.get_pos()[1] >= 240:
			inGame = True
		if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
			480 >= pygame.mouse.get_pos()[1] >= 400:
			break

	cycle += 1
	pygame.display.update()

pygame.quit()

import csv
import os

import pygame

from SkillTree import SkillTree
from UI import UI
from item import *


def load_image(name):
	"""
    Функция загрузки изображения из файла.
    :param name: Имя файла
    :return: изображение
    """
	filename = os.path.join('images', name)
	try:
		image = pygame.image.load(filename)
	except pygame.error as error:
		print('Не могу загрузить изображение:', name)
		raise SystemExit(error)
	return image


class Monster(pygame.sprite.Sprite):
	"""
    Класс монстра
    """

	def __init__(self, speed=False, boss_type=None):
		super().__init__(group_sprites)
		self.difficulty = ['low', 'medium', 'high', 'boss']
		self.monster_statistics = {
			'low': [20, (100, 150), 0.7, 64],  # атака, хп монстра
			'medium': [50, (150, 200), 0.5, 64],
			'high': [75, (200, 250), 0.3, 64],
			'boss': [100, (250, 500), 0.3, 64],
			'boss_eye': [200, (2499, 2500), 0.25, 64]  # надо переделать под дальнюю атаку
		}
		self.timer = 0
		self.scores = {
			'low': 50,
			'medium': 100,
			'high': 150,
			'boss': 200,
			'boss_eye': 500

		}
		self.monster_textures = {
			'low': 'slither.gif',
			'medium': 'spider.gif',
			'high': 'knight.gif',
			'boss': 'boss.gif',
			'boss_eye': 'boss_eye.gif'
		}

		self.x = random.randint(0, 1160)
		self.y = random.randint(0, 610)

		if boss_type is None:  # супер боссы
			self.diff = random.choices(self.difficulty, weights=[4, 3, 2, 1], k=1)[0]
		else:
			self.diff = boss_type

		self.image = load_image(self.monster_textures[self.diff])
		self.images = [load_image(self.monster_textures[self.diff]), pygame.transform.flip(self.image, True, False)]
		self.rect = pygame.Rect(self.x - 64, self.y - 64, 64, 64)

		self.atk = self.monster_statistics[self.diff][0]
		self.hp = random.randint(self.monster_statistics[self.diff][1][0], self.monster_statistics[self.diff][1][1])
		self.max_hp = self.hp
		if speed:
			self.speed = 0
		else:
			self.speed = self.monster_statistics[self.diff][-2]
		self.right = True
		self.attack_range = self.monster_statistics[self.diff][3]
		self.texture = []

	def is_life(self):
		"""
		Проверка живой ли монстр, если нет то выпадает дроп
		:return: bool
		"""
		if self.hp <= 0:
			types = [Weapon, Armor]
			weights = [1, 3]
			if len(player.inventory['potion']) < 3:
				types = [Weapon, Armor, HealingBottle]
				weights.append(2)

			item_type = random.choices(types, weights=weights)[0]
			rar = random.choices(Item.rarities, weights=[5, 4, 3, 2, 1])[0]

			if self.diff == 'boss':
				rar = 'legendary'
			if item_type == Weapon:
				items.append((
					Weapon(pygame.image.load(f'images/{rar}_sword.gif'), rar, 'sword'),
					(self.x, self.y), cycle))
			elif item_type == HealingBottle:
				rar = random.choices(HealingBottle.rarities, weights=[3, 2, 1])[0]
				items.append((
					HealingBottle(pygame.image.load('images/potion.gif'), rar, 'potion'),
					(self.x, self.y), cycle))
			else:
				armor_type = random.choice(['boots', 'trousers', 'helmet', 'breastplate'])

				items.append((
					Armor(pygame.image.load(f'images/{rar}_{armor_type}.gif'), rar, armor_type),
					(self.x, self.y), cycle))
			player.score += self.scores[self.diff]
			tree.point(player.score)
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
		self.rect = pygame.Rect(self.x - 64, self.y - 64, 64, 64)

	def attack(self):
		"""
        Атака по игроку (автоматически) + кд
        :return None
        """
		if (player.attack_range(self.attack_range) or pygame.sprite.collide_mask(self, player)) \
			and self.hp > 0 >= self.timer and not player.immortality:
			player.damage_taken(self.atk)
			self.timer = 500

	def update(self):
		if self.right:
			self.image = self.images[0]
		else:
			self.image = self.images[1]
		if not pygame.sprite.collide_mask(self, player):
			self.monster_move()


class GlobalBoss(Monster):
	def __init__(self):
		super().__init__(boss_type='boss_eye')
		self.rect = pygame.Rect(self.x - 128, self.y - 128, 256, 256)


class Fireball(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__(group_sprites)
		self.x = monsters.x
		self.y = monsters.y
		self.image = load_image('fireball.gif')
		self.rect = pygame.Rect(self.x - 24, self.y - 24, 48, 48)
		self.mask = pygame.mask.from_surface(self.image)

		if player.x > self.x:
			self.vector_x = (player.x - self.x) / 100
		elif player.x < self.x:
			self.vector_x = (player.x - self.x) / 100
		else:
			self.vector_x = 0

		if player.y > self.y:
			self.vector_y = (player.y - self.y) / 100
		elif player.y < self.y:
			self.vector_y = (player.y - self.y) / 100
		else:
			self.vector_y = 0
		self.vector = (self.vector_x, self.vector_y)
		print(self.vector)

	def update(self):
		self.x += self.vector[0]
		self.y += self.vector[1]
		self.rect = self.rect.move(self.vector_x, self.vector_y)
		if pygame.sprite.collide_mask(self, player):
			player.health -= 50
			self.kill()
		if self.x > 2000 or self.y > 2000 or self.x < 0 or self.y < 0:
			self.kill()


class Player(pygame.sprite.Sprite):
	"""
    Класс игрока
    """

	def __init__(self):
		super().__init__(group_sprites)
		self.health = 500
		self.max_health = 500
		self.attack = 50
		self.x = 580
		self.y = 305
		self.timer = 0
		self.score = 0
		self.right = True
		self.immortality = False
		self.global_bosses = 0
		self.inventory = {
			'sword': Item('', '', 'empty'),
			'helmet': Item('', '', 'empty'),
			'breastplate': Item('', '', 'empty'),
			'trousers': Item('', '', 'empty'),
			'boots': Item('', '', 'empty'),
			'potion': []
		}
		self.level = 0

		self.image = load_image('ninja.gif')
		self.images = [load_image('ninja.gif'), pygame.transform.flip(self.image, True, False)]
		self.rect = pygame.Rect(self.x - 64, self.y - 64, 64, 64)
		self.mask = pygame.mask.from_surface(self.image)

	def damage_taken(self, damage):
		"""
		    Функция отнимает здоровье персонажа (броня блокирует процент урона максимум блокировки урона - 60% + пасивки)
		    :param damage: int
		    :return: None
		    """
		if not self.immortality:
			if tree.spell["Я есть грунт"]:
				self.health -= damage / 100 * (  # ?
					100 - (sum([armor.stat for armor in list(self.inventory.values())[1:-1]]) + 5))
			elif tree.spell["Я терпила"] and self.health < 200:
				self.health -= damage / 100 * (  # ?
					100 - (sum([armor.stat for armor in list(self.inventory.values())[1:-1]]) + 15))
			else:
				self.health -= damage / 100 * (  # ?
					100 - (sum([armor.stat for armor in list(self.inventory.values())[1:-1]])))
			if tree.spell["Просвящённый"]:
				monsters.hp -= damage * 0.5
				self.health += damage * 0.2
			if tree.spell["Сила майнкрфта"]:
				monsters.hp -= damage * 0.3

	def damage_given(self):  # Нанесение урона мобу
		"""
		Отнимает здоровье у монстра (начальный урон + дополнительный урон от меча + умения)
		:return: None
		"""
		if monsters.hp > 0 >= player.timer and self.health >= 0:
			if self.attack_range():
				if not self.immortality:
					coof2 = 0
					coof1 = 1
					if tree.spell["Вдохновляющий стяг"]:
						coof1 = 1.1
					elif tree.spell["Светик-Сто-Смертник"]:
						coof2 = 50
					monsters.hp -= coof1 * (coof2 + self.attack + self.inventory['sword'].stat)
				else:
					monsters.hp -= 500
				if monsters.hp < monsters.max_hp // 10 and tree.spell["Лечь костями"]:
					monsters.hp -= monsters.hp
				monsters.is_life()
				if tree.spell["КДАБР"]:
					player.timer = 220
				else:
					player.timer = 300
				pygame.mixer.music.load(random.choice(hits))
			else:
				pygame.mixer.music.load(random.choice(misses))
			pygame.mixer.music.play(0)

	def health_max_more(self):
		"""
        Ограничивает здоровье максимальным
        :return: None
        """
		if self.health > self.max_health:
			if tree.spell["Абаддон"]:
				monsters.hp -= self.health - self.max_health
			self.health = self.max_health

	def attack_range(self, attack_range=128):  # радиус атаки
		"""
        Возвращает True/False в зависимости от того насколько близко монстр находится к игроку (до 128 пикселей - True)
        :return: bool
        """
		if tree.spell["Дуновение ветерка"]:  # Ослобляет игрока (не баг а фича)
			attack_range = 140
		return (-attack_range <= self.x - monsters.x <= attack_range and
		        -attack_range <= self.y - monsters.y <= attack_range)

	def move_left(self):  # Движение игрока по карте
		"""
        Перемещает персонажа по оси Х влево
        :return: None
        """
		coof = 1
		if self.x - coof >= 0 and self.health > 0:
			self.x -= coof
			if tree.spell["Сапоги Гермеса"]:
				self.health += 0.015
			self.rect = self.rect.move(-coof, 0)
			self.right = False

	def move_right(self):  # Движение игрока по карте
		"""
        Перемещает персонажа по оси Х вправо
        :return: None
        """
		coof = 1
		if self.x + coof <= 1160 and self.health > 0:
			self.x += coof
			if tree.spell["Сапоги Гермеса"]:
				self.health += 0.015
			self.rect = self.rect.move(coof, 0)
			self.right = True

	def move_down(self):  # Движение игрока по карте
		"""
        Перемещает персонажа по оси У вниз
        :return: None
        """
		coof = 1
		if self.y + coof <= 610 and self.health > 0:
			self.y += coof
			if tree.spell["Сапоги Гермеса"]:
				self.health += 0.015
			self.rect = self.rect.move(0, coof)

	def move_up(self):  # Движение игрока по карте
		"""
        Перемещает персонажа по оси У вверх
        :return: None
        """
		coof = 1
		if self.health > 0:
			if self.y - coof >= 0:
				self.y -= coof
				if tree.spell["Сапоги Гермеса"]:
					self.health += 0.015
				self.rect = self.rect.move(0, -coof)

	def find_item(self, x, y):
		"""
        Возвращает True/False в зависимости от того находится ли персонаж рядом с зельем
        (расстояние, для того чтобы подобрать предмет)
        :param x: int
        :param y: int
        :return: bool
        """
		return -64 <= self.x - x <= 64 and -64 <= self.y - y <= 64

	def update(self):
		if self.right:
			self.image = self.images[0]
		else:
			self.image = self.images[1]


def game_over():
	picture = pygame.image.load('images/game_over.jpg')
	window.blit(picture, (0, 0))


width, height = 1280, 720

group_sprites = pygame.sprite.Group()

monsters = Monster()
player = Player()

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('fight!')

font = pygame.font.Font('font/joystix.ttf', 18)
buttons_dict = {
	'a': pygame.K_a,
	'b': pygame.K_b,
	'c': pygame.K_c,
	'd': pygame.K_d,
	'e': pygame.K_e,
	'f': pygame.K_f,
	'g': pygame.K_g,
	'h': pygame.K_h,
	'i': pygame.K_i,
	'j': pygame.K_j,
	'k': pygame.K_k,
	'l': pygame.K_l,
	'm': pygame.K_m,
	'n': pygame.K_n,
	'o': pygame.K_o,
	'p': pygame.K_p,
	'q': pygame.K_q,
	'r': pygame.K_r,
	's': pygame.K_s,
	't': pygame.K_t,
	'u': pygame.K_u,
	'v': pygame.K_v,
	'w': pygame.K_w,
	'x': pygame.K_x,
	'y': pygame.K_y,
	'z': pygame.K_z,
	'backspace': pygame.K_BACKSPACE,
	'tab': pygame.K_TAB,
	'clear': pygame.K_CLEAR,
	'return': pygame.K_RETURN,
	'pause': pygame.K_PAUSE,
	'escape': pygame.K_ESCAPE,
	'space': pygame.K_SPACE,
	'exclaim': pygame.K_EXCLAIM,
	'quotedbl': pygame.K_QUOTEDBL,
	'hash': pygame.K_HASH,
	'dollar': pygame.K_DOLLAR,
	'ampersand': pygame.K_AMPERSAND,
	'quote': pygame.K_QUOTE,
	'leftparen': pygame.K_LEFTPAREN,
	'rightparen': pygame.K_RIGHTPAREN,
	'asterisk': pygame.K_ASTERISK,
	'plus': pygame.K_PLUS,
	'comma': pygame.K_COMMA,
	'minus': pygame.K_MINUS,
	'period': pygame.K_PERIOD,
	'slash': pygame.K_SLASH,
	'num0': pygame.K_0,
	'num1': pygame.K_1,
	'num2': pygame.K_2,
	'num3': pygame.K_3,
	'num4': pygame.K_4,
	'num5': pygame.K_5,
	'num6': pygame.K_6,
	'num7': pygame.K_7,
	'num8': pygame.K_8,
	'num9': pygame.K_9,
	'colon': pygame.K_COLON,
	'semicolon': pygame.K_SEMICOLON,
	'less': pygame.K_LESS,
	'equals': pygame.K_EQUALS,
	'greater': pygame.K_GREATER,
	'question': pygame.K_QUESTION,
	'at': pygame.K_AT,
	'leftbracket': pygame.K_LEFTBRACKET,
	'backslash': pygame.K_BACKSLASH,
	'rightbracket': pygame.K_RIGHTBRACKET,
	'caret': pygame.K_CARET,
	'underscore': pygame.K_UNDERSCORE,
	'backquote': pygame.K_BACKQUOTE,
	'delete': pygame.K_DELETE,
	'keypad0': pygame.K_KP0,
	'keypad1': pygame.K_KP1,
	'keypad2': pygame.K_KP2,
	'keypad3': pygame.K_KP3,
	'keypad4': pygame.K_KP4,
	'keypad5': pygame.K_KP5,
	'keypad6': pygame.K_KP6,
	'keypad7': pygame.K_KP7,
	'keypad8': pygame.K_KP8,
	'keypad9': pygame.K_KP9,
	'keypad_period': pygame.K_KP_PERIOD,
	'keypad_divide': pygame.K_KP_DIVIDE,
	'keypad_multiply': pygame.K_KP_MULTIPLY,
	'keypad_minus': pygame.K_KP_MINUS,
	'keypad_plus': pygame.K_KP_PLUS,
	'keypad_enter': pygame.K_KP_ENTER,
	'keypad_equals': pygame.K_KP_EQUALS,
	'up': pygame.K_UP,
	'down': pygame.K_DOWN,
	'right': pygame.K_RIGHT,
	'left': pygame.K_LEFT,
	'insert': pygame.K_INSERT,
	'home': pygame.K_HOME,
	'end': pygame.K_END,
	'pageup': pygame.K_PAGEUP,
	'pagedown': pygame.K_PAGEDOWN,
	'f1': pygame.K_F1,
	'f2': pygame.K_F2,
	'f3': pygame.K_F3,
	'f4': pygame.K_F4,
	'f5': pygame.K_F5,
	'f6': pygame.K_F6,
	'f7': pygame.K_F7,
	'f8': pygame.K_F8,
	'f9': pygame.K_F9,
	'f10': pygame.K_F10,
	'f11': pygame.K_F11,
	'f12': pygame.K_F12,
	'f13': pygame.K_F13,
	'f14': pygame.K_F14,
	'f15': pygame.K_F15,
	'numlock': pygame.K_NUMLOCK,
	'capslock': pygame.K_CAPSLOCK,
	'scrolllock': pygame.K_SCROLLOCK,
	'rshift': pygame.K_RSHIFT,
	'lshift': pygame.K_LSHIFT,
	'rctrl': pygame.K_RCTRL,
	'lctrl': pygame.K_LCTRL,
	'ralt': pygame.K_RALT,
	'lalt': pygame.K_LALT,
	'rmeta': pygame.K_RMETA,
	'lmeta': pygame.K_LMETA,
	'lsuper': pygame.K_LSUPER,
	'rsuper': pygame.K_RSUPER,
	'mode': pygame.K_MODE,
	'help': pygame.K_HELP,
	'print': pygame.K_PRINT,
	'sysreq': pygame.K_SYSREQ,
	'break': pygame.K_BREAK
}

menu_theme = pygame.mixer.Sound('sounds/Mind Flayer Theme.wav')
fight_theme = pygame.mixer.Sound('sounds/Nine Blades.wav')
skills_theme = pygame.mixer.Sound('sounds/Who Are You.wav')

hits = ['sounds/hit1.wav', 'sounds/hit2.wav', 'sounds/hit3.wav']
misses = ['sounds/miss1.wav', 'sounds/miss2.wav', 'sounds/miss3.wav']

background = pygame.image.load('images/background.jpg')
menu = pygame.image.load('images/game_menu.jpg')
potion_model = pygame.image.load('images/potion.gif')
potion_inventory = pygame.image.load('images/potion_in_inventory.gif')
inventory_cell = pygame.image.load('images/inventory.gif')
ui = UI(window, font, player)

stop = "menu"
inGame = False
in_settings = False
items = []
run = True
cycle = 0

tree = SkillTree(player, window, font)

while run:
	with open('binds.csv', encoding="utf8") as csvfile:
		binds = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
		binds = dict(zip(binds[0], binds[1]))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if inGame and event.type == pygame.KEYDOWN and event.key == buttons_dict[binds['use_potion']]:
			if player.inventory['potion']:
				player.inventory['potion'].pop().heal(player)

	key = pygame.key.get_pressed()
	mouse = pygame.mouse.get_pressed(5)
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(False)
	window.blit(background, (0, 0))  # фон

	if inGame:
		skills_theme.stop()
		menu_theme.stop()
		fight_theme.set_volume(0.01)
		fight_theme.play()
		if key[buttons_dict[binds['move_right']]] and player.x < 1160:  # движение героя
			player.move_right()
		if key[buttons_dict[binds['move_back']]] and player.y < 610:
			player.move_down()
		if key[buttons_dict[binds['move_left']]] and player.x >= 64:
			player.move_left()
		if key[buttons_dict[binds['move_forward']]] and player.y >= 64:
			player.move_up()
		if key[pygame.K_e] or mouse[0]:
			player.damage_given()
		if key[pygame.K_j]:
			player.immortality = not player.immortality

		monsters.attack()
		monsters.timer -= 1
		player.timer -= 1

		if monsters.hp <= 0 and monsters.timer <= 0:
			monsters.kill()
			if player.score // 5000 != player.global_bosses:
				monsters = GlobalBoss()
				background = load_image('boss_room.jpg')
				player.global_bosses += 1
			elif tree.spell["Звездочёт"] and random.randint(1, 5) == 4:
				monsters = Monster(speed=True)
			else:
				monsters = Monster()
				background = load_image('background.jpg')

		if key[pygame.K_m]:
			print('Cords= ' + str((player.x, player.y)), str((monsters.x, monsters.y)))
			print('Hp= ' + str(player.health), str(monsters.hp))
			print('monster info:', monsters.diff, monsters.timer)

		if key[pygame.K_0]:
			player.score += 30

		if key[pygame.K_o]:
			tree.points += 1

		if key[pygame.K_ESCAPE]:
			stop = "menu"
			inGame = False

		if key[pygame.K_p]:
			stop = "level"
			inGame = False

		for dropped_item, pos, drop_cycle in items:

			dropped_item.blit_image(window, pos)

			if cycle - drop_cycle == 1000:
				items.pop(items.index((dropped_item, pos, drop_cycle)))  # удаление предметов с земли

			if isinstance(dropped_item, HealingBottle):
				if player.find_item(pos[0], pos[1]) and len(player.inventory['potion']) < 3:
					player.inventory['potion'].append(dropped_item)
					items.pop(items.index((dropped_item, pos, drop_cycle)))
			else:
				if (key[pygame.K_f]) or (player.find_item(pos[0], pos[1]) and (not player.inventory[
					dropped_item.type] or dropped_item.stat > player.inventory[dropped_item.type].stat)):
					player.inventory[dropped_item.type] = dropped_item
					items.pop(items.index((dropped_item, pos, drop_cycle)))

		ui.items_draw()
		ui.inventory_draw()
		ui.write_stats(monsters)

		if cycle % 1000 == 0 and type(monsters) is GlobalBoss:
			Fireball()

		group_sprites.draw(window)
		group_sprites.update()
		player.update()

		if player.health <= 0:
			game_over()

		cycle += 1
		clock.tick(300)
	elif in_settings:
		fight_theme.stop()
		skills_theme.stop()
		menu_theme.play()

		cords = ui.open_settings_window()

		for cord in cords:
			if cord[2] >= pygame.mouse.get_pos()[0] >= cord[0] and cord[3] >= pygame.mouse.get_pos()[1] >= cord[1]:
				pygame.draw.rect(window, '#FFCB30', (cord[0], cord[1], 40, 50))
				for let_char, pg_char in buttons_dict.items():
					if key[pg_char]:
						ui.change_bind(cord[-1], let_char)

		if key[pygame.K_ESCAPE]:
			in_settings = False

		ui.set_cursor()
	else:
		if stop == "menu":
			fight_theme.stop()
			skills_theme.stop()
			menu_theme.play()
			window.blit(menu, (0, 0))  # меню игры, кнопки и тд

			if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
				300 >= pygame.mouse.get_pos()[1] >= 240:
				inGame = True
			if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
				390 >= pygame.mouse.get_pos()[1] >= 320:
				in_settings = True
			if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
				480 >= pygame.mouse.get_pos()[1] >= 400:
				break
		elif stop == "level":
			fight_theme.stop()
			menu_theme.stop()
			skills_theme.play()
			skilltree = pygame.image.load('images/skilltree.png')
			window.blit(skilltree, (0, 0))

			if pygame.mouse.get_pressed()[0] and 810 >= pygame.mouse.get_pos()[0] >= 670 and \
				450 >= pygame.mouse.get_pos()[1] >= 400:
				inGame = True
			tree.cursor_location((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]),
			                     pygame.mouse.get_pressed()[0])
		ui.set_cursor()
	pygame.display.update()

pygame.quit()

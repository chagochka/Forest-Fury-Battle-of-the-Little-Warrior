import random

import pygame
from pygame import transform

from item import *
from UI import UI
from SkillTree import SkillTree
import os


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
            'boss_eye': [250, (2499, 2500), 0.25, 64]  # надо переделать под дальнюю атаку
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
            item_type = random.choices([Weapon, Armor], weights=[1, 4])[0]
            rar = random.choices(Item.rarities, weights=[5, 4, 3, 2, 1])[0]
            if self.diff == 'boss':
                rar = 'legendary'
            if item_type == Weapon:
                items.append((Weapon(pygame.image.load(f'images/{rar}_sword.gif'), rar, 'sword'),
                              (self.x, self.y), cycle))
            else:
                armor_type = random.choice(['boots', 'trousers', 'helmet', 'breastplate'])

                items.append((Armor(pygame.image.load(f'images/{rar}_{armor_type}.gif'), rar, armor_type),
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
        if (player.attack_range(self.attack_range) or pygame.sprite.collide_mask(self, player))\
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


class Player(pygame.sprite.Sprite):
    """
    Класс игрока
    """

    def __init__(self):
        super().__init__(group_sprites)
        self.health = 500
        self.max_health = 1000
        self.attack = 50
        self.x = 580
        self.y = 305
        self.timer = 0
        self.score = 0
        self.right = True
        self.immortality = False
        self.global_bosses = 0
        self.inventory = {
            'sword': '',
            'helmet': '',
            'breastplate': '',
            'trousers': '',
            'boots': ''
        }
        self.items_inventory = [0, 0, 0]
        self.level = 0

        self.image = load_image('ninja.gif')
        self.images = [load_image('ninja.gif'), pygame.transform.flip(self.image, True, False)]
        self.rect = pygame.Rect(self.x - 64, self.y - 64, 64, 64)
        self.mask = pygame.mask.from_surface(self.image)

    def damage_taken(self, damage):
        """
        Функция отнимает здоровье персонажа (броня блокирует процент урона максимум блокировки урона - 60%)
        :param damage: int
        :return: None
        """
        if not self.immortality:
            if tree.spell["Я есть грунт"]:
                self.health -= damage / 100 * (  # ?
                        100 - (sum([armor.stat for armor in list(self.inventory.values())[1:] if armor]) + 5))
            elif tree.spell["Я терпила"] and self.health < 200:
                self.health -= damage / 100 * (  # ?
                        100 - (sum([armor.stat for armor in list(self.inventory.values())[1:] if armor]) + 15))
            else:
                self.health -= damage / 100 * (  # ?
                        100 - (sum([armor.stat for armor in list(self.inventory.values())[1:] if armor])))
            if tree.spell["Просвящённый"]:
                monsters.hp -= damage * 0.5
                self.health += damage * 0.2
            if tree.spell["Сила майнкрфта"]:
                monsters.hp -= damage * 0.3
            # получение урона

    def damage_given(self):  # Нанесение урона мобу
        """
        Отнимает здоровье у монстра (начальный урон + дополнительный урон от меча + умения)
        :return: None
        """
        if self.attack_range():
            if monsters.hp > 0 >= player.timer and self.health >= 0:  # ?
                if not self.immortality:
                    if tree.spell["Вдохновляющий стяг"]:
                        damage = (self.attack + 50 +
                                        (self.inventory['sword'].stat if self.inventory['sword'] else 0)) * 1.1
                    elif tree.spell["Светик-Сто-Смертник"]:
                        damage = (self.attack + 50 +
                                        (self.inventory['sword'].stat if self.inventory['sword'] else 0))
                    else:
                        damage = self.attack + (self.inventory['sword'].stat if self.inventory['sword'] else 0)
                    if tree.spell["Кровосися"]:
                        self.health += damage * 0.05
                        self.health_max_more()
                    if tree.spell["Тёмное братство"] and random.randint(1, 5) == 4:
                        monsters.hp -= damage * 1.5
                    else:
                        monsters.hp -= damage
                else:
                    monsters.hp -= 500
                monsters.is_life()
                if tree.spell["КДАБР"]:
                    player.timer = 220
                else:
                    player.timer = 300

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
        if tree.spell["Дуновение ветерка"]:
            attack_range = 140
        return (-attack_range <= self.x - monsters.x <= attack_range and
                -attack_range <= self.y - monsters.y <= attack_range)

    def move_left(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси Х влево
        :return: None
        """
        coof = 1
        if tree.spell["Сапоги Гермеса"]:
            coof = 1.5
        if self.x - coof >= 0 and self.health > 0:
            self.x -= coof
            if tree.spell["Лечь костями"]:
                self.health += 0.01
            self.rect = self.rect.move(-coof, 0)
            self.right = False

    def move_right(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси Х вправо
        :return: None
        """
        coof = 1
        if tree.spell["Сапоги Гермеса"]:
            coof = 1.5
        if self.x + coof <= 1160 and self.health > 0:
            self.x += coof
            if tree.spell["Лечь костями"]:
                self.health += 0.01
            self.rect = self.rect.move(coof, 0)
            self.right = True

    def move_down(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси У вниз
        :return: None
        """
        coof = 1
        if tree.spell["Сапоги Гермеса"]:
            coof = 1.5
        if self.y + coof <= 610 and self.health > 0:
            self.y += coof
            if tree.spell["Лечь костями"]:
                self.health += 0.01
            self.rect = self.rect.move(0, coof)

    def move_up(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси У вверх
        :return: None
        """
        coof = 1
        if tree.spell["Сапоги Гермеса"]:
            coof = 1.5
        if self.health > 0:
            if self.y - coof >= 0:
                self.y -= coof
                if tree.spell["Лечь костями"]:
                    self.health += 0.01
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
bottle = HealingBottle(pygame.image.load('images/potion.gif'), 'rare', 'potion')

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('fight!')

font = pygame.font.Font('font/joystix.ttf', 18)

background = pygame.image.load('images/background.jpg')
menu = pygame.image.load('images/game_menu.jpg')
potion_model = pygame.image.load('images/potion.gif')
potion_inventory = pygame.image.load('images/potion_in_inventory.gif')
inventory_cell = pygame.image.load('images/inventory.gif')
ui = UI(window, font, player)

stop = "menu"
inGame = False
items = []
run = True
cycle = 0

tree = SkillTree(player, window, font)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed(5)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    window.blit(background, (0, 0))  # фон

    if inGame:
        if key[pygame.K_d] and player.x < 1160:  # движение героя
            player.move_right()
        if key[pygame.K_s] and player.y < 610:
            player.move_down()
        if key[pygame.K_a] and player.x >= 0:
            player.move_left()
        if key[pygame.K_w] and player.y >= 0:
            player.move_up()
        if key[pygame.K_e] or mouse[0]:
            player.damage_given()
        if key[pygame.K_t]:
            print(monsters.timer)
        if key[pygame.K_j]:
            player.immortality = not player.immortality

        monsters.attack()
        monsters.timer -= 1
        player.timer -= 1
        bottle.timer -= 1

        if monsters.hp <= 0 and monsters.timer <= 0:
            bottle.drop(monsters.x, monsters.y)  # нужно сделать геттер
            print('kill')
            monsters.kill()
            if player.score >= 5000 and player.global_bosses == 0:
                monsters = Monster(boss_type='boss_eye')
                player.global_bosses += 1
            elif tree.spell["Звездочёт"] and random.randint(1, 5) == 4:
                monsters = Monster(speed=True)
            else:
                monsters = Monster()

        if key[pygame.K_m]:
            print('Cords= ' + str((player.x, player.y)), str((monsters.x, monsters.y)))
            print('Hp= ' + str(player.health), str(monsters.hp))
            print('monster info:', monsters.diff)

        if key[pygame.K_i]:
            print(player.items_inventory)
            # print(items[0])

        if key[pygame.K_o]:
            tree.points += 1

        if key[pygame.K_ESCAPE]:
            stop = "menu"
            inGame = False

        if key[pygame.K_p]:
            stop = "level"
            inGame = False

        if key[pygame.K_f]:  # на f поднимать предмет (64 пикселя)
            try:
                if player.find_item(*bottle.cords):
                    player.find_heal(bottle.heal)
                    bottle = HealingBottle()  # пересоздаем ботл чтобы нельзя было собрать больше одного раза
                    print('drop')
            except TypeError:  # Пока что не тестил без try. Просто чтобы не крашило
                pass
            except AttributeError:
                pass

        if key[pygame.K_1]:
            if bottle.can_use() and player.items_inventory[0] and player.health > 0:
                player.health += 50
                player.items_inventory[0] -= 1
                bottle.use_heal()

        if key[pygame.K_2]:
            if bottle.can_use() and player.items_inventory[1] and player.health > 0:
                player.health += 75
                player.items_inventory[1] -= 1
                bottle.use_heal()

        if key[pygame.K_3]:
            if bottle.can_use() and player.items_inventory[2] and player.health > 0:
                player.health += 100
                player.items_inventory[2] -= 1
                bottle.use_heal()

        for dropped_item, pos, drop_cycle in items:

            dropped_item.blit_image(window, pos)

            if cycle - drop_cycle == 1000:
                items.pop(items.index((dropped_item, pos, drop_cycle)))  # удаление предметов с земли

            if (key[pygame.K_f]) or (
                    abs(player.x - pos[0]) <= 50 and abs(player.y - pos[1] <= 50) and (not player.inventory[
                dropped_item.type] or dropped_item.stat > player.inventory[dropped_item.type].stat)):
                if player.find_item(pos[0], pos[1]):
                    player.inventory[dropped_item.type] = dropped_item
                    items.pop(items.index((dropped_item, pos, drop_cycle)))  # ?

        ui.items_draw()
        ui.inventory_draw()
        ui.write_stats(monsters)

        group_sprites.draw(window)
        group_sprites.update()
        player.update()

        if player.health <= 0:
            game_over()

        clock.tick(300)
    else:
        if stop == "menu":
            window.blit(menu, (0, 0))  # меню игры, кнопки и тд

            if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
                    300 >= pygame.mouse.get_pos()[1] >= 240:
                inGame = True
            if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
                    480 >= pygame.mouse.get_pos()[1] >= 400:
                break
        elif stop == "level":
            skilltree = pygame.image.load('images/skilltree.png')
            window.blit(skilltree, (0, 0))

            if pygame.mouse.get_pressed()[0] and 810 >= pygame.mouse.get_pos()[0] >= 670 and \
                    450 >= pygame.mouse.get_pos()[1] >= 400:
                inGame = True
            tree.cursor_location((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]),
                                 pygame.mouse.get_pressed()[0])
        ui.set_cursor()
    cycle += 1
    pygame.display.update()

pygame.quit()

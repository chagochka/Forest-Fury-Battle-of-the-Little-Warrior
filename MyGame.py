import random
import pygame
from pygame import transform


class Monster:
    """Класс монстра"""

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
            item.drop_weapon(self.diff, monsters.get_cords())
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

    def get_cords(self):
        return self.x, self.y


class ItemsStats:
    """Класс предмет"""

    def __init__(self):
        self.rarities = ['common', 'uncommon', 'rare', 'mythical', 'legendary']  # редкости снаряжения
        self.weapon = ['sword', 'boots', 'trousers', 'breastplate', 'helmet']  # типы снаряжения (accessory deleted)
        self.weapons = {
            'sword': [(100, 120), (120, 150), (150, 170), (170, 200), (200, 250)],  # статистика снаряжения по редкости
            'boots': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
            'trousers': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
            'breastplate': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
            'helmet': [(3, 5), (5, 8), (8, 10), (10, 13), (13, 15)],
        }
        self.dropped_rarity = ''
        self.dropped_weapon = ''
        self.dropped_statistic = 0
        self.cords = tuple()

    def weapon_stats(self, monster_cords):
        """
        Функция рандомно выбирает тип редкость и статистику предмета
        :monster_cords: tuple
        :return: None
        """
        self.dropped_rarity = random.choices(self.rarities, weights=[5, 4, 3, 2, 1], k=1)[0]  # редкость дропа
        self.dropped_weapon = random.choices(self.weapon, weights=[8, 9, 9, 10, 9], k=1)[0]  # тип оружия/брони
        self.dropped_statistic = random.randint(
            self.weapons[self.dropped_weapon][self.rarities.index(self.dropped_rarity)][0],
            self.weapons[self.dropped_weapon][self.rarities.index(self.dropped_rarity)][1])
        # статистика урон защита и тд
        self.cords = monster_cords

    def drop_weapon(self, diff, monster_cords):
        """
        Функция проверяет сложность побежденного монстра и если сложность босс - то дает в инвентарь игроку случайный
        легендарный дроп иначе - с 30% шансом вызывает функцию для получения любого дропа (даже хуже имеющегося)
        :param monster_cords: tuple
        :param diff: Str - сложность убитого монстра
        :return: None
        """
        if diff == 'boss':  # если игрок убивает босса тоь дропается лег шмотка
            self.dropped_rarity = 'legendary'
            self.dropped_weapon = random.choices(self.weapon, weights=[8, 9, 9, 10, 9], k=1)[0]
            self.dropped_statistic = random.randint(
                self.weapons[self.dropped_weapon][self.rarities.index(self.dropped_rarity)][0],
                self.weapons[self.dropped_weapon][self.rarities.index(self.dropped_rarity)][1])
            self.cords = monster_cords
        else:
            if random.choices([True, False], weights=[2, 1], k=1)[0]:  # определяется выпадет ли дроп
                self.weapon_stats(monsters.get_cords())  # выбор характеристик дропа


class Player:
    """Класс игрока"""

    def __init__(self):
        self.health = 500
        self.attack = 50
        self.x = width // 2 - 64
        self.y = height // 2 - 64
        self.timer = 0
        self.score = 0
        self.right = True
        self.items_inventory = [0, 0, 0]
        self.stats = {
            'sword': 0,
            'boots': 0,
            'trousers': 0,
            'breastplate': 0,
            'helmet': 0
        }
        self.inventory_rarities = {
            'sword': '',
            'boots': '',
            'trousers': '',
            'breastplate': '',
            'helmet': ''
        }
        self.heals = {
            50: 0,
            75: 1,
            100: 2
        }

    def find_item(self, x, y):
        """
        Возвращает True/False в зависимости от того находится ли персонаж рядом с зельем
        (расстояние, для того чтобы подобрать предмет)
        :param x: int
        :param y: int
        :return: bool
        """
        return -64 <= self.x - x <= 64 and -64 <= self.y - y <= 64

    def damage_taken(self, damage):
        """
        Функция отнимает здоровье персонажа (броня блокирует процент урона максимум блокировки урона - 60%)
        :param damage: int
        :return: None
        """
        self.health -= damage / 100 * (100 - self.armor_protection())  # получение урона

    def armor_protection(self):  # определяет общий процент защиты от брони
        """
        Возвращает текущий процент защиты от брони
        :return: int
        """
        print(self.stats)
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

    def damage_given(self):  # Нанесение урона мобу
        """
        Отнимает здоровье у монстра (начальный урон + дополнительный урон от меча)
        :return: None
        """
        if self.attack_range():
            if monsters.hp > 0 >= player.timer and self.health >= 0:
                monsters.hp -= self.attack + self.sword_damage()
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
        if self.x + 1 <= width - 128 and self.health > 0:
            self.x += 1
            self.right = True

    def move_down(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси У вниз
        :return: None
        """
        if self.y + 1 <= height - 128 and self.health > 0:
            self.y += 1

    def move_up(self):  # Движение игрока по карте
        """
        Перемещает персонажа по оси У вверх
        :return: None
        """
        if self.health > 0:
            if self.y - 1 >= 0:
                self.y -= 1

    def find_heal(self, heal_value):
        self.items_inventory[self.heals[heal_value]] += 1


class HealingBottle:
    """Класс зелья здоровья"""

    def __init__(self):
        self.timer = 0
        self.created = False

    def is_created(self):
        """
        Возвращает True/False в зависимости от того выпало ли зелье
        :return: bool
        """
        return self.created

    def drop(self, x, y):
        """
        Устанавливает координаты и рандомно выбирает количество лечения
        :param x: int
        :param y: int
        :return: None
        """
        self.created = True
        self.cords = (x, y)
        self.heal = random.choices([50, 75, 100], weights=[5, 3, 1], k=1)[0]

    def use_heal(self):
        """
        Устанавливает таймер на использование
        :return: None
        """
        self.timer = 300

    def can_use(self):
        """
        Возвращает True/False в зависимости от того можно ли использовать зелье
        :return:
        """
        return self.timer <= 0


def set_items():
    """
    Показывает модельки предметов в верхнем левом углу экрана
    :return: None
    """
    font = pygame.font.SysFont(None, 40)

    if player.inventory_rarities['helmet']:  # показ снаряжения в правом верхнем углу экрана
        window.blit(pygame.image.load(helmet[player.inventory_rarities['helmet']]), (width - 64, 0))
        window.blit(font.render(str(player.stats['helmet']), True, 'white'), (width - 64, 64 - 24))

    if player.inventory_rarities['breastplate']:
        window.blit(pygame.image.load(breastplate[player.inventory_rarities['breastplate']]), (width - 64, 64))
        window.blit(font.render(str(player.stats['breastplate']), True, 'white'), (width - 64, 128 - 24))

    if player.inventory_rarities['trousers']:
        window.blit(pygame.image.load(trousers[player.inventory_rarities['trousers']]), (width - 64, 128))
        window.blit(font.render(str(player.stats['trousers']), True, 'white'), (width - 64, 192 - 24))

    if player.inventory_rarities['boots']:
        window.blit(pygame.image.load(boots[player.inventory_rarities['boots']]), (width - 64, 192))
        window.blit(font.render(str(player.stats['boots']), True, 'white'), (width - 64, 256 - 24))

    if player.inventory_rarities['sword']:
        window.blit(pygame.image.load(sword[player.inventory_rarities['sword']]), (width - 64, 256))
        window.blit(font.render(str(player.stats['sword']), True, 'white'), (width - 64, 320 - 24))


def set_text():
    """
    Выводит на экран игры все надписи (хп героя, хп монстра, кд, хил, результат)
    :return: None
    """
    font = pygame.font.SysFont('timesnewroman', 30)  # отображает на экране хп и тд
    health = font.render('Player: ' + (str(player.health).split('.')[0] + 'hp' if player.health > 0 else 'Dead'),
                         False, (0, 0, 0), (0, 150, 50))
    window.blit(health, (0, 0))

    heat = font.render('Ready to heat: ' + str(player.timer <= 0), False, (0, 0, 0), (200, 100, 100))
    window.blit(heat, (0, 33))

    score = font.render('Score: ' + str(player.score), False, (0, 0, 0), (200, 200, 0))
    window.blit(score, (580, 0))

    monster_hp = font.render('Monster: ' + (str(monsters.hp) + 'hp' if monsters.hp > 0 else 'Dead'),
                             False, (0, 0, 0), (0, 150, 100))
    window.blit(monster_hp, (0, 685))


def every_update():
    """
    Отнимает таймеры и совершает перемещение и атаку монстра
    :return: None
    """
    global monsters, player
    monsters.monster_move()
    monsters.attack()
    monsters.timer -= 1
    player.timer -= 1
    bottle.timer -= 1


def monster_dead():
    """
    Пересоздает монстра в случайном месте и загружает его модельку
    :return: None
    """
    global monsters, monster_model_right, monster_model_left, monster_textures
    if monsters.hp <= 0 and monsters.timer <= 0:
        bottle.drop(*monsters.get_cords())
        del monsters
        monsters = Monster()
        monster_model_right = monster_textures[monsters.diff]
        monster_model_left = transform.flip(monster_model_right, True, False)  # монстр смотрящий влево


def draw_models():
    """
    Загружает модельки героя, монстра, и лежащего предмета
    :return: None
    """
    global monster_model_right, monster_model_left, player_model_right, player_model_left
    try:
        if item:
            window.blit(pygame.image.load(type_items[item.dropped_weapon][item.dropped_rarity]), item.cords)
        if bottle.is_created():
            window.blit(potion_model, bottle.cords)
    except KeyError:  # загружаем модельку выпавшего оружия на землю (не подобранное)
        pass  # не тестил без try

    window.blit(monster_model_right if monsters.right else monster_model_left, (monsters.x, monsters.y))
    window.blit(player_model_right if player.right else player_model_left, (player.x, player.y))
    # загружаем модельку игрока и монстра смотрящую в ту сторону куда направлено движение (право лево)


def inventory_draw():
    """
    Рисует ячейки инвентаря и их содержимое
    :return: None
    """
    font = pygame.font.SysFont(None, 40)

    window.blit(inventory_cell, (width // 2 - 96, height - 64))
    window.blit(inventory_cell, (width // 2 - 32, height - 64))
    window.blit(inventory_cell, (width // 2 + 32, height - 64))
    if player.items_inventory[0]:
        window.blit(potion_inventory, (width // 2 - 96, height - 64))
        window.blit(font.render(str(player.items_inventory[0]), True, (200, 200, 200)),
                    (width // 2 - 96 + 48, height - 64 + 32))
    if player.items_inventory[1]:
        window.blit(potion_inventory, (width // 2 - 32, height - 64))
        window.blit(font.render(str(player.items_inventory[1]), True, (200, 200, 200)),
                    (width // 2 - 32 + 48, height - 64 + 32))
    if player.items_inventory[2]:
        window.blit(potion_inventory, (width // 2 + 32, height - 64))
        window.blit(font.render(str(player.items_inventory[2]), True, (200, 200, 200)),
                    (width // 2 + 32 + 48, height - 64 + 32))


width, height = 1280, 720

item = ItemsStats()
player = Player()
monsters = Monster()
bottle = HealingBottle()

pygame.init()
window = pygame.display.set_mode((width, height))
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
potion_model = pygame.image.load('images/potion.gif')
potion_inventory = pygame.image.load('images/potion_in_inventory.gif')
inventory_cell = pygame.image.load('images/inventory.gif')

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
sword = {'common': 'images/common_sword.gif', 'uncommon': 'images/uncommon_sword.gif',
         'rare': 'images/rare_sword.gif', 'mythical': 'images/mythical_sword.gif',
         'legendary': 'images/legendary_sword.gif'}
type_items = {'sword': sword, 'helmet': helmet, 'breastplate': breastplate, 'trousers': trousers, 'boots': boots}

inGame = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if inGame:
        if key[pygame.K_d]:  # движение героя
            player.move_right()

        if key[pygame.K_s]:
            player.move_down()

        if key[pygame.K_a]:
            player.move_left()

        if key[pygame.K_w]:
            player.move_up()

        if key[pygame.K_e]:
            player.damage_given()

        if key[pygame.K_t]:
            print(monsters.timer)

        if key[pygame.K_f]:  # на f поднимать предмет (64 пикселя)
            try:
                if player.find_item(*item.cords):  # проверка найдено ли снаряжение
                    if player.stats[item.dropped_weapon] < item.dropped_statistic:
                        player.stats[item.dropped_weapon] = item.dropped_statistic
                        player.inventory_rarities[item.dropped_weapon] = item.dropped_rarity
                        item = ItemsStats()
                if player.find_item(*bottle.cords):
                    player.find_heal(bottle.heal)
                    bottle = HealingBottle()  # пересоздаем ботл чтобы нельзя было собрать больше одного раза
            except TypeError:  # Пока что не тестил без try. Просто чтобы не крашило
                pass
            except AttributeError:
                pass

        if key[pygame.K_m]:  # выводит в консоль координаты, хп и сложность монстра
            print('Cords= ' + str((player.x, player.y)), str((monsters.x, monsters.y)))
            print('Hp= ' + str(player.health), str(monsters.hp))
            print('monster info:', monsters.diff)

        if key[pygame.K_i] and player.timer <= 0:  # информация про выпавший предмет в консоль
            print(player.inventory_rarities, player.stats)
            print(item.dropped_statistic, item.dropped_weapon, item.dropped_rarity, item.cords)
            print(player.items_inventory)

        if key[pygame.K_ESCAPE]:  # меню
            inGame = False

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

        window.blit(background, (0, 0))  # фон, монстр, игрок

        monster_dead()  # проверка живой ли монстр и его пересоздание

        draw_models()  # рисует героя, монстра и предметы (на полу)

        set_items()  # устанавливает предметы инвентаря в верхнем правом углу

        set_text()  # устанавливает хп, хп монстра, перезарядку оружия и тд

        every_update()  # делает ход монстра и уменьшает таймеры

        inventory_draw()  # рисует инвентарь

    else:
        window.blit(menu, (0, 0))  # меню игры, кнопки и тд

        if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
                300 >= pygame.mouse.get_pos()[1] >= 240:
            inGame = True
        if pygame.mouse.get_pressed()[0] and 760 >= pygame.mouse.get_pos()[0] >= 510 and \
                480 >= pygame.mouse.get_pos()[1] >= 400:
            break

    pygame.display.update()

pygame.quit()

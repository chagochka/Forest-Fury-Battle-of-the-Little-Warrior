import random
import pygame
from pygame import transform


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
            item.drop_weapon(self.diff, monsters.get_cords())
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

    def get_cords(self):
        return self.x, self.y


class ItemsStats:
    """
    Класс предмет
    """

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
            if random.choices([True, False], weights=[1, 2], k=1)[0] and player.score < 5000:
                player.healing += 30
        else:
            if random.choices([True, False], weights=[2, 1], k=1)[0]:  # определяется выпадет ли дроп
                self.weapon_stats(monsters.get_cords())  # выбор характеристик дропа


class Player:
    """
    Класс игрока
    """
    def __init__(self):
        self.health = 500
        self.attack = 50
        self.x = 580
        self.y = 305
        self.timer = 0
        self.score = 0
        self.healing = 500
        self.right = True
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

    def find_item(self, x, y):
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


def set_items():
    """
    Показывает модельки предметов в верхнем левом углу экрана
    :return: None
    """
    if player.inventory_rarities['helmet']:  # показ снаряжения в правом верхнем углу экрана
        window.blit(pygame.image.load(helmet[player.inventory_rarities['helmet']]), (1192, 0))
    if player.inventory_rarities['breastplate']:
        window.blit(pygame.image.load(breastplate[player.inventory_rarities['breastplate']]), (1192, 64))
    if player.inventory_rarities['trousers']:
        window.blit(pygame.image.load(trousers[player.inventory_rarities['trousers']]), (1192, 128))
    if player.inventory_rarities['boots']:
        window.blit(pygame.image.load(boots[player.inventory_rarities['boots']]), (1192, 192))
    if player.inventory_rarities['sword']:
        window.blit(pygame.image.load(sword[player.inventory_rarities['sword']]), (1192, 256))


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

    heal_point = font.render('Heal: ' + str(player.healing), False, (0, 0, 0), (0, 150, 100))
    window.blit(heal_point, (0, 66))

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


def monster_dead():
    """
    Пересоздает монстра в случайном месте и загружает его модельку
    :return: None
    """
    global monsters, monster_model_right, monster_model_left, monster_textures
    if not monsters.is_life() and monsters.timer <= 0:
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
    except KeyError:  # загружаем модельку выпавшего оружия на землю (не подобранное)
        pass  # не тестил без try

    window.blit(monster_model_right if monsters.right else monster_model_left, (monsters.x, monsters.y))
    window.blit(player_model_right if player.right else player_model_left, (player.x, player.y))
    # загружаем модельку игрока и монстра смотрящую в ту сторону куда направлено движение (право лево)


item = ItemsStats()
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

        if key[pygame.K_f]:  # на f поднимать предмет (64 пикселя)
            try:
                if player.find_item(*item.cords):  # проверка найдено ли снаряжение
                    if player.stats[item.dropped_weapon] < item.dropped_statistic:
                        player.stats[item.dropped_weapon] = item.dropped_statistic
                        player.inventory_rarities[item.dropped_weapon] = item.dropped_rarity
                        item = ItemsStats()
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

        if key[pygame.K_ESCAPE]:  # меню
            inGame = False

        if key[pygame.K_h]:  # хил
            if player.healing > 0 and player.health > 0:
                player.health += 1
                player.healing -= 1

        window.blit(background, (0, 0))  # фон, монстр, игрок

        monster_dead()  # проверка живой ли монстр и его пересоздание

        draw_models()  # рисует героя, монстра и предметы (на полу)

        set_items()  # устанавливает предметы инвентаря в верхнем правом углу

        set_text()  # устанавливает хп, хп монстра, перезарядку оружия и тд

        every_update()  # делает ход монстра и уменьшает таймеры

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

import pygame
from item import *


class SkillTree:
    def __init__(self, player, window, font):
        self.player = player
        self.window = window
        self.font = font
        self.title = ""
        self.description = ["", "", "", ""]
        self.spell = {
            "Сапоги Гермеса": False,  # сделано
            "Светик-Сто-Смертник": False,  # сделано
            "Вдохновляющий стяг": False,  # сделано
            "Дуновение ветерка": False,
            "Тёмное братство": False,
            "Лечь костями": False,
            "Абаддон": False,
            "КДАБР": False,
            "Разбитое сердце": False,
            "Кровосися": False,
            "Геральт с гор": False,
            "Я есть грунт": False,
            "Сила майнкрфта": False,
            "Просвящённый": False,
            "Волчья истерика": False,
            "Удача Дрима": False,
            "Пудж": False,
            "Звездочёт": False,
            "Я терпила": False
        }
        self.points = 0
        self.all_points = 0
        self.error = ''
        self.descriptions = {
            "Сапоги Гермеса": ["За каждый пройденный", 'шаг добовляет', 'мало здоровья', ''],
            "Светик-Сто-Смертник": ["Добавление плоского", 'урона персонажу', '', ''],
            "Вдохновляющий стяг": ["Добавление процентного", 'урона для персонажа', '', ''],
            "Дуновение ветерка": ["Увеличивает радиус", 'атаки', '', ''],
            "Тёмное братство": ["Добавление критичесского", 'урона', '', ''],
            "Лечь костями": ["Добивает врага если", 'у него менее 10 %', '', ''],
            "Абаддон": ["Излишок востанавливаемого", 'наносится врагу', '', ''],
            "КДАБР": ["ускоряет перезарядку", 'атаки', '', ''],
            "Разбитое сердце": ["Увеличивает максимум", 'здоровья в 2 раза', '', ''],
            "Кровосися": ["Добавляет по 5%", 'здоровья от атаки', '', ''],
            "Геральт с гор": ["Позволяет получить", 'чеканную монету', '(нет)', ''],
            "Я есть грунт": ["(ням-ням)", 'Добавляет естественную', 'защиту - 5', ''],
            "Сила майнкрфта": ["Добавляет шипы 1", 'на персонажа', '', ''],
            "Просвящённый": ["Усиляет шипы до 3-го,", 'вампиризм шипам', 'в размере - 10%', ''],
            "Волчья истерика": ["Если здоровья меньше", '5%, увеличивает урон', 'в 2 раза', ''],
            "Удача Дрима": ["Ему не нужна удача", '', '', ''],
            "Пудж": ["Твой злейший враг", '', '', ''],
            "Звездочёт": ["Даёт шанс игроку", 'застанить существо', 'при его спавне', ""],
            "Я терпила": ["Если здоровье меньше", '10% от максимума,', 'увеличивает', 'защиту на 10'],
            "Мечь": ['', '', '', ''],
            "Шлем": ['', '', '', ''],
            "Нагрудник": ['', '', '', ''],
            "Штаны": ['', '', '', ''],
            "Ботинки": ['', '', '', '']
        }
        self.spells = ["Сапоги Гермеса", "Светик-Сто-Смертник", "Вдохновляющий стяг", "Дуновение ветерка",
                       "Тёмное братство", "Лечь костями", "Абаддон", "КДАБР", "Кровосися", "Геральт с гор",
                       "Я есть грунт", "Сила майнкрфта", "Разбитое сердце", "Я терпила", "Просвящённый",
                       "Волчья истерика", "Удача Дрима", "Пудж", "Звездочёт",
                       "Мечь", "Шлем", "Нагрудник", "Штаны", "Ботинки"]

    def point(self, score):
        """
        Даёт очки умений
        :param score: int
        :return: None
        """
        if score > 1000 + self.all_points * 1000:
            self.points += 1
            self.all_points += 1

    def new_text(self):
        """
        Визул для древа навыков
        :return: None
        """
        # вывод названия перкa
        text_surf = self.font.render(str(self.title), False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(65, 310))
        self.window.blit(text_surf, text_rect)

        if self.error:
            text_surf = self.font.render(self.error, False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(460, 370))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
            self.window.blit(text_surf, text_rect)
        # ввывод изучена ли пасивкa
        if self.title != "":
            if self.title in ["Мечь", "Шлем", "Нагрудник", "Штаны", "Ботинки"]:
                text_surf = self.font.render("Не зачарованно", False, (0, 0, 0))
            elif self.spell[self.title]:
                text_surf = self.font.render("Изучено", False, (0, 0, 0))
            else:
                text_surf = self.font.render("Не изучено", False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(70, 270))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
            self.window.blit(text_surf, text_rect)
        # вывод описания пeрка
        for i in range(4):
            text_surf = self.font.render(str(self.description[i]), False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(65, 350 + i * 25))
            self.window.blit(text_surf, text_rect)
        # ввывод очков прокaчки
        text_surf = self.font.render(f"Очки улучшений: {str(self.points)}", False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(460, 320))
        pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
        pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
        self.window.blit(text_surf, text_rect)

    def cursor_location(self, coor, clic):
        """
        Реакция на нажатие кнопок
        :param coor: list
        :param clic: bool
        :return: None
        """
        x, y = coor
        self.new_text()
        self.corup()
        line = open('coords_skill_tree.txt').readlines()
        for i in line:
            x1, y1, x2, y2, num = i.split(".")
            x1, x2, y1, y2, num = int(x1), int(y1), int(x2), int(y2), int(num)
            if x1 < x < x2 and y1 < y < y2 and clic:
                self.title = self.spells[num]
                self.description = self.descriptions[self.spells[num]]
            if 225 < x < 345 and 445 < y < 470 and clic:
                self.contnue()

    def contnue(self):
        """
        Вызывает ошибку (в визуале)
        :return: None
        """
        if self.title in ["Мечь", "Шлем", "Нагрудник", "Штаны", "Ботинки"]:
            self.enchants()
        elif self.title != "":
            if not self.spell[self.title] and self.points >= 1:
                self.error = ""
                self.spell[self.title] = True
                self.points -= 1
                if self.title == "Разбитое сердцe":
                    self.player.max_health = 2500
            elif not self.spell[self.title] and self.points == 0:
                self.error = "Недостаточно ОУ"
        else:
            self.error = "Умение не выбранно"

    def corup(self):
        """
        Визуал для зачарования
        :return: None
        """
        # вывод статистики
        ststic = [f"Убито монстров: {str(self.player.kill)}",
                  f"Весь урона: {str(self.player.all_damage)}",
                  f"Урона монстров: {str(self.player.all_mob_damage)}",
                  f"Общее исцеление: {str(self.player.all_hael)}"]
        for i in range(4):
            text_rect = self.font.render("хочу пицы и спать и балы", False,
                                         (0, 0, 0)).get_rect(bottomleft=(900, 50 + 30 * i))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
            self.window.blit(self.font.render(ststic[i], False, (0, 0, 0)), text_rect)
        # Вывод количества душ
        text_surf = self.font.render(f"Души: {self.player.kill}", False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(1100, 450))
        pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(10, 10))
        pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(20, 20), 3)
        self.window.blit(text_surf, text_rect)
        # Вывод брони и её зачаровние
        armor1 = ["Мечь", "Шлем", "Нагрудник", "Поножи", "Сапоги"]
        armor2 = ['sword', 'helmet', 'breastplate', 'trousers', 'boots']
        for i in range(5):
            # Вывод брони и её зачаровние
            text_surf = self.font.render(armor1[i], False, (0, 0, 0))
            text_rect = self.font.render('Нагрудник', False, (0, 0, 0)).get_rect(bottomleft=(1060, 500 + 50 * i))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(10, 10))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(20, 20), 3)
            self.window.blit(text_surf, text_rect)
            # Вывод зачарований
            text_rect = self.font.render(f"Предмет отсутствует", False,
                                         (0, 0, 0)).get_rect(bottomleft=(750, 500 + 50 * i))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(10, 10))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(20, 20), 3)
            if self.player.inventory[armor2[i]].stat != 0:
                self.window.blit(self.font.render(f"Зачаровать: 5 душ", False, (0, 0, 0)), text_rect)
            else:
                self.window.blit(self.font.render(f"Предмет отсутствует", False, (0, 0, 0)), text_rect)
            # Вывод стат предметов
            text_surf = self.font.render(str(self.player.inventory[armor2[i]].stat), False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(1220, 499 + 50 * i))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(10, 10))
            pygame.draw.rect(self.window, '#aaf0d1', text_rect.inflate(20, 20), 3)
            self.window.blit(text_surf, text_rect)

    def enchants(self):
        """
        Зачарование предметам
        :return: None
        """
        print(True)
        print(self.title)
        items = {"Мечь": 'sword', "Шлем": 'helmet', "Нагрудник": 'breastplate', "Штаны": 'trousers', "Ботинки": 'boots'}
        item = self.player.inventory[items[self.title]]
        if self.title == "Мечь":
            self.player.inventory[items[self.title]] = Weapon(
                pygame.image.load(f'images/{item.rarity}_sword.gif'),
                item.rarity, 'sword', ench=True)
        if self.title != "Мечь":
            self.player.inventory[items[self.title]] = Armor(
                pygame.image.load(f'images/{item.rarity}_{item.type}.gif'),
                item.rarity, item.type, ench=True)


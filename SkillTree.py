import pygame


class SkillTree:
    def __init__(self, player, window, font):
        self.player = player
        self.window = window
        self.font = font
        self.title = ""
        self.description = ["", "", "", ""]
        self.spell = {
            "Сапоги Гермеса": False,
            "Светик-Сто-Смертник": False,
            "Вдохновляющий стяг": False,
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
            "Сапоги Гермеса": ["Увеличивают скорость", 'перемещения персонажа', '', ''],
            "Светик-Сто-Смертник": ["Добавление плоского", 'урона персонажу', '', ''],
            "Вдохновляющий стяг": ["Добавление процентного", 'урона для персонажа', '', ''],
            "Дуновение ветерка": ["Увеличивает радиус", 'атаки', '', ''],
            "Тёмное братство": ["Добавление критичесского", 'урона', '', ''],
            "Лечь костями": ["За каждый пройденный", 'шаг добовляет', 'мало здоровья', ''],
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
            "Я терпила": ["Если здоровье меньше", '10% от максимума,', 'увеличивает', 'защиту на 10']
        }

    def point(self, score):
        if score > 1000 + self.all_points * 1000:
            self.points += 1
            self.all_points += 1

    def new_text(self):
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
            if self.spell[self.title]:
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
        x, y = coor
        self.new_text()
        if 400 < x < 450 and 115 < y < 150 and clic:
            self.title = "Сапоги Гермеса"
            self.description = self.descriptions["Сапоги Гермеса"]

        elif 330 < x < 375 and 70 < y < 115 and clic:
            self.title = "Светик-Сто-Смертник"
            self.description = self.descriptions["Светик-Сто-Смертник"]

        elif 260 < x < 305 and 70 < y < 115 and clic:
            self.title = "Вдохновляющий стяг"
            self.description = self.descriptions["Вдохновляющий стяг"]

        elif 180 < x < 235 and 70 < y < 115 and clic:
            self.title = "Дуновение ветерка"
            self.description = self.descriptions["Дуновение ветерка"]

        elif 115 < x < 160 and 20 < y < 70 and clic:
            self.title = "Тёмное братство"
            self.description = self.descriptions["Тёмное братство"]

        elif 115 < x < 160 and 115 < y < 160 and clic:
            self.title = "Лечь костями"
            self.description = self.descriptions["Лечь костями"]

        elif 40 < x < 90 and 70 < y < 115 and clic:
            self.title = "Абаддон"
            self.description = self.descriptions["Абаддон"]

        elif 330 < x < 375 and 175 < y < 225 and clic:
            self.title = "КДАБР"
            self.description = self.descriptions["КДАБР"]

        elif 250 < x < 300 and 175 < y < 225 and clic:
            self.title = "Кровосися"
            self.description = self.descriptions["Кровосися"]

        elif 175 < x < 225 and 175 < y < 225 and clic:
            self.title = "Геральт с гор"
            self.description = self.descriptions["Геральт с гор"]

        elif 475 < x < 525 and 65 < y < 115 and clic:
            self.title = "Я есть грунт"
            self.description = self.descriptions["Я есть грунт"]

        elif 550 < x < 600 and 65 < y < 115 and clic:
            self.title = "Сила майнкрфта"
            self.description = self.descriptions["Сила майнкрфта"]

        elif 620 < x < 660 and 25 < y < 70 and clic:
            self.title = "Разбитое сердце"
            self.description = self.descriptions["Разбитое сердце"]

        elif 700 < x < 740 and 25 < y < 70 and clic:
            self.title = "Я терпила"
            self.description = self.descriptions["Я терпила"]

        elif 780 < x < 825 and 25 < y < 70 and clic:
            self.title = "Просвящённый"
            self.description = self.descriptions["Просвящённый"]

        elif 480 < x < 525 and 165 < y < 205 and clic:
            self.title = "Волчья истерика"
            self.description = self.descriptions["Волчья истерика"]

        elif 555 < x < 600 and 165 < y < 205 and clic:
            self.title = "Удача Дрима"
            self.description = self.descriptions["Удача Дрима"]

        elif 620 < x < 665 and 115 < y < 160 and clic:
            self.title = "Пудж"
            self.description = self.descriptions["Пудж"]

        elif 685 < x < 735 and 165 < y < 205 and clic:
            self.title = "Звездочёт"
            self.description = self.descriptions["Звездочёт"]

        elif 300 < x < 420 and 280 < y < 310 and clic:
            self.contnue()

    def contnue(self):
        if not self.spell[self.title] and self.points >= 1:
            self.error = ""
            self.spell[self.title] = True
            self.points -= 1
            if self.title == "Разбитое сердцe":
                self.player.max_health = 2500
        elif not self.spell[self.title] and self.points == 0:
            self.error = "Недостаточно ОУ"

import pygame


class SkillTree:
    def __init__(self, player, window, font):
        self.player = player
        self.window = window
        self.font = font
        self.title = ""
        self.description = [
            "",
            "",
            "",
            ""
        ]
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

    def point(self, score):
        if score > 1000 + self.all_points * 1000:
            self.points += 1
            self.all_points += 1

    def new_text(self):
        # вывод названия перка
        text_surf = self.font.render(str(self.title), False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(65, 310))
        self.window.blit(text_surf, text_rect)

        if self.error:
            text_surf = self.font.render(self.error, False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(460, 370))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
            self.window.blit(text_surf, text_rect)
        # ввывод изучена ли пасивка
        if self.title != "":
            text_rect = text_surf.get_rect(bottomleft=(70, 270))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
            pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
            if self.spell[self.title]:
                text_surf = self.font.render("Изучено", False, (0, 0, 0))
                self.window.blit(text_surf, text_rect)
            else:
                # Если не изучен
                text_surf = self.font.render("Не изучено", False, (0, 0, 0))
                self.window.blit(text_surf, text_rect)
        # вывод описания перка
        for i in range(4):
            text_surf = self.font.render(str(self.description[i]), False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(65, 350 + i * 25))
            self.window.blit(text_surf, text_rect)
        # ввывод очков прокачки
        text_surf = self.font.render(f"Очки улучшений: {str(self.points)}", False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(460, 320))
        pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20))
        pygame.draw.rect(self.window, '#f7da9e', text_rect.inflate(20, 20), 3)
        self.window.blit(text_surf, text_rect)

    def cursor_location(self, coor, clic):
        x, y = coor
        self.new_text()
        if 400 < x < 450 and 115 < y < 150 and clic:
            self.boot()

        elif 330 < x < 375 and 70 < y < 115 and clic:
            self.lightning()

        elif 260 < x < 305 and 70 < y < 115 and clic:
            self.banner()

        elif 180 < x < 235 and 70 < y < 115 and clic:
            self.wind()

        elif 115 < x < 160 and 20 < y < 70 and clic:
            self.dark_brotherhood()

        elif 115 < x < 160 and 115 < y < 160 and clic:
            self.lay_down_the_bones()

        elif 40 < x < 90 and 70 < y < 115 and clic:
            self.abaddon()

        elif 330 < x < 375 and 175 < y < 225 and clic:
            self.accelerated_recharge()

        elif 250 < x < 300 and 175 < y < 225 and clic:
            self.vampirism()

        elif 175 < x < 225 and 175 < y < 225 and clic:
            self.the_witcher()

        elif 475 < x < 525 and 65 < y < 115 and clic:
            self.shield()

        elif 550 < x < 600 and 65 < y < 115 and clic:
            self.armor()

        elif 620 < x < 660 and 25 < y < 70 and clic:
            self.broken_heart()

        elif 700 < x < 740 and 25 < y < 70 and clic:
            self.response()

        elif 780 < x < 825 and 25 < y < 70 and clic:
            self.enlightened()

        elif 480 < x < 525 and 165 < y < 205 and clic:
            self.wolf_hysteria()

        elif 555 < x < 600 and 165 < y < 205 and clic:
            self.eye_of_fate()

        elif 620 < x < 665 and 115 < y < 160 and clic:
            self.pudge()

        elif 685 < x < 735 and 165 < y < 205 and clic:
            self.stargazer()

        elif 300 < x < 420 and 280 < y < 310 and clic:
            self.contnue()

    def contnue(self):
        if not self.spell[self.title] and self.points >= 1:
            self.spell[self.title] = True
            self.points -= 1
            if self.title == "Разбитое сердцe":
                self.player.max_health = 2500
        elif not self.spell[self.title] and self.points == 0:
            self.error = "Недостаточно ОУ"

    def boot(self):  # сделано
        """
        Название пассиыного навыка: Сапоги Гермеса
        Увеличивает скорость перемещения персонажа
        :return: None
        """
        self.title = "Сапоги Гермеса"
        self.description = [
            "Увеличивают скорость",
            'перемещения персонажа',
            '',
            ''
        ]

    def lightning(self):  # сделано
        """
        Название пассиыного навыка: Светик-Сто-Смертник
        Добавление плоского урона персонажу
        :return: None
        """
        self.title = "Светик-Сто-Смертник"
        self.description = [
            "Добавление плоского",
            'урона персонажу',
            '',
            ''
        ]

    def banner(self):  # сделано
        """
        Название пассиыного навыка: Вдохновляющий стяг
        Добавление процентного урона персонажу
        :return: None
        """
        self.title = "Вдохновляющий стяг"
        self.description = [
            "Добавление процентного",
            'урона для персонажа',
            '',
            ''
        ]

    def wind(self):  # сделано
        """
        Название пассиыного навыка: Дуновение ветерка
        Увеличивает радиус атаки на 12
          !!!ОСЛОБЛЯЕТ ИГРОКА!!!
        :return: None
        """
        self.title = "Дуновение ветерка"
        self.description = [
            "Увеличивает радиус",
            'атаки',
            '',
            ''
        ]

    def dark_brotherhood(self):  # сделано
        """
        Название пассиыного навыка: Тёмное братство
        Добавление критичесского урона
        :return: None
        """
        self.title = "Тёмное братство"
        self.description = [
            "Добавление критичесского",
            'урона',
            '',
            ''
        ]

    def lay_down_the_bones(self):  # сделано
        """
        Название пассиыного навыка: Лечь костями
        Добавляет регенирацию здоровья
        :return: None
        """
        self.title = "Лечь костями"
        self.description = [
            "За каждый пройденный",
            'пиксель добовляет',
            'мало здоровья',
            ''
        ]

    def abaddon(self):  # сделано
        """
        Название пассиыного навыка: Абаддон
        Излишок востанавливаемого здоровья наносится врагу
        :return: None
        """
        self.title = "Абаддон"
        self.description = [
            "Излишок востанавливаемого",
            'наносится врагу',
            '',
            ''
        ]

    def accelerated_recharge(self):  # сделано
        """
        Название пассиыного навыка: КДАБР
        ускоряет перезарядку атаки
        :return: None
        """
        self.title = "КДАБР"
        self.description = [
            "ускоряет перезарядку",
            'атаки',
            '',
            ''
        ]

    def vampirism(self):  # сделано
        """
        Название пассиыного навыка: Кровосися
        Добовляет по 5% здоровья от атаки
        :return: None
        """
        self.title = "Кровосися"
        self.description = [
            "Добавляет по 5%",
            'здоровья от атаки',
            '',
            ''
        ]

    def the_witcher(self):  # сделано
        """
        Название пассиыного навыка: Геральт с гор
        Позволяет получить ничего
        :return: None
        """
        self.title = "Геральт с гор"
        self.description = [
            "Позволяет получить",
            'чеканную монету',
            '(нет)',
            ''
        ]

    def shield(self):  # сделано
        """
        Название пассиыного навыка: Я есть грунт (ням-ням)
        Добовляет естественную защиту 5
        :return: None
        """
        self.title = "Я есть грунт"
        self.description = [
            "(ням-ням)",
            'Добавляет естественную',
            'защиту 5',
            ''
        ]

    def armor(self):  # сделано
        """
        Название пассиыного навыка: Сила майнкрфта
        Добовляет шипы 1 на персонажа
        :return: None
        """
        self.title = "Сила майнкрфта"
        self.description = [
            "Добавляет шипы 1",
            'на персонажа',
            '',
            ''
        ]

    def broken_heart(self):  # сделано
        """
        Название пассиыного навыка: Разбитое сердце
        Увеличивает максимум здоровья в 2 раза
        :return: None
        """
        self.title = "Разбитое сердце"
        self.description = [
            "Увеличивает максимум",
            'здоровья в 2 раза',
            '',
            ''
        ]

    def response(self):  # сделано
        """
        Название пассиыного навыка: Я не терпила, но терплю
        Если здоровье меньше 10% от максимума увеличивает естественую защиту на 10
        :return: None
        """
        self.title = "Я терпила"
        self.description = [
            "Если здоровье меньше",
            '10% от максимума,',
            'увеличивает',
            'защиту на 10'
        ]

    def enlightened(self):  # сделано
        """
        Название пассиыного навыка: Просвящённый майнкрафтом
        Усиляет шипы 1 до шипы 3 даёт вампиризм шипам 10% от полученого урона
        :return: None
        """
        self.title = "Просвящённый"
        self.description = [
            "Усиляет шипы до 3-го,",
            'вампиризм шипам',
            'в размере - 10%',
            ''
        ]

    def wolf_hysteria(self):
        """
        Название пассиыного навыка: Волчья истерика
        если здоровья меньше 5% увеличивает урон в двое
        :return: None
        """
        self.title = "Волчья истерика"
        self.description = [
            "Если здоровья меньше",
            '5%, увеличивает урон',
            'в 2 раза',
            ''
        ]

    def eye_of_fate(self):  # сделано
        """
        Название пассиыного навыка: Удача Дрима
        Увеличивает шанс выпадения легендарки
        :return: None
        """
        self.title = "Удача Дрима"
        self.description = [
            "Ему не нужна удача",
            '',
            '',
            ''
        ]

    def pudge(self):  # сделано
        """
        Название пассиыного навыка: Пудж
        Увеличивает максимальное здоровье за каждое убийство ценой потери 10% ночального здоровья
        :return: None
        """
        self.title = "Пудж"
        self.description = [
            "Твой злейший враг",
            '',
            '',
            ''
        ]

    def stargazer(self):  # сделано
        """
        Название пассиыного навыка: Звездочёт
        Даёт шанс затанить существо с 10% вероятностью при его спавне до смерти
        :return: None
        """
        self.title = "Звездочёт"
        self.description = [
            "Даёт шанс игроку",
            'застанить существо',
            'при его спавне',
            ''
        ]

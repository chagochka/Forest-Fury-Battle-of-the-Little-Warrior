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

    def new_text(self):
        # вывод названия перка
        text_surf = self.font.render(str(self.title), False, (0, 0, 0))
        text_rect = text_surf.get_rect(bottomleft=(65, 310))
        self.window.blit(text_surf, text_rect)
        # вывод описания перка
        for i in range(4):
            text_surf = self.font.render(str(self.description[i]), False, (0, 0, 0))
            text_rect = text_surf.get_rect(bottomleft=(65, 350 + i * 25))
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

    def boot(self):
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

    def lightning(self):
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

    def banner(self):
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

    def wind(self):
        """
        Название пассиыного навыка: Дуновение ветерка
        Отталкивает врага при атаке
        :return: None
        """
        self.title = "Дуновение ветерка"
        self.description = [
            "Отталкивает врага",
            'при атаке',
            '',
            ''
        ]

    def dark_brotherhood(self):
        """
        Название пассиыного навыка: Тёмное братство
        Если враг умер от одной атаки востанавливает немного здоровья
        :return: None
        """
        self.title = "Тёмное братство"
        self.description = [
            "Если враг умер от",
            'одной атаки,',
            'востанавливает немного',
            'здоровья'
        ]

    def lay_down_the_bones(self):
        """
        Название пассиыного навыка: Лечь костями
        Защищает от смертельной атаки
        :return: None
        """
        self.title = "Лечь костями"
        self.description = [
            "Защищает от",
            'смертельной атаки',
            '',
            ''
        ]

    def abaddon(self):
        """
        Название пассиыного навыка: Абаддон
        после убийства врага следующая атака по игроку не нанесёт урона
        :return: None
        """
        self.title = "Абаддон"
        self.description = [
            "После убийства 2-го врага,",
            'следующая атака по игроку',
            'не нанесёт урона',
            ''
        ]

    def accelerated_recharge(self):
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

    def vampirism(self):
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

    def the_witcher(self):
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

    def shield(self):
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

    def armor(self):
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

    def broken_heart(self):
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

    def response(self):
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

    def enlightened(self):
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

    def eye_of_fate(self):
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

    def pudge(self):
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

    def stargazer(self):
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

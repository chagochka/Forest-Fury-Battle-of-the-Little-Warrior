class SkillTree:
    def cursor_location(coor, clic):
        x, y = coor
        if 400 < x < 450 and 115 < y < 150 and clic:
            print(1)

        elif 330 < x < 375 and 70 < y < 115 and clic:
            print(2)

        elif 260 < x < 305 and 70 < y < 115 and clic:
            print(3)

        elif 180 < x < 235 and 70 < y < 115 and clic:
            print(4)

        elif 115 < x < 160 and 20 < y < 70 and clic:
            print(5)

        elif 115 < x < 160 and 115 < y < 160 and clic:
            print(6)

        elif 40 < x < 90 and 70 < y < 115 and clic:
            print(7)

        elif 330 < x < 375 and 175 < y < 225 and clic:
            print(8)

        elif 250 < x < 300 and 175 < y < 225 and clic:
            print(9)

        elif 175 < x < 225 and 175 < y < 225 and clic:
            print(10)

        elif 475 < x < 525 and 65 < y < 115 and clic:
            print(11)

        elif 550 < x < 600 and 65 < y < 115 and clic:
            print(12)

        elif 620 < x < 660 and 25 < y < 70 and clic:
            print(13)

        elif 700 < x < 740 and 25 < y < 70 and clic:
            print(14)

        elif 780 < x < 825 and 25 < y < 70 and clic:
            print(15)

        elif 480 < x < 525 and 165 < y < 205 and clic:
            print(16)

        elif 555 < x < 600 and 165 < y < 205 and clic:
            print(17)

        elif 620 < x < 665 and 115 < y < 160 and clic:
            print(18)

        elif 685 < x < 735 and 165 < y < 205 and clic:
            print(19)

    def boot(self):
        """
        Название пассиыного навыка: Сапоги Гермеса
        Меняет скорость перемещения персонажа
        :return: None
        """
        pass

    def lightning(self):
        """
        Название пассиыного навыка: Светик-Сто-Смертник
        Добавление плоского урона персонажу
        :return: None
        """
        pass

    def banner(self):
        """
        Название пассиыного навыка: Вдохновляющий стяг
        Добавление процентного урона персонажу
        :return: None
        """
        pass

    def wind(self):
        """
        Название пассиыного навыка: Дуновение ветерка
        Отталкивает врага при атаке
        :return: None
        """
        pass

    def dark_brotherhood(self):
        """
        Название пассиыного навыка: Тёмное братство
        Если враг умер от одной атаки добавляет немного здоровья
        :return: None
        """
        pass

    def lay_down_the_bones(self):
        """
        Название пассиыного навыка: Лечь костями
        Защищает от смертельной атаки
        :return: None
        """
        pass

    def abaddon(self):
        """
        Название пассиыного навыка: Абаддон
        после убийства врага следующая атака по игроку не нанесёт урона
        :return: None
        """
        pass

    def accelerated_recharge(self):
        """
        Название пассиыного навыка: КДАБР
        ускоряет перезарядку атаки
        :return: None
        """
        pass

    def vampirism(self):
        """
        Название пассиыного навыка: Кровосися
        Добовляет по 5% от здоровья врага после нанесения удара
        :return: None
        """
        pass

    def the_witcher(self):
        """
        Название пассиыного навыка: Геральт из Кавказа
        Позволяет получить карточку монстра
        :return: None
        """
        pass

    def shield(self):
        """
        Название пассиыного навыка: Я есть грунт (ням-ням)
        Добовляет естественную защиту 5
        :return: None
        """
        pass

    def armor(self):
        """
        Название пассиыного навыка: Сила майнкрфта
        Добовляет шипы 1 на персонажа
        :return: None
        """
        pass

    def broken_heart(self):
        """
        Название пассиыного навыка: Разбитое сердце
        Увеличивает максимум здоровья в 2 раза, делая текущее здоровье равным четверти максимума
        :return: None
        """
        pass

    def response(self):
        """
        Название пассиыного навыка: Я не терпила, но терплю
        Если здоровье меньше 10% от максимума увеличивает естественую защиту на 10
        :return: None
        """
        pass

    def enlightened(self):
        """
        Название пассиыного навыка: Просвящённый майнкрафтом
        Усиляет шипы 1 до шипы 3 даёт вампиризм шипам 10% от полученого урона
        :return: None
        """
        pass

    def wolf_hysteria(self):
        """
        Название пассиыного навыка: Волчья истерика
        если здоровья меньше 1% увеличивает урон в двое
        :return: None
        """
        pass

    def eye_of_fate(self):
        """
        Название пассиыного навыка: Удача Дрима
        Увеличивает шанс выпадения легендарки
        :return: None
        """
        pass

    def pudge(self):
        """
        Название пассиыного навыка: Пудж
        Увеличивает максимальное здоровье за каждое убийство ценой потери 10% ночального здоровья
        :return: None
        """
        pass

    def stargazer(self):
        """
        Название пассиыного навыка: Звездочёт
        Даёт шанс затанить существо с 10% вероятностью при его спавне до смерти
        :return: None
        """
        pass



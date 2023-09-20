import random


class Main:
    def __init__(self):
        self.questions = [
            ['Архонт который забил на правление своей страной',
             ['A - Фокалорс', 'Б - Барбатос', 'В - Моракс', 'Г - Баал'], 2],
            ['Родная страна главного героя',
             ['А - Мондштат', 'Б - Сумеру', 'В - Фонтейн', 'Г - Каэнриах'], 2],
            ['Самая опасная группировка в Тейвате',
             ['А - Клан Кудзе', 'Б - Фатуи', 'В - Милелиты', 'Г - Рыцари Фавония'], 3],
            ['Что является силой архонтов',
             ['А - Глаз Бога', 'Б - Оружие', 'В - Сердце архонта'], 4] ]



    def user(self):
        win = 0
        while self.questions:
            self.count = random.choice(self.questions)
            self.questions.remove(self.count)
            print(self.count[0])
            print(*self.count[1], sep='\n')
            while True:
                self.us = input('Введите букву ответа: ')
                if int(self.us) == self.count[2]:
                    print('Правильный ответ!')
                    win += 1
                    break
                else:
                    print('Не правильный ответ!')
                    break
        print('\nКонец')
        print(f'Правильных ответов {win}')


a = Main()
a.user()

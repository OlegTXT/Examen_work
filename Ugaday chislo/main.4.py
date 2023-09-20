import random


class Main:
    def __init__(self):
        self.num = random.randint(1, 20)

    def operation(self):
        while True:
            self.number = input('Enter numder: ')
            if float(self.number) == self.num:
                print(f'You win, the nubber is {self.number}')
                break
            elif float(self.number) > self.num:
                print(f'The number is low than {self.number}')
            elif float(self.number) < self.num:
                print(f'The number is high than {self.number}')


a = Main()
a.operation()
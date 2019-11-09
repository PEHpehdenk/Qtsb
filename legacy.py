import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from pygame import mixer  # Load the required library
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
import time
import random
import history

endsi = open('ends.txt', 'r')
lines = endsi.readlines()
konzovki = []
for line in lines:
    konzovki.append(line)

pole = [[], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], [], [], []]

pole2 = pole.copy()


def randomShip(pole):
    ships = []
    num = 0
    while len(ships) != 10:
        ship1 = []
        number = random.randint(0, 99)
        site = random.randint(0, 3)
        if num == 0:
            if site == 0:
                for h in range(0, 4):
                    ship1.append(number - 10 * h)
            if site == 1:
                for h in range(0, 4):
                    ship1.append(number + h)
            if site == 2:
                for h in range(0, 4):
                    ship1.append(number + 10 * h)
            if site == 3:
                for h in range(0, 4):
                    ship1.append(number - h)
        if (num < 3) and num > 0:
            if site == 0:
                for h in range(0, 3):
                    ship1.append(number - 10 * h)
            if site == 1:
                for h in range(0, 3):
                    ship1.append(number + h)
            if site == 2:
                for h in range(0, 3):
                    ship1.append(number + 10 * h)
            if site == 3:
                for h in range(0, 3):
                    ship1.append(number - h)
        if (num < 6) and num > 2:
            if site == 0:
                for h in range(0, 2):
                    ship1.append(number - 10 * h)
            if site == 1:
                for h in range(0, 2):
                    ship1.append(number + h)
            if site == 2:
                for h in range(0, 2):
                    ship1.append(number + 10 * h)
            if site == 3:
                for h in range(0, 2):
                    ship1.append(number - h)
        if (num < 10) and num > 5:
            if site == 0:
                for h in range(0, 1):
                    ship1.append(number - 10 * h)
            if site == 1:
                for h in range(0, 1):
                    ship1.append(number + h)
            if site == 2:
                for h in range(0, 1):
                    ship1.append(number + 10 * h)
            if site == 3:
                for h in range(0, 1):
                    ship1.append(number - h)
        ship = ship1
        answer = True
        for i in range(0, len(ship)):
            if len(ship) > 1:
                vpered = ship[i] > 99
                if (ship[i] % 10 % 10 == 0 and ship[i] != 0 and i != 0 and site % 2 != 0) or vpered or ship[i] < 0:
                    answer = False
                    break
                if ship[-1] // 10 != ship[0] // 10 and (site % 2 == 1):
                    answer = False
                    break
                for k in range(0, len(ships)):
                    for g in range(0, len(ships[k])):
                        ship2 = ships[k][g]
                        if abs(ship[i] // 10 - ship2 // 10) < 2:
                            if abs(ship[i] % 10 - ship2 % 10) < 2:
                                answer = False
                                break
            else:
                ship = ship[0]
                for k in range(0, len(ships)):
                    for g in range(0, len(ships[k])):
                        if abs(ship // 10 - ships[k][g] // 10) < 2:
                            if abs(ship % 10 - ships[k][g] % 10) < 2:
                                answer = False
                                break
        if answer:
            ships.append(ship1)
            num += 1
        for i in range(0, len(ships)):
            for g in range(0, len(ships[i])):
                pole[ships[i][g]] = ['Y']


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    ships = []

    def showHisWin(self):
        self.hisWin = history.HistoryWindow()
        self.hisWin.show()

    def initUI(self):
        self.bnt_showHis = QPushButton(self)
        self.bnt_showHis.move(50, 50)
        self.bnt_showHis.setText('Показать историю')
        self.bnt_showHis.clicked.connect(self.showHisWin)
        self.end = False
        self.retry = QPushButton(self)
        self.retry.setText('расставить корабли #1')
        self.retry.move(700, 150)
        self.retry.clicked.connect(self.rastanovka)
        self.retry.setObjectName('#1')
        self.retry2 = QPushButton(self)
        self.retry2.setText('расставить корабли #2')
        self.retry2.setObjectName('#2')
        self.retry2.move(700, 550)
        self.retry2.clicked.connect(self.rastanovka)
        self.hodi = 0
        self.english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.k = 0
        self.number = '0'
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('The war of sea')
        self.suma1 = 0
        self.suma2 = 0
        self.sumaRasstanovok = 0
        self.sumaError = 0
        self.secretButton = QPushButton('?', self)
        self.secretButton.resize(10, 10)
        self.secretButton.move(0, 0)
        self.secretButton.clicked.connect(self.secret)
        self.fullScreen = QPushButton('FULL HD', self)
        self.fullScreen.resize(100, 100)
        self.fullScreen.move(1000, 350)
        self.fullScreen.clicked.connect(self.HD)
        self.sumaFail = 0
        for i in range(1, 11):
            btn = QLabel(self)
            btn.setText(str(i))
            btn.move(400 + (i - 1) * 20, 430)
        for i in range(0, 10):
            for g in range(0, 10):
                btn = QPushButton("", self)
                btn.move(400 + 20 * g, 450 + 20 * i)
                btn.resize(20, 20)
                text = self.english[i] + str(g + 1)
                btn.setObjectName(text)
                btn.clicked.connect(self.game)
            btn = QLabel(self)
            btn.setText(self.english[i])
            btn.move(380, 450 + 20 * i)
        for i in range(1, 11):
            btn = QLabel(self)
            btn.setText(str(i))
            btn.move(400 + (i - 1) * 20, 30)
        for i in range(0, 10):
            for g in range(0, 10):
                btn = QPushButton("", self)
                btn.move(400 + 20 * g, 50 + 20 * i)
                btn.resize(20, 20)
                text = self.english[i] + str(g + 1) + str('Player')
                btn.setObjectName(text)
                btn.clicked.connect(self.game)
            btn = QLabel(self)
            btn.setText(self.english[i])
            btn.move(380, 50 + 20 * i)
        self.info = QLabel(self)
        self.info.setText('ваш ход                                                                                   ')
        self.info.move(460, 300)
        self.hodi = 0
        self.comPole = QLabel(self)
        self.comPole.setText('корабли компьютера')
        self.comPole.move(430, 400)
        self.youPole = QLabel(self)
        self.youPole.setText('ваши корабли')
        self.youPole.move(450, 0)

    def game(self):
        if not self.end:
            popal = False
            error = False
            self.retry.move(10000, 10000)
            self.retry2.move(10000, 10000)
            cords = self.sender().objectName()
            x = self.english.index(cords[0])
            if 'Player' in cords:
                if cords[2] != 'P':
                    y = int(cords[1:3]) - 1
                else:
                    y = int(cords[1]) - 1
            else:
                y = int(cords[1:]) - 1
            dalshe = False
            if self.hodi % 2 == 0:
                if 'Player' not in self.sender().objectName():
                    if pole[x * 10 + y] == ['Y']:
                        if self.sender().text() == '':
                            self.sender().setText('❌')
                            popal = True
                            mixer.init()
                            mixer.music.load('popal.mp3')
                            mixer.music.play()
                            self.suma1 += 1
                            if self.suma1 == 20:
                                dalshe = True
                                self.info.setText('Игрок #1 выиграл!')
                        else:
                            self.sumaError += 1
                            mixer.init()
                            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                            mixer.music.play()
                            error = True
                    else:
                        if self.sender().text() == '':
                            self.sender().setText('•')
                            mixer.init()
                            mixer.music.load('04598.mp3')
                            mixer.music.play()
                            self.sumaFail += 1
                        else:
                            self.sumaError += 1
                            mixer.init()
                            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                            mixer.music.play()
                            error = True
                    textik = 'вы ударили по: '
                    textik += cords
                    self.info.setText(textik)
                else:
                    self.sumaError += 1
                    self.info.setText('сейчас не ваш ход')
                    mixer.init()
                    mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                    mixer.music.play()
                    error = True
            if self.hodi % 2 == 1:
                if 'Player' in self.sender().objectName():
                    if pole2[x * 10 + y] == ['Y']:
                        if self.sender().text() == '':
                            self.sender().setText('❌')
                            popal = True
                            mixer.init()
                            mixer.music.load('popal.mp3')
                            mixer.music.play()
                            self.suma2 += 1
                            if self.suma2 == 20:
                                dalshe = True
                                self.info.setText('Игрок #2 выиграл!')
                        else:
                            self.sumaError += 1
                            mixer.init()
                            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                            mixer.music.play()
                            error = True
                    else:
                        if self.sender().text() == '':
                            self.sender().setText('•')
                            mixer.init()
                            mixer.music.load('04598.mp3')
                            mixer.music.play()
                            self.sumaFail += 1
                        else:
                            self.sumaError += 1
                            mixer.init()
                            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                            mixer.music.play()
                            error = True
                    textik = 'вы ударили по: '
                    textik += cords
                    self.info.setText(textik)
                else:
                    self.sumaError += 1
                    self.info.setText('сейчас не ваш ход')
                    mixer.init()
                    mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
                    mixer.music.play()
                    error = True
            if not popal and not error:
                self.hodi += 1
            if dalshe:
                if self.sumaFail > 0:
                    if self.suma1 == 20:
                        history.new_res(1)
                        print("Error: Игра становится неинтересной, когда её выиграть, пытайтесь найти пасхалки")
                        dalshe2 = True
                        for line in lines:
                            if 'Неизбежность для первого игрока' in line:
                                dalshe2 = False
                                self.info.setText('Конец')
                        if dalshe2:
                            self.info.setText("ОТКРЫТО: Неизбежность для первого игрока")
                            endsi = open('ends.txt', 'w')
                            endsi.write("Неизбежность для первого игрока")
                            endsi.write('\n')
                            for i in range(0, len(konzovki)):
                                endsi.write(konzovki[i])
                        self.end = True
                    else:
                        history.new_res(2)
                        print("Error: Игра становится неинтересной, когда её выиграть, пытайтесь найти пасхалки")
                        dalshe2 = True
                        for line in lines:
                            if 'Неизбежность для второго игрока' in line:
                                dalshe2 = False
                                self.info.setText('Конец')
                        if dalshe2:
                            self.info.setText("ОТКРЫТО: Неизбежность для второго игрока")
                            endsi = open('ends.txt', 'w')
                            endsi.write("Неизбежность для второго игрока")
                            endsi.write('\n')
                            for i in range(0, len(konzovki)):
                                endsi.write(konzovki[i])
                        self.end = True
                else:
                    history.new_res(0)
                    print("Error: Читерство всегда наказуемо")
                    dalshe2 = True
                    for line in lines:
                        if 'Читер' in line:
                            dalshe2 = False
                            self.info.setText('Конец')
                    if dalshe2:
                        self.info.setText("ОТКРЫТО: Читер")
                        endsi = open('ends.txt', 'w')
                        endsi.write("Читер")
                        endsi.write('\n')
                        for i in range(0, len(konzovki)):
                            endsi.write(konzovki[i])
                    self.end = True
            if self.sumaError == 30:
                history.new_res(0)
                print("Error: Вас предупреждали слишком много раз...")
                dalshe2 = True
                for line in lines:
                    if 'Бунтарь' in line:
                        dalshe2 = False
                        self.info.setText('Конец')
                if dalshe2:
                    self.info.setText("ОТКРЫТО: Бунтарь")
                    endsi = open('ends.txt', 'w')
                    endsi.write("Бунтарь")
                    endsi.write('\n')
                    for i in range(0, len(konzovki)):
                        endsi.write(konzovki[i])
                self.end = True
        else:
            mixer.init()
            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
            mixer.music.play()

    num = 0
    randomShip(pole)
    randomShip(pole2)

    def rastanovka(self):
        if not self.end:
            self.sumaRasstanovok += 1
            if self.sumaRasstanovok == 20:
                dalshe2 = False
                history.new_res(0)
                print("Error: Впредь будьте более уверенным")
                dalshe2 = True
                for line in lines:
                    if 'Сомневающийся' in line:
                        dalshe2 = False
                        self.info.setText('Конец')
                if dalshe2:
                    self.info.setText("ОТКРЫТО: Сомневающийся")
                    endsi = open('ends.txt', 'w')
                    endsi.write("Сомневающийся")
                    endsi.write('\n')
                    for i in range(0, len(konzovki)):
                        endsi.write(konzovki[i])
                self.end = True
            if '#1' in self.sender().objectName():
                randomShip(pole)
            else:
                randomShip(pole2)
        else:
            mixer.init()
            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
            mixer.music.play()

    def secret(self):
        if not self.end:
            dalshe2 = False
            history.new_res(0)
            print("Error: Вы очень внимательны")
            dalshe2 = True
            for line in lines:
                if 'Зоркий глаз' in line:
                    dalshe2 = False
                    self.info.setText('Конец')
            if dalshe2:
                self.info.setText("ОТКРЫТО: Зоркий глаз")
                endsi = open('ends.txt', 'w')
                endsi.write("Зоркий глаз")
                endsi.write('\n')
                for i in range(0, len(konzovki)):
                    endsi.write(konzovki[i])
            self.end = True
        else:
            mixer.init()
            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
            mixer.music.play()

    def HD(self):
        if not self.end:
            dalshe2 = False
            history.new_res(0)
            print("Error: Похоже, вы предпочитаете играть на весь экран...")
            dalshe2 = True
            for line in lines:
                if 'FULL HD' in line:
                    dalshe2 = False
                    self.info.setText('Конец')
            if dalshe2:
                self.info.setText("ОТКРЫТО: FULL HD")
                endsi = open('ends.txt', 'w')
                endsi.write("FULL HD")
                endsi.write('\n')
                for i in range(0, len(konzovki)):
                    endsi.write(konzovki[i])
            self.end = True
        else:
            mixer.init()
            mixer.music.load('wide-design-z_uk-oshibki-windows.mp3')
            mixer.music.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

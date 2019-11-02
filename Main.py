import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QCheckBox


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('discriminant.ui', self)
        self.start.clicked.connect(self.solve)
        self.reset.clicked.connect(self.resets)
        self.count = 0
        self.ds = 0
        # ds = Не вычесленный дискриминант
        self.eq = ''
        # Переменная в которой хранится уравнение в строчном виде
        self.back.clicked.connect(self.fun_back)
        self.next.clicked.connect(self.fun_next)

    def solve(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())

        if b < 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')

            QApplication.processEvents()
            self.eq = (str(a) + 'x²' +
                       str(b) + 'x' + str(c) + ' ' + '= 0')
        elif b < 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + '+' + c + '= 0')
            QApplication.processEvents()
            self.eq = (str(a) + 'x²' +
                       str(b) + 'x' + '+' + c + '= 0')
        elif b >= 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')
            self.eq = (str(a) + 'x²' + '+' +
                       str(b) + 'x' + str(c) + ' ' + '= 0')
            QApplication.processEvents()
        elif b >= 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            self.eq = (str(a) + 'x²' + '+' +
                       str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            QApplication.processEvents()

        discriminant = (b ** 2) - 4 * a * c
        self.ds = discriminant
        discriminant = discriminant ** 0.5

        x1 = (((b * -1) + discriminant) / (2 * a))
        x2 = (((b * -1) - discriminant) / (2 * a))
        if int(self.ds) < 0:
            self.x1.setText('Уравнение не имеет корней')
            QApplication.processEvents()
            self.x2.setText('')
            QApplication.processEvents()
        elif int(self.ds) == 0:
            x = ((b * -1) / (2 * a))
            self.x1.setText('Уравнение имеет один корень:' + " " + str(x))
            QApplication.processEvents()
            self.x2.setText('')
        else:
            if discriminant % 1 == 0:
                self.x1.setText('Первый корень:' + " " + str(x1))
                QApplication.processEvents()
                self.x2.setText('Второй корень:' + " " + str(x2))
                QApplication.processEvents()
            else:

                self.x1.setText(
                    'Корни уравнения:' + ' ' + '(' + '-' + str(b) + '±' + '√' + str(
                        self.ds) + ')' + '/' + '(' + '2' + str(
                        a) + ')')
                QApplication.processEvents()

        if self.with_explains.isChecked():
            self.explanations.setText('Используйте кнопки "Назад" и "Далее" , чтобы увидеть пошаговое обьяснение')

    def resets(self):
        self.explanations.setText('')

    def fun_back(self):

        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())
        self.count -= 1
        discriminant = (b ** 2) - 4 * a * c
        discriminant = discriminant ** 0.5
        x1 = (((b * -1) + discriminant) / (2 * a))
        x2 = (((b * -1) - discriminant) / (2 * a))

        if self.count < 0:
            self.count = 0

        if self.ds < 0:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))

            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))

            elif self.count == 2:
                self.explanations.setText('Так как D < 0, то уравнение не имеет корней')

        elif self.ds == 0:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))
            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))
            elif self.count == 2:
                self.explanations.setText('Так как D = 0, то уравнение имеет один корень:' + '(-b) / (2a)' +
                                          '\n' + str(x2))
        else:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac')
            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))
            elif self.count == 2:
                self.explanations.setText(
                    'Так как D = 0, то уравнение имеет два корня корень:' + '(-b ± D ) / (2a) + ' + ' ' +
                    '\n' + 'Первый корень:' + ' ' + str(
                        x1) + '\n' + 'Второй корень:' + ' ' + str(x2))

    def fun_next(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())
        discriminant = (b ** 2) - 4 * a * c
        x1 = (((b * -1) + discriminant) / (2 * a))
        x2 = (((b * -1) - discriminant) / (2 * a))

        if self.ds < 0:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))

            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))

            elif self.count == 2:
                self.explanations.setText('Так как D < 0, то уравнение не имеет корней')

        elif self.ds == 0:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))
            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))
            elif self.count == 2:
                self.explanations.setText('Так как D = 0, то уравнение имеет один корень:' + '(-b) / (2a)' +
                                          '\n' + str(x2))
        else:
            if self.count == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac')
            elif self.count == 1:
                self.explanations.setText('Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + 'D=' + str(
                    self.ds))
            elif self.count == 2:
                self.explanations.setText(
                    'Так как D = 0, то уравнение имеет два корня корень:' + '(-b ± D ) / (2a) + ' + ' ' +
                    '\n' + 'Первый корень:' + ' ' + str(
                        x1) + '\n' + 'Второй корень:' + ' ' + str(x2))
        self.count += 1


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

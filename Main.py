import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QCheckBox


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('discriminant.ui', self)
        self.setWindowTitle(' ')
        self.start.clicked.connect(self.solve)
        self.reset.clicked.connect(self.resets)
        self.count = 0
        self.str_discriminant = 0
        #   Не вычесленный дискриминант
        self.the_equation = ''
        # Переменная в которой хранится уравнение в строчном виде
        self.back.clicked.connect(self.fun_back)
        self.next.clicked.connect(self.fun_next)
        self.x_1 = 0
        # Первый корень
        self.x_2 = 0
        # Второй корень
        self.x = 0
        # Корень при D = 0

    def solve(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())

        if b < 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')

            QApplication.processEvents()
            self.the_equation = (str(a) + 'x²' +
                                 str(b) + 'x' + str(c) + ' ' + '= 0')
        elif b < 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + '+' + str(c) + '= 0')
            QApplication.processEvents()
            self.the_equation = (str(a) + 'x²' +
                                 str(b) + 'x' + '+' + str(c) + '= 0')
        elif b >= 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')
            self.the_equation = (str(a) + 'x²' + '+' +
                                 str(b) + 'x' + str(c) + ' ' + '= 0')
            QApplication.processEvents()
        elif b >= 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            self.the_equation = (str(a) + 'x²' + '+' +
                                 str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            QApplication.processEvents()

        discriminant = (b ** 2) - 4 * a * c
        self.str_discriminant = discriminant
        discriminant = discriminant ** 0.5

        x1 = (((b * -1) + discriminant) / (2 * a))
        x2 = (((b * -1) - discriminant) / (2 * a))
        x = ((b * -1) / (2 * a))
        self.x_1 = x1
        self.x_2 = x2
        self.x = x

        if int(self.str_discriminant) < 0:

            self.x1.setText('Уравнение не имеет корней')
            QApplication.processEvents()
            self.x2.setText('')
            QApplication.processEvents()
        elif int(self.str_discriminant) == 0:

            self.x1.setText('Уравнение имеет один корень:' + " " + str(x))
            QApplication.processEvents()
            self.x2.setText('')
            QApplication.processEvents()

        else:
            if discriminant % 1 == 0:

                self.x1.setText('Первый корень:' + " " + str(x1))
                QApplication.processEvents()
                self.x2.setText('Второй корень:' + " " + str(x2))
                QApplication.processEvents()


            else:
                self.x1.setText(
                    'Корни уравнения:' + ' ' + '(' + '-' + str(b) + '±' + '√' + str(
                        self.str_discriminant) + ')' + '/' + '(' + '2' + '*' + str(
                        a) + ')')
                QApplication.processEvents()

        if self.with_explains.isChecked():
            self.explanations.setText('Используйте кнопки "Назад" и "Далее" , чтобы увидеть пошаговое обьяснение.'
                                      ' Перед тем как вводить новое уравнение нажмите на кнопку очистить.')

    def resets(self):
        self.explanations.setText('')
        self.count = 1
        self.x1.setText('')
        self.x2.setText('')

    def fun_back(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())
        k = b // 2
        k = int(k)
        discriminant = (b ** 2) - 4 * a * c
        discriminant = discriminant ** 0.5

        k_discriminant = ((k ** 2) - (a * c))
        k_discriminant = int()

        self.count -= 1

        if self.count <= 0:
            self.count = 1

        elif self.str_discriminant < 0:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))

            elif self.count == 2:

                if b % 2 == 0:

                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))
            elif self.count == 3:
                self.explanations.setText('Так как D < 0, то уравнение не имеет корней')

        elif self.str_discriminant == 0:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))
            elif self.count == 2:
                if b % 2 == 0:

                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))
            elif self.count == 3:
                self.explanations.setText('Так как D = 0, то уравнение имеет один корень:' + '(-b) / (2a)' +
                                          '\n' + str(self.x))
        else:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac')
            elif self.count == 2:
                if a == 1:

                    points = [i for i in range(-100, 100)]
                    for i in points:
                        x1 = i
                        for j in points:
                            x2 = j
                            if x1 + x2 == b and x1 * x2 == c:
                                self.explanations.setText(
                                    'Найдём корни по теорме Виета: x1 + x2 = b  x1 * x2 = c' + '\n' + str(
                                        x1) + '+' + str(x2) + '=' + str(b) + '\n' + str(x1) + '*' + str(x2) + '=' + str(
                                        c) + '\n' +
                                    'Следовательно данные числа подходят.')

                elif b % 2 == 0:

                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))
            elif self.count == 3:
                self.explanations.setText(
                    'Так как D = 0, то уравнение имеет два корня корень:' + '(-b ± D ) / (2a)' + ' ' +
                    '\n' + 'Первый корень:' + ' ' + str(
                        self.x_1) + '\n' + 'Второй корень:' + ' ' + str(self.x_2))
                self.x1.setText(
                    'Корни уравнения:' + ' ' + '(' + '-' + str(b) + '±' + '√' + str(
                        self.str_discriminant) + ')' + '/' + '(' + '2' + '*' + str(
                        a) + ')')

    def fun_next(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())
        k = b // 2
        k = int(k)
        discriminant = (b ** 2) - 4 * a * c
        discriminant = discriminant ** 0.5

        k_discriminant = ((k ** 2) - (a * c))
        k_discriminant = int(k_discriminant)
        self.count += 1
        if self.count > 3:
            self.count = 3

        elif self.str_discriminant < 0:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))
            elif self.count == 2:
                if b % 2 == 0:

                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))

            elif self.count == 3:
                self.explanations.setText('Так как D < 0, то уравнение не имеет корней')

        elif self.str_discriminant == 0:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c))
            elif self.count == 2:
                if b % 2 == 0:

                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))
            elif self.count == 3:
                self.explanations.setText('Так как D = 0, то уравнение имеет один корень:' + '(-b) / (2a)' +
                                          '\n' + str(self.x))
        else:
            if self.count == 1:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(self.the_equation) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac')
            elif self.count == 2:
                if a == 1:

                    points = [i for i in range(-100, 100)]
                    for i in points:
                        x1 = i
                        for j in points:
                            x2 = j
                            if x1 + x2 == b and x1 * x2 == c:
                                self.explanations.setText(
                                    'Найдём корни по теорме Виета: x1 + x2 = b  x1 * x2 = c' + '\n' + str(
                                        x1) + '+' + str(x2) + '=' + str(b) + '\n' + str(x1) + '*' + str(x2) + '=' + str(
                                        c) + '\n' +
                                    'Следовательно данные числа подходят.')
                if b % 2 == 0:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = k² - ac' + ' ' + '\n' + 'D=' + str(
                            k) + '²' + '-' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(k_discriminant))
                else:
                    self.explanations.setText(
                        'Формула нахождения дискриминанта: D = b² - 4ac' + ' ' + '\n' + 'D=' + str(
                            b) + '²' + '-' + '4' + '*' + str(a) + '*' + str(c) + '\n' +
                        'D=' + '' + str(self.str_discriminant))
            elif self.count == 3:
                self.explanations.setText(
                    'Так как D = 0, то уравнение имеет два корня корень:' + '(-b ± D ) / (2a)' + ' ' +
                    '\n' + 'Первый корень:' + ' ' + str(
                        self.x_1) + '\n' + 'Второй корень:' + ' ' + str(self.x_2))
                self.x1.setText(
                    'Корни уравнения:' + ' ' + '(' + '-' + str(b) + '±' + '√' + str(
                        self.str_discriminant) + ')' + '/' + '(' + '2' + '*' + str(
                        a) + ')')


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())

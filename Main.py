import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QCheckBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('discriminant.ui', self)
        self.start.clicked.connect(self.solve)
        self.reset.clicked.connect(self.resets)

    def solve(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())
        c = int(self.input_c.text())

        if b < 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')

            QApplication.processEvents()
            eq = (str(a) + 'x²' +
                  str(b) + 'x' + str(c) + ' ' + '= 0')
        elif b < 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' +
                                  str(b) + 'x' + '+' + c + '= 0')
            QApplication.processEvents()
            eq = (str(a) + 'x²' +
                  str(b) + 'x' + '+' + c + '= 0')
        elif b >= 0 and c < 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + str(c) + ' ' + '= 0')
            eq = (str(a) + 'x²' + '+' +
                  str(b) + 'x' + str(c) + ' ' + '= 0')
            QApplication.processEvents()
        elif b >= 0 and c >= 0:
            self.equation.setText('Ваше уравнение будет выглядить так:' + ' ' + str(a) + 'x²' + '+' +
                                  str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            eq = (str(a) + 'x²' + '+' +
                  str(b) + 'x' + "+" + str(c) + ' ' + '= 0')
            QApplication.processEvents()

        discriminant = (b ** 2) - 4 * a * c
        ds = discriminant
        discriminant = discriminant ** 0.5

        x1 = (((b * -1) + discriminant) / (2 * a))
        x2 = (((b * -1) - discriminant) / (2 * a))
        if int(ds) < 0:
            self.x1.setText('Уравнение не имеет корней')
            QApplication.processEvents()
            self.x2.setText('')
            QApplication.processEvents()
        elif int(ds) == 0:
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
                    'Корни уравнения:' + ' ' + '(' + '-' + str(b) + '±' + '√' + str(ds) + ')' + '/' + '(' + '2' + str(
                        a) + ')')
                QApplication.processEvents()
        if self.with_explains.isChecked():
            if int(ds) < 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac' + ' ' + 'D=' + str(
                    ds) + '\n' + 'Так как D < 0, то уравнение не имеет корней')
            elif int(ds) == 0:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac' + ' ' + 'D=' + str(
                    ds) + '\n' + 'Так как D = 0, то уравнение имеет один корень:' + '(-b) / (2a) + ' + '\n' + str(
                    x2))
            else:
                self.explanations.setText('Рассмотрим уравнение' + ' ' + str(eq) + '\n' +
                                          "a =" + str(a) + ";" + " " + 'b= ' + str(b) + ';' + ' ' + 'c=' + str(
                    c) + '\n' + 'D = b² - 4ac' + ' ' + 'D=' + str(
                    ds) + '\n' + 'Так как D = 0, то уравнение имеет два корня корень:' + '(-b ± D ) / (2a) + ' + ' ' +
                                          '\n' + 'Первый корень:' + ' ' + str(
                    x1) + '\n' + 'Второй корень:' + ' ' + str(x2)
                                          )

    def resets(self):
        self.explanations.setText('')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

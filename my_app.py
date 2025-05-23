from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QWidget,
QVBoxLayout,QHBoxLayout, QApplication)
app = QApplication([])
class okno(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Запоминаем число.')
        self.input = QLabel('')
        self.znak = ''
    
        self.btn1 = QPushButton('Сброс')
        self.btn1 = QPushButton('lambada')
        self.btn2 = QPushButton('Сброс всего')   
        self.btn4 = QPushButton('/')

        self.btn5 = QPushButton('7')
        self.btn6 = QPushButton('8')
        self.btn7 = QPushButton('9')
        self.btn8 = QPushButton('*')
            #
        self.btn9 = QPushButton('4')
        self.btn10 = QPushButton('5')
        self.btn11 = QPushButton('6')
        self.btn12 = QPushButton('-')

        self.btn13 = QPushButton('1')
        self.btn14 = QPushButton('2')
        self.btn15 = QPushButton('3')
        self.btn16 = QPushButton('+')

        self.btn17 = QPushButton('+-')
        self.btn18 = QPushButton('0')
        self.btn19 = QPushButton(',')
        self.btn20 = QPushButton('=')
        self.btn21 = QPushButton('+-')

        self.v1 = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        
        self.h1.addWidget(self.label)

        self.h2.addWidget(self.input)

        self.h3.addWidget(self.btn1)
        self.h3.addWidget(self.btn2)
        self.h3.addWidget(self.btn3)
        self.h3.addWidget(self.btn4)

        self.h4.addWidget(self.btn5)
        self.h4.addWidget(self.btn6)
        self.h4.addWidget(self.btn7)
        self.h4.addWidget(self.btn8)
        
        self.h5.addWidget(self.btn9)
        self.h5.addWidget(self.btn10)
        self.h5.addWidget(self.btn11)
        self.h5.addWidget(self.btn12)
        #
        self.h6.addWidget(self.btn13)
        self.h6.addWidget(self.btn14)
        self.h6.addWidget(self.btn15)
        self.h6.addWidget(self.btn16)
        #
        self.h7.addWidget(self.btn17)
        self.h7.addWidget(self.btn18)
        self.h7.addWidget(self.btn19)
        self.h7.addWidget(self.btn20)
        #
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.setLayout(self.v1)
        self.show()
    def obnul(self):
        self.label.setText('')
        self.input.setText('')
        self.znak = ''


class btn_num(QPushButton):
    def__init__(self,text):
        super().__init__()
        self.setText(text)
        self.clicked.connect(self.zxc)
    def zxc(self):
        okno1.nput.setText(okno1.input.text() + self.text())
class btn_znak(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.clicked.connect(self.zxc)
    def zxc(self)
        okno1.znak = self.text()
        okno1.label.setText(okno1.input.text())
        okno1.input.setText('')
    
okno1 = okno()

app.exec_()
print(eva1('2.13 + 11.1'))

def procenti(self):
    x = float(self.label.text())
    a = float(self.input.text())
    a = x/100 * a
    self.input.setText(str(a))


    class btn_num
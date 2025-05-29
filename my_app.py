from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QWidget,
QVBoxLayout,QHBoxLayout, QApplication)
app = QApplication([])
class okno(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('')
        self.input = QLabel('')
        self.btn1 = QPushButton('Сброс')
        self.btn1 = QPushButton(lambada: self.imput.setText(''))
        self.btn2 = QPushButton('Сброс всего')   
        self.btn2.clicked.conect(self.obnul)
        self.btn3 = QPushButton('Стереть')
        self.btn3 = QPushButton(lambada: self.imput.setText(self.input.text()[:-1:]))
        self.btn4 = btn_znak('/')
          
        self.btn5 = btn_num('7')
        self.btn6 = btn_num('8')
        self.btn7 = btn_num('9')
        self.btn8 = btn_num('*')

        self.btn9 = btn_num('4')
        self.btn10 = btn_num('5')
        self.btn11 = btn_num('6')
        self.btn12 = btn_num('-')

        self.btn13 = btn_num('1')
        self.btn14 = btn_num('2')
        self.btn15 = btn_num('3')
        self.btn16 = btn_znak('+')

        self.btn17 = QPushButton('+-')
        self.btn17.clicked.connect(lambada: self.imput.setText(str(int(self.input.text())*-1)))
        self.btn18 = btn_num('0')
        self.btn19 = btn_num('.')
        self.btn20 = QPushButton('=')
        self.btn20.clicked.connect(self.ravno)
        self.btn21 = QPushButton('%')
        self.btn21.clicked.connect(self.procenti)
        self.v1 = QVBoxLayout()
        self.v1 = QVBoxLayout()
        self.v2 = QVBoxLayout()
        self.v3 = QVBoxLayout()
        self.v4 = QVBoxLayout()
        self.v5 = QVBoxLayout()
        self.v6 = QVBoxLayout()
        self.v7 = QVBoxLayout()
        self.v8 = QVBoxLayout()

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
        self.h1.addWidget(self.btn21)
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.v1.addLayout(self.h8)
        self.setLayout(self.v1)
        self.setStyleSheet()

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
    
        self.show()
    def obnul(self):
        self.label.setText('')
        self.input.setText('')
        self.znak = ''
    def ravno(self):
        try:
            a = eval(self.label.text() + self.znak + self.input.text())
            self.input.setText(str(a))
        except:
            self.obnul()

    def procenti(self):
        x = float(self.label.text())
        a = float(self)




def procenti(self):
    x = float(self.label.text())
    a = float(self.input.text())
    a = x/100 * a
    self.input.setText(str(a))


    class btn_num
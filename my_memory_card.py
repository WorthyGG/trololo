
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QRadioButton,QLabel,QGroupBox
class Question():
    def __init__(self,question,right,_answer,wrong1, wrong2, wrong3):
        self.question = questionself.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

App = QApplication([])
main_win = QWidget()
text = QLabel('какой нации не существует?')
button = QPushButton('Ответ')
main_win.resize(500, 600)


line = QVBoxLayout()



RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Спуди мены')
rtbn_2 = QRadioButton('ТАНОСЫ')
rtbn_3 = QRadioButton('Железные дровосеки')
rtbn_4 = QRadioButton('Бомбы')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()



# layout_ans3.addStretch(1)
# layout_ans3.addWidget(btn_ok, addStretch = 2)
# layout_ans3.addStretch(1)
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rtbn_2)
layout_ans3.addWidget(rtbn_3)
layout_ans3.addWidget(rtbn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)
ansgroup = QGroupBox('Результаты теста')
lb_correct = QLabel('правильно/неправильно')
lb_right = QLabel('Правильный ответ')
lay = QVBoxLayout()
lay.addWidget(lb_correct, alignment = Qt.AlignCenter)
lay.addWidget(lb_right, alignment = Qt.AlignCenter)
ansgroup.setLayout(lay)
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(RadioGroupBox,alignment=Qt.AlignCenter)
line.addWidget(ansgroup,alignment=Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
ansgroup.hide()
main_win.setLayout(line)
layout_card = QVBoxLayout()

def show_result():
    RadioGroupBox.hide()
    ansgroup.show(layout_ans3)
    button.setText('Следущий вопрос')
# def start
# def ask(q:Question):


def show_question():
    RadioGroupBox.show()
    ansgroup.hide()
    button.setText('Ответить')



from random import shuffle
main_win.show()
App.exec_()
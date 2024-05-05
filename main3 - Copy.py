import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, \
    QMessageBox

app = QApplication([])
main_win = QWidget()

main_win = QWidget()
main_win.setWindowTitle('test')
main_win.move(100, 100)
main_win.resize(1000, 600)

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )

helo = QLabel(txt_hello)
instu = QLabel(txt_instruction)
butt = QPushButton(txt_next)
vert = QVBoxLayout()

vert.addWidget(helo,alignment=Qt.AlignLeft)
vert.addWidget(instu,alignment=Qt.AlignLeft)
vert.addWidget(butt,alignment=Qt.AlignCenter)


main_win.setLayout(vert)
main_win.show()
app.exec()

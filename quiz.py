from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Vedomstná karta")
main_win.resize(450, 230)

group = QGroupBox("Odpovede")
question = QLabel("Ktorá z národností neexistuje?")
Rbutton1 = QRadioButton()
Rbutton2 = QRadioButton()
Rbutton3 = QRadioButton()
Rbutton4 = QRadioButton()

RadioGroup = QButtonGroup()
RadioGroup.addButton(Rbutton1)
RadioGroup.addButton(Rbutton2)
RadioGroup.addButton(Rbutton3)
RadioGroup.addButton(Rbutton4)

main_line = QVBoxLayout()

groupVline = QVBoxLayout()
groupHline_1 =QHBoxLayout()
groupHline_2 =QHBoxLayout()

FinalButton = QPushButton("Ďalej")

groupHline_1.addWidget(Rbutton1, alignment=Qt.AlignCenter, stretch=5)
groupHline_1.addWidget(Rbutton2, alignment=Qt.AlignCenter, stretch=5)
groupHline_2.addWidget(Rbutton3, alignment=Qt.AlignCenter, stretch=5)
groupHline_2.addWidget(Rbutton4, alignment=Qt.AlignCenter, stretch=5)
groupVline.addLayout(groupHline_1)
groupVline.addLayout(groupHline_2)
group.setLayout(groupVline)

main_line.addWidget(question, alignment=Qt.AlignTop)
main_line.addWidget(group, alignment=Qt.AlignCenter)
main_line.addWidget(FinalButton, alignment=Qt.AlignCenter)

main_win.setLayout(main_line)



#Vyhodnotenie
Ans_group = QGroupBox("Výsledky")
group_label = QLabel("Správne/Nesprávne")
group_label2 = QLabel("Správna odpoveď je 'Československá' !")
wingroupLine = QVBoxLayout()
wingroupHline = QHBoxLayout()
next_button = QPushButton("Ďalšia otázka")
wingroup_mainLine = QVBoxLayout()

wingroupHline.addWidget(group_label,alignment=Qt.AlignLeft)
wingroupLine.addLayout(wingroupHline)
wingroupLine.addWidget(group_label2, alignment=Qt.AlignCenter)
Ans_group.setLayout(wingroupLine)

main_line.addWidget(Ans_group, alignment=Qt.AlignCenter)
main_line.addWidget(next_button)

Ans_group.hide()
next_button.hide()

#    koniec
end_LABEL = QLabel("Gratulujem!")
end_box = QGroupBox("Záver")
end_Box_Line = QVBoxLayout()
end_BoxLabel1 = QLabel("Dokončil si tento kvíz.")
end_BoxLabel2 = QLabel("Získal si (x) bodov z 3!")
end_button = QPushButton("Zavrieť")

end_Box_Line.addWidget(end_BoxLabel1, alignment=Qt.AlignCenter)
end_Box_Line.addWidget(end_BoxLabel2, alignment=Qt.AlignCenter)
end_box.setLayout(end_Box_Line)
main_line.addWidget(end_LABEL)
main_line.addWidget(end_box, alignment=Qt.AlignCenter)
main_line.addWidget(end_button)
end_LABEL.hide()
end_box.hide()
end_button.hide()

show_endButton = QPushButton("Vyhodnotiť")
main_line.addWidget(show_endButton, alignment=Qt.AlignCenter)
show_endButton.hide()
#    ...

answers = [Rbutton1, Rbutton2, Rbutton3, Rbutton4]

def ask(Question, right_answer, incorrect1, incorrect2, incorrect3, final_label):
    global question
    question.setText(Question)
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(incorrect1)
    answers[2].setText(incorrect2)
    answers[3].setText(incorrect3)
    group_label2.setText(final_label)


Question_1 = ["Ktorá z národností neexistuje?", "Československá", "Slovenská", "Česká", "Maďarská", "Správna odpoveď je 'Československá' !"]
Question_2 = ["Ktorá planéta je najbližšie k Slnku?", "Merkúr", "Venuša", "Mars", "Jupiter", "Správna odpoveď je 'Merkúr' !"]
Question_3 = ["Ktorý prvok má chemickú značku O ?", "Kyslík", "Vodík", "Ortuť", "Dusík", "Správna odpoveď je 'Kyslík' !"]
Question_4 = ["Ktoré zviera je cicavec?", "Delfín", "Krokodíl", "Žralok", "Jašterica", "Správna odpoveď je 'Delfín' !"]
Question_5 = ["Koľko strán má štvorec?", "4", "3", "6","40", "Správna odpoveď je '4' !"]
Ans_Que = [Question_1, Question_2, Question_3, Question_4, Question_5]
shuffle(Ans_Que)

otazka = 0
spravne = 0
nespravne1 = 0
nespravne2 = 0
nespravne3 = 0
label = -1

question_num = 1
spravne_odpovede = 0

#------SHOW------
def show_result():
    global label
    global otazka
    global spravne
    global nespravne1
    global nespravne2
    global nespravne3
    global question_num
    global spravne_odpovede

    label += 1

    group.hide()
    FinalButton.hide()

    Ans_group.show()
    next_button.show()

    if answers[0].isChecked() == True:
        group_label.setText("Correct!")
        spravne_odpovede += 1

    else:
        group_label.setText("Incorrect!")

    ask(Ans_Que[otazka][0], Ans_Que[spravne][1], Ans_Que[nespravne1][2], Ans_Que[nespravne2][3], Ans_Que[nespravne3][4], Ans_Que[label][5])

    if question_num == 5:
        show_endButton.show()
        next_button.hide()


def show_question():
    global otazka
    global spravne
    global nespravne1
    global nespravne2
    global nespravne3
    global label
    global question_num

    group.show()
    FinalButton.show()

    #----
    otazka += 1
    spravne += 1
    nespravne1 += 1
    nespravne2 += 1
    nespravne3 += 1
    question_num += 1
    #----

    Ans_group.hide()
    next_button.hide()

    RadioGroup.setExclusive(False)
    Rbutton1.setChecked(False)
    Rbutton2.setChecked(False)
    Rbutton3.setChecked(False)
    Rbutton4.setChecked(False)
    RadioGroup.setExclusive(True)

    ask(Ans_Que[otazka][0], Ans_Que[spravne][1], Ans_Que[nespravne1][2], Ans_Que[nespravne2][3], Ans_Que[nespravne3][4], Ans_Que[label][5])


def end():
    global spravne_odpovede

    group.hide()
    FinalButton.hide()
    Ans_group.hide()
    next_button.hide()
    question.hide()
    show_endButton.hide()

    end_LABEL.show()
    end_box.show()
    end_button.show()

    end_BoxLabel2.setText("Získal si "+ str(spravne_odpovede) +" bodov z 5!")

def close():
    quit()
#----------------

FinalButton.clicked.connect(show_result)

next_button.clicked.connect(show_question)

end_button.clicked.connect(close)

show_endButton.clicked.connect(end)

ask(Ans_Que[otazka][0], Ans_Que[spravne][1], Ans_Que[nespravne1][2], Ans_Que[nespravne2][3], Ans_Que[nespravne3][4], Ans_Que[label][5])

main_win.show()
app.exec_()
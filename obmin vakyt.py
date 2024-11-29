import requests
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

valcode_input  = QLineEdit()
date_input = QLineEdit()
res_output = QLineEdit()
get_res = QPushButton("Отримати")

line = QVBoxLayout()
line.addWidget(valcode_input)
line.addWidget(date_input)
line.addWidget(res_output)
line.addWidget(get_res)

def get_rate():
    date = valcode_input.text()
    valcode = valcode_input.text()
    esponse = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")
    get_res.setText()


window.setLayout(line)
window.show()
app.exec()
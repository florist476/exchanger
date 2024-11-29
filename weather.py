import requests
from PyQt6.QtWidgets import *
from datetime import datetime

app = QApplication([])
window = QWidget()
window_width, window_height = 400, 350
window.resize(window_width, window_height)
main_line = QVBoxLayout()
input_line = QHBoxLayout()
vedenia = QLineEdit()
vedenia.setPlaceholderText("Введіть текст для пошуку")
search = QPushButton("Знайти")
input_line.addWidget(vedenia)
input_line.addWidget(search)
result = QLabel("Результат пошуку")
main_line.addLayout(input_line)
main_line.addWidget(result)
name1 = QLabel("Температура:")
name2 = QLabel("Швидкість вітру:")
name3 = QLabel("Тиск:")
name4 = QLabel("Хмарність:")
name5 = QLabel("Час сходу сонця:")
name6 = QLabel("Час заходу сонця:")
main_line.addWidget(name1)
main_line.addWidget(name2)
main_line.addWidget(name3)
main_line.addWidget(name4)
main_line.addWidget(name5)
main_line.addWidget(name6)


kart = QLabel("Картинка")
pixmam = QPixmap("01n@2x.png")
kart.setPixmap(pixmam)


app.setStyleSheet("""
            QPushButton
            {
                background-color: #F3C301;
                
                
             
                color: green;
                }
            QLineEdit
            {
                border-style: groove;
                border-width: 3px;
                border-color: #F3C301;
            }
            
            
        """)






key = "f81703c1f3b81ad93e6644153c4a426e"

timestamp = 1697011200

def sun():
    cityname = vedenia.text()
    life = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={key}"
    response = requests.get(life)
    if response.status_code == 200:
        data = response.json()
        print(data)
        sunrice = datetime.fromtimestamp(data['sys']['sunrise'])
        suncets = datetime.fromtimestamp(data['sys']['sunset'])
        name1.setText(f"Температура:{data['main']['temp']-273.15}")
        name2.setText(f"Швидкість вітру:{data['wind']['speed']}")
        name3.setText(f"Тиск:{data['main']['pressure']}")
        name4.setText(f"Хмарність:{data['clouds']['all']}")
        name5.setText(f"Час сходу сонця:{sunrice}")
        name6.setText(f"Час заходу сонця:{suncets}")


    else:
        return None

search.clicked.connect(sun)




window.setLayout(main_line)

window.setWindowTitle("Прогноз погоди любої частини України")

window.show()
app.exec()



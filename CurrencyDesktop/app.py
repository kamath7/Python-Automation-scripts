from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
import requests
from bs4 import BeautifulSoup



def cleaner_text(text):
    return float(text.split(" ")[0])

def get_curr(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    curr_rate = soup.find('span', class_="ccOutputRslt").get_text()
    # print(cleaner_text(curr_rate))
    return cleaner_text(curr_rate)

def converter():
    input_text = float(text.text())
    op = str(round(input_text * get_curr('USD','INR'), 2))
    output_label.setText(op)
    

app = QApplication([])
window = QWidget()
window.setWindowTitle('Dollar to INR - Currency Converter')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)

btn.clicked.connect(converter)


output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
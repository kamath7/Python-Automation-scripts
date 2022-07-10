from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

window.setLayout(layout)
window.show()
app.exec()
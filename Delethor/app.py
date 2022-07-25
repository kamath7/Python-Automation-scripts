from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle("Delethor")

layout = QVBoxLayout()

description = QLabel("Delethor helps you <font color=\"red\">delete permanently</font>")
layout.addWidget(description)

window.setLayout(layout)
window.show()
app.exec()
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


app = QApplication([])
window = QWidget()
window.setWindowTitle("Delethor")

layout = QVBoxLayout()

description = QLabel("Delethor helps you <font color=\"red\">delete permanently</font>")
layout.addWidget(description)

open_btn = QPushButton("Open Files")
open_btn.setToolTip("Open a bunch of files/file")
open_btn.setFixedWidth(101)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)


window.setLayout(layout)
window.show()
app.exec()
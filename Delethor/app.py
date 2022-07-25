from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle("Delethor")

layout = QVBoxLayout()

description = QLabel("Delethor helps you <font color=\"red\">delete permanently</font>")
layout.addWidget(description)

open_btn = QPushButton("Open Files")
open_btn.setToolTip("Open a bunch of files/file")
layout.addWidget(open_btn)


window.setLayout(layout)
window.show()
app.exec()
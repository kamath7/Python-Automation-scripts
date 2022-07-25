from fileinput import filename
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    message.setText('\n'.join(filenames))
    # print(filenames)


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText("Destroyed ⛏")



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
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Delete Files")
destroy_btn.setFixedWidth(101)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel(" ")
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
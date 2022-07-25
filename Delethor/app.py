from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("Delethor")

layout = QVBoxLayout()

window.setLayout(layout)
window.show()
app.exec()
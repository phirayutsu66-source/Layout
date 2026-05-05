import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Layout")

        layout = QGridLayout()
        btn_close = QPushButton("Close")
        btn_close.clicked.connect(self.close)

        layout.addWidget(QLabel("cls"), 0, 0)
        layout.addWidget(QLabel("bck"), 0, 1)
        layout.addWidget(QLabel(""), 0, 2)
        layout.addWidget(btn_close, 0, 3)
        layout.addWidget(QLabel("7"), 1, 0)
        layout.addWidget(QLabel("8"), 1, 1)
        layout.addWidget(QLabel("9"), 1, 2)
        layout.addWidget(QLabel("/"), 1, 3)
        layout.addWidget(QLabel("4"), 2, 0)
        layout.addWidget(QLabel("5"), 2, 1)
        layout.addWidget(QLabel("6"), 2, 2)
        layout.addWidget(QLabel("*"), 2, 3)
        layout.addWidget(QLabel("1"), 3, 0)
        layout.addWidget(QLabel("2"), 3, 1)
        layout.addWidget(QLabel("3"), 3, 2)
        layout.addWidget(QLabel("-"), 3, 3)
        layout.addWidget(QLabel("0"), 4, 0)
        layout.addWidget(QLabel("."), 4, 1)
        layout.addWidget(QLabel("="), 4, 2)
        layout.addWidget(QLabel("+"), 4, 3)

        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QHBoxLayout, QGridLayout, QPushButton, QLineEdit)
from PySide6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Main Layout (แนวตั้ง)
        main_layout = QVBoxLayout()

        # 2. หน้าจอแสดงผล (Display)
        self.display = QLineEdit("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 20px;")
        main_layout.addWidget(self.display)

        # 3. แถวปุ่มบน (Backspace, Clear, Clear All)
        top_buttons_layout = QHBoxLayout()
        for text in ["Backspace", "Clear", "Clear All"]:
            btn = QPushButton(text)
            btn.setFixedHeight(40)
            top_buttons_layout.addWidget(btn)
        main_layout.addLayout(top_buttons_layout)

        # 4. ตารางปุ่มตัวเลขและเครื่องหมาย (Grid Layout)
        grid_layout = QGridLayout()
        
        # รายการปุ่มตามลำดับ (ข้อความ, แถว, คอลัมน์)
        buttons = [
            ('MC', 0, 0), ('7', 0, 1), ('8', 0, 2), ('9', 0, 3), ('/', 0, 4), ('Sqrt', 0, 5),
            ('MR', 1, 0), ('4', 1, 1), ('5', 1, 2), ('6', 1, 3), ('*', 1, 4), ('x^2', 1, 5),
            ('MS', 2, 0), ('1', 2, 1), ('2', 2, 2), ('3', 2, 3), ('-', 2, 4), ('1/x', 2, 5),
            ('M+', 3, 0), ('0', 3, 1), ('.', 3, 2), ('+/-', 3, 3), ('+', 3, 4), ('=', 3, 5),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50) # ปรับขนาดปุ่มให้เป็นจัตุรัส
            grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)

        # ตั้งค่าหน้าต่าง
        self.setLayout(main_layout)
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 450) # ล็อกขนาดหน้าต่างให้ใกล้เคียงกับรูป

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
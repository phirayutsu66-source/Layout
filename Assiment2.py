import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QMessageBox)
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. สร้าง Main Layout แบบ VBox (แนวตั้ง)
        vbox = QVBoxLayout()

        # สร้างส่วนเว้นว่างด้านบน (Stretch) เพื่อดันปุ่มลงไปด้านล่างตามภาพ
        vbox.addStretch(1)

        # 2. สร้าง HBox (แนวนอน) สำหรับวางปุ่ม
        hbox = QHBoxLayout()
        
        # เพิ่ม Stretch ใน HBox เพื่อดันปุ่มไปทางขวา
        hbox.addStretch(1)

        # สร้างปุ่ม OK และ Cancel
        self.btn_ok = QPushButton("OK")
        self.btn_cancel = QPushButton("Cancel")

        # เพิ่มปุ่มเข้าไปใน HBox
        hbox.addWidget(self.btn_ok)
        hbox.addWidget(self.btn_cancel)

        # 3. นำ HBox ใส่เข้าไปใน VBox
        vbox.addLayout(hbox)

        # ตั้งค่า Layout หลักให้กับหน้าต่าง
        self.setLayout(vbox)

        # เชื่อมต่อ Event (การคลิกปุ่ม)
        self.btn_ok.clicked.connect(self.show_message)
        self.btn_cancel.clicked.connect(self.close_app)

        # ตั้งค่าหน้าต่างโปรแกรม
        self.setWindowTitle("Buttons")
        self.resize(350, 200)

    # ฟังก์ชันแสดง MessageBox เมื่อกด OK
    def show_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Message")
        msg.setText("คุณได้กดปุ่ม OK")
        msg.exec()

    # ฟังก์ชันปิดโปรแกรมเมื่อกด Cancel
    def close_app(self):
        self.close() # หรือใช้ sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
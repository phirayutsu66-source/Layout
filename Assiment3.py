import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, 
                               QLineEdit, QTextEdit, QLabel)

class ReviewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. สร้าง Layout แบบฟอร์ม
        layout = QFormLayout()

        # 2. สร้าง Widgets
        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.review_display = QTextEdit()
        
        # ปรับให้ Review (QTextEdit) อ่านได้อย่างเดียว (ถ้าต้องการตามโจทย์ที่บอกว่าพิมพ์ Author แล้วไปโชว์ใน Review)
        # หรือถ้าต้องการให้พิมพ์ได้ทั้งสองทาง ก็ไม่ต้องใส่ ReadOnly ครับ
        self.review_display.setPlaceholderText("ข้อความจาก Author จะมาปรากฏที่นี่...")

        # 3. เพิ่ม Widgets ลงใน Layout
        layout.addRow("Title", self.title_input)
        layout.addRow("Author", self.author_input)
        layout.addRow("Review", self.review_display)

        # 4. เชื่อมต่อ Signal (เหตุการณ์เมื่อมีการพิมพ์)
        # textChanged จะทำงานทุกครั้งที่มีการกดปุ่มคีย์บอร์ด
        self.title_input.textChanged.connect(self.update_window_title)
        self.author_input.textChanged.connect(self.update_review_text)

        # ตั้งค่าหน้าต่าง
        self.setLayout(layout)
        self.setWindowTitle("Review") # ชื่อตั้งต้น
        self.resize(400, 300)

    # ฟังก์ชัน: เมื่อพิมพ์ใน Title ให้เปลี่ยนชื่อ Window Title Bar
    def update_window_title(self, text):
        if text:
            self.setWindowTitle(text)
        else:
            self.setWindowTitle("Review")

    # ฟังก์ชัน: เมื่อพิมพ์ใน Author ให้ข้อความไปปรากฏใน Review (QTextEdit)
    def update_review_text(self, text):
        self.review_display.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviewWindow()
    window.show()
    sys.exit(app.exec())
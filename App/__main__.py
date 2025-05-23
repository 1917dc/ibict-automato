from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import sys
import os


class AutomatoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automato - Uma colaboração entre UnDF & IBICT")
        self.setFixedSize(1180, 630)

        # Imagem de fundo
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "fundo.png")))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1180, 630)

        # Botão Menu
        self.menu_btn = QPushButton("Menu", self)
        self.menu_btn.setGeometry(730, 150, 140, 90)  # ← Ajuste horizontal
        self.menu_btn.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        # Botão Páginas
        self.page_btn = QPushButton("Páginas", self)
        self.page_btn.setGeometry(890, 150, 140, 90)
        self.page_btn.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        # Botão INPUT
        self.input_btn = QPushButton("INPUT", self)
        self.input_btn.setGeometry(730, 260, 300, 140)
        self.input_btn.setFont(QFont("Arial", 11, QFont.Weight.Bold))

        # Estilo unificado
        for btn in [self.menu_btn, self.page_btn, self.input_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #005A4F;
                    font-size: 18px;
                    border-radius: 10px;
                    border: 2px solid #005A4F;
                }
                QPushButton:hover {
                    background-color: #005A4F;
                    color: white;
                    border: 2px solid white; 
                    
                }
            """)

        # INPUT destaque
        self.input_btn.setStyleSheet("""
            QPushButton {
                background-color: #005A4F;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 10px;       
            }
            QPushButton:hover {
                background-color: white;
                color: #005A4F;
                border: 2px solid #005A4F;               
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutomatoApp()
    window.show()
    sys.exit(app.exec())

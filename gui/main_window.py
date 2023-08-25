from PyQt5.QtWidgets import QMainWindow
from .menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sentenio")
        self.setGeometry(100, 100, 800, 600)

        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)
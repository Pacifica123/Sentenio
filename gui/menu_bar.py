from PyQt5.QtWidgets import QMenuBar, QAction

class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        file_menu = self.addMenu("File")
        # подменюшки для Файла

        edit_menu = self.addMenu("Edit")
        # подменюшки для Редактирования

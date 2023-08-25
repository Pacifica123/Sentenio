import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    main_w = MainWindow()
    main_w.show()
    sys.exit(app.exec_())
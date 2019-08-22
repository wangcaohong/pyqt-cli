import sys
from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow

class Main(object):
    def __init__(self):
        self.mainWindow = MainWindow()

    def show(self):
        # Window running
        self.mainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

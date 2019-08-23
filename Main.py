import sys
from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow

class Main(object):
    bool = True
    def __init__(self):
        self.mainWindow = MainWindow()
        self.mainWindow.showLableButton.clicked.connect(self.show_text)

    def show(self):
        # Window running
        self.mainWindow.show()
    
    def show_text(self):
        if self.bool == True:
            self.bool = False
        else:
            self.bool = True
        
        self.mainWindow.show_text(self.bool)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

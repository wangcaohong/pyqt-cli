from ui.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def show_text(self, bool):
        QApplication.processEvents()
        if bool == True:
            self.showLableButton.setText('Hidden')
        else:
            self.showLableButton.setText('Show')
        self.helloLabel.setVisible(bool)


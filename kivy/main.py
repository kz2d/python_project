import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        print(4)
        self.ui.pushButton.clicked.connect(self.button)
        #self.ui.verticalSlider.setRepeatAction(self.button,50,50)

    def button(self):
        print(5)
        ok=int( self.ui.verticalSlider.sliderPosition()*2.55)
        ok1 = int(self.ui.verticalSlider_2.sliderPosition()*2.55)
        ok2 = int(self.ui.verticalSlider_3.sliderPosition ()*2.55)
        l=ok*16*16*16*16+ok1*16*16+ok2
        print(str(hex(l))[2::])
        l=str(hex(l))[2::]
        if ok<16:
           l="0"+l
        self.ui.centralwidget.setStyleSheet("QPushButton{background-color: #"+l+";}")

app=QtWidgets.QApplication([])
application=Main()
application.show()

sys.exit(app.exec())
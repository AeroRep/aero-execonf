import sys, logging, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore

VER = 'v0.1'
log = logging
logFilePath = './log/mainlog.log'

try:
    print("Reading..")
    print(os.path.isfile(logFilePath))
    print("Setting up debug log..")
    log.basicConfig(filename='./log/debug-log.log', level=logging.INFO, encoding="utf-8")
    print("Resetting..")
    f = open('./log/debug-log.log', 'w')
    f.close()
except FileNotFoundError:
    if os.path.isfile(logFilePath) == False:
        print("Logging file not exists, making...")
        try:
            f = open('./log/debug-log.log', 'w')
            f.close()
        except:
            print("An error occurred while writing log file.")
            print("It may the file exists or no permission to write file to location.")

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initOOBEUi()
        self.setupWidget()

    def initOOBEUi(self): # init window
        log.info("MAIN: Setup init")
        self.setWindowTitle("aerooobesystemsetup")
        self.setWindowIcon(QIcon('./src/img/Artboard_4.PNG'))
        self.resize(1920, 1080)
        self.center()
        self.setWindowFlags(QtCore.Qt.WindowType.WindowContextHelpButtonHint)
        log.info("MAIN: Showing")
        self.show()

    def setupWidget(self):
        log.info("WIDGET: Setup widget")
        self.mainTitle = QLabel("Welcome!", self);

        mainTextFont = self.mainTitle.font()
        mainTextFont.setFamily('Pretendard JP Variable')
        mainTextFont.setPointSize(20)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

stylesheet = """
    MainWindow {
        background-image: url('./src/img/B_Gradient_Blur_1920.png'); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = Main()
    sys.exit(app.exec_())
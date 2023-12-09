import sys, subprocess, platform
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initmsg()

    def initmsg(self): # init window
        self.chkIfUserInstallEXE()

    def chkIfUserInstallEXE(self):
        chkinstall = QMessageBox.question(self, 'Windows 호환 레이어 설치', '현재 실행할려는 프로그램은 윈도우 전용 프로그램입니다.\n이 프로그램을 실행할려면 호환 레이어를 설치해야합니다, 설치하시겠어요?', QMessageBox.Yes | QMessageBox.No)
        if chkinstall == QMessageBox.Yes:
            if platform.system() != 'Linux':
                QMessageBox.critical(self, '리눅스 전용 프로그램', '이 프로그램은 리눅스만 실행가능한 프로그램입니다,\n현재 ' + platform.system() + ' 에서 실행하고 있습니다.')  
                sys.exit('exited by program')
            else:
                subprocess.run('sudo pacman --no-confirm -Syu')
                subprocess.run('sudo pacman --no-confirm -S wine wine-mono wine-gecko')
                subprocess.run('wine --version')
                QMessageBox.information(self, '설치 성공', '윈도우 호환 레이어가 성공적으로 설치되었습니다!', QMessageBox.Ok)
        else:
            sys.exit('exited by user')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
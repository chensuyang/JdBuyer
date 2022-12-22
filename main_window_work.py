import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import JdBuyerAppProUi

# 创建窗口
def create_window(window_work):
    window_work_obj = window_work()
    window_obj = qtmodern.windows.ModernWindow(window_work_obj)
    # 窗口置顶
    window_obj.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    # 获取窗口大小
    screen = QDesktopWidget().screenGeometry()
    size = window_obj.geometry()
    # 窗体运动
    window_obj.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
    window_obj.show()
    return window_work_obj, window_obj


class MainWindowWork(QtWidgets.QMainWindow):
    close_signal = QtCore.pyqtSignal()
    instance_obj_array = list()
    instance_num = 0

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = JdBuyerAppProUi.Ui_MainWindow()
        self.ui.setupUi(self)


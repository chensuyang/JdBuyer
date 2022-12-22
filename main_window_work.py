import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, Qt, pyqtSignal, QThread
import time
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget, QWidget
import JdBuyerAppProUi
import pprint
import TabSubWidget


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

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = JdBuyerAppProUi.Ui_MainWindow()
        self.ui.setupUi(self)

        self.instance_obj_array = list()
        self.instance_num = 0

        self.ui.AddPushButton.clicked.connect(self.slot_AddPushButton_clicked_callback)
        self.ui.RunPushButton.clicked.connect(self.slot_RunPushButton_clicked_callback)

    def slot_AddPushButton_clicked_callback(self):
        WidgetObj = QWidget()
        TabSubWidgetObj = TabSubWidget.Ui_Form()
        TabSubWidget.Ui_Form.setupUi(TabSubWidgetObj, Form=WidgetObj)
        self.ui.tabWidget.addTab(WidgetObj, "商品%d" % (self.instance_num + 1))
        self.instance_num = self.instance_num +1

    def slot_RunPushButton_clicked_callback(self):
        pass

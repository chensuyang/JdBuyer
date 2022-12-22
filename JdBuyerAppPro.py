import sys
import time

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import main_window_work

if __name__ == '__main__':
    global win

    # 适配高清屏
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    qtmodern.styles.light(app)

    win = main_window_work.MainWindowWork()
    win = qtmodern.windows.ModernWindow(win)
    # 本窗体运动
    win.move(0, 0)
    # 显示主窗口
    win.show()
    win.setWindowTitle("JdBuyerAppPro")
    sys.exit(app.exec_())

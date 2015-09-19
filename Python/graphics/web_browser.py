# -*- coding: utf-8 -*-
'''
用PyQt创建一个Web浏览器

date:2015-09-19
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

class Browser(QWidget):
    def __init__ (self):
        super(Browser, self).__init__()

        self.webview = QWebView(self)
        self.webview.load("http://www.baidu.com")
        self.setGeometry(0, 0, 800, 600)

        self.back_btn = QPushButton("<", self)
        self.back_btn.clicked.connect(self.webview.back)
        self.back_btn.setMaximumSize(20, 20)

        self.forward_btn = QPushButton(">", self)
        self.forward_btn.clicked.connect(self.webview.forward)
        self.forward_btn.setMaximumSize(20, 20)

        self.menu_bar = QHBoxLayout()
        self.menu_bar.addWidget(self.back_btn)
        self.menu_bar.addWidget(self.forward_btn)
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.menu_bar)
        self.main_layout.addWidget(self.webview)
        self.setLayout(self.main_layout)


class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()
        self.widget = Browser()
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
window = BrowserWindow()
window.show()

app.exec_()
app.exit()

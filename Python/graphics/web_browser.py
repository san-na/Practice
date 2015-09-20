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
        self.url_entry = QLineEdit(self)
        self.url_entry.setMinimumSize(200, 20)
        self.url_entry.setMaximumSize(300, 20)

        self.go_btn = QPushButton('Go', self)
        self.go_btn.clicked.connect(self.go_btn_clicked)
        self.go_btn.setMaximumSize(20, 20)

        self.favourites = QComboBox(self)
        self.favourites.addItems(['http://www.baidu.com',
                            'http://www.qq.com',
                            'http://www.cnblogs.com'])
        self.favourites.activated.connect(self.favourite_selected)
        self.favourites.setMinimumSize(200, 20)
        self.favourites.setMaximumSize(300, 20)

        self.search_box = QLineEdit(self)
        self.search_box.setMinimumSize = (200, 20)
        self.search_box.setMaximumSize = (300, 20)

        self.search_btn = QPushButton('Search', self)
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.search_btn.setMaximumSize(50, 20)

        self.zoom_slider = QSlider(Qt.Orientation(1), self)
        self.zoom_slider.setRange(2, 50)
        self.zoom_slider.setValue(10)
        self.zoom_slider.valueChanged.connect(self.zoom_changed)

        self.zoom_label = QLabel('Zoom:')

        self.webview.loadStarted.connect(self.page_loading)

        self.menu_bar = QHBoxLayout()
        self.menu_bar.addWidget(self.back_btn)
        self.menu_bar.addWidget(self.forward_btn)
        self.menu_bar.addWidget(self.url_entry)
        self.menu_bar.addWidget(self.go_btn)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.favourites)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.search_box)
        self.menu_bar.addWidget(self.search_btn)
        self.menu_bar.addWidget(self.zoom_slider)
        self.menu_bar.addWidget(self.zoom_label)
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.menu_bar)
        self.main_layout.addWidget(self.webview)
        self.setLayout(self.main_layout)

    def go_btn_clicked(self):
        self.webview.load(self.url_entry.text())

    def favourite_selected(self):
        self.webview.load(self.favourites.currentText())

    def zoom_changed(self):
        self.webview.setZoomFactor(self.zoom_slider.value()/10)

    def search_btn_clicked(self):
        self.webview.load('http://cn.bing.com/search?q='
                    + self.search_box.text())

    def page_loading(self):
        self.url_entry.setText(self.webview.url().toString())


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

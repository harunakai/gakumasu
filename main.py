import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel, QPushButton, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon, QPixmap

from Ui_gakumasu import Ui_MainWindow
from utils import *


import os
from PIL import Image
import random

hanzi2str = {
    '第一名': '1',
    '第二名': '2',
    '第三名': '3',
    '未进入前三': 'else'
}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super(MainWindow, self).__init__()
        #self.ui = Ui_MainWindow()
        self.setWindowIcon(QIcon('./resource/icon.png'))
        self.setupUi(self)
        self.setWindowTitle('学马士实用小工具')
        self.setFixedSize(600, 400)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.button1_click)
        self.pushButton_2.clicked.connect(self.button2_click)
        self.pushButton_3.clicked.connect(self.button3_click)
        self.pushButton_4.clicked.connect(self.button4_click)
        self.button3_status = False
        self.cal = None
        self.remain_cal = None
        self.image_folder = './resource/idol/'
        self.current_image_index = 0
        #self.label_15.setFixedSize(272, 320)

    def button1_click(self):
        end_rank = self.comboBox.currentText()
        end_score = self.lineEdit.text()
        vo = self.lineEdit_2.text()
        da = self.lineEdit_3.text()
        vi = self.lineEdit_4.text()
        end_score = int(end_score)
        vo = int(vo)
        da = int(da)
        vi = int(vi)
        self.set_data(None, end_rank, end_score, vo, da, vi)
        rank, score = self.get_result()
        self.textBrowser.setText(str(score))
        self.textBrowser_2.setText(rank)

    def button2_click(self):
        end_rank = self.comboBox_3.currentText()
        target_rank = self.comboBox_2.currentText()
        vo = self.lineEdit_5.text()
        da = self.lineEdit_6.text()
        vi = self.lineEdit_7.text()
        vo = int(vo)
        da = int(da)
        vi = int(vi)
        #print(target_rank, end_rank, vo, da, vi)
        self.set_data(target_rank, end_rank, None, vo, da, vi)
        bottom = top = 0
        try:
            bottom, top = self.get_result()
            self.textBrowser_3.setText(str(bottom))
            self.textBrowser_4.setText(str(top))
        except ValueError as e:
            if str(e) == 'bottom too big':
                bottom = '无法达到'
                top = '无法达到'
            elif str(e) == 'top too big':
                top = '无法达到'
                bottom = self.remain_cal.get_bottom()
            self.textBrowser_3.setText(str(bottom))
            self.textBrowser_4.setText(str(top))

    def set_data(self, wanted_rank, end_rank, end_score, vo, da, vi):
        self.end_rank = end_rank
        self.wanted_rank = wanted_rank
        self.end_score = end_score
        if self.end_rank:
            self.end_rank = hanzi2str[self.end_rank]
        self.vo = vo
        self.da = da
        self.vi = vi
        if self.tabWidget.currentIndex() == 1:
            self.remain_cal = get_remain_cal()
            self.remain_cal.set_data(self.wanted_rank, self.end_rank, self.vo, self.da, self.vi)
        elif self.tabWidget.currentIndex() == 0:
            self.cal = get_rank_cal()
            self.cal.set_data(self.end_rank, self.end_score, self.vo, self.da, self.vi)
        elif self.tabWidget.currentIndex() == 3:
            self.cal = get_need_score_cal()
            self.cal.set_data(self.need_score, self.end_rank, self.vo, self.da, self.vi)

    def get_data(self):
        return self.wanted_rank, self.end_rank, self.end_score, self.vo, self.da, self.vi
    
    def get_result(self):
        if self.tabWidget.currentIndex() == 1:
            return self.remain_cal.get_required_score()
        elif self.tabWidget.currentIndex() == 0:
            return self.cal.get_rank(), self.cal.get_score()
        elif self.tabWidget.currentIndex() == 3:
            return self.cal.get_required_score()
        
    def button3_click(self):
        if not self.button3_status:
            self.start_show()
            self.image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        else:
            self.stop_show()

    def start_show(self):
        self.button3_status = True
        self.pushButton_3.setText('停止')
        self.textBrowser_5.setText('今天p：')
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next_image)
        self.timer.start(100)

    def stop_show(self):
        self.button3_status = False
        self.pushButton_3.setText('开始')
        self.timer.stop()
        self.show_random_image()

    def show_next_image(self):
        if not self.image_files:
            return
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        image_path  = os.path.join(self.image_folder, self.image_files[self.current_image_index])
        self.show_image(image_path)

    def show_random_image(self):
        if not self.image_files:
            return
        random_image = random.choice(self.image_files)
        image_path = os.path.join(self.image_folder, random_image)
        name = random_image.split('.')[0]
        name = romaji2hanzi[name]
        if name in ['星南', '美铃']:
            self.textBrowser_5.setText('今天接着睡')
        elif name=='亚纱里':
            self.textBrowser_5.setText('毛球：你是不是和亚纱里老师出轨了')
        elif name=='邦夫':
            self.textBrowser_5.setText('今天p…，这个能p吗')
        else:
            self.textBrowser_5.setText('今天p：' + name)
        self.show_image(image_path)

    def show_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.label_15.setPixmap(pixmap.scaled(self.label_15.size(), Qt.KeepAspectRatio))

    def button4_click(self):
        end_rank = self.comboBox_4.currentText()
        self.need_score = self.lineEdit_9.text()
        vo = self.lineEdit_10.text()
        da = self.lineEdit_11.text()
        vi = self.lineEdit_8.text()
        vo = int(vo)
        da = int(da)
        vi = int(vi)
        self.need_score = int(self.need_score)
        self.set_data(None, end_rank, None, vo, da, vi)
        bottom = top = 0
        try:
            bottom, top = self.get_result()
            self.textBrowser_7.setText(str(bottom))
            self.textBrowser_6.setText(str(top))
        except ValueError as e:
            if str(e) == 'bottom too big':
                bottom = '无法达到'
                top = '无法达到'
            elif str(e) == 'top too big':
                top = '无法达到'
                bottom = self.remain_cal.get_bottom()
            self.textBrowser_7.setText(str(bottom))
            self.textBrowser_6.setText(str(top))

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    #mainWindow.setWindowTitle("学马士")
    mainWindow.show()
    sys.exit(app.exec_())
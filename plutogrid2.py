import pyqtgraph as pg
from PyQt6 import QtCore, QtGui, QtWidgets
import soundcard as sc
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 822)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\signal.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 590, 751, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Markers_btn = QtWidgets.QScrollArea(parent=self.verticalLayoutWidget)
        self.Markers_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Markers_btn.setWidgetResizable(True)
        self.Markers_btn.setObjectName("Markers_btn")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 747, 85))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(0, 0, 21, 91))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 395, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Measurements_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Measurements_btn.setMaximumSize(QtCore.QSize(120, 120))
        self.Measurements_btn.setStyleSheet("background-color: rgb(129, 117, 255);\n"
"color: rgb(255, 255, 255);")
        self.Measurements_btn.setObjectName("Measurements_btn")
        self.horizontalLayout.addWidget(self.Measurements_btn)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 90, 242);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.Scales_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.Scales_btn.setMaximumSize(QtCore.QSize(120, 120))
        self.Scales_btn.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Scales_btn.setObjectName("Scales_btn")
        self.horizontalLayout.addWidget(self.Scales_btn)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.Markers_btn.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.Markers_btn)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(290, 540, 751, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.red_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.red_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.red_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\red.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.red_btn.setIcon(icon1)
        self.red_btn.setObjectName("red_btn")
        self.horizontalLayout_2.addWidget(self.red_btn)
        self.print_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.print_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.print_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\print.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.print_btn.setIcon(icon2)
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout_2.addWidget(self.print_btn)
        self.blue_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.blue_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.blue_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\bluee.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.blue_btn.setIcon(icon3)
        self.blue_btn.setObjectName("blue_btn")
        self.horizontalLayout_2.addWidget(self.blue_btn)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\H.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.horizontalLayoutWidget_2)
        self.graphicsView_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_2.addWidget(self.graphicsView_3)
        self.frequncynless_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.frequncynless_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frequncynless_btn.setText("")
        self.frequncynless_btn.setIcon(icon)
        self.frequncynless_btn.setObjectName("frequncynless_btn")
        self.horizontalLayout_2.addWidget(self.frequncynless_btn)
        self.frequncymore_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.frequncymore_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frequncymore_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\pulse.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.frequncymore_btn.setIcon(icon5)
        self.frequncymore_btn.setObjectName("frequncymore_btn")
        self.horizontalLayout_2.addWidget(self.frequncymore_btn)
        self.graphicsView_5 = QtWidgets.QGraphicsView(parent=self.horizontalLayoutWidget_2)
        self.graphicsView_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_2.addWidget(self.graphicsView_5)
        self.left_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.left_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.left_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.left_btn.setIcon(icon6)
        self.left_btn.setObjectName("left_btn")
        self.horizontalLayout_2.addWidget(self.left_btn)
        self.right_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.right_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.right_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\right-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.right_btn.setIcon(icon7)
        self.right_btn.setObjectName("right_btn")
        self.horizontalLayout_2.addWidget(self.right_btn)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_10.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\letter-t.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.graphicsView_6 = QtWidgets.QGraphicsView(parent=self.horizontalLayoutWidget_2)
        self.graphicsView_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.horizontalLayout_2.addWidget(self.graphicsView_6)
        self.down_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.down_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.down_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\arrow-down-sign-to-navigate.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.down_btn.setIcon(icon9)
        self.down_btn.setObjectName("down_btn")
        self.horizontalLayout_2.addWidget(self.down_btn)
        self.up_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.up_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.up_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Users\\asus\\gui\\../Downloads/upload (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.up_btn.setIcon(icon10)
        self.up_btn.setObjectName("up_btn")
        self.horizontalLayout_2.addWidget(self.up_btn)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 20, 251, 20))
        self.label.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.graphicsView_2 = pg.PlotWidget(parent=self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(13, 71, 491, 451))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.More_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.More_btn.setGeometry(QtCore.QRect(20, 540, 261, 28))
        self.More_btn.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.More_btn.setObjectName("More_btn")
        self.Deleteall_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Deleteall_btn.setGeometry(QtCore.QRect(20, 590, 261, 28))
        self.Deleteall_btn.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.Deleteall_btn.setObjectName("Deleteall_btn")
        self.graphicsView = pg.PlotWidget(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(551, 71, 491, 451))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.thread_record = threading.Thread(target=ui.record_sound)
        self.thread_play = threading.Thread(target=ui.play_sound)

# Start the threads
        self.thread_record.start()
        self.thread_play.start()

        
        # Shared Buffer variable
        self.Buffer = None

# Lock for synchronization
        self.lock = threading.Lock()
        
# Flag to signal threads to stop
        self.stop_threads = False
        
        self.record_sound()
        self.play_sound()
        
        self.update_time()  # เรียกใช้เมธอดเพื่อแสดงเวลาทันที
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # อัปเดตทุกๆ 1000 มิลลิวินาที (1 วินาที)
        self.timer.timeout.connect(self.record_sound)
        self.timer.timeout.connect(self.play_sound)
        self.pushButton.clicked.connect(self.Logout_btn_Check)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Measurements_btn.setText(_translate("MainWindow", "Measurements"))
        self.pushButton_2.setText(_translate("MainWindow", "Markers"))
        self.Scales_btn.setText(_translate("MainWindow", "Scales"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Current Time"))
        self.More_btn.setText(_translate("MainWindow", "More (1 of 2 )"))
        self.Deleteall_btn.setText(_translate("MainWindow", "Delete All"))
           
    def update_time(self):
        current_time = QtCore.QTime.currentTime()
        time_string = current_time.toString("hh:mm:ss")
        self.label.setText("Current time: " + time_string)
    def Logout_btn_Check(self):
        print("Logout Button Clicked!")
        QtWidgets.QApplication.quit()
    def update_function(self):
 
        print("หมดเวลาสนุกแล้วสิ")


        
    def record_sound(self):
        usbmic = sc.get_microphone('Realtek High Definition Audio')
        with usbmic.recorder(samplerate=48000) as mic:

                
            for _ in range(100):  # Enforce loop for 20 iterations
                if self.stop_threads:
                    break

            data = mic.record(numframes=1024)
            scaled_data = data * 1000  # Scale the 
            for i in range(100):
                with self.lock:
                        self.Buffer = scaled_data

                        print(self.Buffer[i][0])

                        
            
    def play_sound(self):
        
        usbsp = sc.get_speaker('Realtek High Definition Audio')
        with usbsp.player(samplerate=48000) as sp:
        
            for _ in range(20):  # Enforce loop for 20 iterations
                if self.stop_threads:
                    break

            with self.lock:
                sp.play(self.Buffer)  # Use the original Buffer, not scaled

                self.update_plot(self.Buffer)
        
            
    def update_plot(self, data):
        # Update the plot with the provided data
        self.graphicsView_2.clear()
        self.graphicsView_2.plot(data[0], pen='b')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

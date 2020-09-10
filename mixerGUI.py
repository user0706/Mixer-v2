# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mixer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 666)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setStyleSheet("background-color: #7989ff;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("min-height: 30px;\n"
"max-height: 30px;\n"
"min-width: 32.319px;\n"
"max-width: 32.319px;\n"
"margin-left:20px;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/img/img/mixer.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("min-width: 95.486px;\n"
"max-width: 95.486px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border:    0px;\n"
"    border-top: 1px; \n"
"    border-style: solid;\n"
"    border-color: rgb(194, 194, 194);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background:  rgba(255, 255, 255, 0%);\n"
"    color: #444;\n"
"    border: 0px;\n"
"    min-height: 30;\n"
"    max-height: 30;\n"
"    padding-right:10px;\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QTabBar::tab:hover    {\n"
"    background:  rgba(255, 255, 255, 0%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: #7989ff;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: #7989ff; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: #c8c8c8; /* same as pane color */\n"
"    color: #c8c8c8;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.ImportTab = QtWidgets.QWidget()
        self.ImportTab.setObjectName("ImportTab")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.ImportTab)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.ImportTab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("margin-bottom: 5px;\n"
"margin-top: 10px;")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.ImportTab)
        self.label_14.setStyleSheet("min-width:350px;\n"
"max-width:350px;\n"
"margin-bottom: 25px;")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_16.addWidget(self.label_14)
        self.CSVCloudRadioButton = QtWidgets.QRadioButton(self.ImportTab)
        self.CSVCloudRadioButton.setEnabled(True)
        self.CSVCloudRadioButton.setStyleSheet("QRadioButton::indicator    {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/img/img/rb_option_two.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::disabled {\n"
"    image: url(:/img/img/rb_disabled.png);\n"
"}")
        self.CSVCloudRadioButton.setObjectName("CSVCloudRadioButton")
        self.verticalLayout_16.addWidget(self.CSVCloudRadioButton)
        self.CloudCSVImportWidget = QtWidgets.QWidget(self.ImportTab)
        self.CloudCSVImportWidget.setStyleSheet("")
        self.CloudCSVImportWidget.setObjectName("CloudCSVImportWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.CloudCSVImportWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.CloudCSVImportWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.URLLineEdit = QtWidgets.QLineEdit(self.CloudCSVImportWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.URLLineEdit.setFont(font)
        self.URLLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:360px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.URLLineEdit.setObjectName("URLLineEdit")
        self.horizontalLayout_8.addWidget(self.URLLineEdit, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.URLValidationLabel = QtWidgets.QLabel(self.CloudCSVImportWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.URLValidationLabel.setFont(font)
        self.URLValidationLabel.setObjectName("URLValidationLabel")
        self.verticalLayout_7.addWidget(self.URLValidationLabel)
        self.verticalLayout_16.addWidget(self.CloudCSVImportWidget)
        self.CSVLocalRadioButton = QtWidgets.QRadioButton(self.ImportTab)
        self.CSVLocalRadioButton.setStyleSheet("QRadioButton::indicator    {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/img/img/rb_option_two.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::disabled {\n"
"    image: url(:/img/img/rb_disabled.png);\n"
"}")
        self.CSVLocalRadioButton.setObjectName("CSVLocalRadioButton")
        self.verticalLayout_16.addWidget(self.CSVLocalRadioButton)
        self.LocalCSVImportWidget = QtWidgets.QWidget(self.ImportTab)
        self.LocalCSVImportWidget.setEnabled(True)
        self.LocalCSVImportWidget.setStyleSheet("")
        self.LocalCSVImportWidget.setObjectName("LocalCSVImportWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.LocalCSVImportWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.LocalCSVImportWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.PathLineEdit = QtWidgets.QLineEdit(self.LocalCSVImportWidget)
        self.PathLineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.PathLineEdit.setFont(font)
        self.PathLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.PathLineEdit.setObjectName("PathLineEdit")
        self.horizontalLayout_9.addWidget(self.PathLineEdit, 0, QtCore.Qt.AlignLeft)
        self.LocalCSVPushButton = QtWidgets.QPushButton(self.LocalCSVImportWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.LocalCSVPushButton.setFont(font)
        self.LocalCSVPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LocalCSVPushButton.setStyleSheet("QPushButton#LocalCSVPushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#LocalCSVPushButton:hover {\n"
"    background-color: rgba(0,0,0,.2);\n"
"}\n"
"\n"
"QPushButton#LocalCSVPushButton:pressed {\n"
"    background-color: rgba(0,0,0,.25);     \n"
"}\n"
"\n"
"QPushButton#LocalCSVPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.LocalCSVPushButton.setObjectName("LocalCSVPushButton")
        self.horizontalLayout_9.addWidget(self.LocalCSVPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.PathValidationLabel = QtWidgets.QLabel(self.LocalCSVImportWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PathValidationLabel.setFont(font)
        self.PathValidationLabel.setObjectName("PathValidationLabel")
        self.verticalLayout_8.addWidget(self.PathValidationLabel)
        self.verticalLayout_16.addWidget(self.LocalCSVImportWidget)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem4)
        self.LoadingLabel = QtWidgets.QLabel(self.ImportTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LoadingLabel.setFont(font)
        self.LoadingLabel.setObjectName("LoadingLabel")
        self.horizontalLayout_29.addWidget(self.LoadingLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem5)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem6)
        self.ImportPushButton = QtWidgets.QPushButton(self.ImportTab)
        self.ImportPushButton.setStyleSheet("QPushButton#ImportPushButton {\n"
"    min-width:80px;\n"
"    max-width:80px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #7989ff;\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: #7989ff;\n"
"    border-radius: 15;\n"
"\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#ImportPushButton:hover {\n"
"    background-color: rgb(110, 126, 231);\n"
"    border-color: rgb(110, 126, 231);\n"
"}\n"
"\n"
"QPushButton#ImportPushButton:pressed {\n"
"    background-color: rgb(101, 116, 214);\n"
"    border-color: rgb(101, 116, 214);\n"
"}")
        self.ImportPushButton.setObjectName("ImportPushButton")
        self.verticalLayout_16.addWidget(self.ImportPushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_16)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.tabWidget.addTab(self.ImportTab, "")
        self.ShemaTab = QtWidgets.QWidget()
        self.ShemaTab.setObjectName("ShemaTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ShemaTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalFrame = QtWidgets.QFrame(self.ShemaTab)
        self.verticalFrame.setStyleSheet("margin-right:10px;")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_22 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("margin-bottom: 5px;\n"
"margin-top: 5px;")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalFrame)
        self.label_23.setStyleSheet("min-width:220px;\n"
"max-width:220px;\n"
"margin-bottom: 20px;")
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.TargetComboBox = QtWidgets.QComboBox(self.verticalFrame)
        self.TargetComboBox.setStyleSheet("QComboBox#TargetComboBox    {\n"
"    min-width:200px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox#TargetComboBox:drop-down    {\n"
"    border:0px;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QComboBox#TargetComboBox:down-arrow    {\n"
"    right:3px;\n"
"    width: 10px;\n"
"    image: url(:/img/img/dd_arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 0px;\n"
"    background:  #ebebeb;\n"
"    color: #495057;\n"
"}")
        self.TargetComboBox.setObjectName("TargetComboBox")
        self.verticalLayout_5.addWidget(self.TargetComboBox)
        self.TargetValidationLabel = QtWidgets.QLabel(self.verticalFrame)
        self.TargetValidationLabel.setObjectName("TargetValidationLabel")
        self.verticalLayout_5.addWidget(self.TargetValidationLabel)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.label_25 = QtWidgets.QLabel(self.verticalFrame)
        self.label_25.setStyleSheet("min-width:220px;\n"
"max-width:220px;\n"
"margin-top:50px;\n"
"margin-bottom: 10px;")
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_5.addWidget(self.label_25)
        self.ApplyShemaPushButton = QtWidgets.QPushButton(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ApplyShemaPushButton.setFont(font)
        self.ApplyShemaPushButton.setStyleSheet("QPushButton#ApplyShemaPushButton {\n"
"    min-width:80px;\n"
"    max-width:80px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #7989ff;\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: #7989ff;\n"
"    border-radius: 15;\n"
"\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#ApplyShemaPushButton:hover {\n"
"    background-color: rgb(110, 126, 231);\n"
"    border-color: rgb(110, 126, 231);\n"
"}\n"
"\n"
"QPushButton#ApplyShemaPushButton:pressed {\n"
"    background-color: rgb(101, 116, 214);\n"
"    border-color: rgb(101, 116, 214);\n"
"}")
        self.ApplyShemaPushButton.setObjectName("ApplyShemaPushButton")
        self.verticalLayout_5.addWidget(self.ApplyShemaPushButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.verticalFrame)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ManageColumnsWidget = QtWidgets.QWidget(self.ShemaTab)
        self.ManageColumnsWidget.setObjectName("ManageColumnsWidget")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.ManageColumnsWidget)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_15 = QtWidgets.QLabel(self.ManageColumnsWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("margin-bottom: 5px;\n"
"margin-top: 10px;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_33.addWidget(self.label_15)
        self.label_20 = QtWidgets.QLabel(self.ManageColumnsWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_33.addWidget(self.label_20)
        self.ManageColumnsScrollArea = QtWidgets.QScrollArea(self.ManageColumnsWidget)
        self.ManageColumnsScrollArea.setWidgetResizable(True)
        self.ManageColumnsScrollArea.setObjectName("ManageColumnsScrollArea")
        self.ManageColumnsScrollAreaWidgetContents = QtWidgets.QWidget()
        self.ManageColumnsScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 148))
        self.ManageColumnsScrollAreaWidgetContents.setObjectName("ManageColumnsScrollAreaWidgetContents")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.ManageColumnsScrollAreaWidgetContents)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.ManageColumnsScrollArea.setWidget(self.ManageColumnsScrollAreaWidgetContents)
        self.verticalLayout_33.addWidget(self.ManageColumnsScrollArea)
        self.ColumnsValidationLabel = QtWidgets.QLabel(self.ManageColumnsWidget)
        self.ColumnsValidationLabel.setObjectName("ColumnsValidationLabel")
        self.verticalLayout_33.addWidget(self.ColumnsValidationLabel)
        self.verticalWidget = QtWidgets.QWidget(self.ManageColumnsWidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_11.setContentsMargins(1, 1, -1, 1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_33.addWidget(self.verticalWidget)
        self.verticalLayout_6.addWidget(self.ManageColumnsWidget)
        self.TargetFeaturesWidget = QtWidgets.QWidget(self.ShemaTab)
        self.TargetFeaturesWidget.setEnabled(True)
        self.TargetFeaturesWidget.setObjectName("TargetFeaturesWidget")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.TargetFeaturesWidget)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_16 = QtWidgets.QLabel(self.TargetFeaturesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("margin-bottom: 5px;\n"
"margin-top: 10px;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_32.addWidget(self.label_16)
        self.label_21 = QtWidgets.QLabel(self.TargetFeaturesWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_32.addWidget(self.label_21)
        self.TargetFeaturesScrollArea = QtWidgets.QScrollArea(self.TargetFeaturesWidget)
        self.TargetFeaturesScrollArea.setWidgetResizable(True)
        self.TargetFeaturesScrollArea.setObjectName("TargetFeaturesScrollArea")
        self.TargetFeaturesScrollAreaWidgetContents = QtWidgets.QWidget()
        self.TargetFeaturesScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 174))
        self.TargetFeaturesScrollAreaWidgetContents.setObjectName("TargetFeaturesScrollAreaWidgetContents")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.TargetFeaturesScrollAreaWidgetContents)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.TargetFeaturesScrollArea.setWidget(self.TargetFeaturesScrollAreaWidgetContents)
        self.verticalLayout_32.addWidget(self.TargetFeaturesScrollArea)
        self.verticalLayout_6.addWidget(self.TargetFeaturesWidget)
        self.verticalWidget_5 = QtWidgets.QWidget(self.ShemaTab)
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_6.addWidget(self.verticalWidget_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.ShemaTab, "")
        self.AnalyzeTab = QtWidgets.QWidget()
        self.AnalyzeTab.setObjectName("AnalyzeTab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.AnalyzeTab)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.AnalyzeTab)
        self.scrollArea_2.setStyleSheet("min-width:250px;\n"
"max-width:250px;\n"
"border:0px;\n"
"background-color: rgba(255, 255, 255,0);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 250, 30))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.line_5 = QtWidgets.QFrame(self.AnalyzeTab)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_7.addWidget(self.line_5)
        self.tableWidget = QtWidgets.QTableWidget(self.AnalyzeTab)
        self.tableWidget.setStyleSheet("border:0px;")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.AnalyzeTab, "")
        self.TrainTab = QtWidgets.QWidget()
        self.TrainTab.setObjectName("TrainTab")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.TrainTab)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_31 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.label_36 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("margin-top: 20px;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_10.addWidget(self.label_36)
        self.ModelNameLineEdit = QtWidgets.QLineEdit(self.TrainTab)
        self.ModelNameLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}")
        self.ModelNameLineEdit.setObjectName("ModelNameLineEdit")
        self.verticalLayout_10.addWidget(self.ModelNameLineEdit)
        self.ModelNameValidationLabel = QtWidgets.QLabel(self.TrainTab)
        self.ModelNameValidationLabel.setObjectName("ModelNameValidationLabel")
        self.verticalLayout_10.addWidget(self.ModelNameValidationLabel)
        self.label_33 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("margin-top: 20px;")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_10.addWidget(self.label_33)
        self.label_35 = QtWidgets.QLabel(self.TrainTab)
        self.label_35.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_10.addWidget(self.label_35)
        self.TrainOptionComboBox = QtWidgets.QComboBox(self.TrainTab)
        self.TrainOptionComboBox.setStyleSheet("QComboBox#TrainOptionComboBox    {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox#TrainOptionComboBox:drop-down    {\n"
"    border:0px;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QComboBox#TrainOptionComboBox:down-arrow    {\n"
"    right:3px;\n"
"    width: 10px;\n"
"    image: url(:/img/img/dd_arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 0px;\n"
"    background:  #ebebeb;\n"
"    color: #495057;\n"
"}")
        self.TrainOptionComboBox.setObjectName("TrainOptionComboBox")
        self.verticalLayout_10.addWidget(self.TrainOptionComboBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_34 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("margin-top: 20px;")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_5.addWidget(self.label_34)
        self.TrainTestParametersInfoPushButton = QtWidgets.QPushButton(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TrainTestParametersInfoPushButton.setFont(font)
        self.TrainTestParametersInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.TrainTestParametersInfoPushButton.setObjectName("TrainTestParametersInfoPushButton")
        self.horizontalLayout_5.addWidget(self.TrainTestParametersInfoPushButton, 0, QtCore.Qt.AlignBottom)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.label_38 = QtWidgets.QLabel(self.TrainTab)
        self.label_38.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_10.addWidget(self.label_38)
        self.TestTrainParametersLineEdit = QtWidgets.QLineEdit(self.TrainTab)
        self.TestTrainParametersLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}")
        self.TestTrainParametersLineEdit.setObjectName("TestTrainParametersLineEdit")
        self.verticalLayout_10.addWidget(self.TestTrainParametersLineEdit)
        self.TestTrainParametersValidationLabel = QtWidgets.QLabel(self.TrainTab)
        self.TestTrainParametersValidationLabel.setObjectName("TestTrainParametersValidationLabel")
        self.verticalLayout_10.addWidget(self.TestTrainParametersValidationLabel)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(0, 10, -1, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_32 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_13.addWidget(self.label_32, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_39 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("margin-top: 15px;")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_6.addWidget(self.label_39)
        self.ClassifierParametersInfoPushButton = QtWidgets.QPushButton(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ClassifierParametersInfoPushButton.setFont(font)
        self.ClassifierParametersInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.ClassifierParametersInfoPushButton.setObjectName("ClassifierParametersInfoPushButton")
        self.horizontalLayout_6.addWidget(self.ClassifierParametersInfoPushButton, 0, QtCore.Qt.AlignBottom)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        self.label_37 = QtWidgets.QLabel(self.TrainTab)
        self.label_37.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_13.addWidget(self.label_37)
        self.ClassifierParametersLineEdit = QtWidgets.QLineEdit(self.TrainTab)
        self.ClassifierParametersLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}")
        self.ClassifierParametersLineEdit.setObjectName("ClassifierParametersLineEdit")
        self.verticalLayout_13.addWidget(self.ClassifierParametersLineEdit)
        self.ClassifierParametersValidationLabel = QtWidgets.QLabel(self.TrainTab)
        self.ClassifierParametersValidationLabel.setStyleSheet("margin-bottom: 15px;")
        self.ClassifierParametersValidationLabel.setObjectName("ClassifierParametersValidationLabel")
        self.verticalLayout_13.addWidget(self.ClassifierParametersValidationLabel)
        self.CountVectorizerWidget = QtWidgets.QWidget(self.TrainTab)
        self.CountVectorizerWidget.setObjectName("CountVectorizerWidget")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.CountVectorizerWidget)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.CountVectorizerCadioButton = QtWidgets.QRadioButton(self.CountVectorizerWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CountVectorizerCadioButton.setFont(font)
        self.CountVectorizerCadioButton.setStyleSheet("QRadioButton::indicator    {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/img/img/rb_option_two.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::disabled {\n"
"    image: url(:/img/img/rb_disabled.png);\n"
"}")
        self.CountVectorizerCadioButton.setObjectName("CountVectorizerCadioButton")
        self.horizontalLayout_10.addWidget(self.CountVectorizerCadioButton)
        self.CountVectParametersInfoPushButton = QtWidgets.QPushButton(self.CountVectorizerWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.CountVectParametersInfoPushButton.setFont(font)
        self.CountVectParametersInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.CountVectParametersInfoPushButton.setObjectName("CountVectParametersInfoPushButton")
        self.horizontalLayout_10.addWidget(self.CountVectParametersInfoPushButton)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.verticalLayout_22.addLayout(self.horizontalLayout_10)
        self.label_46 = QtWidgets.QLabel(self.CountVectorizerWidget)
        self.label_46.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_46.setWordWrap(True)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_22.addWidget(self.label_46)
        self.CountVectorizerParametersLineEdit = QtWidgets.QLineEdit(self.CountVectorizerWidget)
        self.CountVectorizerParametersLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.CountVectorizerParametersLineEdit.setObjectName("CountVectorizerParametersLineEdit")
        self.verticalLayout_22.addWidget(self.CountVectorizerParametersLineEdit)
        self.CounVectorizerParametersValidationLabel = QtWidgets.QLabel(self.CountVectorizerWidget)
        self.CounVectorizerParametersValidationLabel.setStyleSheet("margin-bottom: 15px;")
        self.CounVectorizerParametersValidationLabel.setObjectName("CounVectorizerParametersValidationLabel")
        self.verticalLayout_22.addWidget(self.CounVectorizerParametersValidationLabel)
        self.verticalLayout_13.addWidget(self.CountVectorizerWidget)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.TfIdfTransformerRadioButton = QtWidgets.QRadioButton(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TfIdfTransformerRadioButton.setFont(font)
        self.TfIdfTransformerRadioButton.setStyleSheet("QRadioButton::indicator    {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/img/img/rb_option_two.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/img/img/rb_option_one.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::disabled {\n"
"    image: url(:/img/img/rb_disabled.png);\n"
"}")
        self.TfIdfTransformerRadioButton.setObjectName("TfIdfTransformerRadioButton")
        self.horizontalLayout_12.addWidget(self.TfIdfTransformerRadioButton)
        self.TfIdfVectParametersInfoPushButton = QtWidgets.QPushButton(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TfIdfVectParametersInfoPushButton.setFont(font)
        self.TfIdfVectParametersInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.TfIdfVectParametersInfoPushButton.setObjectName("TfIdfVectParametersInfoPushButton")
        self.horizontalLayout_12.addWidget(self.TfIdfVectParametersInfoPushButton)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.TfIdfTransformerWidget = QtWidgets.QWidget(self.TrainTab)
        self.TfIdfTransformerWidget.setObjectName("TfIdfTransformerWidget")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.TfIdfTransformerWidget)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_47 = QtWidgets.QLabel(self.TfIdfTransformerWidget)
        self.label_47.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_47.setWordWrap(True)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_23.addWidget(self.label_47)
        self.TfIdfTransformerParametersLineEdit = QtWidgets.QLineEdit(self.TfIdfTransformerWidget)
        self.TfIdfTransformerParametersLineEdit.setEnabled(True)
        self.TfIdfTransformerParametersLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.TfIdfTransformerParametersLineEdit.setObjectName("TfIdfTransformerParametersLineEdit")
        self.verticalLayout_23.addWidget(self.TfIdfTransformerParametersLineEdit)
        self.TfIdfTransformerParametersValidationLabel = QtWidgets.QLabel(self.TfIdfTransformerWidget)
        self.TfIdfTransformerParametersValidationLabel.setObjectName("TfIdfTransformerParametersValidationLabel")
        self.verticalLayout_23.addWidget(self.TfIdfTransformerParametersValidationLabel)
        self.verticalLayout_13.addWidget(self.TfIdfTransformerWidget)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem18)
        self.horizontalLayout_14.addLayout(self.verticalLayout_13)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem19)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.PunctuationCheckBox = QtWidgets.QCheckBox(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PunctuationCheckBox.setFont(font)
        self.PunctuationCheckBox.setStyleSheet("QCheckBox::indicator {\n"
"    width: 29.596px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/img/cb_option_two.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/cb_option_one.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/img/img/cb_option_one.png);\n"
"}")
        self.PunctuationCheckBox.setObjectName("PunctuationCheckBox")
        self.verticalLayout_24.addWidget(self.PunctuationCheckBox)
        self.label_48 = QtWidgets.QLabel(self.TrainTab)
        self.label_48.setStyleSheet("min-width:300px;\n"
"max-width:300px;\n"
"margin-bottom: 20px;")
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_24.addWidget(self.label_48)
        self.LowerCaseCheckBox = QtWidgets.QCheckBox(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LowerCaseCheckBox.setFont(font)
        self.LowerCaseCheckBox.setStyleSheet("QCheckBox::indicator {\n"
"    width: 29.596px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/img/cb_option_two.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(:/img/img/cb_option_one.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/img/img/cb_option_one.png);\n"
"}")
        self.LowerCaseCheckBox.setObjectName("LowerCaseCheckBox")
        self.verticalLayout_24.addWidget(self.LowerCaseCheckBox)
        self.label_53 = QtWidgets.QLabel(self.TrainTab)
        self.label_53.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_53.setWordWrap(True)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_24.addWidget(self.label_53)
        self.label_50 = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("margin-top: 20px;")
        self.label_50.setObjectName("label_50")
        self.verticalLayout_24.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.TrainTab)
        self.label_51.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_51.setWordWrap(True)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_24.addWidget(self.label_51)
        self.StopWordsComboBox = QtWidgets.QComboBox(self.TrainTab)
        self.StopWordsComboBox.setStyleSheet("QComboBox#StopWordsComboBox    {\n"
"    min-width:300px;\n"
"    max-width:300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox#StopWordsComboBox:drop-down    {\n"
"    border:0px;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QComboBox#StopWordsComboBox:down-arrow    {\n"
"    right:3px;\n"
"    width: 10px;\n"
"    image: url(:/img/img/dd_arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 0px;\n"
"    background:  #ebebeb;\n"
"    color: #495057;\n"
"}")
        self.StopWordsComboBox.setObjectName("StopWordsComboBox")
        self.verticalLayout_24.addWidget(self.StopWordsComboBox)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem20)
        self.horizontalLayout_14.addLayout(self.verticalLayout_24)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.verticalLayout_14.addLayout(self.horizontalLayout_14)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem22)
        self.TrainLoadingLabel = QtWidgets.QLabel(self.TrainTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TrainLoadingLabel.setFont(font)
        self.TrainLoadingLabel.setObjectName("TrainLoadingLabel")
        self.verticalLayout_14.addWidget(self.TrainLoadingLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem23)
        self.TrainModelPushButton = QtWidgets.QPushButton(self.TrainTab)
        self.TrainModelPushButton.setStyleSheet("QPushButton#TrainModelPushButton {\n"
"    min-width:80px;\n"
"    max-width:80px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #7989ff;\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: #7989ff;\n"
"    border-radius: 15;\n"
"\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#TrainModelPushButton:hover {\n"
"    background-color: rgb(110, 126, 231);\n"
"    border-color: rgb(110, 126, 231);\n"
"}\n"
"\n"
"QPushButton#TrainModelPushButton:pressed {\n"
"    background-color: rgb(101, 116, 214);\n"
"    border-color: rgb(101, 116, 214);\n"
"}")
        self.TrainModelPushButton.setObjectName("TrainModelPushButton")
        self.verticalLayout_14.addWidget(self.TrainModelPushButton, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.TrainTab, "")
        self.EvaluationTab = QtWidgets.QWidget()
        self.EvaluationTab.setObjectName("EvaluationTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.EvaluationTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.EvaluationTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_49 = QtWidgets.QLabel(self.EvaluationTab)
        self.label_49.setStyleSheet("min-width:300px;\n"
"max-width:300px;")
        self.label_49.setWordWrap(True)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_3.addWidget(self.label_49)
        self.ChooseComboBox = QtWidgets.QComboBox(self.EvaluationTab)
        self.ChooseComboBox.setStyleSheet("QComboBox#ChooseComboBox    {\n"
"    min-width:300px;\n"
"    max-width: 300px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox#ChooseComboBox:drop-down    {\n"
"    border:0px;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QComboBox#ChooseComboBox:down-arrow    {\n"
"    right:3px;\n"
"    width: 10px;\n"
"    image: url(:/img/img/dd_arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 0px;\n"
"    background:  #ebebeb;\n"
"    color: #495057;\n"
"}")
        self.ChooseComboBox.setObjectName("ChooseComboBox")
        self.verticalLayout_3.addWidget(self.ChooseComboBox)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.EvaluationTab)
        self.scrollArea_3.setStyleSheet("margin-top:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 659, 421))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem24)
        self.verticalWidget_51 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalWidget_51.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;")
        self.verticalWidget_51.setObjectName("verticalWidget_51")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalWidget_51)
        self.verticalLayout_17.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_24 = QtWidgets.QLabel(self.verticalWidget_51)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.TargetNumberEvaluationLabel = QtWidgets.QLabel(self.verticalWidget_51)
        self.TargetNumberEvaluationLabel.setObjectName("TargetNumberEvaluationLabel")
        self.verticalLayout_17.addWidget(self.TargetNumberEvaluationLabel)
        self.horizontalLayout_2.addWidget(self.verticalWidget_51)
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.verticalWidget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalWidget_6.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;")
        self.verticalWidget_6.setObjectName("verticalWidget_6")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_18.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_27 = QtWidgets.QLabel(self.verticalWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_18.addWidget(self.label_27)
        self.ClassifierNameEvaluationLabel = QtWidgets.QLabel(self.verticalWidget_6)
        self.ClassifierNameEvaluationLabel.setObjectName("ClassifierNameEvaluationLabel")
        self.verticalLayout_18.addWidget(self.ClassifierNameEvaluationLabel)
        self.horizontalLayout_2.addWidget(self.verticalWidget_6)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_2.addWidget(self.line_9)
        self.verticalWidget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalWidget_7.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;")
        self.verticalWidget_7.setObjectName("verticalWidget_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_19.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_40 = QtWidgets.QLabel(self.verticalWidget_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_19.addWidget(self.label_40)
        self.TestedNumberEvaluationLabel = QtWidgets.QLabel(self.verticalWidget_7)
        self.TestedNumberEvaluationLabel.setObjectName("TestedNumberEvaluationLabel")
        self.verticalLayout_19.addWidget(self.TestedNumberEvaluationLabel)
        self.horizontalLayout_2.addWidget(self.verticalWidget_7)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_8.setStyleSheet("")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.verticalWidget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalWidget_8.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;")
        self.verticalWidget_8.setObjectName("verticalWidget_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.verticalWidget_8)
        self.horizontalLayout_15.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.AccuracyPixLabel = QtWidgets.QLabel(self.verticalWidget_8)
        self.AccuracyPixLabel.setStyleSheet("min-width:50px;\n"
"max-width:50px;\n"
"min-height:50px;\n"
"max-height:50px;")
        self.AccuracyPixLabel.setText("")
        self.AccuracyPixLabel.setScaledContents(True)
        self.AccuracyPixLabel.setObjectName("AccuracyPixLabel")
        self.horizontalLayout_15.addWidget(self.AccuracyPixLabel)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_42 = QtWidgets.QLabel(self.verticalWidget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("min-width:80px;\n"
"max-width:80px;")
        self.label_42.setObjectName("label_42")
        self.verticalLayout_25.addWidget(self.label_42)
        self.AccuracyNumberEvaluationLabel = QtWidgets.QLabel(self.verticalWidget_8)
        self.AccuracyNumberEvaluationLabel.setStyleSheet("min-width:80px;\n"
"max-width:80px;")
        self.AccuracyNumberEvaluationLabel.setWordWrap(True)
        self.AccuracyNumberEvaluationLabel.setObjectName("AccuracyNumberEvaluationLabel")
        self.verticalLayout_25.addWidget(self.AccuracyNumberEvaluationLabel)
        self.horizontalLayout_15.addLayout(self.verticalLayout_25)
        self.horizontalLayout_2.addWidget(self.verticalWidget_8)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem25)
        self.verticalLayout_29.addLayout(self.horizontalLayout_2)
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_6.setStyleSheet("border:0px;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_29.addWidget(self.line_6)
        self.DateTimeEvaluationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DateTimeEvaluationLabel.setFont(font)
        self.DateTimeEvaluationLabel.setStyleSheet("margin-top:10px;\n"
"padding-left:10px;\n"
"min-height:30px;\n"
"background-color: #ebebeb;")
        self.DateTimeEvaluationLabel.setWordWrap(True)
        self.DateTimeEvaluationLabel.setObjectName("DateTimeEvaluationLabel")
        self.verticalLayout_29.addWidget(self.DateTimeEvaluationLabel)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 15, 0, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(14, -1, -1, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_3)
        self.scrollArea_4.setStyleSheet("min-width:250px;\n"
"max-width:250px;\n"
"border:0px;\n"
"background-color: rgba(255, 255, 255,0);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 250, 16))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_15.addWidget(self.scrollArea_4)
        self.horizontalLayout_17.addLayout(self.verticalLayout_15)
        self.line_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_15.setStyleSheet("")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout_17.addWidget(self.line_15)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(-1, -1, 23, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("min-width:60px;\n"
"max-width:60px;")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_20.addWidget(self.label_29)
        self.F1InfoPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.F1InfoPushButton.setFont(font)
        self.F1InfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.F1InfoPushButton.setObjectName("F1InfoPushButton")
        self.horizontalLayout_20.addWidget(self.F1InfoPushButton, 0, QtCore.Qt.AlignBottom)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem26)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_20.addWidget(self.label_41, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_21.addLayout(self.horizontalLayout_20)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_21.addWidget(self.line_10)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("min-width:60px;\n"
"max-width:60px;")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_21.addWidget(self.label_43)
        self.AccuracyInfoPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.AccuracyInfoPushButton.setFont(font)
        self.AccuracyInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.AccuracyInfoPushButton.setObjectName("AccuracyInfoPushButton")
        self.horizontalLayout_21.addWidget(self.AccuracyInfoPushButton)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem27)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_21.addWidget(self.label_44)
        self.verticalLayout_21.addLayout(self.horizontalLayout_21)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_21.addWidget(self.line_11)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("min-width:60px;\n"
"max-width:60px;")
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_23.addWidget(self.label_55)
        self.PrecisionInfoPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PrecisionInfoPushButton.setFont(font)
        self.PrecisionInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.PrecisionInfoPushButton.setObjectName("PrecisionInfoPushButton")
        self.horizontalLayout_23.addWidget(self.PrecisionInfoPushButton)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem28)
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_23.addWidget(self.label_56)
        self.verticalLayout_21.addLayout(self.horizontalLayout_23)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_21.addWidget(self.line_12)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("min-width:60px;\n"
"max-width:60px;")
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_24.addWidget(self.label_57)
        self.RecallInfoPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RecallInfoPushButton.setFont(font)
        self.RecallInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.RecallInfoPushButton.setObjectName("RecallInfoPushButton")
        self.horizontalLayout_24.addWidget(self.RecallInfoPushButton)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem29)
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_24.addWidget(self.label_58)
        self.verticalLayout_21.addLayout(self.horizontalLayout_24)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_21.addWidget(self.line_13)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem30)
        self.horizontalLayout_25.addLayout(self.verticalLayout_21)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem31)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem32)
        self.verticalLayout_30.addLayout(self.horizontalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_60 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_22.addWidget(self.label_60)
        self.ConfusionMatrixInfoPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ConfusionMatrixInfoPushButton.setFont(font)
        self.ConfusionMatrixInfoPushButton.setStyleSheet("    min-width:14px;\n"
"    max-width:14px;\n"
"    min-height:14px;\n"
"    max-height:14px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  #666666;\n"
"    border: 1px;\n"
"    border-style: solid;\n"
"    border-color: #666666;\n"
"    border-radius: 7;")
        self.ConfusionMatrixInfoPushButton.setObjectName("ConfusionMatrixInfoPushButton")
        self.horizontalLayout_22.addWidget(self.ConfusionMatrixInfoPushButton)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem33)
        self.verticalLayout_26.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.ConfusionMatrixPixLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ConfusionMatrixPixLabel.setStyleSheet("")
        self.ConfusionMatrixPixLabel.setText("")
        self.ConfusionMatrixPixLabel.setScaledContents(False)
        self.ConfusionMatrixPixLabel.setObjectName("ConfusionMatrixPixLabel")
        self.horizontalLayout_26.addWidget(self.ConfusionMatrixPixLabel)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem34)
        self.verticalLayout_26.addLayout(self.horizontalLayout_26)
        self.verticalLayout_30.addLayout(self.verticalLayout_26)
        self.horizontalLayout_17.addLayout(self.verticalLayout_30)
        self.verticalLayout_29.addLayout(self.horizontalLayout_17)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.EvaluationTab, "")
        self.TestTab = QtWidgets.QWidget()
        self.TestTab.setObjectName("TestTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TestTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 80, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem35)
        self.TestLineEdit = QtWidgets.QLineEdit(self.TestTab)
        self.TestLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:350px;\n"
"    max-width:350px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.TestLineEdit.setObjectName("TestLineEdit")
        self.horizontalLayout_3.addWidget(self.TestLineEdit, 0, QtCore.Qt.AlignHCenter)
        self.TestSubmitPushButton = QtWidgets.QPushButton(self.TestTab)
        self.TestSubmitPushButton.setStyleSheet("QPushButton#TestSubmitPushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#TestSubmitPushButton:hover {\n"
"    background-color: rgba(0,0,0,.2);\n"
"}\n"
"\n"
"QPushButton#TestSubmitPushButton:pressed {\n"
"    background-color: rgba(0,0,0,.25);     \n"
"}\n"
"\n"
"QPushButton#TestSubmitPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.TestSubmitPushButton.setObjectName("TestSubmitPushButton")
        self.horizontalLayout_3.addWidget(self.TestSubmitPushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem36)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.TestTab)
        self.scrollArea_5.setStyleSheet("min-width:410px;\n"
"max-width:410px;\n"
"border:0px;\n"
"background-color: rgba(255, 255, 255,0);")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 410, 16))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_2.addWidget(self.scrollArea_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem37)
        self.tabWidget.addTab(self.TestTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mixer"))
        self.label_3.setText(_translate("MainWindow", "MIXER"))
        self.label_13.setText(_translate("MainWindow", "Import your data"))
        self.label_14.setText(_translate("MainWindow", "The Mixer uses tabular data that you import to train the model. Your dataset must have a minimum of two columns (sentences, targets)."))
        self.CSVCloudRadioButton.setText(_translate("MainWindow", "CSV from cloud"))
        self.label_17.setText(_translate("MainWindow", "Imported CSV dataset must be UTF-8 (comma delimited)"))
        self.URLLineEdit.setPlaceholderText(_translate("MainWindow", "Enter URL"))
        self.URLValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.CSVLocalRadioButton.setText(_translate("MainWindow", "CSV from local"))
        self.label_19.setText(_translate("MainWindow", "Imported CSV dataset must be UTF-8 (comma delimited)"))
        self.PathLineEdit.setPlaceholderText(_translate("MainWindow", "Enter lacal path"))
        self.LocalCSVPushButton.setText(_translate("MainWindow", "Browse"))
        self.PathValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.LoadingLabel.setText(_translate("MainWindow", "Loading ..."))
        self.ImportPushButton.setText(_translate("MainWindow", "Import"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImportTab), _translate("MainWindow", "Import"))
        self.label_22.setText(_translate("MainWindow", "*Select a target"))
        self.label_23.setText(_translate("MainWindow", "Select the column that represents the target. That is, a column with target values."))
        self.TargetValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.label_25.setText(_translate("MainWindow", "Before proceeding, it is advisable to check once again whether everything is done as desired."))
        self.ApplyShemaPushButton.setText(_translate("MainWindow", "Continue"))
        self.label_15.setText(_translate("MainWindow", "*Manage columns"))
        self.label_20.setText(_translate("MainWindow", "The required and sufficient number of selected targets is two (sentences, targets)."))
        self.ColumnsValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.label_16.setText(_translate("MainWindow", "Target features"))
        self.label_21.setText(_translate("MainWindow", "It is necessary to select the desired target values. Only the selected options will be considered when creating the model."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ShemaTab), _translate("MainWindow", "Schema"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnalyzeTab), _translate("MainWindow", "Analyze"))
        self.label_31.setText(_translate("MainWindow", "Train model"))
        self.label_36.setText(_translate("MainWindow", "*Model name"))
        self.ModelNameValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.label_33.setText(_translate("MainWindow", "*Choose a classifier"))
        self.label_35.setText(_translate("MainWindow", "Only one classifier can be selected. \n"
"Depending on the choice of classifier, it is possible to get a more or less accurately trained model."))
        self.label_34.setText(_translate("MainWindow", "Test-Train parameters"))
        self.TrainTestParametersInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_38.setText(_translate("MainWindow", "Specify additional parameters for dividing the dataset into train and test subset. \n"
"Default ratio is 75:25%"))
        self.TestTrainParametersValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.label_32.setText(_translate("MainWindow", "Additional parameters"))
        self.label_39.setText(_translate("MainWindow", "Classifier parameters"))
        self.ClassifierParametersInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_37.setText(_translate("MainWindow", "Possible additional parameters for the classifier depend on the choice of classifier. \n"
"The default classifier is Multinomial Naive Bayes."))
        self.ClassifierParametersValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.CountVectorizerCadioButton.setText(_translate("MainWindow", "Count Vectorizer"))
        self.CountVectParametersInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_46.setText(_translate("MainWindow", "Convert a collection of text documents to a matrix of token counts."))
        self.CounVectorizerParametersValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.TfIdfTransformerRadioButton.setText(_translate("MainWindow", "Tf-Idf Vectorizer"))
        self.TfIdfVectParametersInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_47.setText(_translate("MainWindow", "Convert a collection of raw documents to a matrix of TF-IDF features."))
        self.TfIdfTransformerParametersValidationLabel.setText(_translate("MainWindow", "Validation result information"))
        self.PunctuationCheckBox.setText(_translate("MainWindow", "Punctuation"))
        self.label_48.setText(_translate("MainWindow", "(Removal of punctuation marks, except apostrophes.)"))
        self.LowerCaseCheckBox.setText(_translate("MainWindow", "Lower case"))
        self.label_53.setText(_translate("MainWindow", "(Converting sentences to lowercase)"))
        self.label_50.setText(_translate("MainWindow", "Stop words"))
        self.label_51.setText(_translate("MainWindow", "Remove stop words for the selected language."))
        self.TrainLoadingLabel.setText(_translate("MainWindow", "Loading ..."))
        self.TrainModelPushButton.setText(_translate("MainWindow", "Train model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrainTab), _translate("MainWindow", "Train"))
        self.label.setText(_translate("MainWindow", "Model"))
        self.label_49.setText(_translate("MainWindow", "Choose one of the pre-trained models. \n"
"Testing of the selected model is possible in the Test tab. \n"
"The last trained model is always chosen as the debault."))
        self.label_24.setText(_translate("MainWindow", "Target"))
        self.TargetNumberEvaluationLabel.setText(_translate("MainWindow", "None"))
        self.label_27.setText(_translate("MainWindow", "Classifier"))
        self.ClassifierNameEvaluationLabel.setText(_translate("MainWindow", "None"))
        self.label_40.setText(_translate("MainWindow", "Tested"))
        self.TestedNumberEvaluationLabel.setText(_translate("MainWindow", "None"))
        self.label_42.setText(_translate("MainWindow", "Accuracy"))
        self.AccuracyNumberEvaluationLabel.setText(_translate("MainWindow", "None"))
        self.DateTimeEvaluationLabel.setText(_translate("MainWindow", "None"))
        self.label_29.setText(_translate("MainWindow", "F1 score"))
        self.F1InfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_41.setText(_translate("MainWindow", "None"))
        self.label_43.setText(_translate("MainWindow", "Accuracy"))
        self.AccuracyInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_44.setText(_translate("MainWindow", "None"))
        self.label_55.setText(_translate("MainWindow", "Precision"))
        self.PrecisionInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_56.setText(_translate("MainWindow", "None"))
        self.label_57.setText(_translate("MainWindow", "Recall"))
        self.RecallInfoPushButton.setText(_translate("MainWindow", "?"))
        self.label_58.setText(_translate("MainWindow", "None"))
        self.label_60.setText(_translate("MainWindow", "Confusion matrix"))
        self.ConfusionMatrixInfoPushButton.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EvaluationTab), _translate("MainWindow", "Evaluation"))
        self.TestSubmitPushButton.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TestTab), _translate("MainWindow", "Test"))
import style_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

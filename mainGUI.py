# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workspaceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 269)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.WorkspaceDirLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.WorkspaceDirLineEdit.setStyleSheet("QLineEdit {\n"
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
        self.WorkspaceDirLineEdit.setObjectName("WorkspaceDirLineEdit")
        self.horizontalLayout.addWidget(self.WorkspaceDirLineEdit)
        self.BackupDirPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackupDirPushButton.setStyleSheet("QPushButton#BackupDirPushButton {\n"
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
"QPushButton#BackupDirPushButton:hover {\n"
"    background-color: rgba(0,0,0,.2);\n"
"}\n"
"\n"
"QPushButton#BackupDirPushButton:pressed {\n"
"    background-color: rgba(0,0,0,.25);     \n"
"}\n"
"\n"
"QPushButton#BackupDirPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.BackupDirPushButton.setObjectName("BackupDirPushButton")
        self.horizontalLayout.addWidget(self.BackupDirPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.WorkspaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.WorkspaceLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.WorkspaceLabel.setObjectName("WorkspaceLabel")
        self.verticalLayout.addWidget(self.WorkspaceLabel)
        self.WorkspaceCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.WorkspaceCheckBox.setObjectName("WorkspaceCheckBox")
        self.verticalLayout.addWidget(self.WorkspaceCheckBox)
        self.MainSubmitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainSubmitPushButton.setStyleSheet("QPushButton#MainSubmitPushButton {\n"
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
"QPushButton#MainSubmitPushButton:hover {\n"
"    background-color: rgb(110, 126, 231);\n"
"    border-color: rgb(110, 126, 231);\n"
"}\n"
"\n"
"QPushButton#MainSubmitPushButton:pressed {\n"
"    background-color: rgb(101, 116, 214);\n"
"    border-color: rgb(101, 116, 214);\n"
"}")
        self.MainSubmitPushButton.setObjectName("MainSubmitPushButton")
        self.verticalLayout.addWidget(self.MainSubmitPushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workspace"))
        self.label.setText(_translate("MainWindow", "Workspace directory"))
        self.label_2.setText(_translate("MainWindow", "Enter a location or select the directory where the trained models will be stored."))
        self.BackupDirPushButton.setText(_translate("MainWindow", "Browse"))
        self.WorkspaceLabel.setText(_translate("MainWindow", "Error"))
        self.WorkspaceCheckBox.setText(_translate("MainWindow", "Don\'t ask me again"))
        self.MainSubmitPushButton.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

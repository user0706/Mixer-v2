from mainGUI import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import os
import os.path
import subprocess

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#Brojac predstavlja index slobodnog elementa baze
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.WorkspaceLabel.hide()
		self.ui.BackupDirPushButton.clicked.connect(self.DirPath)
		self.ui.MainSubmitPushButton.clicked.connect(self.Submit)

		self.DontShowStatus = False
		self.directoryPath = None
		self.SYSPATH = os.getenv("SystemDrive")

		self.Main()

	def Main(self):
		subprocess.check_call(["attrib","-H","{}\\Mixer_Config.txt".format(self.SYSPATH)])
		if os.path.isfile("{}\\Mixer_Config.txt".format(self.SYSPATH)):
			config = open("{}\\Mixer_Config.txt".format(self.SYSPATH),"r")
			info = config.read().split('\n')
			config.close()
			#subprocess.check_call(["attrib","+H","{}\\Mixer_Config.txt".format(self.SYSPATH)])

			if info[0] == "True":
				os.system('python mixer.py')
				sys.exit()
		else:
			config = open("{}\\Mixer_Config.txt".format(self.SYSPATH),"w")
			config.close()

		

	def DirPath(self):
		'''
		:
		'''
		self.directoryPath = QFileDialog.getExistingDirectory(self, 'Workspace directory')
		self.ui.WorkspaceDirLineEdit.setText(self.directoryPath)

	def Submit(self):

		self.DontShowStatus = self.ui.WorkspaceCheckBox.isChecked()
		self.directoryPath = self.ui.WorkspaceDirLineEdit.text()
		self.directoryPath = self.directoryPath.replace('/','\\')

		if self.directoryPath:
			subprocess.check_call(["attrib","-H","{}\\Mixer_Config.txt".format(self.SYSPATH)])
			if not os.path.isfile("{}\\Mixer_Config.txt".format(self.SYSPATH)):
				emptyFile = open("{}\\Mixer_Config.txt".format(self.SYSPATH),"w") 
				emptyFile.close()
			if self.DontShowStatus:
				config = open("{}\\Mixer_Config.txt".format(self.SYSPATH),"w")
				config.write(str(True)+'\n')
				config.write(self.directoryPath)
				config.close()
			else:
				config = open("{}\\Mixer_Config.txt".format(self.SYSPATH),"w")
				config.write(str(False)+'\n')
				config.write(self.directoryPath)
				config.close()
			#subprocess.check_call(["attrib","+H","{}\\Mixer_Config.txt".format(self.SYSPATH)])
			os.system('python mixer.py')
			sys.exit()
		else:
			self.ui.WorkspaceLabel.show()



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())
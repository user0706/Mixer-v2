from mixerGUI import *
from functions import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import pickle

from collections import Counter

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import seaborn as sn
import matplotlib.pyplot as plt

from PIL import Image

import webbrowser

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#Brojac predstavlja index slobodnog elementa baze
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ModelNames, self.ModelPaths = getModelList(str(WorkspaceDir())+"\\")

		self.ErrorFlag = False

		self.ui.tabWidget.setTabEnabled(0, True)
		self.ui.tabWidget.setTabEnabled(1, False)
		self.ui.tabWidget.setTabEnabled(2, False)
		self.ui.tabWidget.setTabEnabled(3, False)
		if self.ModelNames:
			self.ui.tabWidget.setTabEnabled(4, True)
			self.ui.tabWidget.setTabEnabled(5, True)
		else:
			self.ui.tabWidget.setTabEnabled(4, False)
			self.ui.tabWidget.setTabEnabled(5, False)

		self.ui.TrainTestParametersInfoPushButton.clicked.connect(self.Info1)
		self.ui.ClassifierParametersInfoPushButton.clicked.connect(self.Info2)
		self.ui.CountVectParametersInfoPushButton.clicked.connect(self.Info3)
		self.ui.TfIdfVectParametersInfoPushButton.clicked.connect(self.Info4)
		self.ui.F1InfoPushButton.clicked.connect(self.Info5)
		self.ui.AccuracyInfoPushButton.clicked.connect(self.Info6)
		self.ui.PrecisionInfoPushButton.clicked.connect(self.Info7)
		self.ui.RecallInfoPushButton.clicked.connect(self.Info8)
		self.ui.ConfusionMatrixInfoPushButton.clicked.connect(self.Info9)

		########################
		# IMPORT TAB VARIABLES #
		########################
		self.RawData = None
		self.FlagCloudCSVImportWidget = None
		self.FlagLocalCSVImportWidget = None

		self.ui.CloudCSVImportWidget.setEnabled(False)
		self.ui.LocalCSVImportWidget.setEnabled(False)
		self.ui.URLValidationLabel.hide()
		self.ui.PathValidationLabel.hide()
		self.ui.LoadingLabel.hide()

		self.ui.CSVCloudRadioButton.toggled.connect(lambda:self.CSVCloudRadioButtonFunction(self.ui.CSVCloudRadioButton))
		self.ui.CSVLocalRadioButton.toggled.connect(lambda:self.CSVLocalRadioButtonFunction(self.ui.CSVLocalRadioButton))

		self.ui.LocalCSVPushButton.clicked.connect(self.LocalCSVChooseDir)
		self.ui.ImportPushButton.clicked.connect(self.ImportPushButtonFunction)

		#######################
		# SHEMA TAB VARIABLES #
		#######################
		self.HeaderElements = []
		self.TargetFeatureElements = None
		self.SelectedTarget = None
		self.FlagApplyShemaPushButton = None
		self.ManageColumnsResults = None
		self.TargetFeaturesResults = None
		self.EndData = None
		
		self.frame = None
		self.horizontalLayout = None
		self.listLabel = None
		self.SelectedTargetSignalLabel = None
		self.listCheckBox = None
		self.ManageColumnsResults = None

		self.TargetFeatureFrame = None
		self.TargetFeatureHorizontalLayout = None
		self.TargetFeatureListLabel = None
		self.TargetFeatureTypeLabel = None
		self.TargetFeatureListCheckBox = None
		self.TargetFeaturesResults = None

		self.ui.TargetValidationLabel.hide()
		self.ui.ColumnsValidationLabel.hide()

		self.ui.TargetComboBox.currentIndexChanged.connect(self.TargetComboBoxSelection)
		self.ui.ApplyShemaPushButton.clicked.connect(self.SubmitShema)

		#########################
		# ANALYZE TAB VARIABLES #
		#########################
		self.AnalizeTabInfoWidget = None
		self.AnalizeTabinfoWidgetLayout = None
		self.AnalizeTabInfoLeftLabel = None
		self.AnalizeTabInfoRightLabel = None

		self.TargetFeaturesNames = None

		#######################
		# TRAIN TAB VARIABLES #
		#######################
		self.ui.TrainLoadingLabel.hide()

		self.NameValidationState = None
		self.TestTrainParametersValidationState = None
		self.FlagCountVectorizerRadioButton = None
		self.FlagTfIdfTransformerRadioButton = None
		self.SelectedClassifier = None
		self.ClassifierList = 	['MultinomialNB',
								'GaussianNB',
								'ComplementNB',
								'BernoulliNB',
								'CategoricalNB']

		self.ui.TrainModelPushButton.clicked.connect(self.SubmitTrain)

		self.ui.ModelNameValidationLabel.hide()
		self.ui.TestTrainParametersValidationLabel.hide()
		self.ui.ClassifierParametersValidationLabel.hide()
		self.ui.CounVectorizerParametersValidationLabel.hide()
		self.ui.TfIdfTransformerParametersValidationLabel.hide()

		self.ui.TrainOptionComboBox.currentIndexChanged.connect(self.ClassifierComboBoxSelection)

		self.ui.CountVectorizerCadioButton.toggled.connect(lambda:self.CountVectorizerRadioButtonFunction(self.ui.CountVectorizerCadioButton))
		self.ui.TfIdfTransformerRadioButton.toggled.connect(lambda:self.TfIdfTransformerRadioButtonFunction(self.ui.TfIdfTransformerRadioButton))
		self.ui.CountVectorizerCadioButton.setChecked(True)
		self.ui.TfIdfTransformerRadioButton.setChecked(False)
		self.UpdateClassifierComboBox()

		self.SelectedStopWords = False
		self.SelectedStopWordsData = None
		MoveStopWords()
		self.StopWordsLanguages, self.StopWordsData = LoadStopWords()
		self.UpdateStopWordsComboBox()

		############################
		# EVALUATION TAB VARIABLES #
		############################

		self.EvaluationTabInfoWidget = None
		self.EvaluationTabinfoWidgetLayout = None
		self.EvaluationTabInfoLeftLabel = None
		self.EvaluationTabInfoRightLabel = None

		self.modelInfo = None

		self.SelectedModel = self.ui.ChooseComboBox.currentText()

		self.ui.ChooseComboBox.currentIndexChanged.connect(self.ModelComboBoxSelection)
		self.UpdateModelComboBox()

		######################
		# TEST TAB VARIABLES #
		######################

		self.ui.TestSubmitPushButton.clicked.connect(self.TestSubmit)
		self.TestInfoWidget = None
		self.TestinfoWidgetLayout = None
		self.TestInfoLeftLabel = None
		self.TestInfoRightLabel = None

	def Info1(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html', new=2)
	def Info2(self):
		webbrowser.open('https://scikit-learn.org/stable/supervised_learning.html', new=2)
	def Info3(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html', new=2)
	def Info4(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html', new=2)
	def Info5(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html', new=2)
	def Info6(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html', new=2)
	def Info7(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html', new=2)
	def Info8(self):
		webbrowser.open('https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html', new=2)
	def Info9(self):
		webbrowser.open('https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html', new=2)

	def DisableEnableWidget(self, trueWidget, falseWidget, trueWidgetFlag, falseWidgetFlag, validationLabel, lineEdit):
		trueWidget.setEnabled(True)
		falseWidget.setEnabled(False)
		trueWidgetFlag = True
		falseWidgetFlag = False
		validationLabel.hide()
		lineEdit.setText(None)

	def UpdateComboBox(self, comboBoxName, listData):
		comboBoxName.clear()

		for option in listData:
			comboBoxName.addItem(option)
	
	##############################################################################
	############################ IMPORT TAB FUNCTIONS ############################
	##############################################################################
	def CSVCloudRadioButtonFunction(self, s):
		if s.isChecked() == True:
			'''
			:If CSVCloudRadioButton is active,
			 it activates the cloud widget or deactivates the path widget.
			'''
			self.ui.CloudCSVImportWidget.setEnabled(True)
			self.ui.LocalCSVImportWidget.setEnabled(False)
			self.FlagCloudCSVImportWidget = True
			self.FlagLocalCSVImportWidget = False
			self.ui.PathValidationLabel.hide()
			self.ui.PathLineEdit.setText(None)

	def CSVLocalRadioButtonFunction(self, s):
		if s.isChecked() == True:
			'''
			:If CSVPathRadioButton is active,
			 it activates the path widget or deactivates the cloud widget.
			'''
			self.ui.LocalCSVImportWidget.setEnabled(True)
			self.ui.CloudCSVImportWidget.setEnabled(False)
			self.FlagLocalCSVImportWidget = True
			self.FlagCloudCSVImportWidget = False
			self.ui.URLValidationLabel.hide()
			self.ui.URLLineEdit.setText(None)

	def LocalCSVChooseDir(self):
		'''
		:The function is activated with the LocalCSVPushButton button,
		 which is used to select the desired CSV file.
		'''
		Path = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\QSJHAISASJ\\Desktop', "Data files (*.csv)")
		self.ui.PathLineEdit.setText(Path[0])

	def ProcessingImportTabLineEdit(self, widgetFlag, lineEdit, validationLabel):
		'''
		:If the flag for the corresponding widget is active, ie if the 
			current path entry option is selected, the current text is read from 
			lineEdit.
		:After reading the path, the correctness is checked as well as loading 
			the dataset
		:If the path is correct (CheckResult is True), positive information is 
			printed on the corresponding label to display the validation 
			results, otherwise negative information.
		'''
		if widgetFlag:
			DatasetPath = lineEdit.text()
			self.CheckResult, self.RawData = URLCheck(DatasetPath)
			if self.CheckResult:
				validationLabel.setText("Loading successful")
				validationLabel.setStyleSheet('color: green')
			else:
				validationLabel.setText("Loading failed")
				validationLabel.setStyleSheet('color: red')
			validationLabel.show()

	def UpdateTargetComboBox(self):
		'''
		######################################################
		# This is a function that operates on the SCHEMA TAB #
		######################################################
		:The header is extracted from RawDat, after which a neutral element 
			is added as the initial value for TargetComboBox
		'''
		self.HeaderElements = list(self.RawData.columns)
		self.HeaderElements.insert(0, "")

		self.UpdateComboBox(self.ui.TargetComboBox, self.HeaderElements)

	def ImportPushButtonFunction(self):
		'''
		:First, it was said that the CheckResult variable was invalid.
		:As such, the CheckResult variable is a security variable that carries 
			information about whether the path entered is true or not.
		:One of the reasons for initially setting CheckResult to False is that 
			initially, the path is not specified.
		:Another reason is to reset the previous state when changing the entry.
		:The entered path is then processed.
		:If the path is correct and the dataset is successfully loaded, it 
			automatically switches to the next (Shema) tab.
		:As soon as it switches to the Shema tab, the TargetComboBox is updated
		'''
		self.CheckResult = False

		self.ui.LoadingLabel.show()
		QApplication.processEvents()

		self.ProcessingImportTabLineEdit(self.FlagCloudCSVImportWidget, self.ui.URLLineEdit, self.ui.URLValidationLabel)
		self.ProcessingImportTabLineEdit(self.FlagLocalCSVImportWidget, self.ui.PathLineEdit, self.ui.PathValidationLabel)
		#CheckFunction("RawData", self.RawData, self.RawData)

		self.ui.LoadingLabel.hide()
		if self.CheckResult:
			self.ui.tabWidget.setTabEnabled(1, True)
			self.ui.tabWidget.setTabEnabled(2, False)
			self.ui.tabWidget.setTabEnabled(3, False)
			if self.ModelNames:
				self.ui.tabWidget.setTabEnabled(4, True)
				self.ui.tabWidget.setTabEnabled(5, True)
			else:
				self.ui.tabWidget.setTabEnabled(4, False)
				self.ui.tabWidget.setTabEnabled(5, False)
			self.ui.tabWidget.setCurrentIndex(1)

		if self.ui.tabWidget.currentIndex() == 1:
			self.UpdateTargetComboBox()
			#CheckFunction("HeaderElements", self.HeaderElements, self.HeaderElements)

			self.frame = list(range(len(self.HeaderElements)))
			self.horizontalLayout = list(range(len(self.HeaderElements)))
			self.listLabel = list(range(len(self.HeaderElements)))
			self.SelectedTargetSignalLabel = list(range(len(self.HeaderElements)))
			self.listCheckBox = list(range(len(self.HeaderElements)))
			self.ManageColumnsResults = list(range(len(self.HeaderElements)))

	#############################################################################
	############################ SHEMA TAB FUNCTIONS ############################
	#############################################################################

	def clearLayout(self, layout):
		'''
		:As the name suggests, it cleans widgets from layout.
		:As long as the layout has items, ie it is not 0, the first (0) item 
			is taken.
		:If the item is a widget, then that widget is deleted.
		'''
		while layout.count():
			child = layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def UpdateManageColumnsScrolArea(self):
		'''
		:Updates item scroll areas.
		:The more items in the HeaderElements list, the more items there will be.
		:The zero (0) element is skipped because it has no meaning and is added 
			to be a neutral state for the comboBox.
		:Then the elements for the widget as well as the widget itself are 
			created, and added to the layout for scrollArea.
		:If the current widget matches the selected target, the light 
			(SelectedTargetSignalLabel) comes on, the checkBox is activated and 
			the possibility of changing its status is turned off.
		'''
		for i, v in enumerate(self.HeaderElements):
			if i != 0:
				self.frame[i] = QtWidgets.QFrame(self.ui.ManageColumnsScrollArea)
				self.frame[i].setStyleSheet("min-height: 25px; max-height: 25px;")
				self.frame[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
				self.frame[i].setFrameShadow(QtWidgets.QFrame.Raised)
				self.frame[i].setObjectName("frame")
				self.horizontalLayout[i] = QtWidgets.QHBoxLayout(self.frame[i])
				self.horizontalLayout[i].setContentsMargins(0, 0, 0, 0)
				self.horizontalLayout[i].setObjectName("horizontalLayout")
				self.listLabel[i] = QtWidgets.QLabel(v)
				self.listLabel[i].setObjectName("label{}".format(i))
				self.horizontalLayout[i].addWidget(self.listLabel[i])
				self.SelectedTargetSignalLabel[i] = QtWidgets.QLabel()
				self.SelectedTargetSignalLabel[i].setStyleSheet("min-width: 10px; max-width: 10px; \nmin-height: 10px; max-height: 10px;\nmargin-left: 5px;")
				self.SelectedTargetSignalLabel[i].setText("")
				self.SelectedTargetSignalLabel[i].setPixmap(QtGui.QPixmap(":/img/img/target_sign.png"))
				self.SelectedTargetSignalLabel[i].setScaledContents(True)
				self.SelectedTargetSignalLabel[i].setObjectName("SelectedTargetSignalLabel")
				self.horizontalLayout[i].addWidget(self.SelectedTargetSignalLabel[i])
				spacerItem = QtWidgets.QSpacerItem(337, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
				self.horizontalLayout[i].addItem(spacerItem)
				self.listCheckBox[i] = QtWidgets.QCheckBox()
				self.listCheckBox[i].setStyleSheet("QCheckBox::indicator {width: 29.596px; height: 20px;}\nQCheckBox::indicator:unchecked {image: url(:/img/img/cb_option_two.png);}\nQCheckBox::indicator:unchecked:pressed {image: url(:/img/img/cb_option_one.png);}\nQCheckBox::indicator:checked {image: url(:/img/img/cb_option_one.png);}")
				self.listCheckBox[i].setObjectName("self.listCheckBox{}".format(i))
				self.horizontalLayout[i].addWidget(self.listCheckBox[i])
				self.ui.verticalLayout_34.addWidget(self.frame[i])

				if v != self.SelectedTarget:
					self.SelectedTargetSignalLabel[i].hide()
				else:
					self.listCheckBox[i].setChecked(True)
					self.listCheckBox[i].setEnabled(False)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_34.addItem(spacerItem)

	def UpdateTargetFeaturesScrolArea(self):
		'''
		:Updates item scroll areas.
		:The more items in the HeaderElements list, the more items there will be.
		:The elements for the widget as well as the widget itself are 
			created, and added to the layout for scrollArea.
		'''
		for i, v in enumerate(self.TargetFeatureElements):
			self.TargetFeatureFrame[i] = QtWidgets.QFrame(self.ui.TargetFeaturesScrollArea)
			self.TargetFeatureFrame[i].setStyleSheet("min-height: 25px; max-height: 25px;")
			self.TargetFeatureFrame[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
			self.TargetFeatureFrame[i].setFrameShadow(QtWidgets.QFrame.Raised)
			self.TargetFeatureFrame[i].setObjectName("frame")
			self.TargetFeatureHorizontalLayout[i] = QtWidgets.QHBoxLayout(self.TargetFeatureFrame[i])
			self.TargetFeatureHorizontalLayout[i].setContentsMargins(0, 0, 0, 0)
			self.TargetFeatureHorizontalLayout[i].setObjectName("horizontalLayout")
			self.TargetFeatureListLabel[i] = QtWidgets.QLabel(str(v))
			self.TargetFeatureListLabel[i].setStyleSheet("min-width: 150px; max-height: 150px;")
			self.TargetFeatureListLabel[i].setObjectName("label{}".format(i))
			self.TargetFeatureHorizontalLayout[i].addWidget(self.TargetFeatureListLabel[i])
			TargetFeatureSpacerItem_1 = QtWidgets.QSpacerItem(337, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
			self.TargetFeatureHorizontalLayout[i].addItem(TargetFeatureSpacerItem_1)
			self.TargetFeatureTypeLabel[i] = QtWidgets.QLabel(str(v.__class__.__name__))
			self.TargetFeatureTypeLabel[i].setObjectName("label{}".format(i))
			self.TargetFeatureHorizontalLayout[i].addWidget(self.TargetFeatureTypeLabel[i])
			TargetFeatureSpacerItem_2 = QtWidgets.QSpacerItem(337, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
			self.TargetFeatureHorizontalLayout[i].addItem(TargetFeatureSpacerItem_2)
			self.TargetFeatureListCheckBox[i] = QtWidgets.QCheckBox()
			self.TargetFeatureListCheckBox[i].setStyleSheet("QCheckBox::indicator {width: 29.596px; height: 20px;}\nQCheckBox::indicator:unchecked {image: url(:/img/img/cb_option_two.png);}\nQCheckBox::indicator:unchecked:pressed {image: url(:/img/img/cb_option_one.png);}\nQCheckBox::indicator:checked {image: url(:/img/img/cb_option_one.png);}")
			self.TargetFeatureListCheckBox[i].setObjectName("checkBox{}".format(i))
			self.TargetFeatureListCheckBox[i].setChecked(True)
			self.TargetFeatureHorizontalLayout[i].addWidget(self.TargetFeatureListCheckBox[i])
			self.ui.verticalLayout_35.addWidget(self.TargetFeatureFrame[i])
		  
		TargetFeatureSpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_35.addItem(TargetFeatureSpacerItem)

	def TargetComboBoxSelection(self):
		'''
		:When the target from the comboBox is selected, the items from the layout 
			for ManageColumnsScrolArea and TargetFeaturesScrolArea are deleted.
		:The validation label is also reset.
		:Taking the selected option from the comboBox and checking it, the variables 
			used to update the widget in TargetFeaturesScrolArea are initialized.
		:As a safety factor, it is checked whether the number of features is greater 
			than 15.
		:If all is well, the item update for scrollAreas will be performed.
		:Otherwise, an error will be displayed.
		'''
		self.clearLayout(self.ui.verticalLayout_34)
		self.clearLayout(self.ui.verticalLayout_35)

		self.ui.TargetValidationLabel.setText("")
		self.ui.TargetValidationLabel.hide()

		self.SelectedTarget = self.ui.TargetComboBox.currentText()

		if self.SelectedTarget:
			self.TargetFeatureElements = list(set(self.RawData[self.SelectedTarget]))

			self.TargetFeatureFrame  = list(range(len(self.TargetFeatureElements)))
			self.TargetFeatureHorizontalLayout  = list(range(len(self.TargetFeatureElements)))
			self.TargetFeatureListLabel  = list(range(len(self.TargetFeatureElements)))
			self.TargetFeatureTypeLabel  = list(range(len(self.TargetFeatureElements)))
			self.TargetFeatureListCheckBox  = list(range(len(self.TargetFeatureElements)))
			self.TargetFeaturesResults = list(range(len(self.TargetFeatureElements)))

			if len(self.TargetFeatureElements) <= 15:
				self.FlagApplyShemaPushButton = True

				self.UpdateManageColumnsScrolArea()
				self.UpdateTargetFeaturesScrolArea()
			else:
				self.ui.TargetValidationLabel.setText("Too many features")
				self.ui.TargetValidationLabel.setStyleSheet('color: red')
				self.ui.TargetValidationLabel.show()

	def ShemaCheckBoxState(self):
		if self.FlagApplyShemaPushButton:
			for i in range(len(self.listCheckBox)):
				if i != 0 and self.listCheckBox[i].isChecked():
					self.ManageColumnsResults[i] = True
				else:
					self.ManageColumnsResults[i] = False

			for i in range(len(self.TargetFeatureListCheckBox)):
				if self.TargetFeatureListCheckBox[i].isChecked():
					self.TargetFeaturesResults[i] = True
				else:
					self.TargetFeaturesResults[i] = False

	def ShemaDataAdaptation(self):
		self.EndData = self.RawData[TrueToName(self.SelectedTarget, self.HeaderElements, self.ManageColumnsResults)]

		TargetFeaturesIndex, self.TargetFeaturesNames = SelectedTargetIndex(self.RawData[self.SelectedTarget], self.TargetFeatureElements, self.TargetFeaturesResults)
	
		self.EndData = self.EndData.iloc[TargetFeaturesIndex, :]

		if self.FlagApplyShemaPushButton:
			self.ui.tabWidget.setTabEnabled(2, True)
			self.ui.tabWidget.setTabEnabled(3, True)
			if self.ModelNames:
				self.ui.tabWidget.setTabEnabled(4, True)
				self.ui.tabWidget.setTabEnabled(5, True)
			else:
				self.ui.tabWidget.setTabEnabled(4, False)
				self.ui.tabWidget.setTabEnabled(5, False)
			self.ui.tabWidget.setCurrentIndex(2)

	#############################################################################
	########################### ANALYZE TAB FUNCTIONS ###########################
	#############################################################################

	def UpdateInfoList(self):
		self.InfoList = [['All target features', self.EndData.shape[0]]]
		for k, v in dict(Counter(self.TargetFeaturesNames)).items():
			self.InfoList.append([k, v])

	def UpdateInfoScrollArea(self):
		for i, v in enumerate(self.InfoList):
			self.AnalizeTabInfoWidget[i] = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents_2)
			self.AnalizeTabInfoWidget[i].setStyleSheet("min-width:230px; max-width:230px; min-height:30px;")
			self.AnalizeTabInfoWidget[i].setObjectName("AnalizeTabInfoWidget[i]")
			self.AnalizeTabinfoWidgetLayout[i] = QtWidgets.QHBoxLayout(self.AnalizeTabInfoWidget[i])
			self.AnalizeTabinfoWidgetLayout[i].setContentsMargins(-1, 1, -1, -1)
			self.AnalizeTabinfoWidgetLayout[i].setObjectName("AnalizeTabinfoWidgetLayout[i]")
			self.AnalizeTabInfoLeftLabel[i] = QtWidgets.QLabel(str(v[0]))
			self.AnalizeTabInfoLeftLabel[i].setStyleSheet("min-width:110px; max-width:110px;")
			self.AnalizeTabInfoLeftLabel[i].setWordWrap(True)
			self.AnalizeTabInfoLeftLabel[i].setObjectName("AnalizeTabInfoLeftLabel[i]")
			self.AnalizeTabinfoWidgetLayout[i].addWidget(self.AnalizeTabInfoLeftLabel[i], 0, QtCore.Qt.AlignLeft)
			self.AnalizeTabInfoRightLabel = QtWidgets.QLabel(str(v[1]))
			self.AnalizeTabInfoRightLabel.setStyleSheet("min-width:90px; max-width:90px;")
			self.AnalizeTabInfoRightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
			self.AnalizeTabInfoRightLabel.setWordWrap(True)
			self.AnalizeTabInfoRightLabel.setObjectName("AnalizeTabInfoRightLabel")
			self.AnalizeTabinfoWidgetLayout[i].addWidget(self.AnalizeTabInfoRightLabel, 0, QtCore.Qt.AlignRight)
			self.ui.verticalLayout_36.addWidget(self.AnalizeTabInfoWidget[i])
		AnalizeTabInfoSpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_36.addItem(AnalizeTabInfoSpacerItem)

	def UpdateTableWidget(self):
		for rowNumber, rowData in enumerate(self.EndData.values.tolist()):
			self.ui.tableWidget.insertRow(rowNumber)
			for colNumber, colData in enumerate(rowData):
				self.ui.tableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))

	def SubmitShema(self):
		self.clearLayout(self.ui.verticalLayout_36)

		self.ui.ColumnsValidationLabel.setText("")
		self.ui.ColumnsValidationLabel.show()
		self.ui.tableWidget.setRowCount(0)

		self.ShemaCheckBoxState()

		if dict(Counter(self.ManageColumnsResults))[True] != 2:
			self.ui.ColumnsValidationLabel.setText("The required and sufficient number of selected columns is two.")
			self.ui.ColumnsValidationLabel.setStyleSheet('color: red')
			self.ui.ColumnsValidationLabel.show()
		else:
			self.ShemaDataAdaptation()
			self.UpdateInfoList()

			self.AnalizeTabInfoWidget = list(range(len(self.InfoList)))
			self.AnalizeTabinfoWidgetLayout = list(range(len(self.InfoList)))
			self.AnalizeTabInfoLeftLabel = list(range(len(self.InfoList)))
			self.AnalizeTabInfoRightLabel = list(range(len(self.InfoList)))

			self.ui.tableWidget.setHorizontalHeaderLabels(TrueToName(self.SelectedTarget, self.HeaderElements, self.ManageColumnsResults))
			self.ui.tableWidget.setRowCount(0)

			header = self.ui.tableWidget.horizontalHeader()
			header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  
			header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

			self.UpdateTableWidget()
			self.UpdateInfoScrollArea()

	###########################################################################
	########################### TRAIN TAB FUNCTIONS ###########################
	###########################################################################

	def UpdateStopWordsComboBox(self):
		self.UpdateComboBox(self.ui.StopWordsComboBox, self.StopWordsLanguages)

	def UpdateClassifierComboBox(self):
		self.UpdateComboBox(self.ui.TrainOptionComboBox, self.ClassifierList)

	def ClassifierComboBoxSelection(self):
		self.SelectedClassifier = self.ui.TrainOptionComboBox.currentText()

	def CountVectorizerRadioButtonFunction(self, s):
		if s.isChecked() == True:
			'''
			:If CSVCloudRadioButton is active,
			 it activates the cloud widget or deactivates the path widget.
			'''
			self.ui.CountVectorizerWidget.setEnabled(True)
			self.ui.TfIdfTransformerWidget.setEnabled(False)
			self.FlagCountVectorizerRadioButton = True
			self.FlagTfIdfTransformerRadioButton = False
			self.ui.CounVectorizerParametersValidationLabel.hide()
			self.ui.TfIdfTransformerParametersLineEdit.setText(None)

	def TfIdfTransformerRadioButtonFunction(self, s):
		if s.isChecked() == True:
			'''
			:If CSVCloudRadioButton is active,
			 it activates the cloud widget or deactivates the path widget.
			'''
			self.ui.TfIdfTransformerWidget.setEnabled(True)
			self.ui.CountVectorizerWidget.setEnabled(False)
			self.FlagTfIdfTransformerRadioButton = True
			self.FlagCountVectorizerRadioButton = False
			self.ui.TfIdfTransformerParametersValidationLabel.hide()
			self.ui.CountVectorizerParametersLineEdit.setText(None)

	def ErrorValidationLabelActions(self, state, label):
		if not state:
			self.ErrorFlag = True
			label.setText("Error")
			label.setStyleSheet('color: red')
			label.show()	
		else:
			label.hide()

	def TrainParametersValidation(self, name, ttparameters, cparameters, cvparameters, tfidfparameters):
		self.ErrorFlag = False

		self.ui.ModelNameValidationLabel.hide()
		self.ui.TestTrainParametersValidationLabel.hide()
		self.ui.ClassifierParametersValidationLabel.hide()

		self.NameValidationState = NameValidation(name)
		self.TestTrainParametersValidationState = TestTrainParametersValidation(ttparameters)
		self.ClassifierParametersValidationState = ClassifierParametersValidation(self.SelectedClassifier, cparameters)
		self.CountVectorizerParametersValidationState = CountVectorizerParametersValidation(cvparameters)
		self.TfIdfTransformerParametersValidationState = TfIdfTransformerParametersValidation(tfidfparameters)

		self.ErrorValidationLabelActions(self.NameValidationState, self.ui.ModelNameValidationLabel)
		self.ErrorValidationLabelActions(self.TestTrainParametersValidationState, self.ui.TestTrainParametersValidationLabel)
		self.ErrorValidationLabelActions(self.ClassifierParametersValidationState, self.ui.ClassifierParametersValidationLabel)
		if self.FlagCountVectorizerRadioButton:
			self.ErrorValidationLabelActions(self.CountVectorizerParametersValidationState, self.ui.CounVectorizerParametersValidationLabel)
		if self.FlagTfIdfTransformerRadioButton:
			self.ErrorValidationLabelActions(self.TfIdfTransformerParametersValidationState, self.ui.TfIdfTransformerParametersValidationLabel)

	def SubmitTrain(self):
		self.ui.TrainLoadingLabel.show()
		QApplication.processEvents()

		modelName = self.ui.ModelNameLineEdit.text()
		testTrainParameters = self.ui.TestTrainParametersLineEdit.text()
		classifierParameters = self.ui.ClassifierParametersLineEdit.text()
		countVectorizer = self.ui.CountVectorizerParametersLineEdit.text()
		tfidfTransformer = self.ui.TfIdfTransformerParametersLineEdit.text()

		punctuationState = self.ui.PunctuationCheckBox.isChecked()
		lowerCaseState = self.ui.LowerCaseCheckBox.isChecked()

		self.TrainParametersValidation(modelName, testTrainParameters, classifierParameters, countVectorizer, tfidfTransformer)
		
		self.SelectedStopWords = self.ui.StopWordsComboBox.currentText()
		self.SelectedStopWordsData = self.StopWordsData.loc[[self.SelectedStopWords]]

		if self.SelectedStopWords == "":
			self.SelectedStopWords = False
		if testTrainParameters == "":
			testTrainParameters = "{}"
		if classifierParameters == "":
			classifierParameters = "{}"
		if countVectorizer == "":
			countVectorizer = "{}"
		if tfidfTransformer == "":
			tfidfTransformer = "{}"

		self.SelectedStopWordsData = list(set([list(row) for index, row in self.SelectedStopWordsData.iterrows()][0]))

		if not self.ErrorFlag:
			TrainInfo = TrainFuction(	modelName,
							self.EndData, 
							self.SelectedClassifier,
							self.FlagTfIdfTransformerRadioButton,
							self.FlagCountVectorizerRadioButton, 
							ast.literal_eval(classifierParameters),
							ast.literal_eval(tfidfTransformer),
							ast.literal_eval(countVectorizer), 
							ast.literal_eval(testTrainParameters), 
							L_Case=lowerCaseState, 
							Pun=punctuationState, 
							S_Word=self.SelectedStopWordsData)
			
			self.ui.tabWidget.setTabEnabled(4, True)
			self.ui.tabWidget.setTabEnabled(5, True)
			self.ui.tabWidget.setCurrentIndex(4)

			SaveModelInfo(modelName, self.SelectedClassifier, testTrainParameters, classifierParameters, self.FlagCountVectorizerRadioButton, countVectorizer, self.FlagTfIdfTransformerRadioButton, tfidfTransformer, punctuationState, lowerCaseState, self.SelectedStopWords, TrainInfo.training_time, TrainInfo.tested, TrainInfo.recall, TrainInfo.precision, TrainInfo.f1, TrainInfo.accuracy, self.SelectedTarget, self.InfoList, TrainInfo.confusion)
			self.ModelNames, self.ModelPaths = getModelList(str(WorkspaceDir())+"\\")
			self.UpdateModelComboBox()

		else:
			print("Error")

		self.ui.TrainLoadingLabel.hide()

	################################################################################
	########################### EVALUATION TAB FUNCTIONS ###########################
	################################################################################

	def UpdateEvaluationInfoScrollArea(self):
		for i, v in enumerate(self.modelInfo['Target info']):
			self.EvaluationTabInfoWidget[i] = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents_3)
			self.EvaluationTabInfoWidget[i].setStyleSheet("min-width:230px; max-width:230px; min-height:30px;")
			self.EvaluationTabInfoWidget[i].setObjectName("EvaluationTabInfoWidget[i]")
			self.EvaluationTabinfoWidgetLayout[i] = QtWidgets.QHBoxLayout(self.EvaluationTabInfoWidget[i])
			self.EvaluationTabinfoWidgetLayout[i].setContentsMargins(-1, 1, -1, -1)
			self.EvaluationTabinfoWidgetLayout[i].setObjectName("EvaluationTabinfoWidgetLayout[i]")
			self.EvaluationTabInfoLeftLabel[i] = QtWidgets.QLabel(str(v[0]))
			self.EvaluationTabInfoLeftLabel[i].setStyleSheet("min-width:110px; max-width:110px;")
			self.EvaluationTabInfoLeftLabel[i].setWordWrap(True)
			self.EvaluationTabInfoLeftLabel[i].setObjectName("EvaluationTabInfoLeftLabel[i]")
			self.EvaluationTabinfoWidgetLayout[i].addWidget(self.EvaluationTabInfoLeftLabel[i], 0, QtCore.Qt.AlignLeft)
			self.EvaluationTabInfoRightLabel = QtWidgets.QLabel(str(v[1]))
			self.EvaluationTabInfoRightLabel.setStyleSheet("min-width:90px; max-width:90px;")
			self.EvaluationTabInfoRightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
			self.EvaluationTabInfoRightLabel.setWordWrap(True)
			self.EvaluationTabInfoRightLabel.setObjectName("EvaluationTabInfoRightLabel")
			self.EvaluationTabinfoWidgetLayout[i].addWidget(self.EvaluationTabInfoRightLabel, 0, QtCore.Qt.AlignRight)
			self.ui.verticalLayout_37.addWidget(self.EvaluationTabInfoWidget[i])
		EvaluationTabInfoSpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_37.addItem(EvaluationTabInfoSpacerItem)

	def UpdateModelComboBox(self):
		self.UpdateComboBox(self.ui.ChooseComboBox, self.ModelNames)

	def UpdateGraphs(self):
		axis = [v[0] for i, v in enumerate(self.modelInfo["Target info"]) if i>0]
		ConfusionMatrixGraph(self.modelInfo["Confusion matrix"], axis, axis)
		subprocess.check_call(["attrib","-H","{}\\confusion.png".format(str(WorkspaceDir()))])
		confusion_pixmap = QPixmap("{}\\confusion.png".format(str(WorkspaceDir())))
		self.ui.ConfusionMatrixPixLabel.setPixmap(confusion_pixmap)
		subprocess.check_call(["attrib","+H","{}\\confusion.png".format(str(WorkspaceDir()))])


		DonutGraph(float(self.modelInfo.Accuracy[:-1]))
		subprocess.check_call(["attrib","-H","{}\\accuracy.png".format(str(WorkspaceDir()))])
		accuracy_pixmap = QPixmap("{}\\accuracy.png".format(str(WorkspaceDir())))
		self.ui.AccuracyPixLabel.setPixmap(accuracy_pixmap)
		subprocess.check_call(["attrib","+H","{}\\accuracy.png".format(str(WorkspaceDir()))])

	def ModelComboBoxSelection(self):
		self.clearLayout(self.ui.verticalLayout_37)

		self.ui.TargetNumberEvaluationLabel.setText(None)
		self.ui.ClassifierNameEvaluationLabel.setText(None)
		self.ui.TestedNumberEvaluationLabel.setText(None)
		self.ui.AccuracyNumberEvaluationLabel.setText(None)

		self.ui.DateTimeEvaluationLabel.setText(None)
		self.ui.label_41.setText(None)
		self.ui.label_44.setText(None)
		self.ui.label_56.setText(None)
		self.ui.label_58.setText(None)

		self.SelectedModel = self.ui.ChooseComboBox.currentText()
		try:
			SelectedModelIndex = self.ModelNames.index(self.SelectedModel)
		except:
			SelectedModelIndex = 0

		path = self.ModelPaths[SelectedModelIndex]
		self.modelInfo = getModelInfo(path)

		self.EvaluationTabInfoWidget = list(range(len(self.modelInfo['Target info'])))
		self.EvaluationTabinfoWidgetLayout = list(range(len(self.modelInfo['Target info'])))
		self.EvaluationTabInfoLeftLabel = list(range(len(self.modelInfo['Target info'])))
		self.EvaluationTabInfoRightLabel = list(range(len(self.modelInfo['Target info'])))

		self.ui.TargetNumberEvaluationLabel.setText(str(self.modelInfo.Target))
		self.ui.ClassifierNameEvaluationLabel.setText(str(self.modelInfo.Classifier))
		self.ui.TestedNumberEvaluationLabel.setText(str(self.modelInfo.Tested))
		self.ui.AccuracyNumberEvaluationLabel.setText(self.modelInfo.Accuracy)

		self.ui.DateTimeEvaluationLabel.setText(str(SecToTime(self.modelInfo['Training time'])))
		self.ui.label_41.setText(str(self.modelInfo.F1))
		self.ui.label_44.setText(str(self.modelInfo.Accuracy))
		self.ui.label_56.setText(str(self.modelInfo.Precision))
		self.ui.label_58.setText(str(self.modelInfo.Recall))

		self.UpdateEvaluationInfoScrollArea()

		self.UpdateGraphs()

	#################################@########################################
	########################### TEST TAB FUNCTIONS ###########################
	##########################################################################
	def UpdateTestInfoScrollArea(self, data):
		val = [float(i[1][:-1]) for i in data]
		maxV = max(val)
		maxElement = val.index(maxV)

		for i, v in enumerate(data):
			if i == maxElement:
				color = '#7989ff'
			else:
				color = '#f2f2f2'
			self.TestInfoWidget[i] = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents_5)
			self.TestInfoWidget[i].setStyleSheet("background-color: {}; min-width:410px; max-width:410px; min-height:20px;".format(color))
			self.TestInfoWidget[i].setObjectName("TestInfoWidget[i]")
			self.TestinfoWidgetLayout[i] = QtWidgets.QHBoxLayout(self.TestInfoWidget[i])
			self.TestinfoWidgetLayout[i].setContentsMargins(-1, 1, -1, -1)
			self.TestinfoWidgetLayout[i].setObjectName("TestinfoWidgetLayout[i]")
			self.TestInfoLeftLabel[i] = QtWidgets.QLabel(str(v[0]))
			self.TestInfoLeftLabel[i].setStyleSheet("min-width:110px; max-width:110px;")
			self.TestInfoLeftLabel[i].setWordWrap(True)
			self.TestInfoLeftLabel[i].setObjectName("TestInfoLeftLabel[i]")
			self.TestinfoWidgetLayout[i].addWidget(self.TestInfoLeftLabel[i], 0, QtCore.Qt.AlignLeft)
			self.TestInfoRightLabel = QtWidgets.QLabel(str(v[1]))
			self.TestInfoRightLabel.setStyleSheet("min-width:90px; max-width:90px;")
			self.TestInfoRightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
			self.TestInfoRightLabel.setWordWrap(True)
			self.TestInfoRightLabel.setObjectName("TestInfoRightLabel")
			self.TestinfoWidgetLayout[i].addWidget(self.TestInfoRightLabel, 0, QtCore.Qt.AlignRight)
			self.ui.verticalLayout_38.addWidget(self.TestInfoWidget[i])
		TestTabInfoSpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_38.addItem(TestTabInfoSpacerItem)

	def TestSubmit(self):
		self.clearLayout(self.ui.verticalLayout_38)
		from joblib import load
		try:
			model, vectorizer, target = load('{}\\{}.joblib'.format(WorkspaceDir(), self.SelectedModel))
		except:
			model, vectorizer, target = load('{}\\{}.joblib'.format(WorkspaceDir(), self.ModelNames[0]))

		string = str(self.ui.TestLineEdit.text())
		try:
			result = Test(string, model, target, vectorizer)

			self.TestInfoWidget = list(range(len(result)))
			self.TestinfoWidgetLayout = list(range(len(result)))
			self.TestInfoLeftLabel = list(range(len(result)))
			self.TestInfoRightLabel = list(range(len(result)))

			self.UpdateTestInfoScrollArea(result)
		except:
			pass
		

		


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())
import pandas as pd
import re
from nltk.tokenize import word_tokenize
import glob
from pathlib import Path
import ast
import numpy as np
import json
import codecs
from shutil import copyfile
import pickle
import os

import seaborn as sn
import matplotlib.pyplot as plt

import os.path
import subprocess

def WorkspaceDir():
	SYSPATH = os.getenv("SystemDrive")

	subprocess.check_call(["attrib","-H","{}\\Mixer_Config.txt".format(SYSPATH)])
	config = open("{}\\Mixer_Config.txt".format(SYSPATH),"r")
	info = config.read().split('\n')
	config.close()
	subprocess.check_call(["attrib","+H","{}\\Mixer_Config.txt".format(SYSPATH)])

	return info[1]

def Punctuation(inSentence):
	'''
	:Removes all punctuation marks except apostrophes (') from the string
	'''
	inSentence = inSentence.replace('?', '')
	return re.sub(r"[^\w\d'\s]+", '', inSentence)

def LowerCase(inSentence):
	'''
	:Converts all characters of a string to a lowercase
	'''
	return inSentence.lower()

def Cleaning(inSentence, L_Case, Pun, S_Word):
	'''
	:Applies functions to convert characters to lowercase as well as to punctuation.
	'''
	if L_Case:
	  inSentence = LowerCase(inSentence)
	if Pun:
	  inSentence = Punctuation(inSentence)
	if S_Word:
	  tokenized = word_tokenize(inSentence)
	  inSentence = " ".join([word for word in tokenized if word not in S_Word])
	return inSentence

def CheckFunction(text, variableType, variableValue):
	'''
	:Displays the data type and the value of a particular variable. 
	:Used to track variables.
	'''
	#print("### CHEKC => {0} Type:\n{1}\n### CHEKC => {0}: \n{2}".format(text, type(variableType), variableValue))


def URLCheck(url):
	try:
		data = pd.read_csv(url)
		return True, data
	except:
		data = None
		return False, data

def PathCheck(path):
	try:
		data = pd.read_csv((path).strip(), encoding='utf8')
		return True, data
	except:
		data = None
		return False, data

def TrueToName(target, originalList, boolList):
	'''
	:data format is pandas DataFrame
	'''
	indexOfTrue = [i for i, v in enumerate(boolList) if v == True]
	Names = [originalList[i] for i in indexOfTrue]
	if Names[1] != target:
		Names[0], Names[1] = Names[1], Names[0]
	return Names

def SelectedTargetIndex(data, originalList, boolList):
	indexOfTrue = [i for i, v in enumerate(boolList) if v == True]
	Names = [originalList[i] for i in indexOfTrue]

	Index = [i for i, v in enumerate(data) if v in Names]
	Names = [v for i, v in enumerate(data) if v in Names]
	return Index, Names

def NameValidation(name):
	if name == "":
		state = False
	else:
		modelsDir = Path(str(WorkspaceDir()))
		if not modelsDir.is_dir():
			modelsDir.mkdir(parents=True, exist_ok=True)

		filesList = glob.glob(str(modelsDir)+"\\*.joblib")
		if str(modelsDir)+"\\"+str(name)+".joblib" in filesList:
			state = False
		else:
			state = True
	return state

def ListToArray(a):
	if type(a) == list:
		a = np.array(a)
	return a

def ParametersValidation(parameters, availableParameters):
	if not parameters:
		state = True
	else:
		try:
			parameters = ast.literal_eval(parameters)

			state = True
			check = all(item in availableParameters.keys() for item in parameters.keys())
			if not check:
				state = False
			else:
				for k1, v1 in parameters.items():
					for k2, v2 in availableParameters.items():
						if k1 == k2 and type(ListToArray(v1)) not in v2:
							state = False
		except:
			state = False
	return state

def TestTrainParametersValidation(parameters):
	availableParameters =	{"test_size":[float, int],
							"train_size":[float, int],
							"random_state":[int],
							"shuffle":[bool]}
	state = ParametersValidation(parameters, availableParameters)
	return state

def ClassifierParametersValidation(classifier, parameters):
	availableParameters	=	{'MultinomialNB':	{"alpha":[float],
												"fit_prior":[bool],
												"class_prior":[np.ndarray]},
							'GaussianNB':	{"prior":[np.ndarray],
											"var_smoothing":[float]},
							'ComplementNB':	{"alpha":[float],
											"fit_prior":[bool],
											"class_prior":[np.ndarray],
											"norm":[bool]},
							'BernoulliNB':	{"alpha":[float],
											"binarize":[float],
											"fit_prior":[bool],
											"class_prior":[np.ndarray]},
							'CategoricalNB':{"alpha":[float],
											"fit_prior":[bool],
											"class_prior":[np.ndarray]}}

	for c, p in availableParameters.items():
		if classifier == c:
			state = ParametersValidation(parameters, p)
			break
	return state

def CountVectorizerParametersValidation(parameters):
	#moguca greska
	#izbaceno "dtype":[str]
	availableParameters =	{"input":[str],
							"encodeing":[str],
							"decode_error":[str],
							"strip_accents":[str],
							"lowercase":[bool],
							"preprocessor":[str],
							"tokenizer":[str],
							"stop_words":[str, list],
							"token_pattern":[str],
							"ngram_range":[tuple],
							"analyzer":[str],
							"max_df":[list, int, float], 
							"max_features":[int],
							"vocabulary":[dict],
							"binary":[bool]}
	state = ParametersValidation(parameters, availableParameters)
	return state

def TfIdfTransformerParametersValidation(parameters):
	availableParameters =	{"norm":[str],
							"use_idf":[bool],
							"smooth_idf":[bool],
							"sublinear_tf":[bool]}
	state = ParametersValidation(parameters, availableParameters)
	return state

def MoveStopWords():
	subprocess.check_call(["attrib","-H","{}\\stopwords.json".format(str(WorkspaceDir()))])
	if not Path(str(WorkspaceDir())+"\\stopwords.json").is_file():
		copyfile("./stopwords.json", str(WorkspaceDir())+"\\stopwords.json")
	subprocess.check_call(["attrib","+H","{}\\stopwords.json".format(str(WorkspaceDir()))])


def LoadStopWords():
	subprocess.check_call(["attrib","-H","{}\\stopwords.json".format(str(WorkspaceDir()))])
	with open(str(WorkspaceDir())+"\\stopwords.json", "r") as f:
		data = json.load(f)
	subprocess.check_call(["attrib","+H","{}\\stopwords.json".format(str(WorkspaceDir()))])
	sw = pd.DataFrame.from_dict(data, orient="index")
	sw.transpose()
	header = [row for row in sw.index]
	return header, sw

class Bunch(dict):
	'''
	:Bunch je identicno kao i dict sa razlikom sto su elementi kod dict, objekti kod Bunch
	:Primer => test['a'] je isto kao i test.a
	'''
	def __init__(self, *args, **kws):
		super(Bunch, self).__init__(*args, **kws)
		self.__dict__ = self

def Matrix_To_Bunch(data, L_Case=False, Pun=False, S_Word=False):
	'''
	: Konvertuje matricu [[],[],...,[]] u Bunch
	'''
	DATA = []
	TARGET = []
	for index, row in data.iterrows():
		DATA.append(Cleaning(row[0], L_Case, Pun, S_Word))
		TARGET.append(row[1])

	TARGET_NAMES = list(set(TARGET))
	TARGET = [TARGET_NAMES.index(name) for name in TARGET]
	TARGET_NAMES = dict(enumerate(TARGET_NAMES))
	return Bunch({"data":DATA, "target_name":TARGET_NAMES, "target":TARGET})





from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, ComplementNB, BernoulliNB, CategoricalNB

from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier, Perceptron, RidgeClassifier, RidgeClassifierCV, SGDClassifier

from sklearn.model_selection import train_test_split
from random import randrange

from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

from sklearn.feature_selection import SelectFromModel

import time

from joblib import dump, load

def TrainFuction(name, data, classifier, tfidf_parameters_flag , vect_parameters_flag, clf_parameters={}, tfidf_parameters={}, vect_parameters={}, tt_parameters={}, L_Case=True, Pun=True, S_Word=False):
	d = Matrix_To_Bunch(data, L_Case, Pun, S_Word)
	X_train, X_test, y_train, y_test = train_test_split(d.data, d.target, **tt_parameters)
	X_train = np.array(X_train)
	if vect_parameters_flag and not tfidf_parameters_flag:
		vectorizer = CountVectorizer(**vect_parameters)
	elif not vect_parameters_flag and tfidf_parameters_flag:
		vectorizer = TfidfVectorizer(**tfidf_parameters)
	else:
		vectorizer = CountVectorizer(**vect_parameters)
	
	X_train = vectorizer.fit_transform(X_train)
	X_train = X_train.toarray()

	X_test = vectorizer.transform(X_test)
	X_test = X_test.toarray()
	X_test = X_test.astype(np.float64)

	if classifier == 'MultinomialNB':
		model = MultinomialNB(**clf_parameters)
	if classifier == 'GaussianNB':
		model = GaussianNB(**clf_parameters)
	if classifier == 'ComplementNB':
		model = ComplementNB(**clf_parameters)
	if classifier == 'BernoulliNB':
		model = BernoulliNB(**clf_parameters)
	if classifier == 'CategoricalNB':
		model = CategoricalNB(**clf_parameters)
	# train the model
	start = time.time()
	model.fit(X_train, y_train)
	stop = time.time()
	training_time = stop-start
	# Predict the test cases
	predicted = model.predict(X_test)

	precision = metrics.precision_score(y_test, predicted, average='macro')*100
	recall = metrics.recall_score(y_test, predicted, average='macro')*100
	f1 = metrics.f1_score(y_test, predicted, average='macro')
	accuracy = np.mean(predicted == y_test)*100
	Confusion_matrix = confusion_matrix(y_test, predicted)

	'''
	print('Accuracy => {}'.format(np.mean(predicted == y_test)))
	print(metrics.classification_report(y_test, predicted, target_names=d.target_name.values()))
	print(metrics.confusion_matrix(y_test, predicted))
	print("Recall => {}%".format(recall))
	print("Precision => {}%".format(precision))
	print("F1 => {}%".format(f1))
	print("Confusion matrix => {}".format(Confusion_matrix))
	'''
	dump((model, vectorizer, d.target_name), str(WorkspaceDir())+"\\"+name+'.joblib')

	recall = '{:.1f}%'.format(recall)
	precision = '{:.1f}%'.format(precision)
	f1 = '{:.4f}'.format(f1)
	accuracy = '{:.1f}%'.format(accuracy)

	return Bunch({'data':d, 
				  'test_target':y_test, 
				  'predicted':predicted,
				  'training_time':training_time,
				  'tested':len(X_test),
				  'recall': recall,
				  'precision':precision,
				  'f1':f1,
				  'accuracy':accuracy,
				  'confusion':Confusion_matrix})

def SaveModelInfo(	model_name, 
					classifier, 
					test_train_parameters, 
					classifier_parameters,
					count_vectorizer_status,
					count_vectorizer_parameters,
					tfidf_status,
					tfidf_transformer_parameters,
					punctuation_check_status,
					lowerCase_check_status,
					selected_stopwords,
					training_time,
					tested,
					recall,
					precision,
					f1,
					accuracy,
					target,
					target_info,
					confusion):

	info_json = {	"Model name": model_name,
					"Classifier": classifier,
					"Test-Train parameters": test_train_parameters,
					"Classifier parameters": classifier_parameters,
					"Count vectorizer status": count_vectorizer_status,
					"Count vectorizer parameters": count_vectorizer_parameters,
					"TfIdf status": tfidf_status,
					"TfIdf transformer parameters": tfidf_transformer_parameters,
					"Punctuation check status": punctuation_check_status,
					"LowerCase check status": lowerCase_check_status,
					"Selected stopwords": selected_stopwords,
					"Training time": training_time,
					"Tested": tested,
					"Recall": recall,
					"Precision": precision,
					"F1": f1,
					"Accuracy": accuracy,
					"Target": target,
					"Target info": target_info,
					"Confusion matrix": confusion.tolist()}

	with codecs.open(str(WorkspaceDir())+"\\"+model_name+'_info.json', 'w', encoding='utf-8') as f:
		json.dump(info_json, f, ensure_ascii=False)

def getModelList(dirpath):
	files = list(filter(os.path.isfile, glob.glob(dirpath + "*.joblib")))
	files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
	names = [''.join(os.path.basename(x).split('.')[:-1]) for x in files]
	return names, files

def getModelInfo(path):
	path = ''.join(path.split('.')[:-1])+'_info.json'
	with open(path, 'r', encoding='utf-8') as f:
		data = json.load(f)
	return Bunch(data)

def SecToTime(seconds): 
	seconds = seconds % (24 * 3600) 
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	mseconds = seconds // 0.001
	  
	return "%d:%02d:%02d:%03d" % (hour, minutes, seconds, mseconds)

def ConfusionMatrixGraph(matrix, x_axis, y_axis):
	
	f = plt.figure()
	ax= f.add_subplot(111)
	sn.heatmap(matrix, annot=True, ax = ax)

	ax.set_xlabel('Predicted')
	ax.set_ylabel('True')

	ax.xaxis.set_ticklabels(x_axis)
	ax.yaxis.set_ticklabels(y_axis)

	try:
		os.remove(str(WorkspaceDir())+"\\confusion.png")
	except:
		pass
	
	plt.savefig(str(WorkspaceDir())+"\\confusion.png", transparent=True)
	

def DonutGraph(value, name='accuracy'):
	SYSPATH = os.getenv("SystemDrive")

	size_of_groups=[value, 100-value]

	plt.figure(figsize=(1,1))

	plt.pie(size_of_groups, colors=['#7989ff', '#bfc7ff'])
	
	my_circle=plt.Circle( (0,0), 0.7, color='white')
	p=plt.gcf()
	p.gca().add_artist(my_circle)
	try:
		os.remove('{}\\{}.png'.format(str(WorkspaceDir()), name))
	except:
		pass
	
	plt.savefig('{}\\{}.png'.format(str(WorkspaceDir()), name), transparent=True, bbox_inches='tight')

def Test(name, model, ctg, vectorizer):
	import numpy as np
	#X_new_counts = vectorizer.transform(name)
	X_new = vectorizer.transform([name])

	predicted = ['{:.3f}%'.format(i*100) for i in model.predict_proba(X_new).tolist()[0]]

	return list(zip([ctg[i] for i in model.classes_], predicted))
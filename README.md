
<p align="center">
  <img height="100" src="https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Logo_v2_beta.png">
</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![python-version](https://img.shields.io/badge/Python-3.6|3.7-<COLOR>.svg)](https://www.python.org/) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
## Description
The purpose of this program is to enable users who do not understand much about programming, that they can create a text classification model.

Mixer is a relatively small and simple tool for creating models for text classification, inspired by Cloud AutoML.

The input `CSV` dataset can be imported online or locally (offline). It must also contain a minimum of two columns (sentences and targets), as well as, the dataset needs to be `UTF-8` encoded, comma delimited.
<br>Within the program, if the dataset contains more than two required columns, additional corrections can be made. These corrections are in the form of selecting the desired columns as well as the desired targets.
<br>After training and evaluation of the model, it is possible to test the trained model in direct interaction within the program.

**Characteristics:**
```diff
+ The whole process takes place locally, offline.
+ The raw dataset as well as the trained model is not stored anywhere online.
+ Uses some of the supervised learning algorithms - Naive Bayes methods.
+ Mixer is a multilingual program, ie language independent. (Not tested)
! So the training speed of the model depends not only on the size of the input dataset, but also on the performance of the user's computer.
```
> All font types that UTF-8 supports are also supported by the Mixer.

> Created and tested in Python 3.6 on Windows 7 x64!

:warning: **This is a beta version and probably contains some bugs. In that case, please [report the new issue](https://github.com/user0706/Mixer-v2/issues).**

## Prerequisites
Enter the following commands in the (terminal/cmd): 
- Natural Language Toolkit (NLTK)
```
#Installing nltk library
pip install nltk

#Access to the python editor
python
(if not, try python3)

#Import nltk functions
import nltk

#Download the punctuation package
nltk.download('punkt')

#Leaving the python editor
exit()
```
- Seaborn
```
pip install seaborn
```
- matplotlib
```
pip install matplotlib
```
-	scikit-learn
```
pip install scikit-learn
```
## How to run Mixer?

- Download repository
```
git clone https://github.com/user0706/Mixer-v2.git
```
- Entry into the download repository
```
cd Mixer-v2
```
- Start the program
```
python main.py
(if not, try python3)
```
## How to use the model?
Example of application of a previously trained model.

```python
from joblib import load
import numpy as np

#Path to .joblib model
# Example for Windows: "G:\\PATH\\TO\\FILE\\model.joblib"
MODEL_PATH = ""

#Loading a trained model
model, vectorizer, target = load(MODEL_PATH)

#Processes the test sentence and returns the result of the class prediction
def Test(name, model, ctg, vectorizer):
	X_new = vectorizer.transform([name])
	predicted = ['{:.3f}%'.format(i*100) for i in model.predict_proba(X_new).tolist()[0]]
	return list(zip([ctg[i] for i in model.classes_], predicted))

#The user enters a test sentence
test_string = input("Sentence: ")

#The moment of processing
result = Test(test_string, model, target, vectorizer)

#Display class prediction results
print(result)
```

## Screenshots
![](https://github.com/user0706/Mixer-v2/blob/master/Ignore/example.gif?raw=true)

## License Information

MIT License

## References
Thanks a lot:
* [svgrepo](https://www.svgrepo.com) for icons
* [scikit-learn](https://scikit-learn.org/stable/) for Naive Bayes methods

## To-Do
- [ ] Adapt code for big data
- [ ] Implement image classification

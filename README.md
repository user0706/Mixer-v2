<p align="center">
  <img height="100" src="https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Logo_v2_beta.png">
</p>

# About Mixer

The purpose of this program is to enable users who do not understand much about programming, that they can create a text classification model.

Mixer is a relatively small and simple tool for creating models for text classification, inspired by Cloud AutoML. But with Mixer: 
```diff
+ The whole process takes place locally, offline.
+ The raw dataset as well as the trained model is not stored anywhere online.
+ Uses some of the supervised learning algorithms - Naive Bayes methods.
+ Mixer is a multilingual program, ie language independent. (Not tested)
! So the training speed of the model depends not only on the size of the input dataset, but also on the performance of the user's computer.
```
All font types that UTF-8 supports are also supported by the Mixer.
### Import tab
The home tab is import tab. Uses tabular data that you import to train the model.<br/> 
Your dataset must have a minimum of two columns: sentences and targets. <br/>
The dataset can be selected locally, from a computer or online. It only supports CSV format which must be UTF-8 encoded, comma delimited.
### Schema tab
In the Schema tab the final modification of the raw data set is performed. This is where the required columns are selected as well as the desired target features.
### Analyze tab
In the Analyze tab an overview of the final data set that will be used to train the sentence classification model can be performed. 
### Train tab
Necessary and optional parameter settings for model training are performed here. <br/>
By clicking on the question mark it is possible to see more detailed information as well as the available parameters. Of course if there is a desire or need for it.
### Evaluation tab
The Evaluation tab provides the option to select one of the previously trained models. By default, the currently displayed information refers to the last trained model.<br/>As just mentioned the Evaluation tab provides an overview of the basic and additional information of the selected model.
### Test tab
The selected model is tested here.<br/>After entering the sentence, the classification results are displayed as a percentage.<br/>The class with the highest percentage, is marked as the definitive answer, to the prediction of the class.

# How to use the model?
Example of application of a previously trained model.

```python
from joblib import load
import numpy as np

#Path to .joblib model
'''
EXAMPLE
-------
	Windows: "G:\\PATH\\TO\\FILE\\model.joblib"
'''
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
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Import.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Schema.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Analyze.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Train.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Evaluation.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Test.png)

## References
Thanks a lot:
* [svgrepo](https://www.svgrepo.com) for icons
* [scikit-learn](https://scikit-learn.org/stable/) for Naive Bayes methods

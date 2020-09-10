<p align="center">
  <img height="100" src="https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Logo_v2_beta.png">
</p>

# About Mixer

Mixer is a relatively small and simple tool for creating models for text classification, inspired by Cloud AutoML. But with Mixer, the whole process takes place locally, offline. So the training speed of the model depends not only on the size of the input dataset, but also on the performance of the user's computer. Uses some of the supervised learning algorithms - [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) methods

Mixer is a multilingual program, ie language independent. All font types that UTF-8 supports are also supported by the Mixer.
### Import tab
The home tab is input tab. Uses tabular data that you import to train the model. Your dataset must have a minimum of two columns: sentences and targets. The dataset can be selected locally, from a computer or online. It only supports CSV format which must be UTF-8, encoded comma delimited.
### Schema tab
In the Schema tab the final modification of the raw data set is performed. This is where the required columns are selected as well as the desired target features.
### Analyze tab
In the Analyze tab an overview of the final data set that will be used to train the sentence classification model can be performed. 
### Train tab
Necessary and optional parameter settings for model training are performed here. By clicking on the question mark it is possible to see more detailed information as well as the available parameters. Of course if there is a desire or need for it.
### Evaluation tab
The Evaluation tab provides the option to select one of the previously trained models. By default, the currently displayed information refers to the last trained model.
As just mentioned the Evaluation tab provides an overview of the basic and additional information of the selected model.
### Test tab
The selected model is tested here. After entering the sentence the classification results are displayed as a percentage. The class with the highest percentage, is marked as the definitive answer, to the prediction of the class. 

## Requirements
The Mixer was created in the Python 3.6.0 programming language. The GUI was created in QtDesigner and PyQt5 v.5.14.2.

## Screenshots
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Import.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Schema.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Analyze.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Train.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Evaluation.png)
![](https://raw.githubusercontent.com/user0706/Mixer-v2/master/Ignore/Test.png)

# Regresion Logistica

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def information():
	current_dir = os.path.dirname(os.path.realpath(__file__)) 
	filename = os.path.join(current_dir,  "dataset/train.csv")
	dataset = pd.read_csv(filename)
	X = dataset.iloc[:, [1,2, 3]].values
	y = dataset.iloc[:, 4].values

	# Division del conjunto de datos en datos de entrenamiento
	# y datos de prueba
	X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size = 0.25, 
                                                    random_state = 0)

	# Ajuste de escala
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	# Ajuste de la regresion logistica al conjunto de entrenamiento
	classifier = LogisticRegression(random_state = 0)
	classifier.fit(X_train, y_train)
	# Prediccion de conjunto de pruebas
	y_pred = classifier.predict(X_test)
	# Retorna valores para mostrar en html
	return [precision_score(y_test, y_pred),classification_report(y_test, y_pred,output_dict=True)]
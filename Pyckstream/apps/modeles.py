import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV
from joblib import dump, load
import time


@st.cache
def data_transformation():
    
	df = pd.read_csv('./base.csv')

	df = df[['blurb_length','country','type_location', 'sub_cat','duration','launched_at_y', 'launched_at_m', 'goal_usd', 'state']]

	df['launched_at_m'] = df['launched_at_m'].astype('object')
	df['launched_at_y'] = df['launched_at_y'].astype('object')

	X = pd.get_dummies(df).drop('state', axis = 1)
	y = df['state']

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=44)

	scaler = StandardScaler()

	scaler.fit(X_train)
	X_train_scaled = pd.DataFrame(scaler.transform(X_train), index=X_train.index, columns=X_train.columns)
	X_test_scaled = pd.DataFrame(scaler.transform(X_test), index=X_test.index, columns=X_test.columns)
   
	return X_train_scaled, X_test_scaled, y_train, y_test

@st.cache
def scores_cb():
    
	X_train_scaled, X_test_scaled, y_train, y_test = data_transformation()

	### Modèle

	cb = load('cb.joblib')

	var_cb = cb.score(X_test_scaled, y_test)

	y_pred = cb.predict(X_test_scaled)
	matrix_confusion_cb = pd.crosstab(y_test, y_pred, normalize = 0)
    
	return var_cb, matrix_confusion_cb

@st.cache
def scores_rf():
    
	X_train_scaled, X_test_scaled, y_train, y_test = data_transformation()

	### Modèle

	rf = load('rf.joblib')

	var_rf = rf.score(X_test_scaled, y_test)

	y_pred = rf.predict(X_test_scaled)
	matrix_confusion_rf = pd.crosstab(y_test, y_pred, normalize = 0)
    
	return var_rf, matrix_confusion_rf

@st.cache
def scores_knn():
    
	X_train_scaled, X_test_scaled, y_train, y_test = data_transformation()

	### Modèle

	knn = load('knn.joblib')

	var_knn = knn.score(X_test_scaled, y_test)

	y_pred = knn.predict(X_test_scaled)
	matrix_confusion_knn = pd.crosstab(y_test, y_pred, normalize = 0)
    
	return var_knn, matrix_confusion_knn, knn

def app():
    
##### Modélisation ##### 


    st.title("Machine Learning")
    st.write('Pour nos expérimentations de Machine Learning nous avons testé différentes méthodes de __classification :__')

    st.write("•	KNeighborsClassifier"
         "\n\n"
        "•	RandomForestClassifier"
         "\n\n"             
        "•	CatBoost")


    st.write("Lors de notre analyse, nous allons utiliser nos variables features pour prédire la variable target nommée state.")
    st.write("Dans le cadre de notre projet, nous avons testé plusieurs modèles de Machine Learning. Découvrons les performances de chacun des modèles.")
    
    
    model = st.selectbox('Choisir le modèle', options = ['-', 'KNeighborsClassifier','RandomForestClassifier', 'Catboost'])
     

    if model == '-':
        st.write('__Veuillez choisir un modèle dans la liste déroulante.__')

    if model == 'KNeighborsClassifier':
        st.write('Le premier modèle que nous avons testé est le KNeighborsClassifier qui nous propose un score de 0,74. Pour un premier modèle, les résultats sont satisfaisants. Cependant le temps de traitement est conséquent : 20 minutes. Nous souhaitons donc améliorer __l\'accuracy et optimiser les temps de calcul__ en analysant d\'autres modèles')
        st.write('Accuracy on test set :', scores_knn()[0])
        st.write('Confusion matrix :', scores_knn()[1])

    if model == 'RandomForestClassifier':
        st.write('Accuracy on test set :',scores_rf()[0])
        st.write('Confusion matrix :',scores_rf()[1])
        
    if model == 'Catboost':
        st.write('Accuracy on test set :', scores_cb()[0])
        st.write('Confusion matrix:', scores_cb()[1])
        
    st.sidebar.info(
        "Projet DA - Promotion Bootcamp Mars 2021"
        "\n\n""\n\n"
        "**Participants**:"
        "\n\n"
        "Ségolène Truffert"
        "\n\n"
        "Théo Bardon"
        "\n\n"
        "Quentin Declercq"
        "\n\n"
        "Paul Choï-Monges "
        )  
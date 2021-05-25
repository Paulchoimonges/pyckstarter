import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.model_selection import GridSearchCV
from joblib import dump, load
import time

@st.cache
def scores():
	# Nous allons calculer l'accuracy du modèle

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

	CatBoost = load('cb.joblib') 

	CatBoost_score = CatBoost.score(X_test_scaled, y_test)

	return CatBoost, df, CatBoost_score

def data(blurb_length, country, sub_cat, duration, launched_at_y, type_location, launched_at_m, goal_usd):
	# Nous allons faire une nouvelle entrée pour faire ensuite une prédiction
	# La fonction renvoie les probabilitées de succès (1) ou failed (0) à partir de la dernière ligne (nouvelle entrée à tester)

	data = scores()[1]
	data = data[['blurb_length','country','type_location', 'sub_cat','duration','launched_at_y', 'launched_at_m', 'goal_usd']]
	data = data.append({'blurb_length' : blurb_length , 'country' : country, 'type_location' : type_location, 'sub_cat' : sub_cat, 'duration' : duration, 'launched_at_y' : launched_at_y , 'launched_at_m' : launched_at_m, 'goal_usd' : goal_usd} , ignore_index=True)
	
	data['launched_at_m'] = data['launched_at_m'].astype('object')
	data['launched_at_y'] = data['launched_at_y'].astype('object')

	X = pd.get_dummies(data)

	scaler = StandardScaler()

	scaler.fit(X)
	X_scaled = pd.DataFrame(scaler.transform(X), index=X.index, columns=X.columns)

	return scores()[0].predict(X_scaled[-1:]), scores()[0].predict_proba(X_scaled[-1:])

def app():
	# Element sur la page


    st.write("Sélection des éléments du projet :")

    #blurb_length = len(st.text_input('Description du Projet'))

    blurb_length = st.slider('Longueur description du projet', min_value=2, max_value=200)

    country = st.selectbox('Pays', np.sort(scores()[1]['country'].unique()))

    type_location = st.selectbox('Type de Localisation', np.sort(scores()[1]['type_location'].unique()))

    sub_cat = st.selectbox('Sous-Catégorie de Projet', np.sort(scores()[1]['sub_cat'].unique()))

    launched_at_m = st.selectbox('Mois de Lancement', np.sort(scores()[1]['launched_at_m'].unique()))

    launched_at_y = st.selectbox('Année de Lancement', np.sort(scores()[1]['launched_at_y'].unique()))

    goal_usd = st.number_input('Objectif du Projet en USD', value = 500)

    #goal_usd = st.slider('Objectif du Projet en USD', min_value=scores()[1]['goal_usd'].min(), 20000)

    duration = st.number_input('Durée du Projet en jour', value = 14)

    #date_lancement = st.date_input("Date de Lancement", [])

    #date_fin = st.date_input("Date de Clôture", [])

    
    st.write("Le score du modèle chargé est de :", round(scores()[2] * 100, 2), '%')

    if st.button('Calculer mes chances de succès'):

    	#launched_at_m = date_lancement.month

    	#launched_at_y = date_lancement.year

    	#duration = date_fin - date_lancement

    	#st.write(date_lancement.month)

    	st.write(data(blurb_length=blurb_length, country=country, sub_cat=sub_cat, launched_at_y=launched_at_y, launched_at_m=launched_at_m, goal_usd=goal_usd, duration=duration, type_location=type_location)[1])


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


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache
def load_file():
	df = pd.read_csv('./base_g.csv').set_index('id')
	return df

def description():
    st.write("Description des colonnes")
    
    col_select = st.selectbox(label = "choisir une colonne pour voir sa définition", options = ['backers_count','blurb','country','type_location','id_creator','deadline','main_cat ','sub_cat','duration','launched_at_y','launched_at_m','launched_at_h','blurb_lengh','blurb_nb_car'])

    if col_select == 'backers_count' :
        st.write("- Nombre de contributeurs à la campagne")
        
    if col_select == 'blurb' :
        st.write("- Texte de description de la campagne")

    if col_select == 'country' :
        st.write("- Pays")
          
    if col_select == 'type_location' :
        st.write("- Milieu rural/citadin")
          
    if col_select == 'id_creator' :
        st.write("- Identifiant kickstarter du créateur")
         
    if col_select == 'deadline' :
        st.write("- Date de clôture de la campagne")
        
    if col_select == 'main_cat ' :         
        st.write("- Catégories principales ")

    if col_select == 'sub_cat':
        st.write("- Sous-catégories ") 
        
    if col_select == 'duration' :
        st.write("- Durée de la récolte de fonds")  
        
    if col_select == 'created_at' :
        st.write("- Date de création de la campagne")  
            
    if col_select == 'launched_at_y' :
        st.write("- Année de lancement de la campagne")  
        
    if col_select == 'launched_at_m' :
        st.write("- Mois de lancement de la campagne")  
        
    if col_select == 'launched_at_h' :
        st.write("- Heure de lancement")  
        
    if col_select == 'goal_usd' :
        st.write("- Objectif de financement en dollars")  
              
    if col_select == 'blurb_lengh' :
        st.write("- Nombre de caractères présents dans la description ")  
        
    if col_select == 'blurb_nb_car' :
        st.write("- Nombre de caractères divisés en intervalles")  

def clean(): 
    st.subheader("Lors de notre analyse nous avons fait des travaux de préparation disponibles ci-dessous.")
    st.write('\n\n')
    if st.checkbox("Afficher"):
    
        
      st.write(
            "La première tâche du projet fut de compiler les données afin d’obtenir une première version exploitable."
            "\n\n"
            "Pour cela nous avons mis en place des fonctions pour fusionner les fichiers et vérifier la qualité des données."
            "\n\n"
            "Nous avons pu faire une première analyse de notre Dataframe et faire les premiers nettoyages :"
            "\n\n"
            " - Suppression des valeurs manquantes avec dropna()"
            "\n\n"
            " - Suppression des doublons du à la fusion"
            "\n\n"
            " - Passer la colonne ID en index."
            "\n\n"
            "Après ce nettoyage, nous avons créé un nouveau dataframe grâce aux données contenues dans les json."        
            "\n\n"
            "Celui-ci contient un nombre important de données inutiles d’un point de vue analytique (logo € et $)."
            "\n\n"
            "Nous avons décidé de garder 17 variables. Certaines ont été créées par des fonctions personnalisées d'autres sont issues du dataframe originel."
            "\n\n"
            "Un nouveau nettoyage de données nous a amené à :"
            "\n\n"
            " - Renommer des variables pour une meilleure compréhension."
            "\n\n"
            " - Nettoyage de la variable target. Notre variable target state comporte 4 modalités : successful / failed /live /cancelled."
            "\n\n"
            "Pour faciliter le traitement des données, nous décidons de supprimer les projets live et d'intégrer les cancelled aux failed."
            "\n\n"
    
        "Nos travaux de nettoyage sont disponibles ci-dessous."
        "\n\n"
        "Après ces retraitements nous avons notre dataframe, sur lequel nous pouvons commencer notre analyse."
        , unsafe_allow_html=True)       
    

def graph_bar(df=load_file(), year = 'all', state = ['successful', 'failed'], country = 'all', colomns = 'launched_at_y', subject = 'main_cat', size=(25,12), normalize = 0, axe = 'h', alpha = 0.85, annotate = 'on'):
  '''

  Fonction similaire à graph_bar_success_bis

  Permet des possibilitées en plus : 
  
  -> axe : Modifier sens du graphique
  -> annotate : Affichage ou non des annotations
  -> normalize : Normalisation des données ou non
  -> alpha : Transparence des couleurs
  -> opt : True si problème affichage

  '''
  def affichage(axe = axe, normalize = normalize):
      for p in ax.patches:
        left, bottom, width, height = p.get_bbox().bounds

        if axe == 'h' and normalize is 0:
          ax.annotate(str(round((width)*100,1)) + ' %', xy=(left+width/2, bottom+height/2), ha='center', va='center')
        elif axe == 'h' and normalize is not 0:
          ax.annotate(str(int(width)), xy=(left+width/2, bottom+height/2), ha='center', va='center')
        elif axe == 'v' and normalize is 0:
          ax.annotate(str(round((height)*100,1)) + ' %', xy=(left+width/2, bottom+height/2), ha='center', va='center')
        elif axe == 'v' and normalize is not 0:
          ax.annotate(str(int(height)), xy=(left+width/2, bottom+height/2), ha='center', va='center')

      ax.set_title('Part de succès des projets selon ' + str(subject) + ' - ' + str(year) + ' - Pays : ' + str(country))

  #if country == 'all':
  #  tab = pd.crosstab(df[subject], df.state, normalize=normalize).sort_values(by = 'successful', ascending = True)
  #elif country == list:
  #  tab = pd.crosstab(df[df[colomns] in country][subject], df[df[colomns] in country].state, normalize=normalize).sort_values(by = 'successful', ascending = True)
  #else:
  #  tab = pd.crosstab(df[df[colomns] == country][subject], df[df[colomns] == country].state, normalize=normalize).sort_values(by = 'successful', ascending = True)

  #tab.sort_values(by = 'successful', ascending = True)
  if country == 'all':
      tab = pd.crosstab(df[df[colomns] == year][subject], df[df[colomns] == year].state, normalize=normalize).sort_values(by = 'successful', ascending = True)
  elif isinstance(country, list):
      tab = pd.crosstab(df[(df[colomns] == year) & (df['country'].isin(country))][subject], df[(df[colomns] == year) & (df['country'].isin(country))].state, normalize=normalize).sort_values(by = 'successful', ascending = True)
  else:
      tab = pd.crosstab(df[(df[colomns] == year) & (df['country'] == country)][subject], df[(df[colomns] == year) & (df['country'] == country)].state, normalize=normalize).sort_values(by = 'successful', ascending = True)
  
 # Si non normalisation, trie selon nombre de projets
  if normalize is not 0:
    tab['Total'] = tab.sum(axis = 1)
    tab = tab.sort_values(by='Total', ascending = False).drop('Total', axis = 1)

  # Si axe horizontal
  if axe == 'h':
    ax = tab.plot.barh(y=state, stacked = True, figsize=size, width = 0.75, color = {'successful' : 'limegreen', 'failed' : 'orangered'}, alpha = alpha)
    if annotate == 'on':
      affichage(axe, normalize)

  # Si axe vertical
  elif axe == 'v':
    ax = tab.plot.bar(y=state, stacked = True, figsize=size, color = {'successful' : 'limegreen', 'failed' : 'orangered'}, alpha = alpha)
    if annotate == 'on':
      affichage(axe, normalize)

def app():
    st.title('Dataset')
    "\n\n"
    clean()
    "\n\n"
    "\n\n"
    st.write("Extrait de notre de notre Dataframe.")

    st.write(load_file()[:20])
    description() 
    
    st.title('Datavisualisation')
    launched_at_y =st.slider(label = 'Année', min_value = 2009, max_value = 2021,step = 1)

    if st.checkbox('Tous les pays ?', value = True) == False:
      country = st.multiselect('Pays', np.sort(load_file()['country'].unique()))
    else:
      country = 'all'

    if st.button("Afficher") : 
      graph_bar(df=load_file(), year = launched_at_y, state = ['successful', 'failed'], country = country, colomns = 'launched_at_y', subject = 'main_cat', size=(25,12), normalize = False, axe = 'v', alpha = 0.85, annotate = 'on')
      st.set_option('deprecation.showPyplotGlobalUse', False)
      st.pyplot()
        
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
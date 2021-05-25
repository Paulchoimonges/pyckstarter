import streamlit as st

def app():
    
     
     st.title("Conclusion et recommandations")
     "\n\n"
     
     st.subheader("Votre campagne kickstarter a-t-elle des chances de succès? ")
     "\n\n"
     "\n\n"
     "\n\n"
     "\n\n"
     st.write("\n\n")  

     "\n\n"
     "\n\n"
     "\n\n"
     st.write(
     "Tous les modèles ont un score supérieur à 70%. Il est assez simple d'atteindre une accurracy supérieure à 70% et l'ajustement des variables nous permet d'augmenter cette dernière de quelques points."
     "\n\n"
     "Tous les modèles sont plus fiables pour trouver les vrais positifs que les vrais négatifs. Ce manque de détection peut être dû à un manque de données extérieures."
     "\n\n"
     
     "Pour améliorer notre Machine Learning, pour notamment s'assurer une meilleure analyse des vrais négatifs, nous pourrions enrichir notre DataFrame avec des informations extérieures telles que les tendances Google, le budget des campagnes marketing si applicables, analyser en détail les autres informations contenues sur le site (description longue, mise en avant sur le site...)."
      , unsafe_allow_html=True)  

        
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
     
     

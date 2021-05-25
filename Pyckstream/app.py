import streamlit as st
from multiapp import MultiApp
from apps import home, data, modeles, demo, conclusion # import your app modules here

app = MultiApp()


st.image('logo.png')   

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Modèles", modeles.app)
app.add_app("Démo", demo.app)
app.add_app("Conclusion", conclusion.app)
# The main app
app.run()

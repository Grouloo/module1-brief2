import streamlit as st
import requests
from loguru import logger
from sys import stderr

logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/sentiment_streamlit.log")

st.header("Analyse de sentiment")

with st.form("my_form"):
    st.write("Saisissez un texte pour analyser le sentiment.")
    text = st.text_area("Entrez un texte pour analyser le sentiment.")
    submitted = st.form_submit_button("Envoyer")

    if submitted:
        logger.info(f"Texte à analyser: {text}")
        try:
            response = requests.post("http://127.0.0.1:80/analyse_sentiment/", json={"text": text})
            response.raise_for_status() 
            sentiment = response.json()

            st.write(f"{sentiment['interpretation']['emoji']} {sentiment['interpretation']['label']}")
            st.write("Résultats de l'analyse :")
            st.write(f"Polarité négative : {sentiment['raw']['neg'] * 100} %")
            st.write(f"Polarité neutre : {sentiment['raw']['neu'] * 100} %")
            st.write(f"Polarité positive : {sentiment['raw']['pos'] * 100} %")
            st.write(f"Score composé : {sentiment['raw']['compound']}")
        except requests.exceptions.RequestException as e: 
            st.error(f"Erreur de connexion à l'API : {e}")           
            logger.error(f"Erreur de connexion à l'API : {e}")
        except requests.exceptions.HTTPError as e:
            st.error(f"Erreur HTTP : {e}")
            logger.error(f"Erreur HTTP : {e}")
        except Exception as e:
            st.error(f"Erreur lors de l'analyse: {e}")
        

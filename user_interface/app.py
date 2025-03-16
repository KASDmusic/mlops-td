import streamlit as st
import requests

api_url = "http://user-api:8000"
    
st.title("Interface Utilisateur : Feedback")
commentaire = st.text_input("Commentaire")
note = st.feedback(options="faces")

if st.button("Envoyer requête"):
    if commentaire and note:
        with st.spinner("Envoi du commentaire..."):
            response = requests.post(f"{api_url}/feedback", json={"comment": commentaire, "rating": note})
            st.json(response.json())
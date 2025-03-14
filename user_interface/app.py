import streamlit as st
import requests
import httpx

socket_path = "/tmp/fastapi-user_api.sock"
    
def post_feedback(comment, rating):
    with httpx.Client(transport=httpx.HTTPTransport(uds=socket_path)) as client:
        response = client.post("http://localhost/feedback", json={"comment": comment, "rating": rating})
        return response.json()
    
st.title("Interface Utilisateur : Feedback")

commentaire = st.text_input("Commentaire")

# Composant pour noter le commentaire
note = st.feedback(options="stars")

if st.button("Envoyer requête"):
    if commentaire and note:
        # bar de chargement
        with st.spinner("Envoi du commentaire..."):
            res = post_feedback(commentaire, note)
            st.json(res)
import streamlit as st
import pandas as pd
import httpx

socket_path = "/tmp/fastapi-admin_api.sock"

# Fonction pour récupérer les données de la table
def get_feedback():
    with httpx.Client(transport=httpx.HTTPTransport(uds=socket_path)) as client:
        response = client.get("http://localhost/feedback")
        feedbacks = response.json()
        df = pd.DataFrame(feedbacks, columns=["id", "comment", "rating"])
        return df

# Fonction pour mettre à jour les valeurs dans la base de données
def update_feedback(id, comment, rating):
    with httpx.Client(transport=httpx.HTTPTransport(uds=socket_path)) as client:
        response = client.put("http://localhost/feedback", json={"id": id, "comment": comment, "rating": rating})
        return response.json()

# Interface Streamlit
st.title("Interface Admin : Gestion des Feedbacks")

# Chargement des données
df = get_feedback()

# texte
st.write("Double cliquez sur une cellule pour la modifier.")

# Affichage interactif avec modification
edited_df = st.data_editor(df, num_rows="fixed")

# Vérification des modifications
if not df.equals(edited_df):
    for index, row in edited_df.iterrows():
        if df.loc[index, "comment"] != row["comment"] or df.loc[index, "rating"] != row["rating"]:
            update_feedback(row["id"], row["comment"], row["rating"])
    st.success("Mise à jour effectuée !")

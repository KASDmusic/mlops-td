import streamlit as st
import pandas as pd
import requests

api_url = "http://admin-api:8001"

def get_feedback():
    response = requests.get(f"{api_url}/feedback")
    feedbacks = response.json()
    df = pd.DataFrame(feedbacks, columns=["id", "comment", "rating"])
    return df

def update_feedback(id, comment, rating):
    response = requests.put(f"{api_url}/feedback", json={"id": id, "comment": comment, "rating": rating})
    return response.json()

st.title("Interface Admin : Gestion des Feedbacks")
df = get_feedback()
st.write("Double cliquez sur une cellule pour la modifier.")
edited_df = st.data_editor(df, num_rows="fixed")

if not df.equals(edited_df):
    for index, row in edited_df.iterrows():
        if df.loc[index, "comment"] != row["comment"] or df.loc[index, "rating"] != row["rating"]:
            update_feedback(row["id"], row["comment"], row["rating"])
    st.success("Mise à jour effectuée !")
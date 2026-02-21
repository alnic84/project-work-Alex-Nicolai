import streamlit as st
import pandas as pd
import joblib
import numpy as np

# === Caricamento modelli e vettorizzatori ===
model_cat = joblib.load("model_cat.pkl")
model_pri = joblib.load("model_pri.pkl")
vectorizer_cat = joblib.load("vectorizer_cat.pkl")
vectorizer_pri = joblib.load("vectorizer_pri.pkl")

# === Funzione per predire un singolo ticket ===
def predici_ticket(title, body):
    text = (title + " " + body).lower()
    X_cat = vectorizer_cat.transform([text])
    X_pri = vectorizer_pri.transform([text])
    cat_pred = model_cat.predict(X_cat)[0]
    pri_pred = model_pri.predict(X_pri)[0]
    return cat_pred, pri_pred, X_cat

# === Funzione per parole più influenti ===
def parole_influenti(model, vectorizer, X):
    feature_names = np.array(vectorizer.get_feature_names_out())
    coef = model.coef_[np.argmax(model.predict_proba(X))]
    top5_idx = np.argsort(coef)[-5:][::-1]
    return feature_names[top5_idx]

# === Interfaccia grafica ===
st.set_page_config(page_title="Dashboard Ticket", page_icon="🎫", layout="wide")

st.title("🎫 Dashboard - Classificazione Automatica Ticket")
st.write("Inserisci un ticket (titolo + descrizione) per prevedere categoria e priorità operativa.")

title = st.text_input("Titolo del ticket")
body = st.text_area("Descrizione del ticket")

if st.button("Classifica Ticket"):
    cat, pri, X = predici_ticket(title, body)
    top_words = parole_influenti(model_cat, vectorizer_cat, X)
    st.success(f"**Categoria prevista:** {cat}")
    st.info(f"**Priorità suggerita:** {pri}")
    st.write(f"🔑 Parole più influenti: {', '.join(top_words)}")

st.divider()
st.subheader("📂 Classificazione batch da CSV")
st.write("Carica un file CSV con colonne 'title' e 'body' per ottenere le predizioni in blocco.")

uploaded = st.file_uploader("Carica file CSV", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
    df["text"] = df["title"].astype(str) + " " + df["body"].astype(str)
    df["Predicted Category"] = model_cat.predict(vectorizer_cat.transform(df["text"]))
    df["Predicted Priority"] = model_pri.predict(vectorizer_pri.transform(df["text"]))
    
    st.success("Classificazione completata!")
    st.dataframe(df[["title", "Predicted Category", "Predicted Priority"]])
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Scarica CSV con predizioni",
        data=csv,
        file_name="ticket_predictions.csv",
        mime="text/csv"
    )

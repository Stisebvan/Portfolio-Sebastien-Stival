import streamlit as st

st.set_page_config(page_title="Sébastien Stival – BI & Dashboarding", page_icon="📊", layout="wide")

# --- Menu latéral ---
st.sidebar.title("Menu")
page = st.sidebar.radio("Aller à", ["Accueil", "Projets", "À propos", "Contact"])

# --- En-tête réutilisable ---
def header():
    st.title("Transformer les données en décisions")
    st.caption("Portfolio de **Sébastien Stival** – Manager Gestion du Risque & Data Product Manager")

# --- Pages ---
if page == "Accueil":
    header()
    st.write(
        "Bienvenue ! Je conçois des tableaux de bord **Power BI / Excel** pour les organismes "
        "de Sécurité sociale. Les visuels présentés sont **anonymisés**."
    )
    st.markdown("—")

elif page == "Projets":
    header()
    st.subheader("📊 Pilotage des dépenses de transport — CPAM des Pyrénées-Orientales")
    st.markdown(
        "**Contexte :** hausse des dépenses de transport.\n\n"
        "**Action :** modélisation des données, indicateurs clés, visualisations Power BI, diffusion sécurisée.\n\n"
        "**Impact :** accès immédiat aux dérives, meilleure priorisation des actions de régulation."
    )
    st.markdown("---")
    st.subheader("📊 Tableau de bord Qualité & Performance — organisme public (anonymisé)")
    st.markdown(
        "**Contexte :** indicateurs dispersés dans plusieurs fichiers Excel.\n\n"
        "**Action :** normalisation et consolidation → tableau de bord Power BI avec page spéciale CODIR.\n\n"
        "**Impact :** réduction du temps de préparation des réunions, fiabilisation des chiffres."
    )

elif page == "À propos":
    header()
    st.write(
        "**Sébastien Stival**, Manager **Gestion du Risque** (CPAM des Pyrénées-Orientales, depuis 2019) "
        "et **Data Product Manager** certifié. 10 ans d’audit interne **ISO 9001**. "
        "Je transforme des besoins métier en outils de pilotage concrets."
    )
    st.write("**Valeurs :** confidentialité • rigueur • discrétion")

elif page == "Contact":
    header()
    st.write("📫 **Contact**")
    st.write("- Email : sebastien.stival@assurance-maladie.fr")
    st.write("- LinkedIn : https://www.linkedin.com (mets ton lien)")
    st.info("Tu pourras ajouter ici un bouton pour télécharger ton CV plus tard.")

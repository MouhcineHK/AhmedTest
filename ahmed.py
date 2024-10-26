import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="MouhcineHK", page_icon="👋")

# Fonction pour convertir une image en base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Charger l'image
image = Image.open("test.jpeg")
image_base64 = image_to_base64(image)

# CSS pour une mise en page responsive et titres avec ligne en dessous
import streamlit as st

st.markdown("""
    <style>
    /* Cacher l'en-tête Streamlit */
    header {
        visibility: hidden;
        height: 0;
    }
    /* Couleur de fond */
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: #00292d;
        color: white;
        height: 100%;
        margin: 0;
        padding: 0;
    }
    /* Conteneur principal */
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        gap: 50px;
        width: 100%;
        padding: 20px;
    }
    .image-container {
        flex: 1;
        display: flex;
        justify-content: center;
    }
    .image-container img {
        border-radius: 20px;
        width: 260px;
        max-width: 100%;
    }
    .info-column {
        flex: 2;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }
    .center-buttons {
        display: flex;
        flex-direction: row;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
        flex-wrap: wrap;
    }
    .center-buttons a {
        color: white;
        background-color: #1E90FF;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        transition: background-color 0.3s ease;
        text-align: center;
    }
    .center-buttons a:hover {
        background-color: #FF6347;
    }
    .stDownloadButton {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    .stDownloadButton:hover {
        background-color: #45a049;
    }
    /* Titres en blanc avec ligne en dessous */
    h2 {
        color: white;
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 2px solid white;
    }
    h3 {
        color: white;
        margin-bottom: 10px;
    }       
    /* Styles pour les écrans mobiles */
    @media (max-width: 768px) {
        .container {
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 20px; /* Réduire l'espacement entre les éléments */
            width: 100%;
            padding: 20px;
        }
        .image-container {
            flex: 1;
            display: flex;
            justify-content: center;
        }
          h1, h2, h3 {
        color: white;
        }
        h1{
            color: white;
            margin-left: 25px;
        
            } 
            
        .image-container img {
            border-radius: 20px;
            width: 260px;
            max-width: 100%;
        }
        .info-column {
            flex: 2;
            display: flex;
            flex-direction: column; /* Aligner verticalement les éléments */
            justify-content: center;
            align-items: center; /* Centrer les éléments en mode mobile */
            text-align: center; /* Centrer le texte */
            padding: 0 20px; /* Ajouter du padding pour éviter que le texte touche les bords */
        }
    }
    </style>
""", unsafe_allow_html=True)



# Charger le PDF en mémoire
with open("CVZaridi.pdf", "rb") as f:
    pdf_data = f.read()

# Mise en page avec deux colonnes alignées horizontalement sur PC
st.markdown(
    f"""
    <div class="container">
        <div class="image-container">
            <img src="data:image/jpeg;base64,{image_base64}" alt="Ahmed ZARIDI"/>
        </div>
        <div class="info-column">
            <h1 style="color: white;">Ahmed ZARIDI</h1>
            <h3>Software Engineer</h3>
            <button class="stDownloadButton">
                📄 
                <a href="data:application/pdf;base64,{base64.b64encode(pdf_data).decode()}" download="CVZaridi.pdf" style="text-decoration: none; color: white;">
                    Download Resume
                </a>
            </button>
            <p>📧 <a href="mailto:ahmedzaridi21@gmail.com" style="color: white;">ahmedzaridi21@gmail.com</a></p>
            <p>📞 (+212) 673199596</p>
            <div class="center-buttons">
                <a href="https:" target="_blank">LinkedIn</a>
                <a href="https:" target="_blank">GitHub</a>
                <a href="https:" target="_blank">LeetCode</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True




)
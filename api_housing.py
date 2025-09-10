# Import des bibliothèques
from fastapi import FastAPI  # Pour l'API
from pydantic import BaseModel  # Pour valider les entrées
import joblib  # Pour charger le modèle
import pandas as pd  # Pour manipuler les données
from fastapi.middleware.cors import CORSMiddleware
 

# Créer l'application
app = FastAPI(title="API Prédiction Prix Maisons")
origins = ["https://housing-static-site.onrender.com"]
app.add_middleware(    CORSMiddleware,    allow_origins=origins,    allow_credentials=True,    allow_methods=["*"],    allow_headers=["*"],)
 

# Définir le modèle d'entrée
class HouseFeatures(BaseModel):
    MedInc: float  # Revenu médian
    HouseAge: float  # Âge
    AveRooms: float  # Pièces moyennes
    AveBedrms: float  # Chambres moyennes
    Population: float  # Population
    AveOccup: float  # Occupation
    Latitude: float  # Latitude
    Longitude: float  # Longitude

# Charger le modèle (local)
model = joblib.load('house_price_model.pkl')

# Endpoint pour prédire
@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = pd.DataFrame([features.dict()])  # Convertir en tableau
    predicted_price = model.predict(input_data)[0]  # Prédire
    return {"predicted_price": predicted_price}  # Renvoie en JSON


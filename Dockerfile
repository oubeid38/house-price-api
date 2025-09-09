# Image de base : Python 3.9 slim (léger)
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires (sans house_price_model.pkl)
COPY requirements.txt . 
COPY prepare_model.py .  
COPY api_housing.py . 

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Générer le modèle dynamiquement (sans copier le fichier lourd)
RUN python prepare_model.py

# Exposer le port 8000
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "api_housing:app", "--host", "0.0.0.0", "--port", "8000"]
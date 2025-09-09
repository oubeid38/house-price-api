#Utiliser une image de base Python
FROM python:3.9-slim

#Définir le répertoire de travail dans le conteneur
WORKDIR /app

#Copier requirements.txt et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copier les fichiers nécessaires
COPY api_housing.py ./ 
COPY house_price_model.pkl ./ 


#Exposer le port 8000
EXPOSE 8000

#Définir la commande pour lancer l'API avec Uvicorn
CMD ["uvicorn", "api_housing:app", "--host", "0.0.0.0", "--port", "8000"]
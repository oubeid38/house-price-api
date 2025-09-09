# Import des bibliothèques
import pandas as pd  # Pour manipuler les données
from sklearn.datasets import fetch_california_housing  # Dataset
from sklearn.model_selection import train_test_split  # Pour séparer les données
# Charger les données
housing_data = fetch_california_housing()
features = pd.DataFrame(housing_data.data, columns=housing_data.feature_names)  # Caractéristiques
target = housing_data.target  # Prix (cible)
# Vérifier les données (optionnel, pour voir un aperçu)
print("Aperçu des caractéristiques :")
print(features.head())
print("\nAperçu des prix :")
print(target[:5])
# Séparer en entraînement (80%) et test (20%)
train_features, test_features, train_target, test_target = train_test_split(
    features, target, test_size=0.2, random_state=42  # 42 pour des résultats reproductibles
)
print(f"Données d'entraînement : {len(train_features)} exemples")
print(f"Données de test : {len(test_features)} exemples")



# Import pour le modèle et les métriques
from sklearn.ensemble import RandomForestRegressor  # Modèle
from sklearn.metrics import mean_squared_error, r2_score  # Évaluation
import numpy as np  # Pour calculs
# Entraîner le modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)  # 100 arbres
model.fit(train_features, train_target)  # Entraîner
# Prédire et évaluer
predicted_prices = model.predict(test_features)
r2 = r2_score(test_target, predicted_prices)  # Précision
rmse = np.sqrt(mean_squared_error(test_target, predicted_prices))  # Erreur
print(f"R² = {r2:.2f} (plus proche de 1, mieux c'est)")
print(f"RMSE = {rmse:.2f} (plus bas, mieux c'est)")



# Import pour sauvegarder
import joblib
# Sauvegarder localement
model_filename = 'house_price_model.pkl'
joblib.dump(model, model_filename)
print(f"Modèle sauvegardé dans {model_filename} (localement)")
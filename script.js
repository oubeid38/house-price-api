function predictPrice() {
    const features = {
        MedInc: parseFloat(document.getElementById('MedInc').value),
        HouseAge: parseFloat(document.getElementById('HouseAge').value),
        AveRooms: parseFloat(document.getElementById('AveRooms').value),
        AveBedrms: parseFloat(document.getElementById('AveBedrms').value),
        Population: parseFloat(document.getElementById('Population').value),
        AveOccup: parseFloat(document.getElementById('AveOccup').value),
        Latitude: parseFloat(document.getElementById('Latitude').value),
        Longitude: parseFloat(document.getElementById('Longitude').value)
    };
    if (Object.values(features).some(v => isNaN(v))) {
        alert("Remplissez tous les champs avec des nombres.");
        return;
    }
    const API_URL = 'https://house-price-api-efse.onrender.com';  
    fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(features)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `<h2>Prix prédit : ${data.predicted_price.toFixed(2)}</h2>`;
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert("Erreur de prédiction.");
    });
}
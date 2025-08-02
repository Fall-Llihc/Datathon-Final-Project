import numpy as np
from flask import Flask, render_template, jsonify
import time # Import time to simulate a delay

app = Flask(__name__)

# --- DRL Model Section ---
sectors = [
    "Teknologi", "Keuangan", "Kesehatan", "Industri",
    "Energi", "Properti", "Konsumer"
]
# --- End DRL Model Section ---

# ROUTE 1: Serves the initial page with the loading indicator
@app.route('/')
def index():
    # This route is now very fast, it just returns the HTML shell.
    return render_template('index.html')

# ROUTE 2: Runs the model and returns data as JSON
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    # Simulate the model taking time to run
    print("Model is running...")
    time.sleep(1) # Pauses for 3 seconds to simulate a long calculation
    print("Model finished.")

    # Your DRL model logic
    action = np.random.rand(len(sectors))
    predicted_weights = np.exp(action) / np.sum(np.exp(action))
    uang_pengguna = 5_000_000
    
    recommendations = []
    for i, sector in enumerate(sectors):
        persentase = predicted_weights[i] * 100
        alokasi_dana = predicted_weights[i] * uang_pengguna
        recommendations.append({
            "sector": sector,
            "percentage": f"{persentase:.2f}%",
            "amount": f"Rp {alokasi_dana:,.2f}"
        })
    
    # Instead of rendering a template, return data in JSON format
    return jsonify({
        "recommendations": recommendations,
        "total_fund": f"Rp {uang_pengguna:,.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'FFT Visualizer API is running!'

@app.route('/compute-fft', methods=['POST'])
def compute_fft():
    try:
        data = request.get_json()
        values = [float(x.strip()) for x in data['values'].split(',')]
        fft_result = np.abs(np.fft.fft(values)).tolist()
        return jsonify({'result': fft_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# For local development
if __name__ == '__main__':
    app.run(debug=True, port=5000)
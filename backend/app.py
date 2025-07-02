# Flask API backend
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "API IA Parkinson en ligne"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    result = sentiment_analyzer(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

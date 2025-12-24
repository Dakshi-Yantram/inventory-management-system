from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Flask service running"})


@app.route("/process", methods=["POST"])
def process():
    data = request.json

    text = data.get("text", "")
    number = data.get("number", 0)

    return jsonify({
        "success": True,
        "upper_text": text.upper(),
        "square": number * number
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)

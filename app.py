"""Simple Flask application with addition operation."""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Return a simple greeting message."""
    return "USN: 1RVU23CSE075"

@app.route('/add', methods=['GET'])
def add():
    """Perform addition of two numbers."""
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"result": num1 + num2})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

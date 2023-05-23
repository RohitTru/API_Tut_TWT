from flask import Flask, request, jsonify

# Initializing Flask
app = Flask(__name__)


# Test endpoint
@app.route("/")
def home():
    return "Home"

# Running our Flask Application
if __name__ == "__main__":
    app.run(debug=True)
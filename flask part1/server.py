from flask import Flask

app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def home():
    # Function that handles requests to the root URL
    # return 'Hello, World!'
    return jsonify(message = "Hello World")
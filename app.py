from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello le sang, {x}. Welcome !"

@app.route('/2')
def hello_worldbis():
	x = 'run'
	return f"Hello le sang, {x}. Welcome !"
if __name__ == "__main__":
    app.run()
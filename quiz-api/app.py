from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}. Welcome !"

if __name__ == "__main__":
    app.run()
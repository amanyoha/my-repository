from flask import Flask 
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Amanuel" 
@app.route("/bye")
def theend():
    return "<h1>The End</h1>"

if __name__ == '__main__':
    app.run(port=8080)

    # app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)
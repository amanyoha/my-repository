from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello Simret"

@app.route("/Bye")
def theend():
    return "<h1>Good Bye Simmy</h1>"
if __name__ == '__main__':

    app.run()

    # app.run(debug=True, port=30000)
    # # app.run(host= '0.0.0.0', port=8081)
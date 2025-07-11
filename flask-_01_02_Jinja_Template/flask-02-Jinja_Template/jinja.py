from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home"

@app.route("/head")
def head():
    return render_template("index.html", number1 = 100, number2 = 500)

@app.route("/sum")
def sum():
    val1 = 40 
    val2 = 50 
    mysum = val1 + val2
    return render_template ("body.html", value1 = val1 , value2 = val2, sum = mysum)

if __name__== "__main__":
    app.run(host="0.0.0.0")
    #app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)
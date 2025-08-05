from chatbot import CB
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))
app.run(debug = True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

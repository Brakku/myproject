from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Breki Hlynsson test3 hotfix2</p>"

app.run()
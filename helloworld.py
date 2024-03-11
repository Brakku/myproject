from flask import Flask

app = Flask(__name__)

#TODO #9 change this
@app.route("/")
def hello_world():
    return "<p>Breki Hlynsson test3 hotfix2</p>"

app.run()
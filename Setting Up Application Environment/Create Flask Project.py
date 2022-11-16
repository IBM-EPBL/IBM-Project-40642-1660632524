

              #Team id=PNTIBM202234039
              #Personal Expenses Tracker Application


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




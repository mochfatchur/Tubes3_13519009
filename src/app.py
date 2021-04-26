# From Flask Tutorial

import os

from flask import (
    Flask, render_template, request
)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return render_template("index.html")
    
@app.route('/', methods=["POST"])
def hello2():
    return "You said \"{}\"".format(request.form["user-input"])
    
app.run(debug=True)
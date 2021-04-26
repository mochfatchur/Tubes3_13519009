# From Flask Tutorial

import os

from flask import (
    Flask, render_template, request, g, redirect
)

global chat_data
chat_data = [("Halo", "Hai")]

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return render_template("index.html", message_data = chat_data[(-5 if len(chat_data) >= 5 else 0):])
    
@app.route('/', methods=["POST"])
def hello2():
    user_input = request.form["user-input"]
    bot_response = "Hahahayyuk"
    chat_data.append((user_input, bot_response))
    return render_template("index.html", message_data = chat_data[(-5 if len(chat_data) >= 5 else 0):])
    # return "You said \"{}\"".format(request.form["user-input"])
    
app.run(debug=True)
print(chat_data)
# From Flask Tutorial

import os
from ContextIdentifier import ContextIdentifier, Context
from SpellChecker import SpellChecker
from Extractor import Extractor

from flask import (
    Flask, render_template, request, g, redirect
)

from DatabaseClass import Database

global chat_data

chat_data = []

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return render_template("index.html", message_data = chat_data[(-5 if len(chat_data) >= 5 else 0):])
    
@app.route('/', methods=["POST"])
def hello2():
    user_input = request.form["user-input"]
    context_identifier = ContextIdentifier()
    context = context_identifier.getContext(user_input)
    bot_response = ""
    suggested_word = []
    
    if context == Context.unknown:
        suggested_word = SpellChecker().getWordSuggestion(user_input)

    elif context == Context.help:
        bot_response = "Terdapat 8 hal yang dapat dilakukan:\n"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
        bot_response += "- Menambah tugas (coba \"Tolong ingatkan kalau ada kuis IF3110 Bab 2 pada 22/04/21\")"
    
    else:
        extractor = Extractor()
        command = extractor.extract(user_input, context)
        
        if command == None:
            suggested_word = SpellChecker().getWordSuggestion(user_input)
        else:
            command.execute()
            bot_response = command.getResult()
            
    if bot_response == "":
        if len(suggested_word) > 0:
            bot_response = "Mungkin maksud kata kunci Anda: " + ", ".join(suggested_word)
        else:
            bot_response = "Saya tidak paham .-."
            
    chat_data.append((user_input, bot_response.split("\n")))
    return render_template("index.html", message_data = chat_data[(-5 if len(chat_data) >= 5 else 0):])

app.run(debug=True)
print(chat_data)
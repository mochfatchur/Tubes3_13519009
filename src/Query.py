import sqlite3
from datetime import datetime
from datetime import date
import os
from Matcher import Matcher
global path

matcher = Matcher()
path = os.path.abspath("database.db")


def getAllTask():
    conn = conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Task")
    val = cursor.fetchall()
    conn.close()
    return val


def getSpesificTimeLeftTask(date):
    conn = conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Task")
    val = cursor.fetchall()
    conn.close()
    dateStart = date.today()
    dateEnd = matcher.stringToDate(date)
    task = []
    for i in range(len(val)):
        valDate = matcher.stringToDate(val[i][4])
        if (valDate < dateEnd) and (valDate > dateStart):
            task.append(val[i])
    return task


def deleteOneTask(id):
    conn = conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Task WHERE ID = ?", (id,))
    conn.close()

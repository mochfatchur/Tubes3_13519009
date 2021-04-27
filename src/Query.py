from Matcher import Context, Matcher
import sqlite3
from datetime import datetime
# from datetime import date
from datetime import timedelta
import os
from Matcher import Matcher
import re
global path


matcher = Matcher()
path = os.path.abspath("database.db")


def getAllTask():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Task")
    val = cursor.fetchall()
    # print(val)
    conn.close()
    return val


def getSpesificTimeLeftTask(dateEnd):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Task")
    val = cursor.fetchall()
    conn.close()
    dateStart = datetime.today()
    dateEnd = matcher.stringToDate(dateEnd)
    task = []
    for i in range(len(val)):
        valDate = matcher.stringToDate(val[i][4])
        if (valDate <= dateEnd) and (valDate >= dateStart):
            task.append(val[i])
    return task


def deleteOneTask(jenis, namaMatkul):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Task WHERE jenis = ? AND nama_matkul = ?",
        (jenis,
         namaMatkul,))
    print(jenis)
    print(namaMatkul)
    conn.commit()
    conn.close()


def stringAllTask(arrTask):
    allTaskString = ""
    for i in range(len(arrTask)):
        allTaskString += str(arrTask[i][0]) + " - " + arrTask[i][2] + \
            " - " + arrTask[i][1] + " - " + arrTask[i][3] + " - " + arrTask[i][4] + "\n"
    return allTaskString


def executeCommand(text):
    matcher = Matcher()
    command = matcher.getContext(text)
    allTaskString = ""

    if (command == Context.updateTask):
        print(1)
    elif (command == Context.getAllTask):
        allTask = getAllTask()
        # print(allTask)
        return stringAllTask(allTask)
    elif (command == Context.getRangeTimeTask):
        dates = matcher.extractDate(text)
    elif (command == Context.getSpesificTimeLeftTask):
        N = int(matcher.nDateExtractor(text))
        Endate = datetime.today() + timedelta(days=N)
        Endate = matcher.dateToString(Endate)
        allTask = getSpesificTimeLeftTask(Endate)
        return stringAllTask(allTask)
    elif (command == Context.deleteTask):
        namaMatkul = matcher.extractMatkul(text)
        jenis = matcher.extractJenis(text)
        deleteOneTask(jenis, namaMatkul)
        return ""


text = "deadline 3 hari ke depan apa saja bot ?"
# text = "tolong ingatkan ada tubes IF2211 (string Matching) pada 28/04/2021"
# text = "ada tugas apa saja sejauh ini ?"
# text = "bot kuis IF2230 sudah selesai ya, tolong dihilangkan"
# matcher = Matcher()
print(executeCommand(text))

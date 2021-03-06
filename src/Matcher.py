from datetime import datetime
import re
from enum import Enum


class Context (Enum):
    addTask = 1
    getAllTask = 2
    getRangeTimeTask = 3
    getSpesificTimeLeftTask = 4
    getDueTodayTask = 5
    updateTask = 6
    deleteTask = 7
    getDeadlineOfTask = 8
    help = 10
    unknown = 9


class Matcher:
    def __init__(self):
        self.keyword = [
            "sejauh ini",
            "antara",
            "dari",
            "hingga",
            "sampai",
            "ke depan",
            "hari ini",
            "dibatalkan",
            "hapus",
            "selesai",
            "tambahkan",
            "ingatkan",
            "kapan",
            "diundur",
            "help"
        ]
        self.dateRegex = r"(([0-3]?[0-9])\/([0-1]?[0-9])\/([0-2][0-9][0-9][0-9]))"
        self.taskRegex = r"(kuis|ujian|tubes|tucil) (IF[0-9]{4}) (\(.*\))"
        self.jenisRegex = r"(kuis|ujian|tubes|tucil)"
        self.matkulRegex = r"(IF[0-9]{4})"
        self.nDate = r"([0-9]) (minggu|hari)"

    def computeFail(self, pattern):
        fail = [-1 for i in range(len(pattern))]
        fail[0] = 0
        m = len(pattern)
        j = 0
        i = 1
        while (i < m):
            if (pattern[j] == pattern[i]):
                # j + 1 chars match
                fail[i] = j + 1
                i += 1
                j += 1
            elif (j > 0):
                # j follows matching prefix
                j = fail[j - 1]
            else:
                # no match
                fail[i] = 0
                i += 1

        return fail

    def kmpMatch(self, text, pattern):
        n = len(text)
        m = len(pattern)
        fail = self.computeFail(pattern)
        i = 0
        j = 0
        while (i < n):
            if (pattern[j] == text[i]):
                if (j == m - 1):
                    return pattern  # match

                i += 1
                j += 1
            elif (j > 0):
                j = fail[j - 1]
            else:
                i += 1

        return None  # no match

    # end of kmpMatch()

    def LevenshteinDistance(self, stringA, stringB):
        if (len(stringB) == 0):
            return len(stringA)
        elif (len(stringA) == 0):
            return len(stringB)
        elif (stringA[0] == stringB[0]):
            return LevenshteinDistance(stringA[1:], stringB[1:])
        else:
            return (
                1 + min(
                    LevenshteinDistance(
                        stringA[1:],
                        stringB),
                    LevenshteinDistance(
                        stringA,
                        stringB[1:]),
                    LevenshteinDistance(
                        stringA[1:],
                        stringB[1:])))

    def extractDate(self, text):
        match = re.findall(self.dateRegex, text)
        dates = []
        for i in range(match):
            dates.append(match[i][0])

        return dates

    def stringToDate(self, stringDate):
        date = datetime.strptime(stringDate, "%d/%m/%Y")
        return date

    def dateToString(self, date):
        stringDate = datetime.strftime(date, "%d/%m/%Y")
        return stringDate

    def getContext(self, text):
        for i in range(len(self.keyword)):
            contextWord = self.kmpMatch(text, self.keyword[i])
            if (contextWord is not None):
                break
        if (contextWord == "sejauh ini"):
            return Context.getAllTask
        elif (contextWord in ["antara", "dari", "hingga", "sampai"]):
            return Context.getRangeTimeTask
        elif (contextWord == "ke depan"):
            return Context.getSpesificTimeLeftTask
        elif (contextWord == "hari ini"):
            return Context.getDueTodayTask
        elif (contextWord in ["dibatalkan", "hapus", "selesai"]):
            return Context.deleteTask
        elif (contextWord in ["tambahkan", "ingatkan"]):
            return Context.addTask
        elif (contextWord == "kapan"):
            return Context.getDeadlineOfTask
        elif (contextWord == "diundur"):
            return Context.updateTask
        elif (contextWord == "help"):
            return Context.help
        else:
            return Context.unknown

    def extractTask(self, text):
        match = re.findall(self.taskRegex, text)
        task = []
        task.append(match[0][0])
        task.append(match[0][1])
        description = match[0][2].replace("(", "")
        description = description.replace(")", "")
        task.append(description)
        return task

    def extractMatkul(self, text):
        match = re.findall(self.matkulRegex, text)
        return match[0]

    def extractJenis(self, text):
        match = re.findall(self.jenisRegex, text)
        return match[0]

    def nDateExtractor(self, text):
        match = re.findall(self.nDate, text)
        if (match[0][1] == "minggu"):
            return 7 * match[0][0]
        elif (match[0][1] == "hari"):
            return match[0][0]


# text = "tugas saya sangat banyak sekali sejauh ini rasanya sudah lelah sekali"
# text = "bot kuis IF2230 sudah selesai ya, tolong dihilangkan"
# pattern = "sejauh ini"
# task = "tubes IF2211 (String Matching) pada 14/04/2021"
# matcher = Matcher()
# print(matcher.extractJenis(text))
# print(matcher.getContext(text))

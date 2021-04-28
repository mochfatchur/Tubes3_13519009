from enum import Enum
from KmpMatcher import KmpMatcher

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

class ContextIdentifier:
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
    
    def getContext(self, text):
        contextWord = ""
        for word in self.keyword:
            matcher = KmpMatcher()
            if (matcher.match(word, text)):
                contextWord = word
                break # found
                
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
            
    def getKeyword(self):
        return [word for word in self.keyword]
import re
from GetDueTodayTaskCommand import GetDueTodayTaskCommand

class Extractor:
    def __init__(self):
        # Nothing to initialize
        pass
        
    # Return command that will be executed
    def extract(self, message, context):
        if context == "AddTask":
            # Implement here
            return None
            
        elif context == "GetAllTask":
            # Implement here
            return None
            
        elif context == "GetRangeTimeTask":
            # Implement here
            return None
            
        elif context == "GetSpecificTimeLeftTask":
            # Implement here
            return None
            
        elif context == "GetDueTodayTask":
            getDueTodayPattern1 = r"[dD]eadline (kuis|tubes|tucil|ujian|)"
            getDueTodayPattern2 = r"(?:([Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|),? |)(?:yang )?deadline (?:pada )?hari ini apa saja"
            
            result2 = re.search(getDueTodayPattern2, message)
            if result2 != None:
                if result2.group(1) == "":
                    # Coba yang result 1
                    result1 = re.search(getDueTodayPattern1, message)
                    if result1 != None:
                        if result1.group(1) != "":
                            return GetDueTodayTaskCommand(result1.group(1)) # return command
                    
                return GetDueTodayTaskCommand(result2.group(1).lower()) # return command
            
            result1 = re.search(getDueTodayPattern1, message)
            if result1 != None:
                return GetDueTodayTaskCommand(result1.group(1)) # return command
                
            return None
            
        elif context == "UpdateTask":
            # Implement here
            return None
            
        elif context == "DeleteTask":
            # Implement here
            return None
            
        else:
            print("Warning\nUnknown context for extractor:{}".format(context))
            return None
            
            
        
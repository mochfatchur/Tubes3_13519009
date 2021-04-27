import re
from GetAllTaskCommand import GetAllTaskCommand
from GetSpesificTimeLeftTaskCommand import GetSpesificTimeLeftTaskCommand
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
            # Extract jenis task
            getAllTaskPattern = r"([Tt](ucil|ubes))|([Kk]uis)|([Uu]jian)"
            result = re.search(getAllTaskPattern, message)
            # Kalau jenisnya spesifik
            if result is not None:
                return GetAllTaskCommand(
                    jenisTask=result.group().lower())
            # Semua task
            else:
                return GetAllTaskCommand()

            return None

        elif context == "GetRangeTimeTask":
            # Implement here
            return None

        elif context == "GetSpecificTimeLeftTask":
            getSpesificTimeLeftTaskPattern1 = r"([Tt](ucil|ubes))|([Kk]uis)|([Uu]jian)"
            getSpesificTimeLeftTaskPattern2 = r"(([Hh]ari)|[Mm]inggu)"
            getSpesificTimeLeftTaskPattern3 = r"\d+"

            result1 = re.search(
                getSpesificTimeLeftTaskPattern1, message)
            result2 = re.search(
                getSpesificTimeLeftTaskPattern2, message)
            result3 = re.search(
                getSpesificTimeLeftTaskPattern2, message)

            if (result1 is not None and result2.group().lower() ==
                    "hari" and result3 is not None):
                return GetSpesificTimeLeftTaskCommand(
                    jenisTask=result1.group().lower(), N=int(result3))
            elif (result1 is not None and result2.group().lower() ==
                    "minggu" and result3 is not None):
                return GetSpesificTimeLeftTaskCommand(
                    jenisTask=result1.group().lower(), N=int(result3) * 7)
            elif (result2.group().lower() == "hari" and result3 is None):
                return GetSpesificTimeLeftTaskCommand(
                    N=int(result3))
            elif (result2.group().lower() == "minggu" and result3 is None):
                return GetSpesificTimeLeftTaskCommand(
                    N=int(result3) * 7)

            return None

        elif context == "GetDueTodayTask":
            getDueTodayPattern1 = r"[dD]eadline (kuis|tubes|tucil|ujian|)"
            getDueTodayPattern2 = r"(?:([Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|),? |)(?:yang )?deadline (?:pada )?hari ini apa saja"

            result2 = re.search(getDueTodayPattern2, message)
            if result2 is not None:
                if result2.group(1) == "":
                    # Coba yang result 1
                    result1 = re.search(getDueTodayPattern1, message)
                    if result1 is not None:
                        if result1.group(1) != "":
                            return GetDueTodayTaskCommand(
                                result1.group(1))  # return command

                return GetDueTodayTaskCommand(
                    result2.group(1).lower())  # return command

            result1 = re.search(getDueTodayPattern1, message)
            if result1 is not None:
                return GetDueTodayTaskCommand(
                    result1.group(1))  # return command

            return None

        elif context == "UpdateTask":
            # Implement here
            return None

        elif context == "DeleteTask":
            # Extract nama matkul
            deleteTaskPattern1 = r"([A-Z]{2}[0-9]{4})"
            # Extract jenis task
            deleteTaskPattern2 = r"([Tt](ucil|ubes))|([Kk]uis)|([Uu]jian)"
            result1 = re.search(deleteTaskPattern1, message)
            result2 = re.search(deleteTaskPattern2, message)
            # Spesifik 1 task
            if ((result1 is not None) and (result2 is not None)):
                return DeleteTaskCommand(
                    jenisTask=result2.group(),
                    namaMatkul=result1.group())
            # Untuk 1 jenis task
            elif (result1 is not None):
                return DeleteTaskCommand(
                    jenisTask=result2.group().lower())
            return None

        else:
            print(
                "Warning\nUnknown context for extractor:{}".format(context))
            return None

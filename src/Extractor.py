import re
from GetAllTaskCommand import GetAllTaskCommand
from GetDeadlineOfTask import  GetDeadlineOfTask
from GetSpecificTimeLeftTaskCommand import GetSpecificTimeLeftTaskCommand
from GetDueTodayTaskCommand import GetDueTodayTaskCommand
from AddTaskCommand import AddTaskCommand
from ContextIdentifier import Context
from UpdateTask import UpdateTask
from DeleteTaskCommand import DeleteTaskCommand
from datetime import datetime

class Extractor:
    def __init__(self):
        # Nothing to initialize
        pass

    # Return command that will be executed
    def extract(self, message, context):
        if context == Context.addTask:
            daftar_bulan = [
                "januari",
                "februari",
                "maret",
                "april",
                "mei",
                "juni",
                "juli",
                "agustus",
                "september",
                "oktober",
                "november",
                "desember"
            ]
        
            # "kuis IF3110 Bab 2 sampai 3 pada 22/04/21"
            jenisTaskPattern = r"[Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|(?:UAS|uas)|(?:UTS|uts)"
            matkulPattern = r"[A-Z]{2}[0-9]{4}"
            deskripsiPattern = r".*"
            tanggalPattern = r"0?[1-9]|[1-2][0-9]|3[01]"
            bulanAngkaPattern = r"0?[1-9]|1[0-2]"
            bulanTulisanPattern = r"[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Jj]uli|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember"
            tahunPattern = r"(?:[0-9][0-9])?[0-9][0-9]"
            
            addPattern1 = r"({}) ({}) ({}) pada ({})[/\-]({})[/\-]({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanAngkaPattern, tahunPattern)
            result1 = re.search(addPattern1, message)
            if result1 != None:
                # matkul, jenis, deskripsi, tahun, bulan, tanggal
                return AddTaskCommand(
                    jenis = result1.group(1).lower() if result1.group(1).lower() not in ["uas", "uts"] else "ujian",
                    matkul = result1.group(2),
                    deskripsi = result1.group(3),
                    tahun = int(result1.group(6)) if len(result1.group(6)) == 4 else int("20" + result1.group(6)),
                    bulan = int(result1.group(5)),
                    tanggal = int(result1.group(4))
                )
            
            # "Ingatkan saya ada UAS IF2230 pada 20 Mei 2021. Saya sedang chaos nih. :("
            addPattern2 = r"({}) ({}) ({}) ?pada ({}) ({}) ({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanTulisanPattern, tahunPattern)
            result2 = re.search(addPattern2, message)
            if result2 != None:
                if (result2.group(5).lower() in daftar_bulan):
                    # matkul, jenis, deskripsi, tahun, bulan, tanggal
                    return AddTaskCommand(
                        jenis = result2.group(1).lower() if result2.group(1).lower() not in ["uas", "uts"] else "ujian",
                        matkul = result2.group(2),
                        deskripsi = result2.group(3) if result2.group(1).lower() not in ["uas", "uts"] else result2.group(1),
                        tahun = int(result2.group(6)) if len(result2.group(6)) == 4 else int("20" + result2.group(6)),
                        bulan = daftar_bulan.index(result2.group(5).lower()) + 1,
                        tanggal = int(result2.group(4))
                    )
                else:
                    return None
                    
            addPattern3 = r"({}) ({}) ({}) ?pada ({}) ({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanTulisanPattern)
            result3 = re.search(addPattern3, message)
            if result3 != None:
                if (result3.group(5).lower() in daftar_bulan):
                    # matkul, jenis, deskripsi, tahun, bulan, tanggal
                    return AddTaskCommand(
                        jenis = result3.group(1).lower() if result3.group(1).lower() not in ["uas", "uts"] else "ujian",
                        matkul = result3.group(2),
                        deskripsi = result3.group(3) if result3.group(1).lower() not in ["uas", "uts"] else result3.group(1),
                        tahun = datetime.now().year,
                        bulan = daftar_bulan.index(result3.group(5).lower()) + 1,
                        tanggal = int(result3.group(4))
                    )
                else:
                    return None
            
            # Kuis IF1210 tentang prosedur ingin ditambahkan ke daftar tugas yang saya akan kerjakan. Waktunya 1-3-2015. Bisa?
            addPattern4 = r"({}) ({}) (?:tentang )?({}) (?:ingin |pada |dengan |yang |, )[^1-9]*({})[/\-]({})[/\-]({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanAngkaPattern, tahunPattern)
            result4 = re.search(addPattern4, message)
            if result4 != None:
                if (result4.group(5).lower() in daftar_bulan):
                    # matkul, jenis, deskripsi, tahun, bulan, tanggal
                    return AddTaskCommand(
                        jenis = result4.group(1).lower() if result4.group(1).lower() not in ["uas", "uts"] else "ujian",
                        matkul = result4.group(2),
                        deskripsi = result4.group(3) if result4.group(1).lower() not in ["uas", "uts"] else result4.group(1),
                        tahun = int(result4.group(6)) if len(result4.group(6)) == 4 else int("20" + result1.group(6)),
                        bulan = daftar_bulan.index(result4.group(5).lower()) + 1,
                        tanggal = int(result4.group(4))
                    )
                else:
                    return None
            
            print("Pattern 5")            
            addPattern5 = r"({}) ({}) (?:tentang )?({}) (?:ingin |pada |dengan |yang |, )[^1-9]*({}) ({}) ({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanTulisanPattern, tahunPattern)
            result5 = re.search(addPattern5, message)
            if result5 != None:
                if (result5.group(5).lower() in daftar_bulan):
                    # matkul, jenis, deskripsi, tahun, bulan, tanggal
                    return AddTaskCommand(
                        jenis = result5.group(1).lower() if result5.group(1).lower() not in ["uas", "uts"] else "ujian",
                        matkul = result5.group(2),
                        deskripsi = result5.group(3) if result5.group(1).lower() not in ["uas", "uts"] else result5.group(1),
                        tahun = int(result5.group(6)) if len(result5.group(6)) == 4 else int("20" + result1.group(6)),
                        bulan = daftar_bulan.index(result5.group(5).lower()) + 1,
                        tanggal = int(result5.group(4))
                    )
                else:
                    return None
                 
            print("Pattern 6")
            addPattern6 = r"({}) ({}) (?:tentang )?({}) (?:yang |pada |dengan |ingin |, )[^1-9]*({}) ({})".format(jenisTaskPattern, matkulPattern, deskripsiPattern, tanggalPattern, bulanTulisanPattern)
            result6 = re.search(addPattern6, message)
            if result6 != None:
                if (result6.group(5).lower() in daftar_bulan):
                    # matkul, jenis, deskripsi, tahun, bulan, tanggal
                    return AddTaskCommand(
                        jenis = result6.group(1).lower() if result6.group(1).lower() not in ["uas", "uts"] else "ujian",
                        matkul = result6.group(2),
                        deskripsi = result6.group(3) if result6.group(1).lower() not in ["uas", "uts"] else result6.group(1),
                        tahun = datetime.now().year,
                        bulan = daftar_bulan.index(result6.group(5).lower()) + 1,
                        tanggal = int(result6.group(4))
                    )
                else:
                    return None
            
            return None

        elif context == Context.getAllTask:
            # Extract jenis task
            getAllTaskPattern = r"[Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|(?:UAS|uas)|(?:UTS|uts)"
            result = re.search(getAllTaskPattern, message)
            # Kalau jenisnya spesifik
            if result is not None:
                return GetAllTaskCommand(
                    jenisTask=result.group().lower())
            # Semua task
            else:
                return GetAllTaskCommand()

            return None

        elif context == Context.getRangeTimeTask:
            # Implement here
            return None

        elif context == Context.getSpesificTimeLeftTask:
            getSpecificTimeLeftTaskPattern1 = r"([Tt](ucil|ubes))|([Kk]uis)|([Uu]jian)"
            getSpecificTimeLeftTaskPattern2 = r"(([Hh]ari)|[Mm]inggu)"
            getSpecificTimeLeftTaskPattern3 = r"\d+"

            result1 = re.search(
                getSpecificTimeLeftTaskPattern1, message)
            result2 = re.search(
                getSpecificTimeLeftTaskPattern2, message)
            result3 = re.search(
                getSpecificTimeLeftTaskPattern3, message)

            if (result2 is not None and result3 is not None):
                if (result1 is not None):
                    if(result2.group().lower() == "hari"):
                        return GetSpecificTimeLeftTaskCommand(jenisTask=result1.group().lower(),N=int(result3.group()))
                    elif (result2.group().lower() == "minggu"):
                        return GetSpecificTimeLeftTaskCommand(jenisTask=result1.group().lower(),N=int(result3.group())*7)
                else:
                    if(result2.group().lower() == "hari"):
                        return GetSpecificTimeLeftTaskCommand(N=int(result3.group()))
                    elif (result2.group().lower() == "minggu"):
                        return GetSpecificTimeLeftTaskCommand(N=int(result3.group())*7)
            return None

        elif context == Context.getDueTodayTask:
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

        elif context == Context.updateTask:
            # Extract jenis task
            updateTaskPattern1 = "[Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|(?:UAS|uas)|(?:UTS|uts)"
            # Extract nama matkul
            updateTaskPattern2 = r"([A-Z]{2}[0-9]{4})"
            # Extract deadlineBaru
            tanggalPattern = r"0?[1-9]|[1-2][0-9]|3[01]"
            bulanAngkaPattern = r"0?[1-9]|1[0-2]"
            bulanTulisanPattern = r"[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Jj]uli|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember"
            tahunPattern = r"(?:[0-9][0-9])?[0-9][0-9]"

            addPattern1 = r"({})[/\-]({})[/\-]({})".format(tanggalPattern, bulanAngkaPattern, tahunPattern)

            result1 = re.search(updateTaskPattern1, message)
            result2 = re.search(updateTaskPattern2, message)
            result3 = re.search(addPattern1, message)

            if ((result1 is not None) and (result2 is not None) and (result3 is not None)):
                return UpdateTask(result1.group(), result2.group(),
                                  "-".join(result3.group().replace("/", "-").split("-")[::-1]))

            return None

        elif context == Context.deleteTask:
            # Extract nama matkul
            deleteTaskPattern1 = r"([A-Z]{2}[0-9]{4})"
            # Extract jenis task
            deleteTaskPattern2 = r"[Kk]uis|[Tt]ubes|[Tt]ucil|[Uu]jian|(?:UAS|uas)|(?:UTS|uts)"
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
        
        elif context == Context.getDeadlineOfTask:
            # Extract matkul task
            getDeadlineTaskPattern1 = r"[A-Z]{2}[0-9]{4}"
            getDeadlineTaskPattern2 = r"[Tt]ubes|[Tt]ucil"
            result1 = re.search(getDeadlineTaskPattern1, message)
            result2 = re.search(getDeadlineTaskPattern2, message)
            if result1 is not None:
                if result2 is not None:
                    return GetDeadlineOfTask(matkul=result1.group(), jenisTask=result2.group().lower())

                else:
                    return GetDeadlineOfTask(matkul=result1.group(), jenisTask="")

            return None
        
        else:
            print(
                "Warning!\nUnknown context for extractor: {}".format(context))
            return None

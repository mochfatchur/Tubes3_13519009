from DatabaseClass import Database


class UpdateTask():
    def __init__(self, jenisTask="", namaMatkul="", deadlineBaru =""):
        self.jenisTask = jenisTask
        self.namaMatkul = namaMatkul
        self.deadlineBaru = deadlineBaru
        self.tempResult = ""

    def execute(self):
        database = Database()
        database.GetCursor().execute(
            """
            SELECT *
            FROM Task t
            {}
            """.format("" if self.jenisTask == "" else "WHERE jenis = \"{}\"".format(self.jenisTask))
        )
        result = database.GetCursor().fetchall()
        print(result)
        if len(result) == 0:
            if self.jenisTask == "":
                self.tempResult = "Tidak ada tugas yang didaftarkan!"
            else:
                self.tempResult = "Tidak ada {} yang harus dikerjakan".format(
                    self.jenisTask)
        else:
            found = False
            i = 0
            while (i < len(result) and found == False):
                if (result[i][1] == self.namaMatkul and result[i]
                        [2] == self.jenisTask):
                    found = True
                i += 1
            if (found):
                # print("ketemu")
                database.GetCursor().execute(
                    """
                        UPDATE Task
                        SET tanggal = "{}"
                        WHERE nama_matkul = "{}" AND jenis = "{}"
                    """.format(self.deadlineBaru,self.namaMatkul, self.jenisTask))
                database.GetConnection().commit()
                self.tempResult = "Yay deadline tugas telah diperbaharui!!!\n"
            else:
                self.tempResult += "Tidak ada {} {}".format(
                    self.jenisTask, self.namaMatkul)

    def getResult(self):
        return self.tempResult

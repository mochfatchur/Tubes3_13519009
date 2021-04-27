from DatabaseClass import Database


class GetAllTaskCommand:
    def __init__(self, jenisTask=""):
        self.jenisTask = jenisTask
        self.tempResult = ""

    def execute(self):
        database = Database()
        database.GetCursor().execute(
            """
            SELECT *
            FROM Task t
            {}
            ORDER BY (
                SELECT nilai
                FROM Prioritas p
                WHERE t.jenis = p.jenis
            )
            """.format("" if self.jenisTask == "" else "WHERE jenis = \"{}\"".format(self.jenisTask))
        )
        result = database.GetCursor().fetchall()
        if len(result) == 0:
            if self.jenisTask == "":
                self.tempResult = "Tidak ada tugas yang didaftarkan!"
            else:
                self.tempResult = "Tidak ada {} yang harus dikerjakan".format(
                    self.jenisTask)
        else:
            self.tempResult = "[Daftar Deadline]"
            for record in result:
                self.tempResult += "\n" + \
                    "(ID: {}) ".format(record[0]) + " - ".join(record[1:])

    def getResult(self):
        return self.tempResult

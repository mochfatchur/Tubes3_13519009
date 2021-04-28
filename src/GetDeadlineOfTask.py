from DatabaseClass import Database


class GetDeadlineOfTask:
    def __init__(self, matkul, jenisTask=""):
        self.matkul = matkul
        self.jenisTask = jenisTask
        self.tempResult = ""

    def execute(self):
        database = Database()
        database.GetCursor().execute(
            """
            SELECT *
            FROM Task t
            ORDER BY (
                SELECT nilai
                FROM Prioritas p
                WHERE t.jenis = p.jenis
            )
            """
        )
        value = database.GetCursor().fetchall()
        matkul = self.matkul
        jenisTask = self.jenisTask

        # print(dateStart)
        # print(dateEnd)
        result = []
        found = False
        i = 0
        while (i<len(value)):
            if (value[i][1] == matkul):
                result.append(value[i])
            i += 1

        print(result)

        if len(result) == 0:
            if(jenisTask == ""):
                self.tempResult = "Tidak ada deadline/jadwal untuk '{}' '{}' pada tanggal tersebut".format(jenisTask, matkul)
            else:
                self.tempResult = "Tidak ada deadline/jadwal untuk '{}' pada tanggal tersebut :)".format(matkul)
        else:
            if(jenisTask == ""):
                for record in result:
                    self.tempResult += "\n" + record[4] + " - " + record[3]
            else:
                count = 0
                for record in result:
                    if(record[2] == jenisTask):
                        count += 1
                        self.tempResult += "\n" + record[4] + " - " + record[3]
                if(count == 0):
                    self.tempResult = "Tidak ada deadline/jadwal untuk '{}' '{}' pada tanggal tersebut".format(
                        jenisTask, matkul)


    def getResult(self):
        return self.tempResult

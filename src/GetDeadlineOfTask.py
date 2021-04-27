from DatabaseClass import Database


class GetDeadlineOfTask:
    def __init__(self, matkul):
        self.matkul = matkul
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

        # print(dateStart)
        # print(dateEnd)
        result = []
        found = False
        i = 0
        while (not found and i<len(value)):
            if (value[i][1] == matkul):
                result.append(value[i])
                found = True
            i += 1

        print(result)

        if len(result) == 0:
            self.tempResult = "Tidak ada deadline/jadwal untuk '{}' pada tanggal tersebut :)".format(matkul)
        else:
            self.tempResult = result[0][4]

    def getResult(self):
        return self.tempResult

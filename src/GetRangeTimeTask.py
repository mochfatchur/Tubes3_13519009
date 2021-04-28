from DatabaseClass import Database

class GetRangeTimeTask:
    def __init__(self, dateStart, dateEnd):
        self.dateStart = dateStart
        self.dateEnd = dateEnd
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
        dateStart = self.dateStart
        dateEnd = self.dateEnd
        print(dateStart)
        print(dateEnd)
        result = []
        for i in range(len(value)):
            if (value[i][4] <= dateEnd and value[i][4] >= dateStart):
                result.append(value[i])
        if len(result) == 0:
            self.tempResult = "Tidak ada deadline/jadwal pada rentang tanggal tersebut, :)"
        else:
            self.tempResult = "[Daftar Deadline]"
            for record in result:
                self.tempResult += "\n" + \
                    "(ID: {}) ".format(record[0]) + " - ".join(record[1:])

    def getResult(self):
        return self.tempResult

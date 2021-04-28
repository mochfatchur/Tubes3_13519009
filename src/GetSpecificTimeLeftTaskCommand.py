from DatabaseClass import Database
from datetime import datetime
from datetime import timedelta


class GetSpecificTimeLeftTaskCommand:
    def __init__(self, jenisTask="", N=0):
        self.jenisTask = jenisTask
        self.tempResult = ""
        self.N = N

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
        value = database.GetCursor().fetchall()
        dateStart = str(datetime.date(datetime.now()))
        dateEnd = str(
            datetime.date(
                datetime.today() +
                timedelta(
                    days=self.N)))
        print(dateStart)
        print(dateEnd)
        result = []
        for i in range(len(value)):
            if (value[i][4] <= dateEnd and value[i][4] >= dateStart):
                result.append(value[i])
        if len(result) == 0:
            if self.jenisTask == "":
                self.tempResult = "Tidak ada tugas yang harus dikerjakan untuk {} hari ke depan".format(
                    self.N)
            else:
                self.tempResult = "Tidak ada {} yang harus dikerjakan untuk {} hari ke depan".format(
                    self.jenisTask, self.N)
        else:
            self.tempResult = "[Daftar Deadline]"
            for record in result:
                self.tempResult += "\n" + \
                    "(ID: {}) ".format(record[0]) + " - ".join(record[1:])

    def getResult(self):
        return self.tempResult

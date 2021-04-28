from DatabaseClass import Database

class GetDueTodayTaskCommand:
    def __init__(self, jenisTask = ""):
        self.jenisTask = jenisTask
        self.tempResult = ""
        
    def execute(self):
        database = Database()
        database.GetCursor().execute(
            """
            SELECT *
            FROM Task t
            WHERE t.tanggal = DATE("now", "localtime")
            {}
            ORDER BY (
                SELECT nilai
                FROM Prioritas p
                WHERE t.jenis = p.jenis                
            )
            """.format("" if self.jenisTask == "" else "AND jenis = \"{}\"".format(self.jenisTask))
        )
        
        result = database.GetCursor().fetchall()
        if len(result) == 0:
            if self.jenisTask == "":
                self.tempResult = "Tidak ada deadline/jadwal untuk hari ini, yay! :D"
                
            else:
                self.tempResult = "Tidak ada {} untuk hari ini, yay! :D".format(self.jenisTask)
            
        else:
            self.tempResult = "[Daftar Deadline]"
            for record in result:
                self.tempResult += "\n" + "(ID: {}) ".format(record[0]) + " - ".join(record[1:])
            
            self.tempResult += "Tetap semangat! ^_^"
            
    def getResult(self):
        return self.tempResult
                
        
        
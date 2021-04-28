from DatabaseClass import Database

class AddTaskCommand:
    
    
    regex_tanggal = [
        r"\d"
    ]

    def __init__(self, matkul, jenis, deskripsi, tahun, bulan, tanggal):
        self.matkul = matkul
        self.jenis = jenis
        self.deskripsi = deskripsi
        self.tahun = tahun
        self.bulan = bulan
        self.tanggal = tanggal
        self.tempResult = ""
        
    def execute(self):
        database = Database()
        
        # matkul tidak boleh kosong
        if self.matkul.strip() != "":
            # mengecek keberadaan jenis
            valid_jenis = database.GetCursor().execute("""
                SELECT jenis FROM Prioritas
            """).fetchall()
            valid_jenis = list(map(lambda row: row[0], valid_jenis))
            
            if self.jenis in valid_jenis:
                # Generate ID
                database.GetCursor().execute("""
                    SELECT ID FROM Task
                """)
                
                id_result = database.GetCursor().fetchall()
                
                new_id = ""
                if len(id_result) == 0:
                    new_id = "1"
                else:
                    print(str(max(list(map(lambda row: int(row[0]), id_result))) + 1))
                    new_id = str(max(list(map(lambda row: int(row[0]), id_result))) + 1)
                
                print(new_id)
                new_id = int(new_id)
                
                #(self,id, matkul, jenis, deskripsi, tanggal):
                database.InsertTask(
                    str(new_id),
                    self.matkul,
                    self.jenis,
                    self.deskripsi,
                    "{:0>4}-{:0>2}-{:0>2}".format(self.tahun, self.bulan, self.tanggal));
                    
                database.GetConnection().commit()
                
                self.tempResult = "Task berhasil ditambahkan! ^o^\n"
                self.tempResult += "(ID: {}) {} - {} - {} - {}".format(new_id, self.matkul, self.jenis, self.deskripsi, "{:0>4}-{:0>2}-{:0>2}".format(self.tahun, self.bulan, self.tanggal))
            
            else:
                self.tempResult = "Saya tidak mengenal jenis \"{}\" ... .-.".format(self.jenis)
        
        else:
            self.tempResult = "Saya bingung apa yang perlu diingatkan. .-."
            
    def getResult(self):
        return self.tempResult
                
        
        
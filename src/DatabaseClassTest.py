from DatabaseClass import Database

class TestClass:
    # Fungsi perlu dimulai dengan "test_"
    def test_insert_task(self): 
        database = Database()
        
        # Hanya untuk menghapus tes sebelumnya jika ada
        database.GetCursor().execute(
            """
            DELETE FROM Task
            WHERE ID = "TEST_ID"
            """
        )
        
        database.InsertTask('TEST_ID','IF3110','Kuis','Bab 2 sampai 3','22/04/2021')
        database.GetCursor().execute("SELECT * FROM Task where ID = \"TEST_ID\"")
        result = database.GetCursor().fetchall()
        assert len(result) == 1, "Primary key Task tidak berjalan dengan baik atau data tidak tersimpan."
        result = result[0]
        assert result[0] == "TEST_ID"
        assert result[1] == "IF3110"
        assert result[2] == "Kuis"
        assert result[3] == "Bab 2 sampai 3"
        assert result[4] == "22/04/2021"
        
        # Hanya untuk menghapus tes sebelumnya jika ada
        database.GetCursor().execute(
            """
            DELETE FROM Task
            WHERE ID = "TEST_ID"
            """
        )
        
        database.GetConnection().commit()
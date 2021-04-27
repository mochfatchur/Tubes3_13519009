import pytest
from DatabaseClass import Database
from AddTaskCommand import AddTaskCommand

class TestClass:
    # Yang diuji:
    # Penambahan normal
    # Penambahan dengan matkul kosong
    # Penambahan dengan deskripsi kosong
    # Penambahan dengan jenis tidak valid
    # (untuk tanggal tidak valid, itu masalah regex [Extractor])

    # Arrange
    @pytest.fixture
    def used_data(self):
        return [
            ("TEST_ATCT_IF1210", "tubes", "Willy Wangky", 2019, 4, 15),
            ("", "ujian", "TEST_ATCT_Ujian mental", 2020, 1, 1),
            ("TEST_ATCT_IF2220", "kuis", "", 2020, 12, 2),
            ("TEST_ATCT_IF2240", "dependensi fungional", "Ini adalah tugas yang sangat rumit", 2021, 2, 3)
        ]
        
    @pytest.fixture(scope="function")
    def initialization(self, request):
        database = Database()
        
        def cleanup():
            database.GetCursor().execute("""
                DELETE FROM Task
                WHERE nama_matkul LIKE \"TEST_ATCT%\"
                OR deskripsi LIKE \"TEST_ATCT%\"
                OR ID LIKE \"TEST_ATCT%\"
            """)
                
            database.GetConnection().commit()
        
        cleanup()
                
        request.addfinalizer(cleanup)
            
    def test_normal_add(self, initialization, used_data):
        taskCommand = AddTaskCommand(*used_data[0])
        taskCommand.execute()
        result = taskCommand.getResult()
        
        assert "TEST_ATCT_IF1210" in result
        assert "tubes" in result
        assert "Willy Wangky" in result
        assert "2019-04-15" in result
        
    def test_empty_matkul_add(self, initialization, used_data):
        taskCommand = AddTaskCommand(*used_data[1])
        taskCommand.execute()
        result = taskCommand.getResult()
        
        assert "TEST_ATCT_" not in result
    
    def test_empty_desc_add(self, initialization, used_data):
        taskCommand = AddTaskCommand(*used_data[2])
        taskCommand.execute()
        result = taskCommand.getResult()
        
        assert "TEST_ATCT_IF2220" in result
        assert "kuis" in result
        assert "2020-12-02" in result
        
    def test_invalid_tasktype_add(self, initialization, used_data):
        taskCommand = AddTaskCommand(*used_data[3])
        taskCommand.execute()
        result = taskCommand.getResult()
        
        assert "TEST_ATCT_" not in result
        
import pytest
from DatabaseClass import Database
from DeleteTask import DeleteTask
from datetime import datetime


class TestClass:
    # Arrange
    @pytest.fixture
    def used_data(self):
        return [
            ("TEST_GDTTCT_001", "IF2220", "kuis", "Regresi", "2021-04-28"),
            ("TEST_GDTTCT_002", "IF2230", "tubes", "System Call", "2021-04-30"),
            ("TEST_GDTTCT_003", "IF2250", "tubes", "Demo", str(datetime.date(datetime.now()))),
            ("TEST_GDTTCT_004", "IF2240", "ujian", "UAS", str(datetime.date(datetime.now())))
        ]

    @pytest.fixture(scope="function")
    def initialization(self, request, used_data):
        database = Database()

        def cleanup():
            for data_id in list(map(lambda row: row[0], used_data)):
                database.GetCursor().execute("""
                    DELETE FROM Task
                    WHERE ID = \"{}\"
                """.format(data_id))

            database.GetConnection().commit()

        cleanup()
        for row in used_data:
            database.InsertTask(*row)

        database.GetConnection().commit()

        request.addfinalizer(cleanup)

    def test_normal_result(self, initialization):
        # database = Database()
        # print(database.GetCursor().execute(
        #     "SELECT * FROM Task").fetchall())
        taskCommand = DeleteTask(
            jenisTask="tubes", namaMatkul="IF2230")
        taskCommand.execute()
        result = taskCommand.getResult()
        assert result != ""
        # assert "TEST_GDTTCT_001" in result
        # assert "TEST_GDTTCT_002" not in result
        # assert "TEST_GDTTCT_003" in result
        # assert "TEST_GDTTCT_004" in result
        assert "Yay tugas sudah selesai!!!" in result
        print("--- RESULT ---")
        print(result)
        print("--- END OF RESULT ---")

    def test_with_no_result(self, initialization):
        taskCommand = DeleteTask(
            jenisTask="tucil", namaMatkul="IF2230")
        taskCommand.execute()
        result = taskCommand.getResult()

        assert "Tidak ada tucil yang harus dikerjakan" in result
        print("--- RESULT ---")
        print(result)
        print("--- END OF RESULT ---")

    def test_task_not_found(self, initialization):
        taskCommand = DeleteTask(
            jenisTask="tubes", namaMatkul="IF2220")
        taskCommand.execute()
        result = taskCommand.getResult()
        assert "Tidak ada tubes IF2220" in result
        print("--- RESULT ---")
        print(result)
        print("--- END OF RESULT ---")

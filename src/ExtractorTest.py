from Extractor import Extractor

class TestClass:
    def test_GetDueTodayTask(self):
        extractor = Extractor()
        result1 = extractor.extract("Apa saja deadline hari ini?", "GetDueTodayTask")
        result2 = extractor.extract("Deadline tubes hari ini apa saja, ya?", "GetDueTodayTask")
        result3 = extractor.extract("yang deadline pada hari ini", "GetDueTodayTask")
        result4 = extractor.extract("Bot, minta daftar deadline dong pada hari ini. Makasih :)", "GetDueTodayTask")
        result5 = extractor.extract("Untuk tucil, deadline pada hari ini apa saja?", "GetDueTodayTask")
        result6 = extractor.extract("Tubes yang deadline pada hari ini apa saja?", "GetDueTodayTask")
        
        assert result1 != None
        assert result1.jenisTask == ""
        assert result2 != None
        assert result2.jenisTask == "tubes"
        assert result3 != None
        assert result3.jenisTask == ""
        assert result4 != None
        assert result4.jenisTask == ""
        assert result5 != None
        assert result5.jenisTask == "tucil"
        assert result6 != None
        assert result6.jenisTask == "tubes"
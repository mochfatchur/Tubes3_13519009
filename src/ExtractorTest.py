from Extractor import Extractor
from datetime import datetime
from ContextIdentifier import Context

class TestClass:
    def test_GetDueTodayTask(self):
        extractor = Extractor()
        result1 = extractor.extract("Apa saja deadline hari ini?", Context.getDueTodayTask)
        result2 = extractor.extract("Deadline tubes hari ini apa saja, ya?", Context.getDueTodayTask)
        result3 = extractor.extract("yang deadline pada hari ini", Context.getDueTodayTask)
        result4 = extractor.extract("Bot, minta daftar deadline dong pada hari ini. Makasih :)", Context.getDueTodayTask)
        result5 = extractor.extract("Untuk tucil, deadline pada hari ini apa saja?", Context.getDueTodayTask)
        result6 = extractor.extract("Tubes yang deadline pada hari ini apa saja?", Context.getDueTodayTask)
        
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
        
    def test_AddTask(self):
        extractor = Extractor()
        # Normal
        result1 = extractor.extract("Halo bot, tolong ingetin kalau ada kuis IF3110 Bab 2 sampai 3 pada 22/04/21", Context.addTask)
        assert result1 != None
        assert result1.matkul == "IF3110"
        assert result1.jenis == "kuis"
        assert result1.deskripsi == "Bab 2 sampai 3"
        assert result1.tahun == 2021
        assert result1.bulan == 4
        assert result1.tanggal == 22
        
        # Normal dengan tanggal yang berbeda format, UAS adalah ujian
        result2 = extractor.extract("Ingatkan saya ada UAS IF2230 pada 20 Mei 2021. Saya sedang chaos nih. :(", Context.addTask)
        assert result2 != None
        assert result2.matkul == "IF2230"
        assert result2.jenis == "ujian"
        assert result2.deskripsi == "UAS"
        assert result2.tahun == 2021
        assert result2.bulan == 5
        assert result2.tanggal == 20
        
        # Tahun yang sama secara implisit, UTS adalah ujian
        result3 = extractor.extract("Beritahukan saya tentang UTS IF2250 pada 1 Januari", Context.addTask)
        assert result3 != None
        assert result3.matkul == "IF2250"
        assert result3.jenis == "ujian"
        assert result3.deskripsi == "UTS"
        assert result3.tahun == datetime.now().year
        assert result3.bulan == 1
        assert result3.tanggal == 1
        
        # Tanggal tidak diawali dengan kata pada
        result4 = extractor.extract("saya ingin menambahkan tucil IF2220 tentang String Matching yang deadline-nya sudah dekat: 28 April", Context.addTask)
        assert result4 != None
        assert result4.matkul == "IF2220"
        assert result4.jenis == "tucil"
        assert result4.deskripsi == "String Matching"
        assert result4.tahun == datetime.now().year
        assert result4.bulan == 4
        assert result4.tanggal == 28
        
        # Tidak ada tanggal (invalid)
        result7 = extractor.extract("Ada tubes IF2210 tentang Worms. Ingatkan.", Context.addTask)
        assert result7 == None
        
        # Tidak ada matkul (invalid)
        result8 = extractor.extract("Ada tucil tentang objek. Deadline 7 September. Ingatkan.", Context.addTask)
        assert result8 == None
        
        # Tidak ada jenis tugas (invalid)
        result9 = extractor.extract("Ingatkan tentang IF2211 tentang BFS dan DFS. Deadline 5 Desember.", Context.addTask)
        assert result9 == None
        
        ### THE REST IS NOT TESTED YET BECAUSE TIME
        ## Tidak ada deskripsi
        #result6 = extractor.extract("Zach ingin tambahkan ujian IF2240 yang dilakukan pada 22 Februari 2002.", Context.addTask)
        #assert result6 != None
        #assert result6.matkul == "IF2240"
        #assert result6.jenis == "ujian"
        #assert result6.deskripsi == ""
        #assert result6.tahun == 2002
        #assert result6.bulan == 22
        #assert result6.tanggal == 2
        
        ## Tidak ada kata pengantar
        #result5 = extractor.extract("Kuis IF1210 tentang prosedur ingin ditambahkan ke daftar tugas yang saya akan kerjakan. Waktunya 1-3-2015. Bisa?", Context.addTask)
        #assert result5 != None
        #assert result5.matkul == "IF1210"
        #assert result5.jenis == "tucil"
        #assert result5.deskripsi == "String Matching"
        #assert result5.tahun == 2015
        #assert result5.bulan == 3
        #assert result5.tanggal == 1
        
        ## Deadline relatif (hari)
        # result10 = extractor.extract("Ada tubes IF2240 tentang Milestone IV yang deadline-nya 10 hari ke depan. Ingatkan, dong. :\')")
        
        ## Deadline dengan kata kunci besok
        # result11 = extractor.extract("Besok itu deadline tucil IF2211 tentang regex. Ingatkan, ya.")
        
        ## Deadline dengan kata kunci lusa, tanpa deskripsi
        # result12 = extractor.extract("Lusa ada ujian IF3150")
        
        ## Deadline dengan kata kunci hari ini
        # result13 = extractor.extract("aaaaaaaaaa hari ini perlu selesaikan tubes IF2210 tentang remainder assistant tolong catat plzplzplz")
# import sqlite3
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()
# # createTableTask = '''
#         CREATE TABLE IF NOT EXISTS Task(
#         ID INT PRIMARY KEY NOT NULL,
#         nama_matkul TEXT NOT NULL,
#         jenis TEXT NOT NULL,
#         deskripsi TEXT NOT NULL,
#         tanggal TEXT NOT NULL);
#         '''
# cursor.execute(createTableTask)


# createTablePrio = '''
#         CREATE TABLE IF NOT EXISTS Prioritas(
#         nilai INTEGER NOT NULL,
#         jenis TEXT NOT NULL,
#         FOREIGN KEY(jenis) REFERENCES Task(jenis)
#             ON DELETE CASCADE ON UPDATE NO ACTION);
#         '''
# cursor.execute(createTablePrio)

# cursor.execute(
#     'INSERT INTO Task VALUES(1,"IF2221","tubes","string matching","27/04/2021")')
# cursor.execute(
#     'INSERT INTO Task VALUES(2,"IF2230","kuis","string matching","28/04/2021")')
# cursor.execute(
#     'INSERT INTO Task VALUES(3,"IF2240","ujian","string matching","29/04/2021")')
# cursor.execute(
#     'INSERT INTO Task VALUES(4,"IF2210","tucil","string matching","30/04/2021")')
# cursor.execute(
#     'INSERT INTO Task VALUES(5,"IF2231","pr","string matching","27/04/2021")')


# cursor.execute("SELECT * FROM TASK")
# print(cursor.fetchall())
# conn.commit()

# conn.close()

# from DatabaseClass import Database 
# database = Database()
# database.InsertTask(6,"IF2210","tubes","deskripsi 1","2021-04-28")
# database.InsertTask(7,"IF2220","ujian","deskripsi 2","2021-04-29")
# database.InsertTask(8,"IF2230","tucil","deskripsi 3","2021-04-30")
# database.InsertTask(9,"IF2240","kuis","deskripsi 4","2021-05-01")
# database.InsertTask(10,"IF2250","tubes","deskripsi 5","2021-05-02")

# database.GetCursor().execute("SELECT * FROM TASK")
# print(database.GetCursor().fetchall())
import sqlite3


connection = sqlite3.connect('../test/database.db')
cursor = connection.cursor()

class Database:
    def __init__(self):
        # create task table
        createTableTask = '''
        CREATE TABLE IF NOT EXISTS Task(
        ID VARCHAR(2) PRIMARY KEY NOT NULL,
        nama_matkul VARCHAR(255) NOT NULL,
        jenis TEXT NOT NULL,
        deskripsi TEXT NOT NULL,
        tanggal DATE NOT NULL);
        '''

        cursor.execute(createTableTask)

        # create prioritas table
        createTablePrio = '''
        CREATE TABLE IF NOT EXISTS Prioritas(
        nilai INTEGER NOT NULL,
        jenis TEXT NOT NULL,
        FOREIGN KEY(jenis) REFERENCES Task(jenis)
            ON DELETE CASCADE ON UPDATE NO ACTION);
        '''
        cursor.execute(createTablePrio)

    def InsertTask(self,id, matkul, jenis, deskripsi, tanggal):
        insertTask = '''INSERT INTO Task VALUES ('{}', '{}', '{}', '{}', '{}'); '''.format(id, matkul, jenis, deskripsi,
                                                                                           tanggal)
        cursor.execute(insertTask)
        connection.commit()

    def InsertPrio(self,nilai, jenis):
        insertTask = '''INSERT INTO Task VALUES ({}, '{}'); '''.format(nilai,jenis)
        cursor.execute(insertTask)
        connection.commit()

    #def __del__(self):
    #    connection.close()
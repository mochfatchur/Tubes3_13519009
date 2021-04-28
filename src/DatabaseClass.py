import sqlite3


class Database:
    connection = None
    cursor = None
    connected = False

    def __init__(self):
        # create task table
        createTableTask = '''
        CREATE TABLE IF NOT EXISTS Task(
        ID VARCHAR(2) PRIMARY KEY NOT NULL,
        nama_matkul VARCHAR(255) NOT NULL,
        jenis TEXT NOT NULL,
        deskripsi TEXT NOT NULL,
        tanggal DATE NOT NULL,
        FOREIGN KEY(jenis) REFERENCES Task(jenis)
            ON DELETE CASCADE ON UPDATE NO ACTION);
        '''

        self.GetCursor().execute(createTableTask)

        # create prioritas table
        createTablePrio = '''
        CREATE TABLE IF NOT EXISTS Prioritas(
        nilai INTEGER NOT NULL,
        jenis TEXT PRIMARY KEY NOT NULL);
        '''
        self.GetCursor().execute(createTablePrio)

        # Add priority if empty
        self.GetCursor().execute("SELECT * From Prioritas")
        if len(self.GetCursor().fetchall()) == 0:
            self.InsertPrio(99, "tubes")
            self.InsertPrio(50, "ujian")
            self.InsertPrio(50, "tucil")
            self.InsertPrio(30, "kuis")

    def InsertTask(self, id, matkul, jenis, deskripsi, tanggal):
        insertTask = '''INSERT INTO Task VALUES ('{}', '{}', '{}', '{}', '{}'); '''.format(
            id, matkul, jenis, deskripsi, tanggal)
        self.GetCursor().execute(insertTask)
        self.GetConnection().commit()

    def InsertPrio(self, nilai, jenis):
        insertTask = '''INSERT INTO Prioritas VALUES ({}, '{}'); '''.format(
            nilai, jenis)
        self.GetCursor().execute(insertTask)
        self.GetConnection().commit()

    def GetConnection(self):
        if not self.connected:
            self.connection = sqlite3.connect('../database.db')
            self.cursor = self.connection.cursor()
            self.connected = True
        return self.connection

    def GetCursor(self):
        if not self.connected:
            self.connection = sqlite3.connect('../database.db')
            self.cursor = self.connection.cursor()
            self.connected = True
        return self.cursor



    # def __del__(self):
    #    connection.close()


